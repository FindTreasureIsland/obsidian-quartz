---
title: AI Agent 记忆架构实战II：让Agent 越用越聪明
author: "Jason Zuo (@xxx111god)"
date: 2026-02-17 09:37
source: "https://x.com/xxx111god/status/2023521632673763473"
tags:
  - twitter
  - article
---

# AI Agent 记忆架构实战II：让Agent 越用越聪明

**作者**: Jason Zuo (@xxx111god)
**时间**: 2026-02-17 09:37
**来源**: [原始链接](https://x.com/xxx111god/status/2023521632673763473)

---

最近看到不少人聊 AI Agent 的多 session 架构
频道隔离、上下文分离，这些都对。
但我发现大部分人漏了一个关键问题：memory 怎么管？

Session 隔离只解决了"当下不乱"。Memory 管理才决定 agent 能不能"越用越聪明"。

之前写过一篇 AI Agent 记忆管理大法。现在跑了一个多月，又踩坑无数。
把我现在的架构和踩过的坑分享出来，你可以直接抄。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

问题：AI 每次醒来都是白纸

不管你用 Claude、OpenClaw 还是别的，session 结束就清空。下次来，它什么都不记得。
不设计 memory 系统，用越久越傻。因为它永远在重新认识你。

我的三层 Memory 架构

直接抄这个结构就行。

MEMORY.md ← 长期记忆（精华，常驻加载）
memory/YYYY-MM-DD.md ← 每日日志（原始流水账）
SESSION-STATE.md ← 工作缓冲区（防压缩丢失）

第一层：每日日志

memory/2026-02-16.md 这种格式。每天一个文件，发生什么记什么。不精炼，不整理，先倒进去。
作用：原始素材。回溯的时候有据可查。

第二层：MEMORY.md 长期记忆

这是精华。定期从日志里提炼：
- 你的偏好（"我喜欢简洁的回复"）
- 重要决策（"用 X 方案，因为 Y"）
- 踩过的坑（"Z 不能这么搞"）
- 关键信息（账号、项目状态）

Agent 每次启动先读这个文件。相当于它的"人格"和"记忆"。

第三层：SESSION-STATE.md 工作缓冲区

这个救过我好几次。
长对话会被压缩，重要细节可能被压没。SESSION-STATE.md 记录当前任务状态，压缩后第一件事读它。

内容示例：
当前任务：写 memory 架构文章
状态：Draft 2 修改中
待确认：是否加代码示例

记忆优先级：P0/P1/P2

不是所有东西都值得永久保留。我用优先级标签：

[P0] 我的时区是 US Eastern ← 永不过期
[P1][2026-02-16] 正在写文章项目 ← 90天后归档
[P2][2026-02-16] 今天试了新工具 ← 30天后归档

写个脚本每天跑一次，过期的自动移到 memory/archive/。MEMORY.md 保持精简。

安全隔离：哪些记忆不该共享

MEMORY.md 只在主 session（1:1 对话）加载。群聊不加载。
为什么？里面有个人信息、项目细节、账号偏好。群里可能有别人，不能泄露。
规则：频道隔离对话，但不是所有记忆都该跨频道共享。

几个救命技巧

1. 压缩前主动 flush
对话变长时，让 agent 把关键状态写进 SESSION-STATE.md。压缩来了也不丢。

2. 语义搜索召回
记忆多了找不到？用 memory_search。问"之前 trading 那个决定"，它从几十个文件里找相关内容。

3. 知识复利
每周花 10 分钟，从日志里提炼精华到 MEMORY.md。日志是素材，MEMORY.md 是结论。

4. Skill = 程序性记忆
重复的工作流写成 Skill 文件。下次匹配到任务自动加载，不用每次解释。

自动化：让 Agent 自己打扫

手动整理记忆太累。我写了两个自动化：

1. memory-janitor.py — 自动归档过期记忆

每天凌晨跑一次，扫描 MEMORY.md：
- P1 超过 90 天 → 移到 memory/archive/
- P2 超过 30 天 → 移到 memory/archive/
- P0 永不动

MEMORY.md 自动保持精简，不用手动清理。

2. 知识复利 — 日志自动提炼

每天检查昨天的日志，自动提炼核心洞察：
- 决策和结论
- 成功的方案
- 失败的教训

提炼完标记 <!-- compounded -->，重要的同步到 MEMORY.md。
日志是原始素材，insights 是蒸馏后的精华。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

直接可用的文件模板

MEMORY.md 模板：

# MEMORY.md - Long-Term Memory
## About [Your Name]
- [P0] 时区：XX
- [P0] 偏好：简洁回复，不要废话
- [P0] 沟通方式：Telegram
## Active Projects
- [P1][日期] 项目名：状态
## Key Decisions
- [P1][日期] 决定了 X，因为 Y
## Lessons Learned
- [P0] 不要在没备份的情况下改配置

SESSION-STATE.md 模板：

# SESSION-STATE.md - Working Buffer
## Current Task
[当前在做什么]
## Context
[重要背景，压缩后需要恢复的信息]
## Pending
- [ ] 待确认项

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

效果

用了这套架构一个月：
- Agent 记得我的偏好，不用每次重复
- 项目上下文不丢，跨天继续
- 压缩不怕，关键信息有备份
- 记忆自动清理，不会越来越臃肿

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

养 agent 不是配个 API key 就完事。
AI 的本质是根据已知的内容输出一个概率分布，完善的记忆管理，决定了 AI 输出的概率分布的范围和准度。
怎么管理它的 memory，决定它能帮你做到什么程度。

把这套结构复制过去，或者直接丢给你的 agent 让它自己改。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HBT-Jf5WAAE2jBk?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HBT9KbmboAA2sY4?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HBT8YxpWkAE782W?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HBT8pwtWAAErAU5?format=jpg&name=medium)

