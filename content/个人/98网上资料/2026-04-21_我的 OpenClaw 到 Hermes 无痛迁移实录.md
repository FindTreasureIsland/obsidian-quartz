---
title: "我的 OpenClaw 到 Hermes 无痛迁移实录"
source: "https://x.com/ResearchWang/status/2045133243629154726"
author:
  - "[[@ResearchWang]]"
published: 2026-04-17
created: 2026-04-21
description: "最近用OpenClaw 辅助我的个人网站进行热点抓取，越用越发现不对劲！网站入口： Research王13 | AI 观察、工具与社群入口开始还挺好， OpenClaw 接上 Telegram 和 飞书 ，让它定时去扫推特和Github的热点，抓回来做分类和摘要。但用了两周之后，..."
tags:
  - "clippings"
---
![图像](https://pbs.twimg.com/media/HFx35yTbwAAoXle?format=jpg&name=large)

**最近用OpenClaw 辅助我的个人网站进行热点抓取，越用越发现不对劲！**

> [网站入口： Research王13 | AI 观察、工具与社群入口](https://researchwang13.space/)

开始还挺好， OpenClaw 接上 Telegram 和 飞书 ，让它定时去扫推特和Github的热点，抓回来做分类和摘要。但用了两周之后，越来越感觉：OpenClaw**不会变聪明，即使我配置了记忆系统，它也不会变聪明！**每次遇到相似的热点结构，它都像第一次见到一样重新处理；你上周手动纠正过的分类错误，同样的问题它会原样再犯一遍。

在扫描出来的热度排行榜里发现，hermes-agent 突然蹿到周榜第一，用了一下发现hermes的智商特别高，它会自动学习工作模式，会经常做知识沉淀

![图像](https://pbs.twimg.com/media/HGE5krLb0AA94nV?format=jpg&name=large)

[https://researchwang13.space/](https://researchwang13.space/)

今天教大家如何把openclaw的配置全部移动到Hermes

# 📚 目录

- 弃用 OpenClaw 的真相：用真实数据丈量
- Hermes 极简安装与一键迁移避坑
- 2招！ 解放Hermes 原生智力

## 一 、弃用 OpenClaw 的真相：用真实数据丈量

为了客观评估这两者的差异，我没有仅凭主观感受，而是拉取了这两个框架各自运行一周的后台日志。今天，我们就用真实的数据来说话，看看所谓“AI Agent 的智商”，到底体现在哪里。

> 为了保证公平，两个通过 Cron 任务每2小时定时抓取固定的50个 AI 领域推特博主及每日 Github Trending 榜单，且统一调用 GPT-5.4模型，进行分类

📊 运行数据对比

![图像](https://pbs.twimg.com/media/HGGXkZLbYAAK33v?format=png&name=large)

Hermes 在准确率、维护成本和运行效率上均优于OpenClaw，我果断将OpenClaw切换到Hermes

## 二 、Hermes 极简安装与一键迁移避坑

我直接在openclaw的服务器上安装hermes （腾讯云 ），安装命令：

```bash
# 安装 hermes - 在服务器的命令行运行

curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

#安装完成后
# 刷新环境
source ~/.bashrc 

#启动hermes
hermes
```

**PS：** 运行的时候会问要不要进行把openclaw迁移到hermes中，一定要选 Y ！！

hermes在迁移的时候，如果你之前配置好了openclaw的telegram频道，飞书频道，wechat都可以一键移植。

![图像](https://pbs.twimg.com/media/HGGaiQqagAAuKMc?format=png&name=large)

hermes常见的配置指令

```bash
hermes setup # 重新运行完整的初始化配置向导

hermes setup model # 更改大模型

hermes setup gateway #配置消息网关。用于绑定、更新或重新授权 Telegram、飞书、Slack、Discord 等即时通讯平台。

hermes setup tools #开启、关闭或配置外置工具。

hermes setup terminal #更改终端后端运行环境

hermes setup agent  #配置 Hermes 的身份标识和性格预设。这个指令可以修改核心的 SOUL.md 文件

hermes config #在终端中打印并查看当前正在生效的全部设置详情。

hermes config edit # 用系统默认的代码编辑器（如 Vim、VS Code 等），直接打开核心配置文件 config.yaml 

hermes config set <key> <value>  #不打开文件，直接用命令行修改某一个特定参数。例如：hermes config set temperature 0.7。

hermes # 直接在命令行启动系统并进入终端聊天模式

hermes model  # hermes setup model 的快捷指令
```

## 三、2招！ 解放Hermes 原生智力

虽然选了一键配置迁移，但这只是把旧家当搬过来了。**OpenClaw 的底层逻辑是依赖的 Prompt 和 RAG 插件，这些对 Hermes反而是累赘！**

```bash
# 启动成功后 执行

hermes config edit
```

在打开的配置文件中，手动做减法：

1. **删掉冗余**了**personalities: 修改成简单的default（可自己根据任务编辑）**

> default: 你现在的核心任务是处理推特和 Github 抓取的数据，输出精炼的 Markdown 摘要。具体的分类标准参考你自身的知识沉淀。

![图像](https://pbs.twimg.com/media/HGHEZGzbAAAqWIE?format=png&name=large)

**2\. 清理旧的记忆插件 ：** 如果你之前的配置里有挂载 Mem0 或 OpenViking 这类外挂数据库节点，直接在代码里删掉确保和下面图一样的记忆配置

![图像](https://pbs.twimg.com/media/HGHBmYqbcAAGDyJ?format=png&name=large)