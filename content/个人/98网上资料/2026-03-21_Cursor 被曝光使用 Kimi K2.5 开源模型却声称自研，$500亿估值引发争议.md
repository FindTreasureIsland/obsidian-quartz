---
title: Cursor 被曝光使用 Kimi K2.5 开源模型却声称自研，$500亿估值引发争议
author: "Aakash Gupta (@aakashgupta)"
date: 2026-03-20T22:39:00
source: "https://x.com/aakashgupta/status/2035003184192630985"
tags:
  - twitter
  - article
---

# Cursor 被曝光使用 Kimi K2.5 开源模型却声称自研，$500亿估值引发争议

**作者**: Aakash Gupta (@aakashgupta)
**时间**: 2026-03-20T22:39:00
**来源**: [原始链接](https://x.com/aakashgupta/status/2035003184192630985)

---

Cursor 正在以 500 亿美元估值融资，宣称其「自研模型生成的代码量超过世界上几乎所有其他 LLM」。发布 Composer 2 不到 24 小时，一位开发者就在 API 响应头中发现了模型 ID：kimi-k2p5-rl-0317-s515-fast。

这就是 Moonshot AI 的 Kimi K2.5，在其基础上加了强化学习。一位名叫 Fynn 的开发者在测试 Cursor 的 OpenAI 兼容端点时发现这个标识符从响应头泄露了。Moonshot 的预训练负责人 Yulun Du 在 X 上确认分词器与 Kimi 完全相同，并质疑 Cursor 的许可合规性。另外两名 Moonshot 员工也发帖确认。三条帖子均已删除。

这是第二次发生这种事。去年 10 月 Cursor 发布 Composer 1 时，多国用户报告模型在中途自发将内部思考切换为中文。Alley Corp 合伙人 Kenneth Auchenberg 发帖称其为「确凿证据」。KR-Asia 和 36Kr 确认 Cursor 和 Windsurf 底层都运行着微调的中文开源模型。Cursor 从未披露 Composer 1 基于什么构建。

---

## 模式：拿开源模型，加 RL，包装成自研突破

规律是：拿一个中文开源模型，在编程任务上跑 RL，然后包装成自研突破发布，发表一份将自己与 Opus 4.6 和 GPT-5.4 对比的价格-质量图表——却不披露你的基础模型是免费的——然后再融一轮。

Composer 2 公告中的那张图表值得单独一说。Cursor 将 Composer 2 与前沿模型在价格-质量坐标轴上对比，来论证他们达到了更优的权衡。但这图表没显示的是：Anthropic 和 OpenAI 是从零训练的模型。Cursor 拿了 Moonshot 花费数亿美元开发的开源模型，在上面跑 RL，然后把输出作为自研的证据来展示。

这就是在他人的 R&D 上做「边际套利」，打扮成基准测试幻灯片。

---

## 许可证问题

Kimi K2.5 以 Modified MIT License 发布，其中有一条专门针对这种情况的条款：如果你的产品月收入超过 2000 万美元，你必须在用户界面上显著显示「Kimi K2.5」。Cursor 今年 2 月 ARR（年度经常性收入）已突破 20 亿美元，约为每月 1.67 亿美元，是门槛的 8 倍。该条款明确覆盖衍生作品。

Cursor 估值 293 亿美元，正在以 500 亿美元融资。Moonshot 上一轮估值 43 亿美元。这家价值高 12 倍的公司，拿了小公司的模型，包装成专有技术，用前沿实验室的叙事来支撑估值。

---

## 三次 Composer 发布

- Composer 1：被发现说中文
- Composer 2：被发现 API 中有 Kimi 模型 ID
- 今年一次 P0 事故

以及一张基准图表：把 RL 微调与需要数十亿训练算力的模型对比，却不披露基础模型是免费的。

---

## 给 500 亿美元轮次投资者的问题

你买的究竟是什么？是一个有强部分发的 VS Code 分支，还是一个前沿研究实验室？API 中的模型 ID 回答了这个问题。

如果 Moonshot 不对一家从其模型衍生产品中每年赚取 20 亿美元的公司执行此许可证，所有未来开源发布中的归属条款将成为摆设。每一家正在观望的 AI 实验室都在算同一笔账：如果拥有更好分发的公司可以剥离归属、称其为专有、以 12 倍于你的估值融资，开源的动机何在？

kimi-k2p5-rl-0317-s515-fast 是 AI 许可史上最贵的模型 ID 泄露。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HD2JoZxbkAAL-5z?format=jpg&name=medium)

