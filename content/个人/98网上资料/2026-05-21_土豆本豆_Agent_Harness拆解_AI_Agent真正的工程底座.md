---
title: "Agent Harness 拆解：AI Agent 真正的工程底座"
author: 土豆本豆
source: https://x.com/Potatoloogs/status/2057391224592667051
created: 2026-05-21
tags: [AI-Agent, Agent-Harness, 工程架构, Context-Management, Memory-System]
description: 深度拆解 Agent Harness——包裹在 LLM 外层的完整软件基础设施，包括编排循环、工具系统、记忆系统、上下文管理、状态持久化、错误处理和安全护栏。
stats:
  likes: 62
  retweets: 11
  views: 5311
cover_images:
  - https://pbs.twimg.com/media/HI1CEPabUAAQ6vz.jpg
---

# Agent Harness 拆解：AI Agent 真正的工程底座

这是一篇关于 Agent Harness 的深度拆解。

它解释了 Anthropic、OpenAI、Perplexity、LangChain 这些公司到底在构建什么：编排循环、工具调用、记忆系统、上下文管理，以及所有那些把一个"无状态 LLM"变成"可用智能体"的工程基础设施。

很多人一开始做的只是 chatbot。

再进一步，可能接了几个工具，写了一个 ReAct loop，看起来已经像 Agent 了。Demo 能跑，演示也挺顺。

但一旦你想做成生产级系统，问题就开始集中爆发：

- 模型忘了三步之前自己做过什么；
- 工具调用静默失败；
- 上下文窗口很快被垃圾信息填满；
- 任务链条稍微一长，结果就开始漂。

问题通常不在模型本身。

真正的问题，是模型外面那整套系统。

LangChain 之前就证明过这一点：他们没有换模型、没有换权重，只改了包在 LLM 外面的基础设施，就在 TerminalBench 2.0 上从 30 名开外跃升到第 5 名。

另一个研究项目甚至让 LLM 自己优化这套基础设施，最终达到了 76.4% 的通过率，超过了人工设计的系统。

这套基础设施，现在有了一个名字：**Agent Harness。**

---

## 一、什么是 Agent Harness？

Agent Harness 这个术语在 2026 年初被正式化，但它背后的概念很早就存在了。

Harness 指的是包裹在 LLM 外面的完整软件基础设施：

- orchestration loop，编排循环
- tools，工具系统
- memory，记忆系统
- context management，上下文管理
- state persistence，状态持久化
- error handling，错误处理
- guardrails，安全护栏

Anthropic 在 Claude Code 文档里说得很直接：

> SDK is the agent harness that powers Claude Code.
> Claude Code 背后的 SDK 就是驱动它的 Agent Harness。

OpenAI 的 Codex 团队也使用了类似说法，把 agent 和 harness 这两个词都用来指代模型之外的基础设施，也就是让 LLM 真正变得有用的那一层。

LangChain 的 Vivek Trivedy 有一个很经典的公式：

> If you're not the model, you're the harness.
> 只要你做的东西不属于模型本身，那它就属于 harness。

这里最容易混淆的是 agent 和 harness 的关系。

Agent 是用户感知到的行为。

它看起来有目标，会使用工具，会自我修正，会持续推进任务。

Harness 是产生这种行为的机器。

当一个人说"我做了一个 Agent"，他做的是一个 harness，然后把它连接到了一个模型上。

---

## 二、用计算机系统来理解 Agent Harness

Beren Millidge 在 2023 年的文章《Scaffolded LLMs as Natural Language Computers》里，给过一个非常准确的类比。

裸 LLM 就像一颗 CPU：

- 它没有 RAM，
- 没有硬盘，
- 没有 I/O，
- 也没有操作系统。

上下文窗口相当于 RAM：速度快，但容量有限。

外部数据库相当于硬盘：容量大，但读写慢。

工具集成相当于设备驱动。

而 harness，就是操作系统。

Millidge 说：

> We have reinvented the Von Neumann architecture.
> 我们其实是在重新发明冯·诺依曼架构。

原因很简单：只要你要构建一个真正能运行任务的计算系统，这套抽象几乎自然会出现。

---

## 三、围绕模型的三层工程

围绕 LLM，有三层工程：

**Prompt Engineering**：Prompt Engineering 负责写模型收到的指令，告诉模型怎么做。

**Context Engineering**：Context Engineering 负责管理模型能看到什么、什么时候看到。

**Harness Engineering**：Harness Engineering 包含前两者，还包括整套应用基础设施：

- 工具编排
- 状态持久化
- 错误恢复
- 验证循环
- 安全控制
- 生命周期管理

Harness 不是包在 prompt 外面的一层壳。

它是让自主智能体行为成为可能的完整系统。

---

## 四、一个生产级 Harness 的 12 个组件

从 Anthropic、OpenAI、LangChain 的实践中，可以归纳出生产级 Agent Harness 的 12 个组件。

### 1. Orchestration Loop：编排循环

编排循环让整个系统持续运转。

它实现的是 Thought-Action-Observation 循环，也就是常说的 TAO 或 ReAct loop。

基本过程是：

1. 组装 prompt
2. 调用 LLM
3. 解析输出
4. 执行工具调用
5. 把结果返回给模型
6. 重复，直到任务结束

从代码层面看，它可能只是一个 while loop。

真正复杂的地方，在于这个 loop 管理的所有东西。

Anthropic 把自己的运行时描述为一个 "dumb loop"：

> 循环本身很笨，智能都在模型里。

Harness 负责管理每一轮交互。

### 2. Tools：工具

工具让 Agent 能操作外部世界。

工具通常会被定义成 schema，包括：

- 工具名称
- 工具描述
- 参数类型
- 输入输出格式

这些 schema 会被注入到模型上下文里，让模型知道自己能调用什么。

工具层要处理很多事情：

- 工具注册
- schema 校验
- 参数提取
- 沙箱执行
- 结果捕获
- 把工具结果格式化成模型能理解的 observation

Claude Code 的工具分为六类：

1. 文件操作
2. 搜索
3. 命令执行
4. Web 访问
5. 代码智能
6. 子 Agent 生成

OpenAI Agents SDK 支持 function tools、hosted tools，以及 MCP server tools。

### 3. Memory：记忆

Memory 有多个时间尺度。

**短期记忆**：短期记忆是单次 session 内的对话历史。

**长期记忆**：长期记忆跨 session 保留。

例如：

- Anthropic 使用 CLAUDE.md 项目文件和自动生成的 MEMORY.md 文件。
- LangGraph 使用按 namespace 组织的 JSON Stores。
- OpenAI 支持基于 SQLite 或 Redis 的 Sessions。

Claude Code 的记忆系统是三层结构：

1. 轻量索引：每条约 150 个字符，始终加载
2. 详细 topic files：按需拉取
3. 原始 transcripts：只通过搜索访问

Agent 应该把自己的记忆当作 hint，而不是事实本身。行动前，用真实状态再验证一遍。

### 4. Context Management：上下文管理

很多 Agent 会在这里悄悄失败。

核心问题是 context rot：上下文腐烂。

研究显示，当关键信息落在上下文窗口中间位置时，模型性能可能下降 30% 以上。

这也和 Stanford 的 "Lost in the Middle" 发现一致。

即使是百万 token 上下文窗口，随着上下文变长，模型的指令遵循能力也会下降。

生产级策略通常包括：

**Compaction（压缩）**：当接近上下文限制时，对历史对话进行总结。Claude Code 会保留架构决策和未解决 bug，同时丢弃重复的工具输出。

**Observation Masking（观察结果遮蔽）**：JetBrains 的 Junie 会隐藏旧工具输出，但保留工具调用可见。

**Just-in-time Retrieval（即时检索）**：系统只保留轻量标识符，需要时再动态加载数据。Claude Code 会优先使用 grep、glob、head、tail，而不是一次性加载完整文件。

**Sub-agent Delegation（子 Agent 委派）**：每个子 Agent 可以探索大量上下文，但最后只返回 1000 到 2000 token 的浓缩摘要。

Anthropic 的 context engineering guide 说得很准：

> 目标是找到最小但高信号的 token 集合，最大化模型完成目标的概率。

### 5. State Persistence：状态持久化

Agent 的运行状态必须持久化，否则每次重启都失忆。

状态类型包括：

- 当前目标
- 进度快照
- 中间结果
- 决策历史

Anthropic 的 Claude Code 会在每次执行后保存 progress 文件：

```
MEMORY.md
CLAUDE.md
```

这些文件在下次启动时被读取，让 Agent 恢复到之前的进度。

### 6. Error Handling & Retry：错误处理与重试

Agent 的错误处理需要分类型：

**确定性错误**：网络超时、工具 schema 不匹配——直接重试

**不确定性错误**：LLM 调用超时、rate limit——指数退避重试

**语义错误**：LLM 返回格式不对、结果不符合预期——需要重试或降级

Agent harness 需要实现**自动错误恢复**，而不只是抛出异常。

### 7. Guardrails：安全护栏

护栏在模型输出到达外部世界之前进行检查。

典型护栏：

- 禁止执行危险命令（rm -rf /）
- 拦截敏感数据外泄
- 检查工具调用权限
- 防止 prompt injection

Anthropic 把护栏分为两类：

**Guards（前馈）**：在行动前拦截

**Sensors（反馈）**：在行动后观察

### 8. Multi-Agent Orchestration：多 Agent 编排

当单 Agent 扩展到极限时，需要多 Agent 协作。

VLA 报告称，多 Agent 系统中的失败有 40% 来自 agent 间通信问题。

关键问题：

- 何时创建新 Agent
- 如何分配任务
- 如何处理 Agent 间上下文传递
- 如何合并多 Agent 结果

### 9. Routing & Planning：路由与规划

ReAct 会在每一步交织推理和行动。

Plan-and-execute 会把规划和执行分开。

LLMCompiler 报告称，相比顺序 ReAct，它能带来 3.6 倍速度提升。

但规划本身也有成本：过于详细的规划可能导致过度思考，过于简单的规划又可能导致执行失败。

### 10. Observability：可观测性

Agent 的可观测性比传统软件更难。

因为模型输出不确定，推理过程不透明。

关键可观测性维度：

- 每轮 token 消耗
- 工具调用成功率
- 任务完成率
- 中间步骤的 token 分布

Agent 工作单元不像 API 调用，不能简单用延迟和错误率衡量。

### 11. Lifecycle Management：生命周期管理

Agent 的生命周期管理：

- 启动时初始化 harness
- 运行中管理状态
- 完成后保存结果
- 失败时优雅退出

### 12. Tool Definition Management：工具定义管理

工具定义的演进是 harness 复杂度的重要来源。

Manus 在六个月内重写了五次，每次重写都在删除复杂性：

- 复杂工具定义变成了通用 shell execution
- "管理型 Agent" 变成了简单的结构化 handoff

这指向一个 co-evolution principle：

> 模型现在会在特定 harness 中参与后训练。

所以，随意更换工具实现，可能导致性能下降。

因为模型和 harness 之间已经形成了紧耦合。

---

## 五、生产级 Harness 的共同模式

### Anthropic Claude Agent SDK

Anthropic 的 Claude Agent SDK 通过一个 query() 函数暴露 harness。

这个函数会创建 agentic loop，并返回一个 async iterator 来流式输出消息。

运行时本身是 "dumb loop"。智能留给模型。

Claude Code 使用的是 Gather-Act-Verify 循环：

- Gather context：搜索文件、阅读代码
- Act：编辑文件、运行命令
- Verify：运行测试、检查输出
- Repeat：继续循环

### OpenAI Agents SDK

OpenAI Agents SDK 通过 Runner class 实现 harness，有三种模式：

- async
- sync
- streamed

这个 SDK 是 code-first 的。

工作流逻辑用原生 Python 表达，而不是图 DSL。

Codex harness 在此基础上扩展成三层架构：

1. Codex Core：agent code + runtime
2. App Server：双向 JSON-RPC API
3. Client Surfaces：CLI、VS Code、Web App

所有界面共享同一套 harness。

这也是为什么 Codex 模型在 Codex surfaces 上用起来会比普通聊天窗口更顺。

模型相同，运行环境不同，表现就会不同。

### LangGraph

LangGraph 把 harness 显式建模成 state graph。

最简单的结构是两个节点：

- llm_call
- tool_node

它们之间通过 conditional edge 连接：

- 如果有 tool calls，路由到 tool_node
- 如果没有 tool calls，路由到 END

LangGraph 是从 LangChain 的 AgentExecutor 演进而来。

AgentExecutor 在 v0.2 被弃用，因为它难扩展，也缺少多 Agent 支持。

### CrewAI

CrewAI 实现的是基于角色的多 Agent 架构。

它有三个核心概念：

**1）Agent**：包在 LLM 外面的 harness，由 role、goal、backstory 和 tools 定义。

**2）Task**：任务单元。

**3）Crew**：多个 Agent 的集合。

CrewAI 的 Flows 层进一步提供了一条"确定性骨架"。

它负责路由和校验，Crew 则负责自治协作。

换句话说，流程控制交给 deterministic backbone，智能部分交给 Agent。

### AutoGen

AutoGen 正在演进为 Microsoft Agent Framework。

它比较早提出了 conversation-driven orchestration。

它的三层架构是：

- Core
- AgentChat
- Extensions

支持五种编排模式：

- sequential
- concurrent，fan-out / fan-in
- group chat
- handoff
- magentic

其中 magentic 模式会让一个 manager agent 维护动态任务账本，协调多个 specialist。

---

## 六、Scaffolding：脚手架这个比喻为什么准确？

Scaffolding 这个词不是装饰性的比喻。

它非常精准。

建筑脚手架是一套临时基础设施。

它不会自己建楼。

但没有它，工人够不到高层。

Agent Harness 也是一样。

它不直接产生智能。

但没有它，模型无法稳定完成复杂任务。

但脚手架在建筑完成后会被拆掉。

随着模型变强，harness 的复杂度应该逐渐下降。

Manus 在六个月内重写了五次，每次重写都在删除复杂性。

复杂工具定义变成了通用 shell execution。

"管理型 Agent" 变成了简单的结构化 handoff。

这指向一个 co-evolution principle：

> 模型现在会在特定 harness 中参与后训练。

Claude Code 的模型学会了使用它训练时绑定的那套 harness。

所以，随意更换工具实现，可能导致性能下降。

因为模型和 harness 之间已经形成了紧耦合。

判断一个 harness 设计是否稳健，可以问一个问题：

> 当模型能力提升时，这套 harness 是否能自然吃到模型红利，而不需要继续增加复杂度？

如果答案是肯定的，设计就比较健康。

---

## 七、每个 Harness 架构师都要做的 7 个选择

### 1. Single-agent 还是 Multi-agent？

Anthropic 和 OpenAI 都建议：先把单 Agent 做到极限。

多 Agent 会带来额外开销：

- 额外 LLM 调用
- 路由成本
- handoff 时的上下文损失

只有当工具数量超过约 10 个重叠工具，或者任务领域明显分离时，再考虑拆成多 Agent。

### 2. ReAct 还是 Plan-and-execute？

ReAct 会在每一步交织推理和行动。

它灵活，但每一步成本更高。

Plan-and-execute 会把规划和执行分开。

LLMCompiler 报告称，相比顺序 ReAct，它能带来 3.6 倍速度提升。

### 3. 上下文窗口管理策略

生产环境中常见五种策略：

1. 基于时间清理
2. 对话总结
3. observation masking
4. 结构化记笔记
5. 子 Agent 委派

ACON 研究显示，通过优先保留 reasoning traces，而不是原始工具输出，可以减少 26% 到 54% 的 token，同时保持 95% 以上准确率。

### 4. 验证循环设计

计算型验证提供确定性真值，例如：

- tests
- linters
- type checkers

推理型验证，比如 LLM-as-judge，可以发现语义问题，但会增加延迟。

Martin Fowler 的 Thoughtworks 团队把这类机制分成两类：

**1）Guides**：前馈机制，在行动前引导模型。

**2）Sensors**：反馈机制，在行动后观察结果。

一个好的 harness 通常两者都需要。

### 5. 权限和安全架构

这里有两个方向：

**1）Permissive**：更快，但风险更高。多数操作自动批准。

**2）Restrictive**：更安全，但更慢。每个关键操作都要确认。

怎么选，取决于部署场景。

个人本地工具、企业生产系统、金融医疗场景，对安全边界的要求完全不同。

### 6. 工具范围策略

工具不是越多越好。

更多工具经常意味着更差的表现。

Vercel 从 v0 中移除了 80% 的工具，结果表现变好了。

Claude Code 通过 lazy loading 实现了 95% 的上下文压缩。

原则很简单：

> 当前步骤只暴露最少、最必要的工具。

### 7. Harness 厚度

也就是：多少逻辑放在 harness 里，多少交给模型。

Anthropic 倾向于 thin harness，相信模型会持续变强。

图式框架更倾向于显式控制，把更多逻辑写在外部系统里。

Anthropic 会随着新模型版本发布，定期从 Claude Code harness 中删除规划步骤。

因为新模型已经把部分能力内化了。

---

## 八、Harness 本身就是产品

两个产品即使用完全相同的模型，也可能因为 harness 设计不同，表现差很多。

TerminalBench 的证据很清楚：

> 只改 harness，就能让 Agent 排名提升 20 多位。

Harness 不是一个已经解决的商品化层。

它恰恰是最难的工程部分。把上下文当稀缺资源管理，设计验证循环避免错误复合，构建记忆系统同时控制幻觉——这些都不简单。

还有更基本的问题：脚手架该建多厚，哪些能力该交给模型、哪些要留在系统里。

整个行业正在走向更薄的 harness。

因为模型变强之后，很多外部脚手架会被吸收进模型能力里。

但 harness 不会消失。

再强的模型，也需要某些东西来管理上下文窗口、执行工具调用、持久化状态，并验证结果。

所以下次你的 Agent 失败时，别急着骂模型。

先看看它外面的 harness。
