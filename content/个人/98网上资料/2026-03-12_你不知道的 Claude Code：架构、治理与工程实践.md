---
title: 你不知道的 Claude Code：架构、治理与工程实践
author: "Tw93 (@)"
date: 2026-03-12 13:48
source: "https://x.com/HiTw93/status/2032091246588518683"
tags:
  - twitter
  - article
---

# 你不知道的 Claude Code：架构、治理与工程实践

**作者**: Tw93 (@)
**时间**: 2026-03-12 13:48
**来源**: [原始链接](https://x.com/HiTw93/status/2032091246588518683)

---

你不知道的 Claude Code：架构、治理与工程实践

Tw93
@HiTw93
·
35分钟

0. 太长不读
今天这篇文章源于最近半年深度使用 Claude Code、两个账号每月 40 刀氪金换来的一些踩坑经验，希望能给大伙一些输入。
刚开始我也把它当 ChatBot 用，后来很快发现不对劲：上下文越来越乱、工具越来越多但效果越来越差、规则越写越长却越不遵守，折腾了一段时间，研究了 Claude Code 本身之后才意识到，这不是 Prompt 问题，而是这套系统的设计就是这样的。
这篇文章想和大伙聊聊这几个事：Claude Code 底层怎么运作、上下文为什么会乱以及怎么治理、Skills 和 Hooks 应该怎么设计、Subagents 的正确用法、Prompt Caching 的架构影响，以及怎么写一个真正有用的 CLAUDE.md。
我觉得最直接的理解方式，是把 Claude Code 拆成六层来看：
只强化其中一层，系统就会失衡，CLAUDE.md 写太长，上下文先污染自己了；工具堆太多了，选择就搞不清楚了；subagents 开得到处都是，状态就漂移了；验证这步跳过了，出了问题根本不知道是哪里挂的。

1. 它底层是怎么运行的
Claude Code 的核心不是"回答"，而是一个反复循环的代理过程：
收集上下文 → 采取行动 → 验证结果 → [完成 or 回到收集]
     ↑                    ↓
  CLAUDE.md          Hooks / 权限 / 沙箱
  Skills             Tools / MCP
  Memory
用了一段时间才意识到，卡住的地方几乎从来不是模型不够聪明，更多时候是给了它错误的上下文，或者写出来了但根本没法判断对不对，也没法撤回。
真正要关注的五个层面：
对着这几个面看，很多问题就好排查了。结果不稳定，查上下文加载顺序，不是模型的事；自动化失控，看控制层有没有设计，不是 agent 太主动；长会话质量下降，中间产物把上下文污染了，换个新会话比反复调 prompt 有用得多。

2. 概念边界：MCP / Plugin / Tools / Skills / Hooks / Subagents
简单记：给 Claude 新动作能力用 Tool/MCP，给它一套工作方法用 Skill，需要隔离执行环境用 Subagent，要强制约束和审计用 Hook，跨项目分发用 Plugin。

3. 上下文工程：最重要的系统约束
很多人把上下文当"容量问题"，但卡住的地方通常不是不够长，而是太吵了，有用的信息被大量无关内容淹没了。

上下文最佳实践
保持 CLAUDE.md 短、硬、可执行，优先写命令、约束、架构边界。

4. Skills 设计：不是模板库，是用的时候才加载的工作流
一个好 Skill 应该满足什么
描述要让模型知道"何时该用我"，而不是"我是干什么的"，这两个差很多

5. 工具设计：怎么让 Claude 少选错
好工具 vs 坏工具
几个实用设计原则

6. Hooks：在 Claude 执行操作前后，强制插入你自己的逻辑
适合 vs 不适合放到 Hooks 的

7. Subagents：派一个独立的 Claude 去干一件具体的事
Subagent 就是从主对话派出去的一个独立 Claude 实例

8. Prompt Caching：Claude Code 内部架构的核心
工程界有句话 "Cache Rules Everything Around Me"，对 agent 同样如此

9. 验证闭环：没有 Verifier 就没有工程上的 Agent
「Claude 说完成了」其实没啥用，你得能知道它做没做对

10. 高频命令的工程意义
这些命令说白了就干一件事：主动管理上下文，别等系统自己处理。

11. 如何写一个好的 CLAUDE.md
CLAUDE.md 在我看来更像是你和 Claude 之间的协作契约

12. 最近自己折腾中得到的新经验
春节放假时，我用 Claude Code 做了一个开源 terminal 项目 Kaku

13. 常见反模式

14. 配置健康检查
基于文章里的六层框架，我把这套检查整理成了一个开源 Skill 项目 tw93/claude-health

15. 结语
用 Claude Code 大概会经历三个阶段：

想发布自己的文章？
升级为 Premium

Tw93
@HiTw93
Father of Kaku · Mole · Pake • MiaoYan

---

## 图片

![Image 1](https://pbs.twimg.com/media/HDNlwyUbQAEWZLm?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HDNmq2FbkAAPRmY?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HDNmz0xbUAAK0qh?format=png&name=900x900)

![Image 4](https://pbs.twimg.com/media/HDNnGJybQAA7KCR?format=jpg&name=medium)

![Image 5](https://pbs.twimg.com/media/HDNngxyaMAAcgV9?format=jpg&name=medium)

![Image 6](https://pbs.twimg.com/media/HDNnxhbbQAEmIP5?format=png&name=900x900)

![Image 7](https://pbs.twimg.com/media/HDNn8yFbQAIICH4?format=jpg&name=medium)

![Image 8](https://pbs.twimg.com/media/HDNoHhibQAY_flX?format=jpg&name=medium)

![Image 9](https://pbs.twimg.com/media/HDNoRWTbQAQLNdd?format=png&name=small)

![Image 10](https://pbs.twimg.com/media/HDNoiGJbQAUjQKF?format=jpg&name=medium)

![Image 11](https://pbs.twimg.com/media/HDNomYAbQAMSRGR?format=jpg&name=medium)

![Image 12](https://pbs.twimg.com/media/HDNp6PubQAQLtnc?format=jpg&name=medium)

![Image 13](https://pbs.twimg.com/media/HDNqC4cbQAAB9VJ?format=jpg&name=medium)

![Image 14](https://pbs.twimg.com/media/HDNqIrfaMAAHaV2?format=jpg&name=medium)

![Image 15](https://pbs.twimg.com/media/HDNqL8ta4AAcN7Y?format=jpg&name=medium)

![Image 16](https://pbs.twimg.com/media/HDNqUs6bQAIoN6w?format=jpg&name=medium)

![Image 17](https://pbs.twimg.com/media/HDNqhp3akAAntdH?format=jpg&name=medium)

![Image 18](https://pbs.twimg.com/media/HDNqpqgbQAE9WB8?format=jpg&name=medium)

![Image 19](https://pbs.twimg.com/media/HDNq7sibQAMI3un?format=jpg&name=medium)

![Image 20](https://pbs.twimg.com/media/HDNrVY3bQAQFm9Z?format=jpg&name=medium)

![Image 21](https://pbs.twimg.com/media/HDNrmnsbsAE7Fti?format=jpg&name=medium)

![Image 22](https://pbs.twimg.com/media/HDNsdBSbAAA_nY5?format=jpg&name=medium)

![Image 23](https://pbs.twimg.com/media/HDNsXW1bAAAYfy2?format=jpg&name=medium)

