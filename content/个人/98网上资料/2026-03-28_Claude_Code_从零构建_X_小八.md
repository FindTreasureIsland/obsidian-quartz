# 从零开始两天构建一个 Claude Code：带你拆解 AI CLI 的每一层

**作者**: 小八 (@IceBearMiner)
**平台**: X (Twitter)
**发布时间**: 2026-03-28 21:45
**链接**: https://x.com/i/status/2037888800341610684
**观看数**: 7.2万 | **转帖**: 36 | **喜欢**: 235 | **书签**: 481

---

## 前言

前两天突发奇想：一个生产级的 agentic CLI 到底需要哪些组件？每一层的具体怎么实现？SSE 缓冲区怎么管理、system prompt 怎么分段、工具权限怎么拦截、上下文满了怎么压缩。这些问题靠读文档回答不了，靠逆向混淆代码效率极低。

所以选择了另一条路：以 Claude Code 为参照系，从零重建一个功能等价的实现——纯 TypeScript，零框架，唯一的依赖是 fast-glob（因为原生 glob 在跨平台路径处理上有已知缺陷）。

两天之后的结果是 **46 个文件，一万行 TypeScript**。这篇文章记录的是这个过程中每一层的技术决策和实现细节。

---

## 整体架构

核心流程如下：

用户输入 → 组装请求 → API 调用（SSE）→ 解析响应事件流 → 根据 stop_reason 决定分支：
- `end_turn` — 输出文本，结束本轮
- `tool_use` — 执行工具调用 → 将 tool_result 追加到 messages → 反复迭代

目录结构按层划分：

| 目录 | 职责 |
|------|------|
| `core/` | 引擎层，包含 Agent Loop、SSE 客户端、context 管理、compact 逻辑 |
| `tools/` | 工具系统，包含所有内置工具的实现和 MCP 客户端 |
| `ui/` | 终端渲染层，处理流式文本输出、进度指示、颜色主题 |
| `plugins/` | 扩展系统，允许运行时注入工具和 hook |
| `skills/` | 技能库，对应 Claude Code 的 slash command 高级功能 |
| `commands/` | 处理 / 前缀命令的解析和分发 |

这六层之间的依赖是**单向的**，core/ 不依赖 ui/，tools/ 不依赖 skills/。

**技术选型的核心理由**：Node.js 22 的原生能力。fetch 和 ReadableStream 在 22 版本中已经稳定，不需要 node-fetch 或任何 HTTP 客户端库。TextDecoder 处理 UTF-8 字节流，Buffer 处理二进制，child_process.exec 执行 Shell 命令——所有这些都是标准库。

---

## 多平台LLM兼容

默认支持御三家和自定义平台，自定义模型（OpenAI 兼容格式）是一个附加需求。部分本地模型（如 Ollama、LM Studio）暴露 OpenAI 兼容接口，事件格式与其他格式不同。处理方式是在 SSE 客户端初始化时传入 `format: 'openai'` 参数，在事件解析层做格式适配，将 OpenAI 的 delta 结构翻译成统一的内部事件类型。这样 **Agent Loop 层完全不感知 API 格式差异**。

---

## System Prompt 分段架构与 Prompt Caching

最直觉的 system prompt 写法是一个大字符串。这个方式在原型阶段没问题，但在生产环境有两个显著缺陷：

1. 每轮对话 system prompt 几乎不变，但如果以单字符串传入，API 缓存无法有效命中
2. 部分内容（如当前目录、Git 状态、CLAUDE.md 文件内容）每轮都会变化，与静态内容混在一起会污染缓存

将 system 参数设为 **block 数组**，每个 block 可以独立设置 cache_control。

### 静态段（打缓存）
- 身份声明
- 工具使用规范
- 编码风格
- 安全执行规则

### 动态段（每轮重新计算）
- 当前工作目录和系统环境
- Git 仓库状态
- CLAUDE.md 内容
- MCP 服务器的自定义指令

**关键洞察**：Anthropic 的 prompt caching 按照 block 数组的**前缀匹配**来识别缓存，排在前面的静态内容越稳定，缓存命中率越高。这就是官方订阅为什么 API 调用能省不少钱。

---

## Agent Loop：while 循环背后的状态机

Agent Loop 的骨架是一个有上限的 while 循环，**最大迭代次数 25 次**，每次迭代对应一轮模型调用。

每次迭代的流程：
1. 检查是否需要 compact
2. 构建完整 prompt
3. 发起流式请求
4. 实时处理事件流
5. 检查 stop_reason — tool_use 则执行工具，end_turn 或 max_tokens 则结束循环
6. 构建 tool_result message，追加到 messages 数组，进入下一轮

### 工具执行管线的六个阶段：
1. `renderToolCall` — 在终端展示将要执行的工具名和参数
2. `permissionCheck` — 根据工具类型和参数决定是否需要用户确认
3. `preHook` — 插件系统的前置拦截点
4. `checkpoint` — 对于破坏性操作，在执行前快照相关文件状态
5. `executeTool` — 调用实际工具函数
6. `postHook` — 插件后置钩子

### 自动 Compact 机制
在每轮迭代开始时，估算当前 messages 数组的 token 数，如果超过模型上下文限制的 85%，触发压缩——用一次独立 API 调用生成摘要，替换原来的 messages 数组。

### Prompt Caching 的三个施力点
1. system prompt blocks — 静态段走缓存
2. tools 数组 — 最后一个 tool definition 打上 cache_control
3. 最后一条 tool_result message — 作为缓存断点

三层叠加的实际效果：**每轮 API 调用只有少量 tokens 是真正的输入计费，大部分走缓存价格**（约为正常输入价格的 10%）。

---

## 21 个内置工具

工具系统的入口是 TOOL_DEFINITIONS，一个 JSON Schema 数组。核心工具：

| 工具 | 实现要点 |
|------|---------|
| Read | fs.readFile 读取文件后加行号前缀，支持 offset 和 limit 参数分页读取 |
| Write | 写入前 fs.mkdir({ recursive: true }) 确保父目录存在 |
| Edit | 精确字符串替换，old_string 必须在文件中唯一出现 |
| Bash | child_process.exec 执行，120 秒超时，输出超 500 行时截断 |
| Grep | 自实现 regex 引擎，不依赖系统 grep |
| WebFetch / WebSearch | fetch + HTML 剥离 + 截断，搜索走 DuckDuckGo |

### Deferred Tools 性能优化
低频工具（如 NotebookRead、TodoWrite）不放入每次请求的 tools 数组，而是标记为 deferred——模型需要时通过 ToolSearch 工具按关键词查询获取完整 schema。这个机制将 tools 数组的**固定开销降低了约 40%**。

---

## 权限系统：三种模式与两阶段分类器

### 三种模式
- **default** — safe 类工具自动执行，dangerous 和 write 类需要用户确认
- **auto** — 绕过所有交互式提示，适合 CI 环境——但 deny rules 仍然生效
- **plan** — 只读沙箱，只看执行计划，不实际执行

### 两阶段分类器（增强 auto 模式安全性）
- **Stage 1** — 纯模式匹配：维护已知安全/危险命令的规则表，命中即返回，覆盖 90%+ 的情况，零延迟
- **Stage 2** — 处理未覆盖的情况：将命令字符串发给 Haiku 模型，要求返回 allow/deny/ask_user 三种之一。Haiku 延迟约 300-500ms，相比模型主循环几乎可以忽略

---

## MCP 动态工具与 LSP 集成

### MCP（Model Context Protocol）
本质是一个标准化的工具发现协议。工具可以独立部署为进程，通过统一接口被任何兼容客户端发现和调用。

- 协议层：JSON-RPC 2.0 over stdio
- 启动序列固定：initialize 握手 → tools/list 获取工具定义数组
- McpManager 管理多个 server 的生命周期，工具名加上 `mcp__` 前缀做命名空间隔离

### LSP 集成
不是扩展工具，而是给模型提供**实时的代码诊断信息**。LspManager 维护文件扩展名到语言服务器的路由表，Write/Edit 执行后自动通知对应语言服务器，诊断结果作为 lsp_diagnostics section 注入下一轮 system prompt。

**这个设计让模型在修改代码后能立即看到编译器反馈**，而不需要单独的"检查错误"工具调用，缩短了发现问题到修复问题的路径。

---

## 插件系统与 Skills

插件系统回答的问题是：如何在不修改 CLI 核心代码的情况下扩展能力？答案是 **manifest 驱动的目录结构**。

每个插件是一个目录，包含 plugin.json，声明提供的六类扩展点：skills、agents、hooks、commands、mcpServers、lspServers。

### 8 个内置 Skill
- `commit / pr / review` — Git 操作类
- `init` — 扫描项目结构，生成配置文件
- `simplify` — 审查变更代码，查找重复/低效逻辑，直接修复
- `loop / schedule` — 自动化类
- `update-config` — 修改 CLI 自身配置

Skill 查找优先级：**内置 → 插件 → 项目 .clio/skills/**。项目级 skill 可以覆盖插件级，但不能覆盖内置，防止安全敏感的内置 skill 被意外替换。

---

## Agent Teams：多 Agent 协作

单 Agent 的瓶颈在于**串行执行**。当任务可以分解为多个独立子任务时，多 Agent 并行能显著缩短完成时间。

- 子 Agent 通过 `executeSubAgent()` 运行，最多 15 轮迭代
- **隔离模式**：创建 Git worktree，子 Agent 在独立分支上操作，完成后由主 Agent 决定是否合并
- **后台 Agent**：`run_in_background: true` 标记，Promise 存入 Map，完成时以 tool_result 形式通知主 Agent
- **自定义 Agent** 定义在 `.clio/agents/*.md` 文件中，YAML front-matter 声明工具子集、模型选择、最大迭代次数

完整协作流程：TeamCreate → SendMessage 分发任务 → 等待完成 → 汇总结果 → TeamDelete。

---

## Auto Memory：跨会话记忆

LLM 本身是无状态的。每次对话从空白上下文开始，之前建立的偏好、项目约定、用户反馈全部消失。Auto Memory 用**文件系统模拟持久记忆**。

四种记忆类型：
- **user** — 用户偏好（角色、习惯、专长）
- **feedback** — 行为纠正（用户确认或否定的做法）
- **project** — 项目约定（不可从代码/git 推导的上下文）
- **reference** — 外部资源指针（URL、看板、文档链接）

MEMORY.md 是索引文件，每次对话开始时注入 system prompt，模型按需通过 Read 工具读取具体内容。

**关键设计**：记忆的写入完全复用现有工具链——Write 创建、Edit 更新、Read 读取。零新增代码路径，工具权限模型自动适用。

---

## 核心结论

整个项目验证了一个认知：**Claude Code 的工程质量确实高于平均水平**。

分段 prompt 的三层缓存设计——静态系统提示缓存、工具定义缓存、动态内容不缓存——这个粒度的 cache 意识在大多数 LLM 应用里是缺失的。

**核心难点在于 Harness Engineering**。毕竟调用 API 是十行代码的事，只有把工具调用结果正确地反馈给模型、在流式输出中间插入用户交互、处理长任务里的错误恢复——这些才是真正区分 toy project 和 production system 的地方。

---

*来源: 小八 @IceBearMiner*
