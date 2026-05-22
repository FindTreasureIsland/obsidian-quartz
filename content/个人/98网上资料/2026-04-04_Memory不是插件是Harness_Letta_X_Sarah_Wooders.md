# Memory不是插件，是Harness——MemGPT创始人的思考

## 作者信息
- **作者**：Sarah Wooders (@sarahwooders) + Charles Packer（MemGPT/Letta创始人）
- **平台**：X (Twitter)
- **发布时间**：2026年4月4日
- **原始链接**：https://x.com/i/status/2040121230473457921
- **浏览量**：5万+

## 核心内容

### 问题：如何把Memory系统接入我的Agent？

Sarah Wooders 和 Charles Packer（MemGPT/Letta创始人）被问得最多的一个问题：

> "如何把你们的Memory系统接入我的Agent？"

他们认为这个问题本身就有问题。

---

### 核心观点：Memory不是插件，是Harness

**"把Memory插入Agent"这个问题，就像问"如何把驾驶能力插入汽车"一样——驾驶不是一个插件，而是汽车这个Harness的核心能力。**

管理Context（上下文），进而管理Memory，是Agent Harness的**核心职责**。

如果Harness不管理Context，那它在干什么？

---

### RAG不是Memory

很多人把 MemGPT 误认为是一个"可插拔的Memory工具"，但 MemGPT 实际上是一个**有状态的Agent Harness**——早在"harness"这个词流行之前就已经是了。

Agent的Memory来自于：
1. Harness暴露的、用于重写Prompt的工具
2. 管理外部状态的工具
3. Harness自身的Context管理

RAG只是Memory的一个小部分，而且做得好的RAG效果和`grep`差不了多少。

---

### Harness做的隐性决策

一个外部插件无法控制的Harness隐性决策：

- AGENTS.md / CLAUDE.md 如何加载到Context？
- Skill元数据如何呈现给Agent？（System Prompt？System Messages？）
- Agent能否修改自己的System Instructions？
- 什么内容经过Compaction后存活，什么会丢失？
- 对话历史是否被存储并可查询？
- Memory元数据如何呈现给Agent？
- 当前工作目录如何表示？暴露了多少文件系统信息？

不同的Harness对每个问题的答案都不同。

---

### Claude Code的Memory架构

从Claude Code泄露源码分析来看，它的Memory系统设计极其精巧：

不是"存储一切"，而是**受限的、结构化的**多层Memory层级，直接构建在Harness内部。

---

### Letta的Context Constitution

Letta最新发布的Context Constitution：Agent应遵循的Context管理原则，这是Harness设计的基础。

---

## 数据亮点
- 浏览量：5万+
- 转发：182
- 评论：28
- 点赞：367
