# 从Claude Code刚泄漏的源码，看当前第一梯队 AI Agent 的工程架构

> 作者：Max For AI（@MaxForAI）
> 原文来源：X/Twitter
> 发布日期：2026-03-31
> 原始链接：https://x.com/i/status/2038957626177081435

## 事件背景

2026年3月31日，Anthropic 再次因打包流程的低级失误，将其最新版 Claude Code（v2.1.88）的完整前端与客户端源码暴露在了 npm 仓库中。

网友发布了一个未被剔除的 `cli.js.map` 文件，直接还原出了约 1900 个文件、超过 51 万行的原生 TypeScript 代码。

对于 Anthropic 而言，这是继前几天 Mythos 模型文档外泄后的又一次严重 OpSec 事故。

但对于整个大模型应用层的开发者和行业研究者来说，这份源码是一份毫无保留的、价值极高的前沿 AI Agent 工程架构白皮书。

## 不仅仅是一个 CLI 工具

从目录结构（`src/` 下约 40 个一级模块）可以看出，Claude Code 的复杂度远超目前市面上开源的常规单体 Agent。

**技术栈选型**：
- 语言：TypeScript
- 运行时：Bun（性能更激进）
- CLI 框架：Commander
- 终端渲染层：**React + Ink**（出人意料）

### 为什么一个命令行工具要用 React？

源码中的 `screens/REPL.tsx`（高达 5005 行）给出了答案。

在大模型流式输出（Streaming）和多工具并发执行的场景下，终端 UI 的状态管理变得极其复杂（例如同时渲染思考过程、工具调用进度条、代码 Diff 预览等）。

采用声明式的 React 配合极简的 Zustand 风格自定义 Store，是应对这种高频局部刷新的最佳工程实践。

### 两种运行模式

- **交互式 REPL 模式**：通过 Ink 驱动前端终端 UI，主要面向人类开发者
- **无头/SDK 模式**（QueryEngine 类）：完全剥离 UI，支持 JSON 流式输出。为后续将其作为底层引擎嵌入 IDE（如类似 Cursor 的形态）或 CI/CD 流程中埋下了伏笔

### 极致并发优化启动流程

在 `main.tsx` 中，配置读取（MDM Settings）和 Keychain 密钥预取等 I/O 密集型操作被放在子进程中，与主模块 ~135ms 的加载过程并行执行。这种对启动延迟的毫秒级苛求，贯穿了整个代码库。

## Prompt Cache 工程学

这是整份源码中最具技术含量的部分，也是拉开 Claude Code 与普通套壳应用体验差距的核心壁垒。

目前 Agent 工具在处理长上下文时，往往还在简单粗暴地拼接 System Prompt 和历史对话。而在 Claude Code 的 `services/api/claude.ts`（长达 3419 行的核心交互模块）中，提示词组装被做到了字节级的精打细算。

### 分段缓存架构

众所周知，Anthropic 的 Prompt Cache 机制采用前缀匹配（Prefix Matching）。为了最大化缓存命中率，Claude Code 设计了严密的分段缓存架构：

**静态段（全局可缓存）**：通过 `systemPromptSection()` 生成，包含模型身份介绍、安全规则、代码风格限制、工具使用基础指南等。这部分在整个会话生命周期内几乎不变。

**动态分界线**：源码中硬编码了一个特殊标记 `SYSTEM_PROMPT_DYNAMIC_BOUNDARY`。

**动态段（会话级缓存/不缓存）**：包含当前工作目录信息（CWD）、Git 状态、MCP 指令、用户配置等高频变化的数据。

### 防缓存穿透的兜底工作

Claude Code 做了大量看似繁琐的兜底工作：

- **确定性排序**：传给大模型的工具描述被严格按照内置工具前缀 + MCP 工具后缀进行字母表排序
- **哈希路径映射**：配置文件的路径不使用随机 UUID，而是使用基于内容的哈希值，避免每次注入路径不同破坏缓存
- **状态外置**：连当前可用的 Agent 列表也被从工具描述中剥离，转移到了消息附件（Attachments）中。据源码注释透露，仅这一项改动就减少了约 **10.2% 的 Cache Creation Tokens 消耗**

> 现阶段优秀的 AI 应用层开发，本质上就是在贪婪且精细地压榨 API 缓存系统的价值。

## 工具系统与流式并发执行

Claude Code 内置了超过 **40 种工具**（涵盖文件读写、Bash 执行、网络抓取等），其工具系统架构采用了高度模块化的工厂模式（Factory Pattern）。

每个工具继承自基础的 Tool 接口，必须实现 `checkPermissions()`、`validateInput()` 和 `isConcurrencySafe()` 等方法。

### 按需加载的 ToolSearch 机制

当工具数量超过某个阈值时，如果把所有工具的描述都塞进 Prompt，Token 成本将不可接受。Claude Code 采用了名为 ToolSearch 的优雅策略：

非核心工具被标记为 `defer_loading: true`。模型在当前 Prompt 中看不到这些工具的具体定义，只知道有一个 ToolSearch 工具。当模型认为自己需要额外能力时，必须先调用 ToolSearch 去动态加载对应的工具配置。

### StreamingToolExecutor

为了提升执行效率，系统支持工具的并发调用。协调器（`toolOrchestration.ts`）会将大模型返回的工具调用请求分区为并发批次和串行批次：

- 并发安全的工具（如同时读取多个不相关的文件、并发发起网络搜索）会被并行触发
- 非并发安全的工具（如先后修改同一个代码文件）则严格串行

大结果集的工具设有 `maxResultSizeChars` 预算，超过预算的内容会被直接截断并持久化到本地临时文件中，只给 LLM 返回一个预览摘要。

## 解决上下文污染的 Fork 机制

目前的单体 Agent 存在一个致命缺陷：在执行复杂任务时，模型可能会反复读取错误的文件、尝试错误的命令，这些试错过程会产生大量的垃圾上下文，迅速污染主对话。

Claude Code 引入了 **Coordinator Mode** 和 **Fork Subagent** 机制来解决这一问题。

### Coordinator-Workers 架构

在环境变量启用协调器模式后，系统会被重构为：

- **Coordinator（协调者）**：被剥夺了直接操作文件的权限，只保留 Agent（派生子代理）、SendMessage 和 TaskStop 三个工具，唯一工作是规划工作流（Research → Synthesis → Implementation → Verification）
- **Workers（执行者）**：携带具体的工具描述被派生出来

### Fork 继承机制

当需要进行大范围代码探索时，Coordinator 会 Fork 出一个 Explore Agent。这个子 Agent 会继承父对话的缓存（共享 Prompt Cache 以节约成本），但其后续的探索动作完全在其隔离的上下文中进行。探索结束后，子 Agent 只需要通过特定的 XML 格式 `<task-notification>`，将提炼好的关键结论传回给 Coordinator 即可。

> 这种用完即毁，只留结论的设计，是目前业界处理复杂多 Agent 长文本协同的最佳实践之一。

## Agent Swarm 并发机制

除了用于解决上下文污染的串行 Fork 机制，源码还展示了更具野心的并发多 Agent 架构——**Swarm（Teammate）集群**。

系统支持一种名为 `in_process_teammate` 的任务类型。在终端 CLI 环境中搞多 Agent 并发，会面临两个致命的工程挑战：**权限弹窗冲突**和 **UI 渲染混乱**。

### Anthropic 的解法

**Leader 权限桥接**（`permissionSync.ts`）：所有 Teammate 子进程都不允许直接向用户弹窗请求权限。它们会将权限请求通过内部通道"桥接"给主进程的 Leader Agent，由 Leader 统一在主终端进行安全拦截和用户确认。

**终端布局自动化**：源码直接集成了 iTerm2 和 Terminal.app 的 AppleScript 控制指令。当派生新的 Teammate 时，系统会自动在终端中切分窗格（Split Pane），为每个子 Agent 分配独立的输出视窗。

> 这标志着 AI 正在从"单体思考"正式向"集群并发协作"演进。

## Dream 记忆架构

在 RAG 大行其道的今天，几乎所有的 AI 产品都在集成向量数据库。但 Claude Code 的记忆系统（`memdir/` 模块）极其复古且务实——完全基于本地文件系统。

### 架构组成

- **MEMORY.md**：作为高层索引，被限制在最多 200 行/25KB 以内
- **多个基于 Frontmatter 格式的主题文件**

记忆被精细划分为 User、Feedback、Project、Reference 四大类。

### KAIROS 模式（尚未发布）

隐藏在源码中的 KAIROS 助手模式是一个令人惊喜的彩蛋。这是一个尚未正式发布的长期运行（Daemon）模式：

1. 记忆系统采用类似人类日志的追加模式（写入 `logs/YYYY/MM/YYYY-MM-DD.md`）
2. 到了夜间或闲置时间，后台会唤醒一个名为 **Dream（做梦）** 的离线任务 Agent
3. 这个 Agent 的职责是对白天的流水账日志进行总结、蒸馏，然后将其提取固化到结构化的长期主题文件中

这种从短期日志到长期记忆的异步整合机制，绕开了向量检索的召回率痛点，代表了端侧 AI 助理向永远在线、持续学习演进的明确方向。

## 权限收敛与安全

Claude Code 采用了一套多层权限收敛架构：

- 底层：基于 `@anthropic-ai/sandbox-runtime` 的文件/网络沙箱
- 中层：特定危险操作（如 `git push --force`）的硬编码拦截
- 工具级：校验

### YOLO Classifier

最引人注目的是其名为 **Auto Mode Classifier**（`yoloClassifier.ts`）的组件。

当用户开启自动模式时，系统并没有使用死板的正则表达式来评估命令的危险性，而是使用了一个**侧查询（Side Query）机制**：

系统会在后台静默调用一个更小、更便宜的 LLM，将当前对话的精简转录（Transcript）和即将执行的 Bash 命令抛给它，让这个侧边模型输出 Allow 或 Deny 的决策。

此外，系统内部还有一个基于阈值的 **Denial Tracking**——当自动工具被频繁拒绝时，系统会优雅降级，退回到 Prompting 模式请求人类介入。

> 这种用小 AI 监管大 AI 的动态权限系统，比传统的静态拦截规则要灵活得多。

## 一些小彩蛋

### 卧底模式（Undercover Mode）

针对员工在开源或公共仓库工作的场景，系统默认开启且无法强制关闭。该模式会在 Prompt 中明确要求模型"Do not blow your cover"，并强制剥离所有由 AI 生成的免责声明或代号痕迹。

### Buddy System（电子宠物）

源码中包含了一个隐藏的电子宠物系统（生成鸭子、猫头鹰等）。为了保证宠物生成的随机性与确定性，工程师使用了用户的 ID 配合 Mulberry32 伪随机数生成算法。

```
18 种物种: duck, goose, blob, cat, dragon, octopus, owl, penguin...
5 种稀有度: common(60%), uncommon(25%), rare(10%), epic(4%), legendary(1%)
```

最搞笑的一个细节是：由于某个动物物种的英文名称恰好与 Anthropic 极其机密的内部模型代号重名，工程师竟然使用 `String.fromCharCode()` 来动态拼装这个单词以绕过合规代码扫描仪的违禁词检测。

## 我们能学到什么？

从 Claude Code 的底层设计可以看出：

> 大模型应用层创业，单纯依靠拼凑 Prompt、堆砌向量数据库、套一个简单循环外壳的时代已经结束了。

真正的壁垒建立在：

- **Token 成本的极致抠门**（Prompt Cache 优化）
- **对多状态机协同的流式调度**（Coordinator 与 Fork 机制）
- **对用户意图容错与安全干预的平衡**（YOLO Classifier）
- **对宿主操作系统深度的文件流集成**

Claude Code 展示出的工程化水平，已经为 2026 年的 AI Agent 产品树立了一个全新的技术标杆。

---

## 数据统计
- 👁 4.6万 阅读
- 💬 3 评论
- 🔁 26 转发
- ❤️ 177 点赞
