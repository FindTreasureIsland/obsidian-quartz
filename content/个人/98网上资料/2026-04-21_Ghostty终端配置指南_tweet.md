---
title: Mac装机首选的AI友好型终端Ghostty配置指南
author: AI少年 (@aehyok)
source: tweet
tags: [Mac, Ghostty, 终端, AI工具]
stats:
  likes: 71
  retweets: 10
  views: 7075
date: 2026-04-21
---

# Mac装机首选的AI友好型终端Ghostty配置指南

**来源**：https://x.com/aehyok/status/2046468146790568359

**作者**：AI少年（全栈独立开发者，公众号：那个曾经的少年回来了）

---

## 核心观点

如果拿到一款新的Mac，最先安装的终端工具就是Ghostty。它对AI工具特别友好，支持macOS和Linux（不支持Windows）。

适合使用AI终端比较多的开发者：Claude Code、Codex、Gemini CLI等。

## Ghostty的核心优势

### 1. 分屏功能强大

- **Tab管理**：Command + 1/2 轻松切换Tab
- **左右分屏**：Command + D
- **上下分屏**：Command + Shift + D
- **焦点切换**：Command + Option + Left/Right/Up/Down

### 2. AI友好特性

- 支持多窗口管理，方便同时操作多个AI会话
- 与Claude Code等AI工具无缝配合
- 滚动缓冲区大（默认50MB）
- 打字时自动隐藏鼠标

### 3. 视觉体验

- 主题跟随系统深色模式自动切换（Catppuccin Latte/Mocha）
- 背景透明度可调（0.0~1.0）
- 背景模糊（毛玻璃效果）
- 支持连字（liga）和特色字体（推荐Maple Mono NF CN）

## 安装方法

```bash
# 通过Homebrew安装
brew search ghostty
brew install --cask ghostty

# 或去官网下载
# ghostty.org/download
```

## 配置文件

关键配置项：
- `theme` — 主题设置
- `background-opacity` — 透明度
- `background-blur` — 模糊效果
- `font-family` — 字体（推荐Maple Mono NF CN）
- `window-save-state = always` — 记住窗口状态
- `copy-on-select = clipboard` — 选中即复制
- `macos-option-as-alt = true` — Option键作为Alt

## 快捷键汇总

| 功能 | 快捷键 |
|------|--------|
| 打开配置 | Cmd + , |
| 重载配置 | Cmd + Shift + , |
| 新Tab | Cmd + T |
| 关闭Tab | Cmd + W |
| 左右分屏 | Cmd + D |
| 上下分屏 | Cmd + Shift + D |
| 焦点切换 | Cmd + Option + 方向键 |

## Mac使用指南系列

1. [Homebrew软件包管理器从入门到精通](https://x.com/aehyok/status/2042527221332508866)
2. [从零搭建Codex App桌面端结合GitHub CLI](https://x.com/aehyok/status/2044239791231996394)
3. 本文：Ghostty配置指南

---

**原文链接**：https://x.com/aehyok/status/2046468146790568359
