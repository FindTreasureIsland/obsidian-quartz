---
title: OpenClaw 多 Agent 架构实践：一个进程跑三个独立 AI 助手
author: "雪踏乌云 (@Pluvio9yte)"
date: 2026-02-18T23:59:00Z
source: "https://x.com/Pluvio9yte/status/2024151797900718086"
tags:
  - twitter
  - article
---

# OpenClaw 多 Agent 架构实践：一个进程跑三个独立 AI 助手

**作者**: 雪踏乌云 (@Pluvio9yte)
**时间**: 2026-02-18T23:59:00Z
**来源**: [原始链接](https://x.com/Pluvio9yte/status/2024151797900718086)

---

用 OpenClaw 搭了个多 agent 系统，一台 Mac mini 上跑三个独立 AI，各有各的 Telegram bot，能够分工协作先说说什么是 OpenClaw

OpenClaw 是一个开源的 AI Gateway，可以理解为一个"AI 管家后台"。它跑在你自己的机器上（Mac、Linux、树莓派、云服务器上都行），帮你把 Claude、GPT 这些大模型接入到 Telegram、Discord、WhatsApp 等聊天工具里。

关键是：它不只能跑一个 AI，还能同时跑多个，每个都是独立的"人格"，有自己的名字、记忆、技能和聊天窗口。架构：一个 Gateway，三个 Agent

我的配置是三个 agent，各管一摊事：

📷 总督 — 主 agent
负责日常对话和统筹协调。相当于"老板"，其他两个 agent 都是它帮我配出来的。平时跟我聊天、管配置、装技能、处理杂事都找它。

📷 巡查 — 定时任务专员
专门干重复性的定时工作。我给它配了 cron 任务，每天定时自动跑数据采集和对比，跑完把结果推送到 Telegram 给我。我不用管，它自己干。

📷 营造 — 开发助手
写代码、调脚本、排查技术问题。有独立的工作区，不会跟其他 agent 的文件混在一起。需要写东西的时候直接找它。每个 agent 都有自己的：
• 工作区（独立的文件夹，放代码、数据、笔记）
• 记忆（MEMORY.md，它自己维护的长期记忆）
• 人设（SOUL.md，定义它的性格、说话风格、行为准则）
• Telegram bot（独立的聊天窗口，互不干扰）简单说就是：三个 AI 各有各的"大脑"和"办公室"，但共用一个后台进程，省资源。配置步骤如下（5 分钟加一个 agent）
直接将下面这些发给你的 OpenClaw 即可① 创建工作区目录

mkdir -p ~/.openclaw/workspace-patrol
mkdir -p ~/.openclaw/agents/patrol/agent

然后在工作区里写好几个文件：
• SOUL.md — 告诉它"你是谁"，比如"你是巡查，专注定时任务，风格简洁"
• USER.md — 告诉它"你的用户是谁"，比如时区、语言偏好
• MEMORY.md — 初始记忆，比如要用到的 API 凭证、工作流说明

② 复制认证文件

cp ~/.openclaw/agents/main/agent/auth-profiles.json ~/.openclaw/agents/patrol/agent/

这一步容易忘。每个 agent 的 API key 是独立管理的，不会自动从主 agent 继承。

③ 创建 Telegram bot

去 Telegram 找 @BotFather，发 /newbot，起个名字，拿到 bot token。

④ 编辑配置文件 openclaw.json

加三段内容：

agents.list 里注册新 agent：
{
"id": "patrol",
"name": "巡查",
"workspace": "~/.openclaw/workspace-patrol",
"identity": { "name": "巡查", "emoji": "📷" }
}

channels.telegram.accounts 里加 bot 信息：
"patrol": {
"botToken": "你的token",
"dmPolicy": "allowlist",
"allowFrom": ["你的TelegramID"],
"proxy": "http://127.0.0.1:7897"
}

bindings 里加路由规则（告诉 Gateway 这个 bot 的消息交给哪个 agent 处理）：
{ "agentId": "patrol", "match": { "channel": "telegram", "accountId": "patrol" } }

⑤ 重启 Gateway，新 agent 立刻上线



Agent 间通信

config 里开一个开关就行：
"tools": {
"agentToAgent": {
"enabled": true,
"allow": ["main", "patrol", "builder"]
}
}

开了之后，总督可以给巡查发指令，巡查也能把结果汇报回来。skills 共享

把 skills 放到 ~/.openclaw/skills/ 目录，所有 agent 自动共享。不用每个 agent 都装一遍。

踩过的坑

• 新 agent 首次收消息可能报 "Session file path" 错误 → 删掉 sessions/sessions.json 重启就好
• auth-profiles.json 必须手动复制到每个 agent 目录，不会自动继承
• dmPolicy 建议用 allowlist + 指定你的 Telegram ID，比默认的 pairing 模式省事
• 每个 bot 的 proxy 要单独配，不会继承全局设置

最终效果

三个 Telegram 聊天窗口，三个独立 AI 助手，一个后台进程。各管各的事，互不干扰，需要协作的时候又能互相通信。跑在一台 Mac mini 上，稳定运行。

---

## 图片

_无图片_
