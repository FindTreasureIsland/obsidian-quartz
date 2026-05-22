---
title: Working with worktree in the Codex app
author: Thomas Ricouard (@Dimillian)
source: tweet
tags: [Codex, Git, Worktree, AI编程]
stats:
  likes: 159
  retweets: 8
  views: 35555
date: 2026-04-19
---

# Working with worktree in the Codex app

**来源**：https://x.com/Dimillian/status/2045908187618894176

**作者**：Thomas Ricouard，Developer Experience @OpenAI Codex

---

## 核心观点

Git worktree 在 Codex app 中是如何工作的。

## 什么是 Git Worktree

Git worktree 让你可以在同一个 repo 的不同分支上同时工作，而不需要反复 clone 或频繁切换分支。

简单说：每个有意义的任务都可以有自己独立的隔离工作副本。

## Codex App 的三层架构

### 第一层：Sparse Checkout

Codex 团队使用 sparse checkout，只 checkout app 需要的部分，避免每次都拉取整个仓库。

### 第二层：环境配置

本地环境配置文件定义了如何安装依赖、运行 app、运行检查和测试。这样不需要每次都问"这个 repo 需要什么特殊命令"。

### 第三层：Worktree 可视化

Codex app 在产品层面展示 worktree。当任务需要隔离时，app 可以：
- 创建 worktree
- 显示设置进度
- 将对话路由到对应 workspace
- 保持 terminal/action 关联
- 后续帮助清理

## 在 Codex App 中的具体使用

### 启动任务

在 Codex app 中启动任务时，可以选择：
- 本地运行
- 云端运行
- 新建 worktree

### 环境管理

可以创建和编辑 setup script（设置脚本），用于 worktree 创建后的初始化配置。不同平台还可以有不同的变体。

### 提交和推送

三种方式：
1. **$yeet**：内置 skill，一键创建 PR，保持 worktree
2. **Handoff to branch**：保持 worktree 与新分支同步
3. **Commit and push UI**：手动提交、推送、创建 PR

### 清理

完成 worktree 后，可以 archive thread，Codex app 会自动清理旧的 worktree，节省空间。

---

**原文链接**：https://x.com/Dimillian/status/2045908187618894176
