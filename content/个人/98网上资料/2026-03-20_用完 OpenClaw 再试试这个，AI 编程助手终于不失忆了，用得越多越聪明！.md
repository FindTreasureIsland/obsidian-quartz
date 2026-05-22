---
title: 用完 OpenClaw 再试试这个，AI 编程助手终于不失忆了，用得越多越聪明！
author: "sitin (@sitinme)"
date: 2026-03-19T09:31:00
source: "https://x.com/sitinme/status/2034442505882919201"
tags:
  - twitter
  - article
---

# 用完 OpenClaw 再试试这个，AI 编程助手终于不失忆了，用得越多越聪明！

**作者**: sitin (@sitinme)
**时间**: 2026-03-19T09:31:00
**来源**: [原始链接](https://x.com/sitinme/status/2034442505882919201)

---

前两天用 Claude Code 写了一下午代码，中间纠正了三次"别用 sudo 跑 Docker"，结果第二天打开它又用 sudo 了。

AI 编程助手什么都好，就是不长记性，你跟它说过的偏好、踩过的坑、项目的技术栈，关掉窗口就全忘了。

后来在GitHub 上刚出了一个项目可以解决这个问题----Hermes Agent，Nous Research 出品，它的核心思路就一句话：用得越多越聪明。

它会自动记住你的偏好，自动从复杂任务中提炼出可复用的"技能"，下次遇到类似任务直接调用，不需要你教它，它自己学。

---

## Hermes Agent 到底是什么？

一句话概括：一个会自我进化的 AI Agent 平台。

它不是 VS Code 插件，也不是浏览器里的聊天框。它是一个独立运行的 Agent——可以跑在你的笔记本上，也可以跑在一台 $5 的 VPS 上。你通过终端、Telegram、Discord、Slack、WhatsApp 甚至 Signal 跟它对话，它帮你写代码、搜信息、管理服务器、跑定时任务。

听起来跟 OpenClaw 很像？没错，它可以视为 OpenClaw 的竞争对手，甚至还专门做了一个 hermes claw migrate 命令，一键把你的 OpenClaw 配置、记忆、Skills 全部迁移过来。

但 Hermes Agent 有一个 OpenClaw 目前做不到的东西——自动学习闭环。

---

## 核心能力：自动学习闭环

说实话，看完这个机制我挺意外的。它的学习分三层，一层比一层狠：

**第一层：记住你是谁**

Hermes 有两个持久化记忆文件：
- **MEMORY.md** — 它自己的笔记本，记环境信息、项目结构、踩过的坑（上限 2,200 字符）
- **USER.md** — 你的画像，记你的偏好、沟通风格、技术栈（上限 1,375 字符）

不需要手动维护这两个文件，它会**自动**在对话过程中提取关键信息写进去。

比如你说了一句"我用的是 PostgreSQL 16"，它就记下来了，下次让它写数据库代码，它直接按 PostgreSQL 16 来。

记忆满了怎么办？它会自己整理——把过时的信息删掉，给新的腾地方。

**第二层：自动创建 Skills**

这是最酷的部分。

当 Hermes 完成一个复杂任务（比如调了 5 次以上工具、中间踩了坑又解决了），它会自动把整个流程提炼成一个 Skill 保存下来。下次遇到类似任务，直接调用这个 Skill，不用重新摸索。

更厉害的是，**Skills 在使用过程中会自我改进**。如果某个 Skill 在执行时发现了更好的做法，它会自动更新自己。

这些 Skills 存在 ~/.hermes/skills/ 目录下，可以随时查看、编辑、删除。格式兼容 agentskills.io 开放标准，也就是说在 Claude Code 里用的 Skills，Hermes 也能用。

**第三层：跨会话搜索**

Hermes 用 FTS5 全文索引保存所有历史对话，搜索时结合 LLM 做摘要，可以说"我上周跟你讨论过的那个部署方案"，它能翻出来。

---

## 安装：一行命令搞定

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

支持 Linux、macOS 和 WSL2。安装脚本会自动处理 Python、Node.js 和所有依赖。装完之后：

source ~/.bashrc && hermes

就能开始对话了。

---

## 配置模型：不绑定任何厂商

Hermes 不强制你用某个模型。运行 hermes model 进入交互式选择：

随时用 hermes model 切换，不需要改代码。

---

## 连接你的聊天平台

这是 Hermes 的另一个亮点——它不只活在终端里。

hermes gateway setup

一条命令配好消息网关，支持：
- Telegram
- Discord
- Slack
- WhatsApp
- Signal
- Home Assistant

配好之后，在 Telegram 上发一条消息，Hermes 在你的 VPS 上执行，结果推回 Telegram。人在地铁上，活在服务器干。

---

## 定时任务：用自然语言设置 Cron

传统 Cron 要写 0 9 * * * /path/to/script.sh。在 Hermes 里，你只需要说：

> 每天早上 9 点，去 Hacker News 找 AI 相关新闻，整理一份摘要发到我的 Telegram。

它自己设好定时任务，到点自动执行，结果推送到你指定的平台。

---

## 40+ 内置工具

开箱就能用的工具有 40 多个，列几个关键的：
- **终端操作** — 执行命令、管理文件
- **网页搜索** — 内置搜索，不需要额外配置
- **代码编辑** — 读写文件、精准替换
- **子 Agent** — 拆分任务，并行执行
- **MCP 集成** — 连接任何 MCP 服务器

用 hermes tools 管理哪些工具启用、哪些关闭。

---

## 6 种运行环境

不想让 AI 直接操作你的电脑？Hermes 支持 6 种终端后端：

```bash
hermes config set terminal.backend docker  # Docker 隔离
hermes config set terminal.backend ssh      # 远程服务器
```

Daytona 和 Modal 特别适合个人开发者——环境空闲时自动休眠，来任务了秒级唤醒，不跑的时候不花钱。

---

## 从 OpenClaw 迁移

如果你现在在用 OpenClaw，Hermes 提供了完整的迁移工具：

```bash
hermes claw migrate        # 交互式迁移
hermes claw migrate --dry-run  # 先预览，不实际执行
```

会导入这些内容：
- SOUL.md 人设文件
- MEMORY.md 和 USER.md 记忆
- 你创建的 Skills
- 命令白名单
- 消息平台配置（Telegram 等）
- API Key（Telegram、OpenRouter、OpenAI、Anthropic、ElevenLabs）

基本上是无痛切换。

---

## Skills 商店

除了自动学习的 Skills，Hermes 也有自己的 Skills 市场：

```bash
hermes skills search kubernetes  # 搜索
hermes skills install openai/skills/k8s  # 安装
```

兼容 agentskills.io 标准，skills.sh 上的 Skills 也能装。

---

## 跟 OpenClaw 比，到底怎么选？

公平地说，OpenClaw 在社区生态和稳定性上目前还是领先的，但 Hermes Agent 在"自动学习"这个方向上确实走在了前面。

最后，Hermes Agent 代表了 AI Agent 发展的一个方向：**从"工具"变成"伙伴"**。

现在的大多数 AI 编程助手，本质上还是一个高级工具，你给它指令，它执行，结束。下次再来，它不认识你了。Hermes 想做的是一个真正的"数字伙伴"：它记住你，了解你的习惯，从每次合作中积累经验。时间越长，配合越默契。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HDqLIXSbgAANiHL?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HDqJmLYaoAA2xz4?format=jpg&name=900x900)

![Image 3](https://pbs.twimg.com/media/HDqJsCybEAMDcgF?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HDqJ5fibwAAetKi?format=png&name=900x900)

![Image 5](https://pbs.twimg.com/media/HDqKFz1bEAMDf58?format=jpg&name=medium)

![Image 6](https://pbs.twimg.com/media/HDqKL25bgAAkAz8?format=png&name=900x900)

![Image 7](https://pbs.twimg.com/media/HDqKkEibQAEs5GY?format=jpg&name=medium)

![Image 8](https://pbs.twimg.com/media/HDqKwsrbEAAKpAn?format=jpg&name=medium)

![Image 9](https://pbs.twimg.com/media/HDqK8oabIAACtDj?format=jpg&name=large)

