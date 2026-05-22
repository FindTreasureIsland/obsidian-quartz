---
title: DeepSeek-V4预览版：迈入百万上下文普惠时代
author: DeepSeek
source: 人人都是产品经理
tags: [AI, DeepSeek, 大模型, 开源]
date: 2026-04-24
stats:
  views: 1071
  collections: 6
  readtime: 7分钟
---

# DeepSeek-V4预览版：迈入百万上下文普惠时代

**来源**：https://www.woshipm.com/ai/6383155.html

**作者**：DeepSeek

**发布时间**：2026-04-24

---

## 核心亮点

DeepSeek-V4拥有**百万字超长上下文**，在Agent能力、世界知识和推理性能上均实现国内与开源领域领先。

两个版本：
- **DeepSeek-V4-Pro**：性能比肩顶级闭源模型
- **DeepSeek-V4-Flash**：兼顾效率与成本

---

## 核心能力

### DeepSeek-V4-Pro：性能比肩顶级闭源模型

**Agent能力大幅提高**
- Agentic Coding评测中，达到当前开源模型最佳水平
- 公司内部员工使用的Agentic Coding模型
- 体验优于Sonnet 4.5，交付质量接近Opus 4.6非思考模式

**世界知识**
- 世界知识测评大幅领先其他开源模型
- 仅稍逊于顶尖闭源模型Gemini-Pro-3.1

**推理性能**
- 数学、STEM、竞赛型代码测评超越所有已公开评测的开源模型
- 比肩世界顶级闭源模型

### DeepSeek-V4-Flash：更快捷高效的经济之选

- 世界知识储备稍逊，但推理能力接近
- 参数和激活更小，提供更快捷、经济的API服务
- 简单任务上与Pro版旗鼓相当，高难度任务有差距

---

## 技术创新

### 结构创新：超高上下文效率

- 全新注意力机制，token维度压缩
- 结合DSA稀疏注意力（DeepSeek Sparse Attention）
- 实现全球领先的长上下文能力
- 大幅降低计算和显存需求

**1M上下文成为DeepSeek所有官方服务标配**

---

## Agent能力专项优化

针对主流Agent产品进行适配和优化：
- Claude Code
- OpenClaw
- OpenCode
- CodeBuddy

在代码任务、文档生成任务等方面表现均有提升。

---

## API访问

- base_url不变
- model参数改为 `deepseek-v4-pro` 或 `deepseek-v4-flash`
- 最大上下文长度1M
- 支持非思考模式与思考模式
- 思考模式支持reasoning_effort参数设置思考强度

**旧接口（deepseek-chat、deepseek-reasoner）将于三个月后（2026-07-24）停止使用**

---

## 开源信息

- HuggingFace: https://huggingface.co/collections/deepseek-ai/deepseek-v4
- ModelScope: https://modelscope.cn/collections/DeepSeek-ai/DeepSeek-V4
- 技术报告：https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf

---

## 写在后面的话

「不诱于誉，不恐于诽，率道而行，端然正己。」

感谢每一位用户的信任与支持，我们将始终秉持长期主义的原则理念，在尝试与思考中踏实前行，努力向实现AGI的目标不断靠近。

---

**原文链接**：https://www.woshipm.com/ai/6383155.html
