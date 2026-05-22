# I want to build an AI agent today (full course)

> 来源：X (Twitter) @hooeem  
> 发布时间：2026年3月27日  
> 链接：https://x.com/i/status/2037250422403113188  
> 观看：167.6万 | 转帖：608 | 喜欢：3762 | 书签：15013

---

## 前言

没有人做过一个完整的课程，让任何人都能从零开始创建 AI agent。

如果你想的话，你可以读这篇文章，然后创建一个对你有用的 agent——因为为了做 agent 而做 agent 没有任何意义，它需要有一个目的。

作者从 Anthropic、OpenAI 和互联网上其他专家那里收集资源，与 Claude 一起创建了一个面向小白的完整课程。

---

## 目录

1. How agents work
2. Five workflows
3. Building your agent
4. Utilising tools
5. Giving your agent memory
6. Making your agent work
7. Multiple agents
8. Wrapping it all up

---

## 1: HOW AGENTS WORK

所有 agents 的核心循环：

```
User input → LLM thinks → LLM decides (respond or call a tool) → if tool: execute it, feed result back → repeat
```

- LLM = 推理的"大脑"
- Tools = 执行动作的"手"（计算器、搜索、文件操作）
- Memory = 记录发生事情的"笔记本"

### Augmented LLMs（增强型 LLM）

普通 LLM 只接收文本并输出文本。增强型 LLM 添加三个能力：

1. **Tools**：模型可以调用的函数（计算器、数据库、API、文件操作等）
2. **Retrieval**：从外部来源提取相关信息的能力（搜索引擎、文档、向量数据库）
3. **Memory**：通过消息历史或持久存储在交互中保留信息的能力

### Workflows vs. True Agents

| | Workflows | Agents |
|---|---|---|
| 执行方式 | 确定性；代码控制 | 动态；LLM 决定下一步 |
| 适用场景 | 固定步骤的明确定义任务 | 开放式任务 |
| 成本 | 更便宜 | 更贵 |

建议：从简单 workflow 开始，看是否需要升级为 autonomous agent。

---

## 2: THE FIVE CORE WORKFLOW PATTERNS

大多数问题实际上不需要完整的自治就能解决。这五个模式覆盖了常见场景：

### Pattern 1: Prompt Chaining（提示词链）

将任务分解为顺序步骤。每个 LLM 调用处理前一个的输出。在步骤之间添加程序化"门"来验证质量。

适用场景：可以干净地分解为固定子任务的任务。

### Pattern 2: Routing（路由）

对传入输入进行分类，然后路由到专门的处理器。每个处理器获得自己优化的提示词。

适用场景：不同类别的输入需要根本不同的处理。

### Pattern 3: Parallelisation（并行化）

同时运行多个 LLM 调用。Sectioning 将任务分成独立子任务并行处理。Voting 多次运行同一任务并聚合结果以获得更高置信度。

适用场景：子任务独立（sectioning）或需要对关键决策达成共识（voting）。

### Pattern 4: Orchestrator-workers（编排器-工作者）

中央 LLM（编排器）动态分解任务并将子任务委托给工作者 LLM。与并行化不同，子任务是预先未定义的，编排器在运行时决定。

适用场景：无法提前预测结构的复杂任务。

### Pattern 5: Evaluator-optimiser（评估器-优化器）

一个 LLM 生成输出，另一个评估并提供反馈。如果评估失败，反馈循环回去。重复直到满足质量标准。

适用场景：存在明确的评估标准且迭代改进能增加可衡量价值的场景。

---

## 3: BUILDING YOUR AGENT

### 构建 Agent 的四个问题

1. **结果是什么？** Agent 实际应该产生什么？
2. **需要什么信息？** 它需要网络搜索、文件、数据库、电子表格、CRM，还是只需要用户的消息？
3. **允许执行什么操作？** 只能回答？能搜索？能编辑文件？能发送邮件？能写代码？能调用自定义函数？
4. **必须遵守什么规则？** 语气、格式、约束、安全规则、不确定时怎么做、"好"的标准是什么。

如果你能清楚回答这四个问题，通常一天内就能构建出第一版 agent。

### Agent 设计公式

```
Agent = Role + Goal + Tools + Rules + Output format
```

### 五种初学者 Agent 类型

1. **Research agent** — 收集信息并总结（需要：网络搜索、文件搜索、清晰输出格式）
2. **Content agent** — 写、改写、总结或转换内容（需要：强系统提示词、可选文件访问）
3. **Workflow agent** — 遵循可重复的业务流程（需要：明确分类、规则、自定义工具）
4. **Personal knowledge agent** — 使用你的文档回答问题（需要：文件搜索或 RAG）
5. **Operator agent** — 在环境中执行操作（需要：工具、权限、强的安全边界）

### Anthropic vs OpenAI 选择指南

**选择 Anthropic**，如果你想要：
- 读写和编辑文件
- 使用 shell 命令
- 搜索网络
- 使用 MCP 工具
- 良好的编码和技术任务
- 像一个能干的助手一样一步一步操作

**选择 OpenAI**，如果你想要：
- 非常干净的 agent API
- 简单的自定义函数工具
- 内置托管工具
- 专家之间的handoffs
- guardrails 和 tracing
- 从原型到生产的平滑路径

### 构建步骤

```
Step 1: 写一句话描述 agent
Step 2: 让 Claude 或 ChatGPT 帮你转化为：agent spec、system prompt、tool list、10 个测试提示
Step 3: 构建最小可行版本（不要多 agent、复杂 memory、RAG）
Step 4: 用 10 个真实例子测试
Step 5: 一次改进一件事
```

---

## 4: UTILISING TOOLS

### 核心原则

- **More tools ≠ smarter agent**
- **Better tools = smarter agent**
- **Fewer tools = more reliable agent**

### 工具添加决策

问自己：模型能仅用推理回答吗？还是需要真实世界数据或操作？

- 不需要工具：改写邮件、总结文本、解释概念
- 需要工具：查天气、搜索最新新闻、计算复利、从电子表格拉数据

### 工具设计原则

- **一个工具 = 一个明确的工作**
- Bad: `manage_files(action, file, destination, overwrite, format, permissions)`
- Good: `read_file(path)` / `write_file(path, content)` / `delete_file(path)`

### 告诉 Agent 何时使用工具

- Bad: "Calculator tool"
- Good: "Use this tool whenever maths is required. Never guess calculations."

---

## 5: GIVE YOUR AGENT MEMORY

### 两种类型的 Memory

1. **Short-term memory（短期记忆）** = "到目前为止说过什么"
   - 默认处理，你不需要做任何事

2. **Long-term memory（长期记忆）** = "以后可以查找的东西"
   - 你的笔记、PDF、文档、数据库

### Memory 决策

- 需要跨消息记住东西？→ 是 → 短期
- 需要使用外部文档？→ 是 → 长期
- 否则 → 你可能不需要

### 三个选项

- **Option A: No memory（从这里开始）** — 适合70%的用例
- **Option B: Conversation memory** — SDK 默认处理，不重置消息即可
- **Option C: File-based memory（简单 RAG）** — 上传文档，使用文件搜索工具

👉 规则：如果 agent 没有 memory 就能工作，就不要加它。

---

## 6: MAKING YOUR AGENT WORK IRL

### 测试是一切

用 AI 创建真实测试用例：
```
创建15个真实用户输入：
- 凌乱的
- 模糊的
- 真实世界风格的
- 包括边缘情况
- 包括混乱输入
- 包括错误输入
```

### 像真实用户一样测试

- 不要测：`"Please classify this billing request"`
- 要测：`"why tf did i get charged again"`

### 失败时问

- 提示词不清楚？
- 输出格式模糊？
- 缺少工具？
- 缺少规则？

---

## 7: MULTIPLE AGENTS

### 核心原则

- **More agents ≠ more powerful**
- 从一个 agent 开始，总是如此

### 只有这三种情况需要多 Agent

1. **不同的技能** — 研究 agent + 写作 agent
2. **明确的 pipeline** — Input → Analyse → Write → Output
3. **不同的权限** — 一个 agent 可以读数据，另一个可以执行操作

### 最安全的模式

Supervisor model: `User → Main agent → (calls others if needed)`

不要从 swarm 或完全自治的多 agent 系统开始——它们容易崩溃。

---

## 8: WRAPPING THIS ARTICLE UP

### 三个可操作的要点

1. **先从零开始构建 agent**
   理解原始循环让每个框架都透明而不是神奇。你会更快调试问题，更明智地选择工具。

2. **从最简单的模式开始**
   Prompt chain 处理大多数多步骤任务。Routing pattern 处理大多数分类然后行动的工作流。只有当你需要 LLM 动态决定执行路径时，才升级到自治 agent。

3. **尽早投资工具设计和评估**
   设计良好的工具（名称清晰、描述准确、结构化错误消息）比切换模型或框架更能提高 agent 性能。20个好的测试用例比任何手动测试都能捕获更多 bug。

### MCP 一年成为通用标准，两个主要提供商都推出了 Agent SDK，新框架每月出现。但本指南的基础是稳定的：agentic loop、五个工作流模式、良好工具设计的原则、从简单开始的纪律。掌握这些，你就能适应接下来发生的事情。

---

**YOU CAN NOW BUILD AN AGENT.**
