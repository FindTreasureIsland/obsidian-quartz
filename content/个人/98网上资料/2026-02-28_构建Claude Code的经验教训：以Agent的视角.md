---
title: 构建Claude Code的经验教训：以Agent的视角
author: "trq212 (@trq212)"
date: 2026-02-28T10:00:00
source: "https://x.com/trq212/status/2027463795355095314"
tags:
  - twitter
  - article
---

# 构建Claude Code的经验教训：以Agent的视角

**作者**: trq212 (@trq212)
**时间**: 2026-02-28T10:00:00
**来源**: [原始链接](https://x.com/trq212/status/2027463795355095314)

---

这篇文章分享了构建Claude Code过程中关于AI Agent工具设计的经验。

## 核心观点

1. **像Agent一样思考**：设计工具时，要根据模型能力来调整。为Agent提供与其能力相符的工具。

2. **改进Elicitation和AskUserQuestion工具**：
   - 尝试#1：向ExitPlanTool添加参数，但让Claude感到困惑
   - 尝试#2：修改输出格式为Markdown，但不能保证每次成功
   - 尝试#3：创建AskUserQuestion工具，效果最好

3. **Tasks和Todos的演进**：
   - 模型初期需要Todo list保持专注
   - 随着模型改进，Todo反而成为限制
   - 用Task Tool替换TodoWrite，Tasks更适合agents间沟通

4. **设计搜索界面**：
   - 从RAG向量数据库到让Claude自己搜索
   - Claude可以自行构建上下文

5. **渐进式披露（Progressive Disclosure）**：
   - 让agents通过探索逐步发现相关上下文
   - 通过skills递归读取文件来添加新功能

6. **Claude Code指南Agent**：
   - 当用户询问Claude自身问题时调用
   - 不添加工具的情况下扩展action space

## 总结

工具设计既是科学也是艺术，取决于模型能力、agent目标和运行环境。需要不断实验，阅读输出，尝试新事物。

---

## 图片

_无图片_
