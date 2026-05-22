---
title: "从 Skills 到分层 Workflow：AI Agent 工程化的下一层抽象"
author: 关木
source: X.com
tags: [AI, Agent, Skills, Workflow, 工程化, 分层设计, Unified-Skills]
date: 2026-05-10
stats:
  likes: 85
  retweets: 13
  views: 7622
---

# 从 Skills 到分层 Workflow：AI Agent 工程化的下一层抽象

**来源**：https://x.com/i/status/2053004758508843319

**作者**：关木

**发布时间**：2026-05-10

---

## 核心论点

很多 AI Agent 项目走到中后期，都会开始沉淀 skills。但系统一旦继续生长，skills 的数量增加，并不必然带来 Agent 行为的稳定性。

**Skills 解决的是"怎么做"，而 Workflow 解决的是"什么时候做、由谁做、做到什么程度算通过、失败时退回哪里、过程证据留在哪里"。**

当 Agent 开始承担连续工程任务时，真正要治理的就不再是能力本身，而是能力进入流程的方式。

---

## 一、Skills Library 的上限，不是能力不足，而是工程失稳

Skills Library 的方式：TDD skill、debug skill、review skill、writing skill，各自解决局部问题。

但这套方式的上限很清楚：**工程工作从来不是一次技能调用，而是一条连续推进的责任链。**

当任务复杂度上升，系统会开始暴露出四类典型失稳：

### 1. 时序失稳：Agent 会跳步骤

Skill 可以告诉它测试该怎么写，debug 应该怎么做，但 skill 本身并不能天然约束它：什么时候才有资格开始写，什么时候必须先澄清，什么时候必须先停下来做设计。

### 2. 责任失稳：Agent 会自证通过

同一个 Agent 可以自己理解需求，自己做设计，自己列计划，自己完成实现，再自己 review，最后得出"没有问题"的结论。

**问题不在于它不努力，而在于工程系统不能把"提出问题、执行任务、判断通过"全部交给同一个认知视角。**

### 3. 证据失稳：过程不可追踪

一次对话里 Agent 看起来完成了很多工作，但几天之后往往很难回答：
- 当时的需求边界到底是什么？
- 哪些外部资料被采纳，哪些被拒绝？
- 设计时讨论过哪些替代方案？
- review 审的是 spec 完整性，还是只是代码风格？

### 4. 治理失稳：skills 之间没有组织关系

如果它们只是平铺在一个目录里，Agent 仍然要在运行时临场决定：先调哪个，什么时候切换，什么情况下跳过，失败后回到哪里。

---

## 二、Workflow 不是 Skills 的顺序表，而是阶段协议

Unified Skills 的第一层升级，是把 skills 放进一个明确的阶段流里：

```
/refine -> /design -> /plan -> /build -> /review -> /ship
```

这条路径背后的判断是：**工程交付需要状态机，而不是自由联想。**

| 阶段 | 任务 | 核心约束 |
|------|------|---------|
| /refine | 把模糊想法收敛成可验证规格 | 问题是什么；用户是谁；成功标准是什么 |
| /design | 在实现前冻结创作与体验判断 | UI、文章、deck、视觉稿都需要先完成创作判断 |
| /plan | 定义任务拓扑，而非写待办清单 | 哪些任务必须串行；哪些可以并行；哪些风险需要前置处理 |
| /build | 消费已批准输入，不重新发明目标 | 只消费已经批准的 spec、design 和 plan |
| /review | 门控，而非口头确认 | 有能力阻断流程，发现 blocking 问题就退回 |
| /ship | 交付完成，不等于实现结束 | 发布、导出、同步、记录、回滚信息 |

---

## 三、CANON：所有 Workflow 的宪法

最上层是 CANON.md。它定义的不是某类任务技巧，而是**不可放松的底线**：

- 先陈述假设
- 控制范围
- 验证优先
- 遇到矛盾先停止并澄清
- 调试先找根因
- 不做 yes-machine

**为什么必须独立存在？** 如果没有 CANON，每个 skill 都会带着自己的隐含价值观。TDD skill 强调测试，debug skill 强调根因，review skill 强调质量，但它们之间缺少统一的行为合同。

---

## 四、六层分层结构

Unified Skills 抽象成六层，每层都解决一个问题，同时拒绝解决另一个问题：

```
CANON
  -> Command（阶段控制器）
  -> Agent（责任视角）
  -> Skill（方法论单元）
  -> Artifact（证据链）
  -> Hook / validate（护栏）
```

### Command：阶段控制器，而非快捷入口

回答问题：现在处在哪个阶段，这个阶段应该读什么、产出什么，通过条件是什么。

它不负责告诉你"debug 怎么做"，而负责回答：当前阶段是否具备进入条件，当前产物是否达到通过条件。

### Agent：责任视角，而非人格表演

Agent 层核心不是角色扮演，而是**责任切分**。

- review agent 不应该重新定义需求
- software engineer agent 不应该在 build 阶段决定任务拓扑
- design reviewer 不应该只说"视觉不错"

### Skill：真正可复用的方法论单元

一个合格的 skill，必须说明：
- 什么时候进入
- 什么时候退出
- 具体步骤是什么
- 哪些说法是常见借口
- 哪些情况必须停止
- 如何验证自己做完了

### Artifact：把过程变成证据链

01-spec.md、02-design.md、03-plan.md、04-review.md、05-ship.md 这些文件，并不是文档洁癖，而是 **Agent 行为的审计轨迹**。

### Hook / Validate：把约定变成护栏

只靠提示词约束 Agent 是不稳定的。Hooks 和 ./validate 负责把一部分纪律从"应该遵守"变成"违反就会暴露"。

---

## 五、两阶段 Review：分层门控的具体例子

Unified Skills 里的 review 拆成两关：

### 第一关：Spec Compliance

检查实现是否覆盖了 spec 中定义的功能需求、边界条件、错误路径和验收标准。关心的是：实现了什么，是否把该做的事情做全了。

### 第二关：Code Quality

只有在第一关通过后，才进入第二关。讨论 correctness、readability、architecture、security、performance 等质量维度。

**两阶段 review 的作用，就是把问题类型切开：先确认做没做对，再确认做得好不好。**

---

## 六、从 Prompt 到 Workflow，再到治理结构

```
Prompt = 表达
Skill = 方法
Workflow = 制度
Layered Workflow = 治理结构
```

真正成熟的 Agent 系统，不应该只是"会做很多事"，而应该知道：
- 在什么阶段
- 由什么模块
- 以什么责任
- 依据什么证据
- 完成什么结果

**AI Agent 的下一层抽象，不是继续堆 skills，而是把 skills 放进一套有阶段状态机、责任分离、证据链和运行护栏的分层 workflow。**

---

**原文链接**：https://x.com/i/status/2053004758508843319