---
title: "Agent Harness Engineering"
author: Addy Osmani
source: X.com
tags: [AI, Agent, Harness-Engineering, 提示词工程, Claude-Code, 代理框架]
date: 2026-05-10
stats:
  likes: 1797
  retweets: 230
  views: 307019
---

# Agent Harness Engineering

**来源**：https://x.com/i/status/2053231239721885918

**作者**：Addy Osmani（@addyosmani，Google Chrome团队，工程经理）

**发布时间**：2026-05-09

---

## 核心定义

> Agent = Model + Harness. If you're not the model, you're the harness.

A coding agent is the model plus everything built around it. Harness engineering treats that scaffolding as a living artifact, tightening it every time the agent makes a mistake.

Simply put: **whenever an agent fails, you engineer a permanent solution so it never makes that exact mistake again.**

---

## 为什么模型只是系统的一半

过去两年行业一直在争模型：哪个最聪明，哪个写 React 最干净，哪个幻觉最少。

但这错过了系统的另一半。模型只是运行中 agent 的一个输入。其余的都是 harness：提示词、工具、上下文策略、hooks、沙箱、子 agent、反馈循环和恢复路径。

**一个 decent model 加 great harness  consistently 打败 great model 加 bad harness。**

越来越明显，最有趣的工程工作不在选择模型，而在设计周围的脚手架。

---

## Harness 实际上包含什么

| 类别 | 内容 |
|------|------|
| **Prompts** | System prompts, CLAUDE.md, AGENTS.md, skill files, subagent instructions |
| **Tools** | Tools, skills, MCP servers, 及其技术描述 |
| **Infrastructure** | Filesystem, sandboxes, headless browsers |
| **Orchestration** | Spawning subagents, handling handoffs, routing models |
| **Hooks & Middleware** | Deterministic execution like lint checks or context compaction |
| **Observability** | Logs, traces, cost, latency metering |

**Agent 的核心是：一个系统，在循环中运行工具以实现目标。真正的技能在于设计工具和那个循环。**

Claude Code, Cursor, Codex, Aider, Cline 都是 harnesses。底层模型可能在各平台相同，但你体验到的行为由 harness 决定。

---

## 重新审视 "Skill Issue"

当 agent 做出荒谬的事情时，工程师通常会责怪模型，认为"等下一个版本"就好了。

Harness-engineering 思维拒绝这种默认。失败通常是可以理解的：
- 如果 agent 忽略了一个 convention，把它加到 AGENTS.md
- 如果它运行了破坏性命令，写一个 hook 来阻止它
- 如果它在 40 步任务中迷失了，把架构分成 planner 和 executor
- 如果它总是以 broken code 结束，把类型检查 back-pressure 信号接入循环

**正如 HumanLayer 所说："不是模型问题。是配置问题。"**

一个 leading model 在现成框架中运行通常得分远低于同一个 model 在 custom, highly-tuned harness 中运行。把 model 移入有更好 codebase tools、tighter prompts、sharper back-pressure 的环境，可以解锁原始设置留下的能力。

**今天的模型理论上能做的，和你实际看到它们做的之间的差距，很大程度上是 harness gap。**

---

## The Ratchet：每个错误都变成一条规则

Harness engineering 中最重要的习惯：**把 agent 的错误当作永久信号，而不是一次性的侥幸，要 retry 然后忘记。**

如果 agent 提交了一个带有注释掉测试的 PR 被意外合并了，那是输入。下一次 AGENTS.md 必须说明："Never comment out tests; delete or fix them." 下一次 pre-commit hook 应该自动标记 diff 中的 .skip(。Reviewer subagent 必须更新以阻止注释掉的测试。

约束应该只在你观察到真实失败时添加，只在 capable model 使它们冗余时移除。好的 system prompt 中的每一行都应该追溯到一个具体的、历史的失败。

**因此，harness engineering 是一门学科，而不是一刀切的框架。特定代码库的正确 harness 完全由其独特的失败历史塑造。**

---

## Working backwards from behavior

设计 harness 最有效的方式是从期望的行为开始，建立提供该行为的组件：

```
Desired behavior → Harness design to achieve it
```

Harness 的每个部分必须有明确的工作。如果你不能命名一个组件存在的特定行为，它应该被删除。

---

## 核心组件设计

### Filesystem and Git — 持久状态

Filesystem 是基础。模型只能操作适合其上下文窗口的内容。Filesystem 提供了读取数据的工作区、存放中间工作的地方，以及多个 agent 协调的表面。

添加 Git 提供免费版本控制，允许 agent 跟踪进度、分支实验、回滚错误。

### Bash and Code Execution — 通用工具

大多数 agent 在 ReAct 循环上操作：reason, act via a tool call, observe, repeat。不必为每个可想象的动作预构建工具，给 agent bash 访问允许它按需构建所需的东西。

Agent 通常擅长 shell 命令，使 bash 和代码执行成为自主问题解决的默认策略。

### Sandboxes and Default Tooling

Bash 只有在安全运行时才有用。Sandbox 为 agent 提供隔离环境来运行代码、检查文件、验证工作而不危Host machine。

一个好的 sandbox 带有强默认：预装语言运行时、测试 CLI、headless browsers，允许 agent 观察自己的工作并关闭自我验证循环。

### Memory and Search — 持续学习

模型的 knowledge beyond 训练权重和当前上下文。Harness 使用 memory 文件（如 AGENTS.md）将知识注入每个会话。

对于实时信息（如新库版本或实时数据），网络搜索和 MCP 工具直接 baked 进入 harness。

---

## Battling Context Rot

模型在上下文窗口填满时 reasoning 能力下降。Harness 使用三种主要技术管理这种稀缺：

| 技术 | 说明 |
|------|------|
| **Compaction** | 智能总结和 offload 旧上下文以防止 API 错误 |
| **Tool-call offloading** | 将 massive tool 输出存储在文件系统，同时只保留 context 中重要的 headers 和 footers |
| **Progressive disclosure** | 仅在任务明确需要时才揭示指令和工具，而不是在启动时加载一切 |

---

## Long-Horizon Execution

自主的、长时间运行的工作容易 early stopping 和 poor problem decomposition。Harness 通过结构性设计来对抗：

- **Loops** — 拦截 model 试图退出的行为，迫使其在 fresh context window 中继续朝着 completion goal 努力
- **Planning** — 强制 model 将目标分解为逐步计划文件，在每步后通过 self-verification hooks 检查其工作
- **Splits** — 将 generation 和 evaluation 分离成不同的 agent，防止 model 给自己的工作打分时固有的 positive bias

---

## Hooks 是你的 Enforcement Layer

Hooks 弥合请求动作和执行之间的差距。它们在特定生命周期运行：tool call 之前、file edit 之后、commit 之前。

Hooks 阻止破坏性命令，强制 auto-formatting 以节省 tokens，运行 test suites。

理想情况下，成功是 silent 的，失败是 verbose 的。如果 typecheck 通过，agent 听不到任何声音；如果失败，错误直接注入循环以进行 self-correction。

---

## 规则手册和工具选择

代码库根目录的 flat markdown 文件仍然是最高杠杆的配置点。然而，它必须被视为飞行员的 checklist，而不是 style guide。

**保持简短，确保每条规则都通过过去的失败赢得。**

同样的纪律适用于工具。十个高度专注的工具总是优于五十个重叠的工具。

此外，因为 tool descriptions 填充提示词，恶意或草率的外部集成（如未验证的 MCP servers）可以在 agent 开始工作之前注入坏提示词。

---

## 生产环境中的样子

最清晰的公开图片是 Fareed Khan 对 Claude Code 架构的（估计）分解。

几乎前一部分的每个概念都作为命名组件出现在这个图表中：
- Context injection 是 knowledge layer
- Loop state 存在于 memory store 和 worktree isolator
- Destructive-action hooks 位于 permission gate 后面
- Subagent context firewalls 是整个 multi-agent layer
- Tool dispatch registry 是 MCP servers 和 bash 都插入的地方

**Claude Code 的 trajectory 至少与其下面的 model 一样是关于 harness 的。**

---

## Harnesses Don't Shrink, They Move

随着模型改进，对 harness 的需求不会消失——它会转移。

近期模型升级大大减少了"context-anxiety" mitigation 的需求。但随着 floor 上升，ceiling 也上升了。之前无法触及的任务现在可以做了，带来全新的失败模式。

**Harness 中的每个组件都对 model 不能独立做什么做出了假设。当 model 改进时，过时的脚手架应该被移除，而新的脚手架必须被构建以达到下一个 horizon。**

---

## Training Loop 的反馈

Harness 设计和 model 训练之间有一个 active feedback loop。

今天的模型通常在特定 harness 在循环中的情况下进行 post-training，产生一定程度的 overfitting。Model 在 harness 设计者优先的特定动作（如 filesystem ops, bash, subagent dispatch）上变得异常出色。

**这使得 harness 成为一个活的系统，而不是静态配置文件，并且证明"最好的" harness 是针对你独特任务和工作流优化的那个。**

---

## Harness-as-a-Service (HaaS)

行业正在从在 LLM APIs 上构建（提供 completions）转向在 Harness APIs 上构建（提供 runtime）。SDK 现在开箱即提供 loop、tools、context management、hooks、sandboxes。

现代默认不再是从头构建编排，而是选择 harness framework，配置其核心支柱，纯綷关注领域特定的 prompt 和 tool design。

这就是使故障排除可扩展的原因：你是在调优一个 factored configuration surface，而不是重新发明整个 agent 架构。

---

## Where This Is Going

如果你看今天 top 的 coding agents，它们彼此之间比底层模型更相似。模型不同，但 harness patterns 正在收敛。行业正在快速识别将生成文本转换为可发布软件所需的 load-bearing scaffolding。

最令人兴奋的 open problems 正在超越单个 agent：
- 在 parallel 中编排多个 agent
- 让 agent 分析自己的 traces 以修复 harness-level 失败
- 构建动态即时组装工具的环境

**最终，这是 harnesses 停止成为静态配置文件，开始更像是编译器的阶段。**

---

## 资源

如果你在寻找一个很好的 agent harness framework，@FredKSchott 写了 Flue。它很 solid，显然受了这篇文章早期版本的启发！

---

**原文链接**：https://x.com/i/status/2053231239721885918