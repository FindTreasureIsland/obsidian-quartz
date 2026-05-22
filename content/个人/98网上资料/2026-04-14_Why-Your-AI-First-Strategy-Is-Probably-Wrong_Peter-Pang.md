# Why Your "AI-First" Strategy Is Probably Wrong

## 作者信息
- **作者**：Peter Pang
- **认证账号**：@intuitiveml
- **发布日期**：2026年4月13日
- **原文链接**：https://x.com/i/status/2043545596699750791
- **浏览量**：44.9万
- **互动**：34回复 / 149转帖 / 985喜欢 / 3,304书签

---

## 核心内容

### 开篇数据
> 99% of our production code is written by AI. Last Tuesday, we shipped a new feature at 10 AM, A/B tested it by noon, and killed it by 3 PM because the data said no. We shipped a better version at 5 PM. Three months ago, a cycle like that would have taken six weeks.

**公司背景：**
- CREAO 是一个 agent 平台
- 25名员工，10名工程师
- 2025年11月开始构建 agent
- 两个月前从零开始重构了整个产品架构和工程工作流

**核心概念 — Harness Engineering：**
> OpenAI published a concept in February 2026 that captured what we'd been doing. They called it harness engineering: the primary job of an engineering team is no longer writing code. It is enabling agents to do useful work. When something fails, the fix is never "try harder." The fix is: what capability is missing, and how do we make it legible and enforceable for the agent?

---

## AI-First Is Not the Same as Using AI

**AI-Assisted（大多数公司的状态）：**
> Most companies bolt AI onto their existing process. An engineer opens Cursor. A PM drafts specs with ChatGPT. QA experiments with AI test generation. The workflow stays the same. Efficiency goes up 10 to 20 percent. Nothing structurally changes.

**AI-First（真正的变革）：**
> AI-first means you redesign your process, your architecture, and your organization around the assumption that AI is the primary builder.

**关键问题转变：**
- 从"AI如何帮助工程师？"
- 到"我们如何重组一切，让AI来构建，工程师提供方向和判断？"

**区别是乘数级的（multiplicative）。**

**关于 Vibe Coding：**
> A common version of this is what people call vibe coding. Open Cursor, prompt until something works, commit, repeat. That produces prototypes. A production system needs to be stable, reliable, and secure. You need a system that can guarantee those properties when AI writes the code. You build the system. The prompts are disposable.

---

## Why We Had to Change — 三个瓶颈

### 1. Product Management Bottleneck
> Our PMs spent weeks researching, designing, specifying features. Product management has worked this way for decades. But agents can implement a feature in two hours. When build time collapses from months to hours, a weeks-long planning cycle becomes the constraint.

**结论：** 花几个月思考再用两个小时构建是没有意义的。

**解决方案：** PM需要进化成"product-minded architects"，以迭代速度工作，或者退出构建循环。设计需要通过快速 prototype-ship-test-iterate 循环发生，而不是委员会评审的规格文档。

### 2. QA Bottleneck
> Same dynamic. After an agent shipped a feature, our QA team spent days testing corner cases. Build time: two hours. Test time: three days.

**结论：** 用AI构建的测试平台测试AI编写的代码。验证必须以与实现相同的速度移动。

**原则：** 否则你在下游10英尺处建立了另一个瓶颈。

### 3. Headcount Bottleneck
> Our competitors had 100x or more people doing comparable work. We have 25. We couldn't hire our way to parity. We had to redesign our way there.

**三个系统需要贯穿AI：**
1. 如何设计产品
2. 如何实现产品
3. 如何测试产品

**如果任何一个保持手动，它会约束整个管道。**

---

## The Bold Decision: Unifying the Architecture

**问题：**
> Our old architecture was scattered across multiple independent systems. A single change might require touching three or four repositories. From a human engineer's perspective, it is manageable. From an AI agent's perspective, opaque. The agent can't see the full picture. It can't reason about cross-service implications. It can't run integration tests locally.

**解决方案 — 单体仓库（Monorepo）：**
> I had to unify all the code into a single monorepo. One reason: so AI could see everything.

**Harness Engineering 原则：**
> The more of your system you pull into a form the agent can inspect, validate, and modify, the more leverage you get. A fragmented codebase is invisible to agents. A unified one is legible.

**自举成就：**
> CREAO is an agent platform. We used our own agents to rebuild the platform that runs agents. If the product can build itself, it works.

---

## The Stack

| 组件 | 工具 | 功能 |
|------|------|------|
| **基础设施** | AWS | 自动扩展容器服务，熔断回滚 |
| **监控** | CloudWatch | 中央神经系统，结构化日志，25+警报 |
| **CI/CD** | GitHub Actions | 六阶段管道 |
| **AI代码审查** | Claude Opus 4.6 | 三遍并行审查 |
| **特性开关** | Statsig | 渐进式发布，即时kill switch |
| **PR管理** | Graphite | 合并队列，stacked PRs |
| **异常报告** | Sentry | 跨服务结构化异常 |
| **工单系统** | Linear | 自动创建工单，severity评分 |
| **团队沟通** | Microsoft Teams | 每日健康报告 |

### CI/CD 六阶段管道
1. Verify CI
2. Build and Deploy Dev
3. Test Dev
4. Deploy Prod
5. Test Prod
6. Release

**每个PR都强制执行：** 类型检查、lint、单元和集成测试、Docker构建、Playwright端到端测试、环境一致性检查。

**管道是确定性的，所以agent可以预测结果并推理失败。**

### AI Code Review — 三遍并行审查
- **Pass 1：** 代码质量 — 逻辑错误、性能问题、可维护性
- **Pass 2：** 安全 — 漏洞扫描、认证边界检查、注入风险
- **Pass 3：** 依赖 — 供应链风险、版本冲突、许可证问题

**这些是审查门禁，不是建议。**

### The Self-Healing Feedback Loop

**每日9:00 AM UTC：**
Claude Sonnet 4.6 查询 CloudWatch，分析所有服务的错误模式，生成执行健康摘要，发送到 Microsoft Teams。

**一小时后：**
分类引擎运行。它聚类来自 CloudWatch 和 Sentry 的生产错误，在九个severity维度上对每个聚类进行评分，并在 Linear 中自动生成调查工单。每个工单包括示例日志、受影响用户、受影响端点和建议的调查路径。

**系统会去重：** 如果开放工单涵盖相同的错误模式，它会更新该工单。如果先前关闭的工单再次出现，它会检测回归并重新打开。

**修复流程：**
1. 工程师推送修复
2. 三遍 Claude 审查评估PR
3. CI 验证
4. 六阶段部署管道推进
5. 分类引擎重新检查 CloudWatch
6. 如果原始错误已解决，Linear 工单自动关闭

**核心理念：** 每个工具处理一个阶段。没有工具试图做一切。每日循环创建自愈循环，错误被检测、分流、修复和验证，最少人工干预。

---

## How a Feature Moves from Idea to Production

### New Feature Path
1. 架构师将任务定义为结构化prompt，包含代码库上下文、目标和约束
2. Agent 分解任务、计划实现、编写代码并生成自己的测试
3. PR 打开。三遍 Claude 审查评估。人类审查员检查战略风险，而非逐行正确性
4. CI 验证：类型检查、lint、单元测试、集成测试、端到端测试
5. Graphite 的合并队列重新base，重新运行CI，如果是绿色的则合并
6. 六阶段部署管道在每个阶段进行测试，推进通过dev和prod
7. 特性门为团队开启。渐进式百分比推广。监控指标
8. 如果任何问题下降则使用kill switch。严重问题自动熔断回滚

### Bug Fix Path
1. CloudWatch 和 Sentry 检测错误
2. Claude 分类引擎评分severity，创建带有完整调查上下文的 Linear 工单
3. 工程师调查。AI已经做了诊断。工程师验证并推送修复
4. 相同的审查、CI、部署和监控管道
5. 分类引擎重新验证。如果已解决，工单自动关闭

---

## The Results

**14天内：** 每天平均3-8次生产部署。按旧模式，两周时间甚至不会产生一次生产发布。

- 坏特性在发布的同一天被撤回
- 新特性在构思的同一天上线
- A/B测试实时验证影响

**质量 vs 速度的误解：**
> People assume we're trading quality for speed. User engagement went up. Payment conversion went up. We produce better results than before, because the feedback loops are tighter. You learn more when you ship daily than when you ship monthly.

---

## The New Engineering Org

### Two Types of Engineers

#### The Architect（架构师）
> One or two people. They design the standard operating procedures that teach AI how to work. They build the testing infrastructure, the integration systems, the triage systems. They decide architecture and system boundaries. They define what "good" looks like for the agents.

**这个角色需要深度批判性思维。你批评AI，而不是跟随它。** 当agent提出计划时，架构师找出漏洞：
- 遗漏了哪些失败模式？
- 跨越了哪些安全边界？
- 积累了哪些技术债务？

> I have a PhD in physics. The most useful thing my PhD taught me was how to question assumptions, stress-test arguments, and look for what's missing. The ability to criticise AI will be more valuable than the ability to produce code.

**这也是最难填补的角色。**

#### The Operator（操作员）
> Everyone else. The work matters. The structure is different.

- AI 分配任务给人类
- 分类系统找到bug，创建工单，提炼诊断，并分配给正确的人
- 人类调查、验证和批准修复
- AI 制作 PR，人类审查是否存在风险

**任务包括：** bug调查、UI改进、CSS改进、PR审查、验证。这些需要技能和注意力，但不需要旧模型所要求的架构推理能力。

---

## Who Adapts Fastest

**意外发现：**
> Junior engineers adapted faster than senior engineers.

- 传统实践较少的初级工程师感到被赋权。他们可以使用放大影响的工具。他们没有十年习惯要抛弃。
- 具有强传统实践的高级工程师适应最困难。两个月的工作可以在一小时内由AI完成。这是多年建立稀有技能后的艰难接受。

---

## The Human Side

### Management Collapsed
> Two months ago, I spent 60% of my time managing people. Today: below 10%.

**从管理到构建：** 从管理到构建。早上9点到凌晨3点写代码。设计SOP和维护harness。

### Less Arguing, Better Relationships
> My relationships with co-founders and engineers are better than before. Before the transition, most of my interaction with the team was alignment meetings. Now I still talk to my team. We talk about other things. Non-work topics. Casual conversations. We get along better because we stopped arguing about work that can be easily done by our system.

### Uncertainty Is Real
**合理的担忧：**
- 当我停止每天与人交谈时，一些团队成员感到不确定
- 有些人花更多时间争论AI是否能做他们的工作，而不是做工作
- 转型期产生焦虑

**原则：** 我们不会因为工程师引入生产bug而解雇他。我们改进审查流程，加强测试，添加保护措施。这同样适用于AI。

---

## Beyond Engineering

> If engineering ships features in hours but marketing takes a week to announce them, marketing is the bottleneck.

**CREAO的AI原生运营：**
- 产品发布说明：从changelog和特性描述AI生成
- 特性介绍视频：AI生成的动态图形
- 社交媒体每日帖子：AI编排和自动发布

---

## 结论

> The tools exist for any team to do this. Nothing in our stack is proprietary.

**竞争优势是做决定的意愿和吸收成本的能力。成本是真实的：员工不确定性、CTO每天工作18小时、高级工程师质疑自己的价值、两周的旧系统消失新系统未证实的过渡期。**

**两个月后，数字说话：**
> We build an agent platform. We built it with agents.

---

*最后更新：2026-04-14*
