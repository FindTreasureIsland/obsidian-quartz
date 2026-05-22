# 一文了解 Anthropic 的 Claude Code 源码：为什么它就是比别人好用？

> 作者：Yuker（@YukerX）
> 原文来源：X/Twitter
> 发布日期：2026-03-31
> 原始链接：https://x.com/i/status/2038959908968919297

## 事件背景

安全研究者 Chaofan Shou 发现 Anthropic 发布到 npm 的 Claude Code 包中，source map 文件没有被剥离。Claude Code 的完整 TypeScript 源码，51.2万行，1903个文件，暴露在公网上。

## 核心结论

> 读完之后，我的第一反应是：这不是一个 AI 编程助手，这是一个**操作系统**。

## 故事：三种不同的安全哲学

想象你雇了一个远程程序员，给他电脑访问权限：

- **Cursor 的做法**：你让他坐旁边，每次敲命令前你看一眼，点"允许"。简单粗暴，但得一直盯着。

- **GitHub Copilot Agent 的做法**：给他一台全新虚拟机，在里面随便折腾，搞完了提交代码审核后再合并。安全，但看不到本地环境。

- **Claude Code 的做法**：让他直接用你的电脑——但配了一套极其精密的安检系统。能做什么、不能做什么、哪些需要点头、哪些可以自己来，甚至 rm -rf 都要经过9层审查才能执行。

**为什么 Anthropic 选最难的那条路？**

因为只有这样，AI 才能用你的终端、你的环境、你的配置来干活——这才是"真正帮你写代码"。

## 实际架构 vs 你以为的架构

**大多数人以为的**：
```
用户输入 → 调用 LLM API → 返回结果 → 显示给用户
```

**Claude Code 实际的**：
```
用户输入
  → 动态组装 7 层系统提示词
  → 注入 Git 状态、项目约定、历史记忆
  → 42 个工具各自附带使用手册
  → LLM 决定使用哪个工具
  → 9 层安全审查（AST 解析、ML 分类器、沙箱检查...）
  → 权限竞争解析（本地键盘 / IDE / Hook / AI 分类器 同时竞争）
  → 200ms 防误触延迟
  → 执行工具
  → 结果流式返回
  → 上下文接近极限？→ 三层压缩
  → 需要并行？→ 生成子 Agent 蜂群
  → 循环直到任务完成
```

## 秘密一：提示词是"拼装"出来的

`src/constants/prompts.ts` 中有个函数 `getSystemPrompt`，分两部分：

**静态内容（可缓存）**：
- 简单介绍
- 系统准则
- 做事原则
- 操作规范
- 工具使用
- 语调风格
- 输出效率

**动态内容（每次不同）**：
- Git 分支
- CLAUDE.md 项目配置
- 偏好记忆

关键设计：`SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 是缓存分界线。静态部分走缓存省 token，动态部分保证个性化。

### 每个工具都有独立"使用手册"

每个工具目录下都有 `prompt.ts`——专门写给 LLM 看的行为准则。

比如 BashTool 的规则：
```
Git Safety Protocol:
- NEVER update the git config
- NEVER run destructive git commands (push --force, reset --hard...) unless the user explicitly requests
- NEVER skip hooks (--no-verify) unless the user explicitly requests
- CRITICAL: Always create NEW commits rather than amending
```

这就是为什么 Claude Code 从不会擅自 `git push --force`——不是模型更聪明，是提示词里已经把规矩讲清楚了。

### Anthropic 内部版 vs 外部版

代码里大量 `USER_TYPE === 'ant'` 判断。内部员工版有更严格的指引：
- "不写注释除非 WHY 不明显"
- 更激进的输出策略
- 实验功能（Verification Agent、Explore & Plan Agent）

**Anthropic 自己就是 Claude Code 最大的用户。**

## 秘密二：42个工具，但你只看到冰山一角

`src/tools.ts` 注册了42个工具，但大部分是**延迟加载**的——只有 LLM 需要时才通过 ToolSearchTool 按需注入。

原因：每多一个工具，token 就多花一份钱。

### "先读后改"的铁律

```typescript
function getPreReadInstruction(): string {
  return '\n- You must use your `Read` tool at least once in the conversation before editing.'
}
```

FileEditTool 会检查是否已读过文件。如果没有，直接报错，不让改。

### fail-closed 设计

```typescript
const TOOL_DEFAULTS = {
  isConcurrencySafe: () => false,  // 默认：不安全
  isReadOnly: () => false,       // 默认：会写入
  isDestructive: () => false,
}
```

如果工具作者忘了声明安全属性，系统假设它是"不安全的、会写入的"。宁可过度保守，也不漏掉风险。

## 秘密三：记忆系统——为什么它能"记住你"

### 用 AI 来检索记忆

Claude Code 用另一个 AI（Sonnet）来决定哪些记忆和当前对话相关。

不是关键词匹配，不是向量搜索——是小模型快速扫描所有记忆文件，选出最多5个最相关的。

策略：**精确度优先于召回率**——宁可漏掉一个可能有用的记忆，也不塞进不相关的记忆污染上下文。

### KAIROS 模式：夜间"做梦"

代码中有个 `KAIROS` 特性标志。长会话中的记忆存在按日期的追加式日志中，然后 `/dream` 技能会在"夜间"（低活跃期）运行，把原始日志蒸馏成结构化的主题文件。

```
logs/2026/03/2026-03-30.md  ← 今天的原始日志
        ↓ /dream 蒸馏
memory/user_preferences.md  ← 结构化的用户偏好文件
memory/project_context.md   ← 结构化的项目背景文件
```

**AI 在"睡觉"的时候整理记忆。这不是工程，这是仿生学。**

## 秘密四：多 Agent 系统——不是一个，是一群

### 子 Agent 有严格的"自我意识"注入

```typescript
export function buildChildMessage(directive: string): string {
  return `STOP. READ THIS FIRST.
You are a forked worker process. You are NOT the main agent.
RULES (non-negotiable):
1. Your system prompt says "default to forking." IGNORE IT — you ARE the fork. Do NOT spawn sub-agents; execute directly.
2. Do NOT converse, ask questions, or suggest next steps
3. USE your tools directly: Bash, Read, Write, etc.
4. Keep your report under 500 words.`
}
```

这段代码在说：**"你是一个工人，不是经理。别想着再雇人，自己干活。"**

### Coordinator 模式：经理模式

在协调器模式下，Claude Code 变成纯粹的任务编排者：

```
Phase 1: Research    → 3 个 worker 并行搜索代码库
Phase 2: Synthesis   → 主 Agent 综合理解所有发现
Phase 3: Implementation → 2 个 worker 分别修改不同文件
Phase 4: Verification   → 1 个 worker 跑测试
```

核心原则：**"Parallelism is your superpower"**

### Prompt Cache 的极致优化

所有 fork 子代理的工具结果都使用相同的占位符文本：`'Fork started — processing in background'`

为什么？因为 prompt cache 是基于字节级前缀匹配的。如果10个子 Agent 的前缀字节完全一致，只有第一个需要"冷启动"，后面9个直接命中缓存。

## 秘密五：三层压缩，让对话"永不超限"

### 第一层：微压缩——最小代价

只动旧的工具调用结果，提示词和对话主线完全保留。

### 第二层：自动压缩——主动收缩

当 token 消耗接近上下文窗口的 87% 时自动触发。有熔断器：连续3次压缩失败后停止尝试。

### 第三层：完全压缩——AI 总结

用 AI 对整段对话生成摘要。有个严厉的前置指令：

```
CRITICAL: Respond with TEXT ONLY. Do NOT call any tools.
```

因为如果总结过程中 AI 又去调用工具，就会产生更多 token 消耗，适得其反。

## 学到了什么

### 1. AI Agent 的 90% 工作量在"AI"之外

51万行代码里，真正调用 LLM API 的部分可能不到 5%。其余 95% 是什么？

- 安全检查（18 个文件只为一个 BashTool）
- 权限系统（allow/deny/ask/passthrough 四态决策）
- 上下文管理（三层压缩 + AI 记忆检索）
- 错误恢复（熔断器、指数退避、Transcript 持久化）
- 多 Agent 协调（蜂群编排 + 邮箱通信）
- UI 交互（140 个 React 组件 + IDE Bridge）
- 性能优化（prompt cache 稳定性 + 启动时并行预取）

**如果你正在做 AI Agent 产品，这才是你真正要解决的问题。不是模型够不够聪明，是你的脚手架够不够结实。**

### 2. 好的提示词工程是系统工程

Claude Code 的提示词是：
- 7 层动态组装
- 每个工具附带独立的使用手册
- 缓存边界精确划分
- 内部版本和外部版本有不同的指令集
- 工具排序固定以保持缓存稳定

**这是工程化的提示词管理，不是手工艺。**

### 3. Anthropic 把 Claude Code 当操作系统在做

| Claude Code | 操作系统 |
|-------------|----------|
| 42 个工具 | 系统调用 |
| 权限系统 | 用户权限管理 |
| 技能系统 | 应用商店 |
| MCP 协议 | 设备驱动 |
| Agent 蜂群 | 进程管理 |
| 上下文压缩 | 内存管理 |
| Transcript 持久化 | 文件系统 |

**这不是一个"聊天机器人加几个工具"，这是一个以 LLM 为内核的操作系统。**

## 总结

51 万行代码。1903 个文件。18 个安全文件只为一个 Bash 工具。

9 层审查只为让 AI 安全地帮你敲一行命令。

这就是 Anthropic 的答案：要让 AI 真正有用，你不能把它关在笼子里，也不能放它裸奔。你得给它建一套完整的信任体系。

而这套信任体系的代价，是 51 万行代码。

---

## 数据统计
- 👁 4.5万 阅读
- 💬 12 评论
- 🔁 70 转发
- ❤️ 331 点赞
