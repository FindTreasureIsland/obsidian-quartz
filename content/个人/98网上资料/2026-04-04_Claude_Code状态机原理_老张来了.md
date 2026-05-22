# Claude Code 的心脏：Agent 状态机是怎么工作的

## 作者信息
- **作者**：老张来了 (@laozhang2579)
- **平台**：X (Twitter)
- **发布时间**：2026年4月3日
- **原始链接**：https://x.com/i/status/2040095376154480966
- **浏览量**：1,908

## 核心内容

### 背景
很多人看Claude Code泄露的源码，第一反应是：
- 它怎么把用户输入变成任务执行的结果？
- 它怎么在模型调用、工具、上下文、异常中断、继续下一轮之间来回切换的？
- while (true) 为什么不是死循环？
- 如果我想做自己的agent，从哪里开始？

---

### 一、Claude Code整体架构

Claude Code 不是一个普通的CLI客户端，而是一个Agent分层系统。

通过梳理Claude Code的请求主线的主链路，抓到了核心引擎就是 query.ts

---

### 二、Agent 状态机长什么样？

**1. 状态机入口query异步函数**
作用是把构建的信息传递给agent loop

```typescript
export async function* query(
  params: QueryParams,
): AsyncGenerator<...> {
  const consumedCommandUuids: string[] = []
  const terminal = yield* queryLoop(params, consumedCommandUuids)
  return terminal
}
```

**2. Agent最底层就是 agent loop 状态机**
CC里对应queryLoop异步while循环函数

```typescript
async function* queryLoop(
  params: QueryParams,
  consumedCommandUuids: string[],
): AsyncGenerator<...> {
  // 状态机当前状态
  let state: State = {
    messages: params.messages,
    toolUseContext: params.toolUseContext,
    turnCount: 1,
    transition: undefined,
  }

  while (true) {
    // 每轮先读取当前状态
    let { toolUseContext } = state
    ...
  }
}
```

**3. 模型调用阶段**
通过注入deps.callModel来调取并发送给LLM模型，然后流式模型输出

```typescript
for await (const message of deps.callModel({
  messages: prependUserContext(messagesForQuery, userContext),
  systemPrompt: fullSystemPrompt,
  tools: toolUseContext.options.tools,
  ...
})) {
  if (message.type === 'assistant') {
    const msgToolUseBlocks = message.message.content.filter(
      content => content.type === 'tool_use',
    )
    if (msgToolUseBlocks.length > 0) {
      toolUseBlocks.push(...msgToolUseBlocks)
      needsFollowUp = true
    }
  }
}
```

**4. 判断是否继续下一轮**
模型输出后会判断：如果没有tool_use或者已经处理完，决定结束还是继续下一轮

**5. 标准状态转移**
如果满足终止条件，就直接return，整个循环结束；否则构造下一状态继续运行

---

### 三、为什么 while(true) 不是死循环？

Agent核心其实就是一个while循环，Claude Code的具体实现是query.ts里的while(true)。

**关键在于：**
- 执行之前会读取状态
- 执行过程中会计算下一状态transition
- 根据状态决定是否退出

```typescript
let state = {
  messages: params.messages,
  toolUseContext: params.toolUseContext,
  turnCount: 1,
  transition: undefined,
}

while (true) {
  // 每一轮开始时，都先读取当前状态
  let { toolUseContext } = state
  const { messages, turnCount } = state

  ...

  // 某个分支触发后，不是原地空转，而是先构造下一状态
  const next = {
    messages: [...newMessages],
    toolUseContext: toolUseContextWithQueryTracking,
    turnCount: nextTurnCount,
    transition: { reason: 'next_turn' },
  }

  // 把当前状态切换成下一状态
  state = next

  // 然后再进入下一轮
  continue

  ...

  // 如果满足终止条件，就直接 return，整个循环结束
  return { reason: 'max_turns', turnCount: nextTurnCount }
}
```

---

### 四、最小可运行的Agent状态机

作者把query.ts删减为最小可运行的Agent状态机，方便阅读理解Agent的核心原理：

**GitHub地址**：https://github.com/Aibd/mini-agent

**如果要做自己的agent，建议按这个顺序搭：**
1. 把内置工具拆成独立tools/目录，做成可注册结构
2. 给模型输出加流式处理，让终端能边生成边显示
3. 增加文件读取、文件写入、命令执行等工具
4. 把消息历史持久化，支持连续会话
5. 增加更明确的状态、日志和错误分层
6. 再往上做更完整的Agent编排逻辑

---

## 数据亮点
- 浏览量：1,908
- 转发：6
- 评论：1
- 点赞：3
