# 同步阻塞 vs 异步编排：Hermes Delegate 与 OpenClaw 多 Agent 机制深度实战对比

## 作者信息
- **作者**：huangserva (@servasyy_ai)
- **平台**：X (Twitter)
- **发布时间**：2026年4月11日 21:00
- **原始链接**：https://x.com/i/status/2042951017462169812
- **浏览量**：1.7万

## 核心内容

### 两种设计哲学

| 框架 | 模式 | 特点 |
|------|------|------|
| **Hermes** | 总承包商-分包商 | 父agent阻塞等待，精简高效 |
| **OpenClaw** | 交响乐团编排 | 异步事件驱动，可发送"引导消息" |

---

### Hermes delegate：精简高效的并行执行器

**工作模式：**
- 单任务模式：提供一个goal参数启动单个子agent同步执行
- 批量模式：最多3个任务数组，通过ThreadPoolExecutor并行处理

**子Agent构造与隔离：**
- 每次委派创建全新AIAgent实例
- 拥有独立的对话历史、Terminal session、System Prompt
- 模型可继承父agent或使用delegation.model配置
- 工具集通过交集计算（子不能获得父没有的工具）

**严格工具剥夺：**
- delegate_task被禁用（防止递归委派）
- clarify被移除（不能与用户交互）
- memory工具被剥夺（保护共享记忆）
- execute_code被禁用（避免子agent编写复杂脚本）
- send_message被移除（防止跨平台消息发送）

**深度限制：**
- MAX_DEPTH = 2（父0 → 子1，不能再spawn孙子）
- 迭代上限默认50轮
- **致命短板：没有超时机制**（future.result()不带timeout参数）

**Token效率：**
- 纯粹单向返回，所有中间tool调用不进入父上下文
- 子agent是有损压缩器，将中间推理压缩为summary字符串

---

### OpenClaw Subagent：异步协作的编排系统

**三种角色：**
- main（主agent）
- orchestrator（编排器，可继续spawn子agent）
- leaf（叶节点，不可再spawn）

**默认配置：**
- 全局最多8路并发
- 每个agent最多管理5个活跃子agent
- 嵌套深度可配置

**核心创新：异步事件驱动通信**
- 父agent spawn子agent后立即返回，继续处理其他任务
- 子agent完成后，通过runSubagentAnnounceFlow()将结果以"user message"形式推送回父agent
- 推送式设计避免轮询开销

**Steer机制（OpenClaw独有）：**
- 父agent可以向运行中的子agent发送引导消息
- 触发其重新调整方向
- 限流保护：每2秒最多一次，消息最大4000字符

**完整生命周期管理：**
- runTimeoutSeconds参数（默认300秒）提供时间维度控制
- runs.json持久化运行记录支持orphan recovery
- resumeSessionId允许恢复已有会话

---

### 架构差异的深层逻辑

**同步 vs 异步：**
- Hermes：父agent在子运行期间完全停滞，无法响应新需求
- OpenClaw：父agent同时管理多个子agent，动态调整策略

**信息论视角：**
- Hermes子agent是有损压缩器，上下文零膨胀
- OpenClaw更像分布式系统，需要更复杂的状态管理

**安全视角：**
- Hermes的强隔离形成天然沙箱，适合安全敏感场景
- OpenClaw的子agent保留更多能力，攻击面更大

---

### 如何选择？场景决定架构

| 场景 | 推荐选择 |
|------|---------|
| 并行处理3件互不相关的事 | Hermes |
| 需要隔离并行的子任务 | Hermes |
| 需要在子agent运行中调整方向 | OpenClaw |
| 需要超时控制防止无限运行 | OpenClaw |
| 调用外部编码agent（Claude Code/Codex）作为子agent | OpenClaw |
| 构建多层嵌套的agent树 | OpenClaw |
| 超过3个agent并行工作 | OpenClaw |
| 长流程任务需要持久化和恢复 | OpenClaw |

---

### 混合架构：取长补短

最佳实践是根据任务特性选择合适模式：

```
OpenClaw异步编排层（处理复杂工作流）
    ↓
嵌入Hermes风格的delegate调用（隔离并行的子任务）
    ↓
OpenClaw的announce和steer机制（保持灵活性）
```

---

### Hermes的改进方向

1. **最高优先级**：加入timeout机制
2. **改进Gateway interrupt逻辑**：用户发送"？"时返回进度而非杀死所有agent
3. **中等优先级**：引入Steer能力、放宽并发上限、支持持久化和恢复
4. **长期**：支持外部Agent（通过ACP启动Claude Code/Codex）

---

## 数据亮点
- 浏览量：1.7万
- 转发：20
- 评论：95
- 点赞：176

## 关联 wiki 页面
- mentioned_in: [[00知识库Wiki/03概念沉淀/多智能体协作模式]]

---

*最后更新：2026-04-12*
