---
title: "World Action Models: The Next Frontier in Embodied AI"
author: Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu, Chenchen Yang, Yikang Zhou, Zhaoye Fei, Jingjing Gong, Jinlan Fu, Mike Zheng Shou, Xuanjing Huang, Xipeng Qiu, Yu-Gang Jiang
source: https://openmoss.github.io/Awesome-WAM/
created: 2026-05-17
tags: [WAM, World Action Models, Embodied AI, VLA, World Models, 机器人, 具身智能, Survey]
stats:
  likes: N/A
  retweets: N/A
  views: N/A
---

**论文链接**: https://arxiv.org/abs/2605.12090
**项目仓库**: https://github.com/OpenMOSS/Awesome-WAM
**作者**: Siyin Wang, Junhao Shi, Zhaoyang Fu, Xinzhe He, Feihong Liu et al.
**机构**: Fudan University, Shanghai Innovation Institute, National University of Singapore

---

## 一句话定义

World Action Models (WAMs) 是具身基础模型，统一了预测性世界建模与动作生成——只有当未来状态预测成为策略的核心组成部分，而非外部模拟器或辅助骨干时，模型才称得上 WAM。

> **原文**：WAMs unify environmental dynamics modeling with motor control. A model qualifies as a WAM only when it performs forward predictive modeling of future state and couples action generation to that anticipated future, targeting **p(o', a | o, l)**.

---

## 核心要点

### VLA、WM 与 WAM 的区别

| 模型 | 目标函数 | 性质 | 局限性 |
|------|---------|------|--------|
| **VLA** | p(a \| o, l) | 反应式，直接从观测映射到动作 | 语义接地强，但本质是反应式，未来物理演化未显式表示 |
| **World Model** | p(o' \| o, a) | 预测性，想象未来观测 | 可预测但不可执行，本身不定义机器人策略 |
| **WAM** | p(o', a \| o, l) | 联合预测未来状态+动作 | 统一于单一具身策略框架 |

### 两大架构范式

**Cascaded WAM（级联架构）**
- 先由世界模型合成未来状态预测，再由独立动作模型从该计划解码可执行命令
- 优势：模块结构清晰
- 劣势：两阶段耦合质量是核心瓶颈
- 形式：显式规划（视频/深度法线/4D结构）vs 隐式规划（潜特征/未来token/隐藏状态）

**Joint WAM（联合架构）**
- 未来状态与动作在同一共享模型内联合预测，端到端联合监督
- 生成方式：自回归生成（共享token空间/多头路由）vs 扩散式生成（单引擎/多引擎扩散+非自回归）
- 核心问题：如何在离散token化、自回归序列建模、扩散、流匹配或并行生成中实现耦合

### 训练数据四大类

1. **Robot-Centric Teleoperation**：高频机器人轨迹，对齐的状态-动作对、低sim-to-real gap
2. **Portable Human Demonstration (UMI风格)**：重定向人类演示，低成本多样性、灵巧运动、多视角交互
3. **Simulation**：特权物理监督，可扩展变化、深度/姿态/碰撞/3D结构/可控物理
4. **Human/Egocentric Video**：海量互联网规模世界先验，长时序活动语义多样性

### 评估体系（双轴）

**世界建模能力**：
- 视觉保真度：PSNR、SSIM、LPIPS、DreamSim、DINO、FVD
- 物理常识：VideoPhy、PhyGenBench、VBench-2.0、WorldModelBench、Physics-IQ、WorldScore、EWMBench
- 动作 plausibility：WorldSimBench、IDM Turing Test

**动作策略能力**：
- 通用操作：Meta-World、RLBench、ManiSkill、LIBERO、RoboCasa、GemBench、CALVIN
- 双臂/人形：RoboTwin、BiGym、HumanoidBench、HumanoidGen
- 移动操作：ManipulaTHOR、HomeRobot、BEHAVIOR-1K
- 接触/变形：SoftGym、PlasticineLab、DaXBench、TacSL、ManiFeel
- 真实设备：RoboArena、RoboChallenge、Maniparena

### 六大开放挑战

1. **Architectural Coupling**：匹配规模/数据/协议下的系统比较仍缺失
2. **Multimodal Physical State**：仅RGB预测遗漏触觉/力/声/变形线索
3. **Data Utilization and Mixture Design**：机器人数据/仿真/第一人称视频的边际作用理解不足
4. **Long-Horizon Planning**：分布漂移、动作误差累积、时序抽象弱
5. **Inference Latency and Efficiency**：扩散和自回归预测对闭环设置仍太慢
6. **Evaluation and Safe Deployment**：缺乏 imagined futures 与 executed actions 之间的因果一致性联合指标

---

## 论文库（64篇）

论文库收录于 GitHub：https://github.com/OpenMOSS/Awesome-WAM

代表性工作（部分）：
- **MotuBrain** (2026) — Joint WAM / Diffusion-based，Multi DiT + Cross Attention
- **X-WAM** (2026) — Unified 4D World Action Modeling，Unified DiT
- **MWM** (2026) — Mask World Model，Cascaded，Implicit
- **pi0.7** (2026) — Cascaded WAM，Explicit + Learned
- **DreamZero** (2026) — Joint WAM，DiT，World Action Models are Zero-shot Policies
- **Veo-Act** (2026) — How Far Can Frontier Video Models Advance Generalizable Robot Manipulation?

---

## 印象

这是**首个系统性 WAM 综述**，将 VLA 和 World Model 的融合脉络梳理得非常清楚——核心贡献是把"世界预测必须成为策略的一部分"作为 WAM 的定义边界，区分了 Cascaded 和 Joint 两大架构路线。论文库目前收录64篇工作，梳理了从2026年以来的爆发式增长。

对于理解具身智能的当前状态和未来走向，这是很好的入口材料。