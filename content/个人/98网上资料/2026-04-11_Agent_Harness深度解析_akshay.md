# The Anatomy of an Agent Harness

## 作者信息
- **作者**：Akshay (@akshay_pachaar)
- **平台**：X (Twitter)
- **发布时间**：2026年4月6日 21:31
- **原始链接**：https://x.com/akshay_pachaar/status/2041146899319971922
- **浏览量**：27.2万

## 核心内容

### 问题的本质
LangChain只改了harness（同样模型），从Top 30冲到TerminalBench第5名。

### 什么是 Agent Harness？

**定义：** 包裹在LLM外面的完整软件基础设施，包括：
- 编排循环（Orchestration Loop）
- 工具（Tools）
- 记忆（Memory）
- 上下文管理
- 状态持久化
- 错误处理
- 安全 guardrails

**一句话：** "如果你不是模型，那你就是harness。"

### 三层工程

| 层次 | 负责 |
|------|------|
| Prompt工程 | 模型的指令 |
| 上下文工程 | 模型看到什么、何时看到 |
| Harness工程 | 整个应用基础设施 |

### 生产级 Harness 的 12 个组件

1. **编排循环** — TAO循环（Thought-Action-Observation/ReAct）
2. **工具** — 模型的"手"，执行具体操作
3. **记忆** — 短中期（对话历史）、长期（跨会话）
4. **上下文管理** — 防止上下文腐烂
5. **Prompt构建** — 分层组装
6. **输出解析** — 结构化工具调用
7. **状态管理** — checkpointing、resume
8. **错误处理** — 10步99%成功率，组合后只有90%
9. **Guardrails** — 安全边界
10. **验证循环** — 2-3x质量提升
11. **子Agent编排** — Fork、Teammate、Worktree
12. **生命周期管理**

### 脚手架隐喻

- 脚手架不是建筑本身，但没了它工人上不了高层
- 模型越强，harness应该越薄
- 但harness不会消失——它管理上下文窗口、执行工具调用、持久化状态、验证结果

### 关键洞察

**下次你的Agent又崩了，别怪模型。看看你的harness。**

---

## 数据亮点
- 浏览量：27.2万
- 转发：28
- 评论：182
- 点赞：1,149
