# 从零开始两天构建一个 Claude Code：拆解 AI CLI 的每一层

**作者**：小八 @IceBearMiner
**日期**：2026年3月28日
**原文链接**：https://x.com/i/status/2037888800341610684
**数据**：49万观看、1476喜欢、325转帖、3351书签

---

前两天突发奇想：一个生产级的 agentic CLI 到底需要哪些组件？每一层的具体怎么实现？

SSE 缓冲区怎么管理、system prompt 怎么分段、工具权限怎么拦截、上下文满了怎么压缩。

这些问题靠读文档回答不了，靠逆向混淆代码效率极低。所以选择了另一条路：**以 Claude Code 为参照系，从零重建一个功能等价的实现**——纯 TypeScript，零框架，唯一依赖是 fast-glob。

两天之后：46 个文件，一万行 TypeScript。

---

## 整体架构

核心流程：
```
用户输入 → 组装请求 → API 调用（SSE）→ 解析响应事件流 → 根据 stop_reason 决定分支：
· end_turn — 输出文本，结束本轮
· tool_use — 执行工具调用 → 将 tool_result 追加到 messages → 反复迭代
```

**六层目录结构：**

| 层级 | 目录 | 职责 |
|------|------|------|
| 引擎层 | core/ | Agent Loop、SSE 客户端、context 管理、compact 逻辑 |
| 工具系统 | tools/ | 所有内置工具实现和 MCP 客户端 |
| 终端渲染 | ui/ | 流式文本输出、进度指示、颜色主题 |
| 扩展系统 | plugins/ | 运行时注入工具和 hook |
| 技能库 | skills/ | slash command 高级功能 |
| 命令解析 | commands/ | / 前缀命令的解析和分发 |

依赖单向：core/ 不依赖 ui/，tools/ 不依赖 skills/

**技术选型**：Node.js 22 原生能力——fetch、ReadableStream、TextDecoder、Buffer、child_process.exec 全部标准库，唯一外部依赖 fast-glob（处理 gitignore 和大型目录性能优异）。

---

## 多平台 LLM 兼容

默认支持御三家和自定义平台。部分本地模型（Ollama、LM Studio）暴露 OpenAI 兼容接口，事件格式不同。

**处理方式**：SSE 客户端初始化时传入 `format: 'openai'` 参数，在事件解析层做格式适配，将 OpenAI 的 delta 结构翻译成统一的内部事件类型。**Agent Loop 层完全不感知 API 格式差异**。

---

## System Prompt 分段架构与 Prompt Caching

最直觉的写法是一个大字符串，但生产环境有两个显著缺陷：
1. 每轮 system prompt 几乎不变，但以单字符串传入，API 缓存无法有效命中
2. 部分内容（当前目录、Git 状态、CLAUDE.md）每轮变化，污染缓存

**解决方案**：将 system 参数设为 block 数组，每个 block 独立设置 cache_control。

**静态段**（打 cache_control，首次写入缓存，后续命中）：
- 身份声明
- 工具使用规范
- 编码风格规范
- 安全执行规则

**动态段**（不带 cache_control，每轮重新计算）：
- 当前工作目录和系统环境
- Git 仓库状态
- CLAUDE.md 内容
- MCP 服务器自定义指令

**这就是官方订阅为什么 API 调用省钱——缓存命中率高。**

---

## Agent Loop：while 循环背后的状态机

骨架是一个有上限的 while 循环，**最大迭代次数 25 次**。25 轮足够完成大多数真实任务，同时防止 runaway loop 耗尽 API 额度。

**每次迭代流程：**

1. 检查是否需要 compact
2. 构建完整 prompt
3. 发起流式请求
4. 实时处理事件流
5. 检查 stop_reason — tool_use 则执行工具，end_turn 或 max_tokens 则结束循环
6. 构建 tool_result message，追加到 messages 数组，进入下一轮

**工具执行六阶段：**

1. `renderToolCall` — 终端展示将要执行的工具名和参数
2. `permissionCheck` — 根据工具类型和参数决定是否需要用户确认
3. `preHook` — 插件系统的前置拦截点
4. `checkpoint` — 破坏性操作前快照相关文件状态
5. `executeTool` — 调用实际工具函数
6. `postHook` — 插件后置钩子

**自动 compact 机制**：每轮迭代开始时估算 token 数，超过上下文限制 85% 触发压缩——发起独立 API 调用生成摘要，用 `[{role: 'user', content: summary}, {role: 'assistant', content: 'Understood.'}]` 替换原 messages。

**Prompt Caching 三层叠加**：
- system prompt blocks — 静态段走缓存
- tools 数组 — 最后一个 tool definition 打 cache_control
- 最后一条 tool_result message — 作为缓存断点

三层叠加的实际效果：每轮 API 调用只有少量 tokens 是真正的输入计费，大部分走缓存价格（约正常价格的 10%）。

---

## 21 个内置工具

工具系统入口是 TOOL_DEFINITIONS，一个 JSON Schema 数组，描述每个工具的名称、用途和参数结构。执行入口是单一的 `executeTool` 函数，内部用 switch 按工具名分发。

**核心工具实现细节：**

| 工具 | 实现要点 |
|------|----------|
| Read | fs.readFile 加行号前缀，支持 offset/limit 分页 |
| Write | 写入前 `fs.mkdir({ recursive: true })` 确保父目录存在 |
| Edit | 精确字符串替换，old_string 必须在文件中唯一出现 |
| Bash | 120 秒超时，输出超 500 行时截断（保留前 200 + 后 100）|
| Grep | 自实现 regex 引擎，支持三种输出模式、上下文行、跨行匹配 |
| WebFetch/Search | fetch + HTML 剥离 + 截断，搜索走 DuckDuckGo |

**Deferred Tools**：低频工具不放入每次请求的 tools 数组，标记为 deferred——模型需要时通过 ToolSearch 查询获取完整 schema。**将 tools 数组固定开销降低约 40%**。

---

## 权限系统：三种模式与两阶段分类器

**三种模式：**

| 模式 | 行为 |
|------|------|
| default | safe 类工具自动执行，dangerous 和 write 类需要用户确认 |
| auto | 绕过所有交互式提示，适合 CI——deny rules 仍然生效 |
| plan | 只读沙箱，safe 工具放行，dangerous 和 write 工具静默拒绝 |

**工具分类**（注册时静态声明）：
- **safe** — Read, Glob, Grep, WebFetch, WebSearch
- **dangerous** — Bash, Agent（副作用范围不可预测）
- **write** — Write, Edit（文件修改是最常见的审计操作）
- **bypass** — PlanMode 切换，始终无需确认

**两阶段分类器增强 auto 模式安全性：**

- **Stage 1** — 纯模式匹配：维护已知安全/危险命令的规则表，命中即返回，覆盖 90%+ 情况，零延迟
- **Stage 2** — Haiku 模型：处理未覆盖情况，返回 allow/deny/ask_user 三种之一。Haiku 延迟 300-500ms，相比主循环几乎可忽略

---

## MCP 动态工具与 LSP 集成

**MCP（Model Context Protocol）**：标准化的工具发现协议，让工具变成可独立部署的进程，通过统一接口被任何兼容客户端发现和调用。

**协议层**：JSON-RPC 2.0 over stdio。启动序列固定：initialize 握手 → tools/list 获取工具定义数组。McpManager 管理多个 server 的生命周期，工具名加上 `mcp__` 前缀做命名空间隔离。

**LSP 集成**：不是扩展工具，而是给模型提供实时代码诊断信息。LspManager 维护文件扩展名到语言服务器的路由表，Write/Edit 执行后自动通知对应语言服务器，诊断结果作为 lsp_diagnostics section 注入下一轮 system prompt。

**让模型在修改代码后能立即看到编译器反馈**，缩短发现问题到修复问题的路径。

---

## 插件系统与 Skills

**插件系统**：manifest 驱动的目录结构，每个插件是包含 `plugin.json` 的目录，声明六类扩展点：skills、agents、hooks、commands、mcpServers、lspServers。

**Skills**：比自定义 Agent 更轻量的复用单元，本质是参数化的 prompt 模板。输入 `/commit` 时，skill 系统展开模板、注入上下文，提交给当前 agent loop。

**8 个内置 skill：**

| Skill | 用途 |
|-------|------|
| commit / pr / review | Git 操作，生成规范化消息或 PR 描述 |
| init | 扫描项目结构，生成配置文件 |
| simplify | 审查变更代码，查找重复/低效逻辑，直接修复 |
| loop / schedule | 自动化类，持续执行或定时触发 |
| update-config | 修改 CLI 自身配置 |

**Skill 查找优先级**：内置 → 插件 → 项目 `.clio/skills/`。项目级可覆盖插件级，但不能覆盖内置，防止安全敏感的内置 skill 被意外替换。

---

## Agent Teams：多 Agent 协作

**子 Agent**：`executeSubAgent()` 是主 agent loop 的简化版本，排除团队管理工具防止无限嵌套，最多 15 轮迭代。隔离模式可选：`isolation: "worktree"` 创建 Git worktree，子 Agent 在独立分支上操作，完成后由主 Agent 决定是否合并。

**后台 Agent**：`run_in_background: true` 标记，Promise 存入 Map，完成时以 tool_result 形式通知主 Agent。

**完整协作流程**：TeamCreate 创建团队 → SendMessage 分发任务 → 等待完成 → 汇总结果 → TeamDelete 释放资源。**没有消息队列，没有共享状态，只有显式的消息传递。**

---

## Auto Memory：跨会话记忆

**问题**：LLM 本身无状态。每次对话从空白上下文开始，之前建立的偏好、项目约定、用户反馈全部消失。

**解决方案**：用文件系统模拟持久记忆，不引入数据库，不设计新存储格式。

**记忆文件**：带 YAML frontmatter 的 Markdown 文件，四种类型：

| 类型 | 内容 |
|------|------|
| user | 用户偏好（角色、习惯、专长）|
| feedback | 行为纠正（用户确认或否定的做法）|
| project | 项目约定（不可从代码/git 推导的上下文）|
| reference | 外部资源指针（URL、看板、文档链接）|

MEMORY.md 是索引文件，每次对话开始时注入 system prompt，模型按需通过 Read 工具读取具体内容。

**记忆写入完全复用现有工具链**：Write 创建、Edit 更新、Read 读取。零新增代码路径，工具权限模型自动适用。

---

## 结论

这个项目验证了一个认知：**Claude Code 的工程质量确实高于平均水平**。

分段 prompt 的三层缓存设计——静态系统提示缓存、工具定义缓存、动态内容不缓存——这个粒度的 cache 意识在大多数 LLM 应用里是缺失的。

**核心难点在于 Harness Engineering**。调用 API 是十行代码的事，只有把工具调用结果正确地反馈给模型、在流式输出中间插入用户交互、处理长任务里的错误恢复——这些才是构建 agent 工具/产品的真正挑战。

---

**链接**：
- 项目：纯 TypeScript，零框架，从零构建 Claude Code 等价实现
- 关联文章：《龙虾Token焦虑？深度拆解我基于Pimono二开的openclaw与如何节省token》
