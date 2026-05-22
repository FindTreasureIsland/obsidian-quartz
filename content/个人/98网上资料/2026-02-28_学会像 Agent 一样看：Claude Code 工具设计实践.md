---
title: X Article
author: "meng shao (@shao__meng)"
date: 2026-02-28 01:58
source: "https://x.com/shao__meng/status/2027564092173725790"
tags:
  - twitter
  - article
---

# X Article

**作者**: meng shao (@shao__meng)
**时间**: 2026-02-28 01:58
**来源**: [原始链接](https://x.com/shao__meng/status/2027564092173725790)

---

学会像 Agent 一样看：Claude Code 工具设计实践

来自 Claude Code 开发者 @trq212，记录了 Anthropic 团队在开发 Claude Code 过程中关于 Agent 工具设计 的实践经验，有一个很核心的观点「开发者需要学会"像 Agent 一样看世界"」

第一层：工具设计的基本框架
如何为 Agent 设计动作空间？看一个数学题的比喻：
· 纸笔：最低门槛，受限于手动计算
· 计算器：更强，需要知道如何操作
· 高级功能计算机：最强大，需要会编程

指向一个设计原则：工具应当与使用者的能力相匹配。给一个不会编程的人一台电脑，不如给他一个计算器。同理，给模型的工具必须是它能理解和有效调用的。

这里隐含了一个重要判断——工具不是越多越好，也不是越通用越好，要"shaped to its own abilities"。

第二层：AskUserQuestion 工具的三次迭代
尝试 1：在 ExitPlanTool 中附加问题参数
最省事的做法——复用现有工具。但失败了，原因是语义冲突：一个工具同时承担"输出计划"和"提出疑问"两个职责，模型会困惑。如果用户的回答推翻了计划怎么办？模型是否需要再调用一次？一个工具承载两个意图，会让模型无法形成清晰的调用决策。

尝试 2：修改输出格式（结构化 Markdown）
思路是让模型在普通文本输出中嵌入特定格式的问题，然后由前端解析。这是最"通用"的方案，不需要新增工具。但模型的输出不够稳定——会多加句子、遗漏选项、改变格式。自由文本输出的可靠性不足以支撑结构化交互。

尝试 3：独立的 AskUserQuestion Tool
最终方案是创建专用工具，在 plan mode 中尤其鼓励使用。调用时弹出模态框，阻塞 Agent 循环直到用户作答。

这个方案成功的关键在于三点：
· 结构化输出——工具的参数 schema 强制模型给出选项，而非自由发挥
· 可组合性——可以在 Agent SDK 和 Skills 中引用
· 模型的自然倾向——"Claude seemed to like calling this tool"，模型对这个工具有良好的调用直觉

最后一点尤其值得注意。Thariq 明确说："Even the best designed tool doesn't work if Claude doesn't understand how to call it." 工具设计不仅是工程问题，还是与模型认知特性的匹配问题。

第三层：工具需要随模型能力进化
TodoWrite 到 Task Tool 的演变揭示了一条重要规律：曾经必要的工具，可能随着模型进步反而成为约束。

早期模型容易"忘记"待办事项，所以需要 TodoWrite 来追踪任务，并且每 5 轮插入系统提醒。但随着模型能力提升：
· 模型不再需要被提醒 Todo 列表
· 系统提醒反而让模型过于僵化地遵循列表，而不是灵活调整
· Opus 4.5 对 subagent 的调度能力大幅提升，但 Todo 列表无法在多个 subagent 之间协调

于是 TodoWrite 被 Task Tool 取代。Task Tool 的核心转变是：从"帮模型记住事情"变为"帮 Agent 之间通信"——支持依赖关系、跨 subagent 同步、动态增删任务。

这里的教训很直接：定期回顾你对工具的假设。模型在变，你的工具也必须跟着变。

第四层：从 RAG 到自主搜索——上下文构建的范式转移
阶段 1：RAG 向量数据库 -> 被动接收上下文，需要索引和配置，环境兼容性差

阶段 2：Grep 工具 -> 模型主动搜索代码库，自己构建上下文

阶段 3：渐进式披露 -> 模型读取 Skill 文件，文件中引用其他文件，模型递归地展开搜索链条

这个演进的本质是：从"给模型喂上下文"到"让模型自己找上下文"。随着模型推理能力增强，它越来越擅长判断自己缺什么信息、去哪里找、找到后如何利用。

第五层：渐进式披露——不加工具也能扩展能力
Claude Code 目前约有 20 个工具，团队对新增工具的门槛很高，因为每多一个工具就多一个模型需要权衡的选项。

以"Claude Code 自身使用说明"为例：
· 写入系统提示词：用户很少问这类问题，常驻上下文造成 context rot
· 给模型文档链接让它自行加载：模型会加载大量结果，污染上下文
· 专用 Guide subagent：由 subagent 搜索文档并只返回精准答案

最终方案是 Guide subagent：不增加新工具，而是通过 subagent + 专用指令来扩展能力。这就是 Progressive Disclosure 的应用——在模型需要的时候，才逐层展开信息，而不是一次性塞入所有可能用到的知识。

这个思路对所有 Agent 开发者都有参考价值：能用信息架构解决的问题，就不要用新工具解决。

对 Agent 开发者的启示
以 Claude Code 为案例，方法论适用于所有 Agent 系统的构建：
· 先理解模型的能力边界，再设计工具，而非反过来
· 一个工具只做一件事，语义清晰，边界分明
· 结构化胜过自由文本，尤其在需要可靠输出的场景
· 渐进披露优于一次性加载，信息架构本身就是一种工具
· 定期审视既有工具，模型在进化，工具也必须跟上
· 读模型的输出——这是理解模型"如何看世界"的唯一途径

正如 Thariq 所言，这是一门手艺（art），不是一套公式（science）。核心方法论只有一句话：学会像 Agent 一样看。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HCNayNbbEAAij9O?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HCLxeR3acAAf2R9?format=jpg&name=medium)

