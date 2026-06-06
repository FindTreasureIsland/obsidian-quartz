---
title: "A Functional Taxonomy of World Models"
type: article
source: X/Twitter NoteTweet
author: Fei-Fei Li (李飞飞)
url: https://x.com/drfeifei/status/2062247238143996275
created: 2026-06-03
tags: [AI, WorldModels, SpatialIntelligence, Simulation, Robotics]
---

# A Functional Taxonomy of World Models

> *"The world is everything that is the case."*
> — Ludwig Wittgenstein, Tractatus Logico-Philosophicus, 1921

**作者：** Fei-Fei Li（李飞飞），Stanford CS教授，World Labs CEO/Co-founder
**平台：** X/Twitter NoteTweet
**链接：** https://x.com/drfeifei/status/2062247238143996275

---

## 核心观点

### 世界模型的三种功能分类

李飞飞在这篇长文中提出，世界模型（World Models）并非单一概念，而是三种不同功能的总称：

**1. Renderer（渲染器）**
- 输出像素/图像，服务于人眼
- 质量标准：**视觉保真度**
- 例子：文生视频模型（Genie 3、Runway、Sora）
- 局限：视觉漂亮但物理上不可信，无法用于训练机器人

**2. Simulator（模拟器）**
- 输出**状态**：几何的、物理的、动力学上可信的世界表示
- 质量标准：**结构准确性**（几何结构+物理定律）
- 例子：NVIDIA Omniverse、物理引擎
- 双重消费者：人类（建筑师/设计师）+ 计算机程序（RL训练）

**3. Planner（规划器）**
- 输出**动作**：给定观测和目标，回答"下一步该做什么"
- 例子：VLA模型（Vision-Language-Action）、模型控制系统
- 现状：最有趣但最早期，实验室demo很好看，但真实世界部署差距巨大

---

## 关键洞察

### 为什么模拟器是枢纽

- **渲染器**最成熟（商业化最快），但天花板是视觉而非物理可信
- **规划器**最有潜力但最早期，真实世界厨房/仓库/手术室的差距仍然巨大
- **模拟器**是连接两者的桥梁——几何/物理/动力学是世界本身的结构

> "If language is an abstraction of the world and pixels are a projection of it, then geometry, physics, and dynamics are the world itself."

模拟器的商业规模惊人：NVIDIA Omniverse 目标市场超过万亿美元（工厂、仓库、供应链、数字孪生）。

### 边界正在崩塌

最前沿的pattern是三者开始融合——渲染、模拟、规划共享同一个底层世界理解。

World Labs 的 **Marble** 就是这个方向的第一步：输入多模态prompt（文本/图像/视频/空间草图），生成可探索3D环境，输出高斯散点和碰撞网格。

统一世界模型的逻辑终点：一个foundation model能渲染逼真视图、产生物理准确结构、规划动作序列，根据下游需求切换输出模态。

---

## 金句

> "Language gave machines a way to talk about that world. World models are how machines will finally come to understand, imagine, reason and interact with it."

---

## 相关链接

- 李飞飞 Substack：https://drfeifei.substack.com/p/from-words-to-worlds-spatial-intelligence
- World Labs：https://www.theworldlabs.com
- Stanford HAI：https://hai.stanford.edu