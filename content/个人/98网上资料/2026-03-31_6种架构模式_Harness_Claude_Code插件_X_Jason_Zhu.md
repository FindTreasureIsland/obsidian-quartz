# 6种架构模式+60%质量提升：这个开源项目把 Harness Engineering 从概念变成了工具

> 作者：Jason Zhu（@GoSailGlobal）
> 原文来源：X/Twitter
> 发布日期：2026-03-31
> 原始链接：https://x.com/i/status/2038878300614099180

## 核心内容

上周聊了 Anthropic 和 OpenAI 对 Harness Engineering 的不同理解，现在有人给出了具体落地方案。

开发者 revfactory 做了一个叫 Harness 的 Claude Code 插件，直接把 Harness Engineering 的理念变成了可安装、可运行的工具。

## 六种架构模式

Harness 内置了六种 Agent 团队协作模式：

| 模式 | 适用场景 | 特点 |
|------|----------|------|
| Pipeline | 强依赖顺序任务 | 上一个输出喂给下一个，任一环节卡住整条线停 |
| Fan-out/Fan-in | 多专家并行分析 | 多个专家同时工作，最后汇总结果 |
| Expert Pool | 动态分配专家 | 路由器根据输入类型分配，不用所有人同时在线 |
| Producer-Reviewer | 生成+评审 | 呼应 Anthropic 核心发现，Agent 评审自己几乎无效 |
| Supervisor | 动态调度 | 运行时根据实际情况分配任务，大规模代码迁移适用 |
| Hierarchical Delegation | 复杂任务递归拆解 | 限制两层以内，防止上下文丢失 |

## A/B 测试数据

- 15个软件工程任务对比
- 平均质量评分：49.5 → 79.3（提升60%）
- 胜率：100%（15/15）
- 按复杂度分层：基础+23.8%、进阶+29.6%、专家级+36.2%
- **任务越复杂，Harness 价值越大**

## 值得注意的设计细节

1. 所有 Agent 强制指定 model: "opus"（弱模型省 token 但协作容易崩）
2. 文件系统作为协作基础设施（_workspace/ 目录解决持久化和多 Agent 共享）
3. Progressive Disclosure：Skill 文件分三层控制上下文消耗
4. 团队规模硬限制：2-7人，每人多3-6个任务，层级最多两层

## 局限性

- Agent Teams 功能还需要手动开启环境变量（实验性）
- A/B 测试只覆盖软件工程场景
- 六种模式之间的选型建议还比较粗粒度

---

## 数据统计
- 👁 6,296阅读
- 💬 10评论
- 🔁 81转发
- ❤️ 147点赞
