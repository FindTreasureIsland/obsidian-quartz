---
title: 我用 Claude 写了一个 DBA 运维 Agent：从零到生产的完整记录
author: "plantegg (@plantegg)"
date: 2026-03-03 11:43
source: "https://x.com/plantegg/status/2028677544791138751"
tags:
  - twitter
  - article
---

# 我用 Claude 写了一个 DBA 运维 Agent：从零到生产的完整记录

**作者**: plantegg (@plantegg)
**时间**: 2026-03-03 11:43
**来源**: [原始链接](https://x.com/plantegg/status/2028677544791138751)

---

作为一个 MySQL DBA，我花了一个下午，用 Claude Code 从零搭建了一个能自主诊断 MySQL 和 Linux 的 AI Agent。它能自己决定该查什么、怎么查，最后给出一份完整的诊断报告。

题图是 agent 和 LLM 交互的完整过程，可以看到什么时候执行工具什么时候组合成完整 prompt 发给 LLM

这篇文章记录整个开发过程，以及我对 Agent 开发的理解。

什么是 Agent？

一句话：
Agent = 让大模型持续思考、持续调用外部工具、直到解决用户问题的程序。

和普通的 ChatGPT 对话不同，Agent 不只是"聊天"，它能动手。

普通 LLM 调用：你问一个问题，模型从训练数据里找答案，一问一答就结束了。

Agent：模型分析你的问题后，主动决定调用什么工具（比如 SSH 到服务器执行命令、查 MySQL），拿到真实数据后继续分析，不够就再调，直到能给出完整答案。

核心区别就一个：
模型有了"手脚"，能主动获取实时信息。

ReAct：Agent 背后的核心原理

几乎所有主流 Agent 框架都基于 ReAct 模式，来自 2022 年的论文 "ReAct: Synergizing Reasoning and Acting in Language Models"。

ReAct = Reasoning（推理）+ Acting（行动）

它的工作循环非常直觉：
Thought（思考）→ Action（行动）→ Observation（观察）→ 再 Thought ...

翻译成人话就是：
- 思考："用户问的是主从复制状态，我应该先查 SHOW SLAVE STATUS"
- 行动：调用 mysql_query 工具执行这条 SQL
- 观察：工具返回"无结果集"——说明这台不是从库
- 再思考："那看看是不是主库吧"
- 再行动：执行 SHOW MASTER STATUS
- 再观察：有 binlog 信息，确认是主库
- ......
- 最终思考："信息够了，可以给出完整诊断报告"

关键在于：
你不需要写 if-else 来编排这些步骤。
模型自己决定调什么工具、调几次、什么时候停止。你只需要提供工具，剩下的交给模型推理。

Agent 开发三要素

Agent = LLM + Tools + Prompt

LLM（大脑）：选什么模型、怎么连。我用的是 Claude Sonnet 4.5，通过公司内部的 OpenAI 兼容网关调用。

Tools（手脚）：写 Python 函数让模型能调用。这是 80% 的工作量。我写了三个工具：ssh_command（远程执行 Linux 命令）、mysql_query（执行只读 SQL）、write_file（保存报告到文件）。

Prompt（指令）：告诉模型它是谁、能做什么。比如"你是资深 DBA，精通 MySQL 5.7/8.0，所有操作只读，用中文回答"。

六步开发流程

Step 1：定义场景和工具边界
先想清楚三个问题：
- Agent 解决什么问题？→ MySQL/Linux 远程只读诊断
- 需要哪些工具？→ SSH 命令、MySQL 查询、写文件
- 安全红线是什么？→ 绝对只读，拦截所有写操作

Step 2：搭项目骨架
用 CrewAI 框架，项目结构很简单：config.yaml（配置）、main.py（入口）、crew.py（Agent 定义）、tools/ 目录下放各个工具。

Step 3：写工具（核心）
每个工具就是一个 Python 类，有一个 name、一个 description（模型靠它决定什么时候调用）、一个 _run 方法（实际执行逻辑）。

工具开发的四个要点：
- description 要写清楚——模型完全靠这段描述来决定什么时候用这个工具
- _run 返回纯文本——模型只能理解文本
- 做好安全拦截——模型可能会尝试执行 DROP TABLE
- 加超时控制——防止 tail -f 这类命令卡死整个 Agent

Step 4：配置 LLM
配好模型名称、API 地址、密钥。如果用的是 OpenAI 兼容网关，模型名需要加 "openai/" 前缀让路由层正确转发。

Step 5：组装 Agent
把 LLM、工具列表、角色 Prompt 组合到一起，创建 Agent 实例。

Step 6：运行
把用户的问题包装成 Task，交给 Crew 执行，拿到结果。

实际效果

我对 Agent 说："检查这台机器的主从复制状态"
它自己完成了以下操作：
- 执行 SHOW SLAVE STATUS → 发现不是从库
- 执行 SHOW MASTER STATUS → 确认是主库，拿到 binlog 和 GTID 信息
- 执行 SHOW SLAVE HOSTS → 发现没有从库连接
- 查询半同步复制变量 → 发现半同步已降级为异步
- SSH 查看 MySQL 错误日志 → 找到超时切换的时间点
- 查询复制用户权限 → 确认配置完整
- 查看 processlist → 确认没有 Binlog Dump 线程

最终输出了一份完整的诊断报告，准确指出：主库配置正常但当前无从库连接，半同步复制因超时已降级，存在数据丢失风险，并给出了紧急处理建议。

整个过程 6 轮 LLM 调用，全自动，无需人工干预。

踩过的坑

真实开发中踩了不少坑，记录几个典型的：

MySQL root 不允许 TCP 连接：root 账户只允许 unix socket 登录，SSH 隧道转发的 127.0.0.1 TCP 连接被拒。解决方案：放弃 pymysql 直连，改为 SSH 到目标机器后用 mysql CLI 通过 socket 执行。

模型后端不支持 assistant prefill：公司网关后面的某些模型走 AWS Bedrock，而 Bedrock 不支持 CrewAI 使用的 assistant message prefill 特性。解决方案：逐个测试网关上的模型，找到走非 Bedrock 后端的模型。

tail -f 卡死 Agent：模型执行 "tail -100 slow-queries.log" 时，如果日志行数不够，tail 会等待新数据写入，导致 SSH 命令永远不返回。解决方案：用 paramiko channel 级别的非阻塞读取 + deadline 超时机制替代 exec_command。

调试回调被框架覆盖：我写了一个 --debug 模式输出每次 LLM 交互的完整 prompt/response，但 CrewAI 内部会重置 litellm 的回调列表。解决方案：monkey-patch 框架的 set_callbacks 方法，确保自定义 logger 始终存在。

一个公式

Agent 效果 = 模型能力 x 工具质量 x Prompt 清晰度

- 模型不够强 → 换更大的模型
- 工具返回乱码 → 格式化输出，让模型能理解
- 模型不知道用哪个工具 → 改工具的 description
- 模型反复犯错重试 → 加 --debug 看完整 prompt，调整角色描述

总结

Agent 开发没有想象中那么难。本质上就是：
- 给大模型一组工具
- 告诉它是什么角色
- 让它自己决定怎么用工具解决问题

80% 的工作量在写好工具——安全拦截、超时控制、输出格式化。剩下 20% 是选模型和调 Prompt。

框架（CrewAI/LangChain/AutoGen）只是脚手架，真正决定 Agent 好不好用的是你的工具质量和对业务场景的理解。

---

## 图片

![Image 1](https://pbs.twimg.com/media/Gi4p7jLaQAAk4S3?format=jpg&name=large)

