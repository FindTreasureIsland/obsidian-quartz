---
title: 从 0 开始构建专属 Agent Team ：tmux 安装与基础入门
author: "劳伦斯 (@LawrenceW_Zen)"
date: 2026-03-21 15:51
source: "https://x.com/LawrenceW_Zen/status/2035383740239855810"
tags:
  - twitter
  - article
---

# 从 0 开始构建专属 Agent Team ：tmux 安装与基础入门

**作者**: 劳伦斯 (@LawrenceW_Zen)
**时间**: 2026-03-21 15:51
**来源**: [原始链接](https://x.com/LawrenceW_Zen/status/2035383740239855810)

---

这是「从 0 开始构建专属 Agent Team」系列的预告篇。

之后的正篇里我们会用到 tmux，但很多人可能没装过甚至没听过这个东西。这篇单独把安装和最基础的用法讲清楚，正篇就不再重复了。

## tmux 是什么

大概就是：tmux 让你在一个终端窗口里同时跑多个终端。

你可以把终端窗口想象成一张桌子。正常情况下，桌子上只能放一台电脑。tmux 做的事就是把桌子分成好几块，每一块上面都能放一台电脑，独立运行。

## 为什么我们需要它？

因为后面我们要让 Claude Code 和 Codex 同时跑在一个终端窗口里——左边跟 Claude 聊天，右边看 Codex 干活。没有 tmux，做不到这件事。

## 让 Claude 帮你安装 tmux

你不需要查系统版本、找对应命令，直接跟 Claude 说：

> 帮我安装 tmux。

Claude 会自动检测你的系统（macOS、Ubuntu、WSL 等），选择合适的安装方式，并执行安装命令。

Claude 会：

- 检测你的操作系统
- 检查是否已经安装 tmux
- 如果没有，选择合适的命令安装
- 验证安装（运行 tmux -V 确认版本）

## 让 Claude 帮你配好 tmux

你不需要手动改配置文件，直接跟 Claude 说：

> 帮我配置 tmux，要求：鼠标支持、pane 编号从 1 开始、pane 标题显示当前命令、状态栏简洁、历史缓冲区加大到 10000 行。

Claude 会自动：

- 检查你的 ~/.tmux.conf 是否存在
- 写入 Agent Team 专用配置
- 执行 tmux source-file 使其生效
- 验证配置（列出当前 pane 看编号格式对不对）

配置完成后，Claude 会显示一条确认信息，告诉你 tmux 已经准备好为 Agent Team 服务了。

另外，AI 操作 tmux 的命令，你不用记。

后面正篇里，这些命令都是 Claude 自动帮你执行的，你不需要手动敲。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HD8g2MwbYAAyDVA?format=jpg&name=medium)

