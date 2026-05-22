---
title: "Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more"
author: Mnimiy
source: X.com
tags: [AI, Claude, CLAUDE.md, 提示词工程, 工程实践, Claude-Code]
date: 2026-05-12
stats:
  likes: 5562
  retweets: 534
  views: 3342609
---

# Karpathy's 4 CLAUDE.md rules cut Claude mistakes from 41% to 11%. After 30 codebases, I added 8 more

**来源**：https://x.com/i/status/2053116311132155938

**作者**：Mnimiy

**发布时间**：2026-05-12

---

## 背景

2026年1月，Andrej Karpathy 发帖抱怨 Claude 写代码的三个问题：silent wrong assumptions、over-complication、orthogonal damage。

Forrest Chang 把这些抱怨打包成4条行为规则放在 CLAUDE.md 文件里，GitHub 第一天就获得了 5,828 stars，两周 60,000  bookmarks，现在 120,000 stars。2026 年增长最快的单文件 repo。

然后作者在 30 个代码库上测试了 6 周。

---

## 核心数据

| 配置 | Mistake Rate |
|------|-------------|
| Karpathy 4条规则 | 40% → ~3% |
| 12条规则 | 41% → 3% |

**有意思的结果**：从 4 条规则增加到 12 条，compliance 只下降了 2%（78% → 76%），但 mistake rate 又降低了 8 个百分点。

---

## Why CLAUDE.md matters

Claude Code 的 CLAUDE.md 是整个 AI 编码堆栈中利用最少的文件。大多数开发者要么：
- 把它当作偏好垃圾桶，膨胀到 4,000+ tokens，compliance 降到 30%
- 完全跳过，每次都 prompt，5x token 浪费
- 复制一次模板然后忘记，两周后就悄悄崩溃

Anthropic 官方文档说：CLAUDE.md 是 advisory 的，Claude 大约 80% 的时间遵循它。超过 200 行，compliance急剧下降，因为重要规则被埋在了噪音里。

---

## 原始的 4 条规则（Karpathy）

### Rule 1 — Think Before Coding
No silent assumptions. State what you're assuming. Surface tradeoffs. Ask before guessing. Push back when a simpler approach exists.

### Rule 2 — Simplicity First
Minimum code that solves the problem. No speculative features. No abstractions for single-use code. If a senior engineer would call it overcomplicated — simplify.

### Rule 3 — Surgical Changes
Touch only what you must. Don't "improve" adjacent code, comments, or formatting. Don't refactor what isn't broken. Match existing style.

### Rule 4 — Goal-Driven Execution
Define success criteria. Loop until verified. Don't tell Claude what steps to follow, tell it what success looks like and let it iterate.

---

## 新增的 8 条规则

### Rule 5 — Don't make the model do non-language work

模型决定应该由确定性代码决定的事情——是否重试 API 调用、如何路由消息、何时升级。不同决定每周不同。$0.003/token 的随机 if-else。

### Rule 6 — Hard token budgets, no exceptions

没有预算的 CLAUDE.md 是空白支票。每个循环都可能螺旋成 50,000-token 的上下文转储。模型不会自己停下来。

### Rule 7 — Surface conflicts, don't average them

当代码库两部分不一致时，Claude 试图同时满足两者。结果是 incoherent。

### Rule 8 — Read before you write

"Surgical Changes" 告诉 Claude 不要触摸相邻代码。它没有告诉 Claude 先理解相邻代码。没有这个，Claude 写的新代码会与 30 行外的现有代码冲突。

### Rule 9 — Tests are not optional, but they're not the goal

Claude 把"tests pass"当作唯一目标，写出通过浅层测试但破坏其他一切的代码。

### Rule 10 — Long-running operations need checkpoints

Karpathy 的模板假设一次性交互。真正的 Claude Code 工作是多步骤的——跨 20 个文件重构、构建功能超过一个会话。没有检查点，一次错误就失去所有进展。

### Rule 11 — Convention beats novelty

在有既定模式的代码库中，Claude 喜欢引入自己的模式。即使它的方式"更好"，两种模式的引入也比单独任何一种更糟糕。

### Rule 12 — Fail visibly, not silently

最昂贵的 Claude 失败是看起来像成功的那些。函数"工作了"但返回错误数据。迁移"成功完成"但跳过了 30 条记录。

---

## Karpathy 模板悄悄失效的四个地方

### 1. 长时间运行的 agent 任务
Karpathy 的规则针对 Claude 写代码的时刻。Multi-step pipeline 时没有规则。没有预算规则。没有检查点规则。Pipelines 会漂移。

### 2. 多代码库一致性
"Match existing style" 假设一种风格。在有 12 个服务的 monorepo 中，Claude 必须选择哪种风格。原始规则没有告诉它怎么做。它随机选择或取平均。

### 3. 测试质量
Goal-Driven Execution 把"tests pass"当作成功。没有说测试必须有意义。结果是测试测试了无用的东西但让 Claude 很自信。

### 4. Production vs 原型
同样的 4 条规则在保护生产代码免受过度工程化影响的同时，也减缓了需要 100 行 speculative scaffolding 来弄清楚方向的原型的速度。Karpathy 的"Simplicity First"在早期代码上 overfires。

---

## What didn't work

- **添加从 Reddit/X 看到的规则**：大多数要么是 Karpathy 4 条的重新表述，要么是不通用的领域特定规则
- **超过 12 条规则**：超过 14 条 compliance 从 76% 降到 52%。200 行天花板是真的
- **依赖可能不存在的工具的规则**：如"always use eslint"，当 eslint 没安装时规则就静默失败
- **在 CLAUDE.md 中放例子而不是规则**：例子比规则更重，三个例子的上下文成本大约等于 10 条规则
- **"Be careful" / "think hard" / "really focus"**：噪音，compliance 降到约 30%
- **告诉 Claude 要"senior"**：没用，Claude 已经认为自己很 senior

---

## 心理模型

CLAUDE.md 不是愿望清单。它是关闭你观察到的特定失败模式的行为合同。

每条规则应该回答：这只防止什么错误？

- Karpathy 的 4 条防止 2026 年 1 月他看到的失败模式：silent assumptions、over-engineering、orthogonal damage、weak success criteria。它们是基础，不要跳过。
- 新增的 8 条防止 2026 年 5 月出现的失败模式：没有预算的 agent 循环、没有检查点的多步骤任务、不测试的测试、隐藏silent failures 的 silent successes。它们是附加的。

**你自己的 6 条规则针对你真正的失败模式，胜过有 6 条你永远不需要的 12 条规则。**

---

**原文链接**：https://x.com/i/status/2053116311132155938