---
title: "Learning to Model the World: A Survey of World Models in Artificial Intelligence"
title_zh: "学会建模世界：人工智能世界模型综述"
source: "https://www.preprints.org/manuscript/10.20944/preprints202603.0739.v1"
author: "Jiahua Dong, Qi Lyu, Baichen Liu, Xudong Wang, Wenqi Liang, Duzhen Zhang, Jiahang Tu, Hongliu Li, Hanbin Zhao, Henghui Ding, Yulun Zhang, Zhi Han, Nicu Sebe, Fahad Shahbaz Khan, Salman Khan, Mubarak Shah, Philip Torr, Ming-Hsuan Yang, Dacheng Tao"
published: 2026-03-10
created: 2026-04-18
tags:
  - "世界模型"
  - "人工智能"
  - "综述"
  - "世界模型"
  - "World Models"
  - "clippings"
keywords:
  - "world models"
  - "simulation"
  - "planning"
  - "decision-making"
  - "general-purpose intelligent systems"
language: en-zh
---

# 学会建模世界：人工智能世界模型综述

> **本文来源**：系统综述人工智能领域中世界模型（World Models）的最新进展。根据建模机制将世界模型分为四大范式：观测级生成模型、潜空间模型、强化学习模型和以对象为中心模型。涵盖机器人在操作/导航/策略学习/运动控制、自动驾驶、科学发现、虚拟游戏模拟、GUI代理，以及可解释性与可信性等广泛应用领域。提供基准数据集、仿真平台与评估指标的全面梳理，并讨论长期一致性、泛化性和因果推理等核心挑战与未来方向。

---

## Abstract · 摘要

World models (WMs) provide a unified approach for modeling how environments evolve over time by learning predictive representations of states and observations. Recent advances in large-scale generative modeling and multimodal foundation models have substantially broadened their applicability across a wide range of interactive and multimodal domains; however, existing research remains fragmented across modeling paradigms, application domains, and evaluation protocols.

世界模型（WMs）提供了一种统一方法，通过学习状态和观测的预测表征来建模环境随时间的演变方式。大规模生成式建模和多模态基础模型的最新进展显著拓宽了它们在广泛的交互和多模态领域的适用性；然而，现有研究在建模范式、应用领域和评估协议方面仍呈碎片化。

This survey provides a systematic and in-depth review of WMs in artificial intelligence. Based on the world modeling paradigms of existing methods, we first categorize WMs into four branches with formal mathematical formulations: observation-level generative, latent space, reinforcement learning-based, and object-centric WMs.

本综述对人工智能中的世界模型提供了系统而深入的综述。基于现有方法的世界建模范式，我们首先将世界模型分为四个分支，并给出正式数学公式：观测级生成、潜空间、强化学习驱动和以对象为中心的世界模型。

We further review a broad range of WM applications spanning robotics, autonomous driving, scientific discovery, game simulation, GUI-based agents, as well as interpretability and trustworthiness, and analyze benchmarks, new evaluation metrics, simulation platforms, and comparative results across WMs.

我们进一步综述了广泛的世界模型应用，涵盖机器人、自动驾驶、科学发现、游戏模拟、基于GUI的代理，以及可解释性和可信性，并分析了基准数据集、新评估指标、仿真平台以及各世界模型间的比较结果。

Finally, we discuss key challenges, including long-horizon consistency, and generalization, and outline promising directions for future research.

最后，我们讨论了关键挑战，包括长期一致性和泛化性，并概述了未来研究的有前景方向。

This survey provides an actively updated GitHub Repository to track developments in WMs and aims to offer a unified reference for understanding, comparing, and advancing WMs.

本综述提供了一个持续更新的GitHub仓库以追踪世界模型的发展，旨在为理解、比较和推进世界模型提供统一参考。

---

## 1. INTRODUCTION · 引言

World models (WMs) have emerged as a fundamental mechanism for building intelligent systems capable of simulation, planning, and decision-making in complex environments. Instead of reacting solely to instantaneous observations, a world model seeks to learn internal representations of the environment that capture its underlying structure, temporal dynamics, and uncertainty. Such an internal model can predict future states, simulate alternative outcomes, and evaluate candidate actions without requiring direct interaction with the real world, which is particularly important in scenarios where data collection is expensive, limited, or safety-critical.

世界模型（WMs）已成为构建智能系统的基本机制，这些系统能够在复杂环境中进行模拟、规划和决策。世界模型不是仅对瞬时观测做出反应，而是寻求学习环境的内部表征，捕获其底层结构、时间动态和不确定性。这种内部模型可以预测未来状态、模拟替代结果，并在不需要与真实世界直接交互的情况下评估候选动作，这在数据收集昂贵、有限或安全关键的场景中尤为重要。

Meanwhile, the limitations of purely model-free methods, including low sample efficiency and poor generalization, have further motivated renewed interest in WMs. Thus, WMs are increasingly viewed as general-purpose intelligent systems that bridge perception, cognition, and control.

同时，纯模型无关方法的局限性（包括低样本效率和差泛化性）进一步激发了对世界模型 renewed 的兴趣。因此，世界模型正日益被视为连接感知、认知和控制的通用智能系统。

The development of WMs has progressed through several stages, driven by advances in representation learning, dynamics modeling, and large-scale training. Early classical model-based approaches, such as Gaussian processes and control-oriented dynamics, rely on explicit or low-dimensional dynamics with strong assumptions about environment structure, which limits their scalability to complex real-world scenarios.

世界模型的发展经历了几个阶段，由表征学习、动力学建模和大规模训练的进步驱动。早期经典基于模型的方法（如高斯过程和控制导向动力学）依赖于对环境结构有强假设的显式或低维动力学，这限制了其向复杂真实场景的可扩展性。

Recent advances in deep learning, especially in large-scale generative modeling such as video prediction and multimodal foundation models, have significantly accelerated research on WMs. Modern WMs increasingly adopt latent representations to model high-dimensional observations, enabling a clearer separation between perception and dynamics prediction. Meanwhile, transformer frameworks and slot encoding are employed to learn interpretable object-centric embeddings, enabling WMs to model latent dynamics through interacting entities.

深度学习（尤其是视频预测和多模态基础模型等大规模生成式建模）的最新进展显著加速了世界模型研究。现代世界模型越来越多地采用潜表征来建模高维观测，使感知与动力学预测之间实现更清晰的分离。同时，Transformer框架和槽编码被用于学习可解释的以对象为中心的嵌入，使世界模型能够通过交互实体建模潜动态。这一转变为神经世界模型奠定了基础，并拓宽了其在视觉和连续控制领域的适用性。

Based on their modeling mechanisms and intended usage, most existing WMs can be mainly categorized into four categories:

基于其建模机制和预期用途，现有世界模型主要可分为四类：

1. **Observation-level generative WMs** directly predict future visual, language, 3D or 4D observations from past environmental observations and actions in high-dimensional spaces, typically using autoregressive, NeRF or diffusion-based generative architectures.

   **观测级生成世界模型** 在高维空间中直接从过去的环境观测和动作预测未来视觉、语言、3D或4D观测，通常使用自回归、NeRF或基于扩散的生成架构。

2. **Latent embedding-based WMs** first encode high-dimensional observations into compact latent representations. They then learn transition dynamics in the latent space, allowing efficient prediction and decision-making without operating on raw observations.

   **潜嵌入世界模型** 首先将高维观测编码为紧凑的潜表征。然后在潜空间中学习转换动态，实现高效预测和决策，而无需操作原始观测。

3. **Reinforcement learning (RL)-based WMs** learn a predictive model of environment dynamics from agent-environment interactions. This learned model then performs planning or policy optimization through imagined rollouts, reducing the need for direct real-world interaction.

   **强化学习（RL）驱动的世界模型** 从智能体-环境交互中学习环境动力学的预测模型。然后这个学到的模型通过想象 rollout 执行规划或策略优化，减少对直接真实世界交互的需求。

4. **Object-centric WMs** represent the environment as a collection of discrete objects with structured attributes. They learn object-level dynamics and relational dependencies, enabling compositional reasoning and generalization across scenes and tasks.

   **以对象为中心的世界模型** 将环境表示为具有结构化属性的离散对象集合。它们学习对象级动力学和关系依赖，实现跨场景和任务的组合推理与泛化。

Over the past few years, WMs have played an increasingly important role across a broad range of application domains, including robotics, autonomous driving, virtual game simulation, GUI-based agents, and scientific discovery. For example, in robotics and autonomous driving, they are used to simulate future scenarios, predict the behavior of surrounding agents or physical systems, and support risk-aware planning and decision-making, thereby improving robustness in uncertain environments.

在过去的几年中，世界模型在广泛的应用领域中发挥了越来越重要的作用，包括机器人、自动驾驶、虚拟游戏模拟、基于GUI的代理和科学发现。例如，在机器人和自动驾驶中，它们被用于模拟未来场景、预测周围智能体或物理系统的行为，并支持风险感知规划和决策，从而在不确定环境中提高鲁棒性。

Beyond control-oriented applications, WMs also excel at modeling physical, biological, and medical treatment domains, accelerating scientific discovery through simulation and hypothesis testing. Evidently, they not only advance the development of intelligent systems, but also contribute to broader societal benefits, including safer transportation, more capable robots, and faster scientific innovation.

在控制导向应用之外，世界模型在物理、生物和医疗领域也表现出色，通过模拟和假设检验加速科学发现。显然，它们不仅推动了智能系统的发展，还为更广泛的社会福利做出贡献，包括更安全的交通、更能干的机器人和更快的科学创新。

**本文贡献：** 本综述与以往工作不同，做出以下主要贡献：

- **深度系统分析**：深入系统地综述世界建模范式、方法论、关键功能及其相互关系，而非聚焦于特定应用或概念性讨论。

- **数学形式化**：从更广视角总结现有主要世界模型的关键演进发展及其跨分支的核心数学公式。

- **全面应用覆盖**：不仅限于常研究的应用领域，全面综述至今已探索的世界模型所有应用领域：机器人、自动驾驶、科学发现、虚拟游戏模拟、基于GUI的代理，以及可解释性和可信性。

- **基准与评估**：提供基准数据集、评估指标、仿真平台和各世界模型比较实验的更全面综述。

**本文结构：** 综述整体结构如下：第2节介绍世界模型的四大主要范式：观测级生成世界模型、潜空间世界模型、RL驱动世界模型和以对象为中心世界模型。第3节综述世界模型的应用领域：机器人、自动驾驶、科学发现、虚拟游戏模拟、基于GUI的代理，以及可解释性和可信性。第4节总结基准数据集与评估指标、仿真平台和性能比较。第5节讨论限制世界模型部署和泛化的关键挑战，并概述强调统一科学建模、因果推理、可扩展训练和真实世界验证的未来方向。

---

## 2. FOUNDATIONAL WORLD MODELS · 基础世界模型

世界模型旨在学习捕获世界当前状态并预测其随时间演变的环境潜动力学，支持模拟、规划和决策。一般而言，在时刻 t，世界模型可视为利用历史状态以及可选的智能体动作来预测未来环境状态的函数：

zt+1 ~ η(zt, at, ot+1)

其中 η 表示世界模型，zt 和 zt+1 分别是 t 和 t+1 时刻的潜环境状态，at 表示 t 时刻的可选智能体动作，ot+1 表示 t+1 时刻的观测。

在世界模型中，**模拟**使用学到的动力学生成一组想象未来轨迹；**规划**在这些模拟的未来轨迹上进行评估或优化，以识别理想轨迹并获得其动作序列 {at}T t=1；**决策**基于规划结果选择并执行最终动作 aT。

### 2.1 Observation-Level Generative World Models · 观测级生成世界模型

观测级生成世界模型利用强生成先验，基于动作及其他输入（如语言提示、视觉图像或相机轨迹）来建模环境动力学。它们主要通过直接在观测级生成未来观测来实现忠实模拟。

观测级生成世界模型通常引入解码器，将潜环境状态 zt+1（以智能体动作 at 和额外输入 ct 为条件）映射到未来观测 ôt+1。其目标可正式表述为：

ôt+1 = D(zt+1 ~ η(zt, at, ct))

预测的观测 ôt+1 是 t+1 时刻的未来观测。

当代生成模型（如大语言模型LLM、扩散模型、流匹配模型和高斯splatting）可视为世界模型的早期初级形式。然而，它们不能纳入与底层世界状态交互的智能体动作，而仅依赖额外输入 ct 来实现逼真的观测级生成：

ôt+1 = D(zt+1 ~ η(zt, ct))

这些常用生成模型无法捕获环境的因果动力学，导致长期模拟稳定性差、可控性有限。目前，从上式到理想观测级生成世界模型仍有相当差距。

#### 2.1.1 Language Observations · 语言观测

语言观测支持抽象转换建模，但在错误累积时可能遭受脆弱的长期 rollout。RAP利用LLM通过将推理框架为在世界模型内的规划来改进决策，通过搜索中间结果而非依赖单一前向传递。可靠性可通过注入显式结构（先决条件和效果知识，以及用于干预的因果抽象）进一步改善。上下文缩放仍然是核心，长上下文架构将建模扩展到百万长度视频和语言序列。总体而言，整合长语言建模、结构和规划对于鲁棒可扩展的语言级世界模型至关重要。

#### 2.1.2 Visual Observations · 视觉观测

视频生成器学习可似然未来的视觉观测，并作为世界建模的强大初始化。Emu3通过用下一token预测目标训练统一多模态Transformer，展示高生成保真度和时间一致性。近期基础视频模型展示强视觉保真度和一致性，使其成为可控仿真器的天然先验。Wan采用LLaVA风格架构通过低秩机制增强视觉理解。为实现更好规划和控制，近期工作将视频生成模型适配为交互式仿真器，通过注入动作和强制状态持续性。物理感知引导减少不可似然动力学，显式记忆在变化视角下改善长期一致性。总体而言，视觉逼真是核心目标，物理和运动驱动机制的结合将在未来构建可控世界模型中发挥重要作用。

#### 2.1.3 3D and 4D Observations · 3D和4D观测

视觉观测提供强外观保真度，而3D和4D观测在不同视角变化中展现稳定、几何接地状态。Text2Room采用多视图图像迭代融合从文本提示直接生成高质量网格。4D-fy将这一能力扩展到时间维度，交替整合来自3D感知模型以及文生图和文生视频模型的监督信号。WonderWorld在保持视觉质量和几何一致性同时实现交互式3D世界的高效生成。Invisible Stitch通过引入深度修复解决由单目深度估计引起的3D场景生成中的几何不一致问题。总体而言，3D和4D世界模型可构建高保真和交互式世界，但仍需改进效率和物理一致性。

### 2.2 Latent-Space World Models · 潜空间世界模型

与观测级生成世界模型不同，潜空间世界模型使用高维潜表征来建模环境动力学，使其能更好地捕获底层语义结构和运动，从而主要支持模拟和规划。

基于自监督基础框架JEPA和V-JEPA，V-JEPA 2扩展这些方法构建潜空间世界模型。具体而言，V-JEPA 2引入潜空间预测器来预测 t+1 时刻的未来潜表征 ẑt+1，然后将 ẑt+1 与对应的真实表征 zt+1 的差异最小化。

V-JEPA 2将训练扩展到超过百万小时视频并引入动作条件化，seq-JEPA解纠缠等变和不变量特征以提高表征区分度，MC-JEPA通过联合训练光流估计进一步增强运动建模。另一显著趋势利用预训练视觉基础模型。DINO-WM、DINO-World和DINO-Foresight使用预训练DINO模型将空间patch特征作为环境状态，实现有效零样本规划和通过掩码Transformer预测演化语义特征。

### 2.3 Reinforcement Learning-Based World Models · 强化学习驱动的世界模型

RL驱动的世界模型使用学到的动力学来促进规划和策略决策。基于方程，引入奖励模型来预测 t 时刻的奖励 rt ~ R(zt, at)。其目标是最大化T个时间步的累积奖励。

RL驱动世界模型的主导潜动力学骨干是递归状态空间模型（RSSM）。RSSM结合确定性递归状态与潜变量来捕获不确定性。在此激励下，Dreamer引入潜想象作为昂贵环境交互的替代方案，通过想象 rollout 学习策略。DreamerV2展示离散潜变量稳定学习并扩展到基于像素的Atari控制，而DreamerV3强调使用单一配置跨多样化领域的鲁棒性。

模型基 rollout 实现更好规划和决策能力，但分布偏移和鲁棒性在闭环设置中仍具挑战性。近期RL驱动世界模型通过紧固模型-策略环（通过协作或策略条件化建模）以及稳定价值估计和规划的目标来解决这些限制。然而，这些模型仍依赖独立奖励模型。一些方法在无奖励条件下训练鲁棒世界模型。此外，基于token的世界模型将环境观测转换为类似语言的离散token序列，并利用序列模型在潜空间中预测环境动力学。

### 2.4 Object-Centric World Models · 以对象为中心的世界模型

为解决对象跟踪和可解释动力学的局限性，以对象为中心的世界模型使用槽注意力将结构化场景表示为可组合实体（对象槽）集合，并建模具有更好可解释性和组合泛化的对象级动力学。

灵感来自槽注意力，以对象为中心的世界模型专注于最小化未来时间步预测对象槽与对应真实值之间的差异：

ĥt+1 ~ P(ĥt, at)
min L = E[D(ĥt+1, A(ot+1))]

其中 A(·) 表示将观测映射到一组槽的槽注意力函数。A(ot) 和 A(ot+1) 分别表示 t 和 t+1 时刻的槽集合。

SlotFormer将顺序观测编码为对象级表征并通过学习视觉动力学预测未来对象状态。为改进槽质量和可控性，Dyn-O为Procgen风格游戏引入基于槽的世界模型，注入分割先验并解纠缠静态和动态因素。相关工作构建以对象为中心的动力学以支持高效探索、多步规划和改进策略学习。

### 2.5 Discussion of Expected World Models · 期望世界模型的讨论

虽然现有基础世界模型已取得令人瞩目的进展，但距离设想中的未来世界模型仍有相当距离——在知识如何表征、更新和验证方面。当前世界模型主要从观测数据优化预测准确性，而不强制因果、机械或可证伪结构。

未来世界模型以符号形式编码知识（如方程和形式关系），独立于特定数据集或观察者。知识通过扩展共享理论累积更新，而非通过不透明、纠缠的参数变化。这样的知识可被社会验证：方程和证明可被检查，预测可通过可重复实验测试。这些模型有明确的适用域，失败源于支配定律（如相对论速度下的经典力学或湍流状态下的Navier-Stokes方程）的有原则崩溃，而非不可预测的外推误差。

相比之下，当前世界模型往往不透明地失败，主要作为复杂插值器而非显式、理论接地模型。弥合这一差距可能需要整合符号和神经组件、强制硬物理约束，以及设计奖励因果发现和可证伪性而非单纯重建的协议。

---

## 3. APPLICATIONS OF WORLD MODELS · 世界模型的应用

### 3.1 World Models for Robotics · 机器人世界模型

AI for robotics requires robots to operate under partial observability and rich physical interaction. This field has been significantly advanced by embodied foundational world models, which scale world modeling through large multimodal data and unified model interfaces, aiming to integrate perception, prediction, and action into a transferable backbone.

用于机器人的AI要求机器人在部分可观测性和丰富物理交互下运行。该领域已被具身基础世界模型显著推进，这些模型通过大规模多模态数据和统一模型接口扩展世界建模，旨在将感知、预测和动作整合到可迁移的主干中。

我们从控制-感知环视角综述机器人操作、从导航-推理环视角综述导航，而非仅聚焦于视觉语言感知。

#### 3.1.1 Manipulation · 操作

机器人操作对世界模型提出严格要求，因为涉及接触丰富的动力学和不连续状态转换（如抓取或释放）。我们从控制环中世界模型的使用方式和预测目标对操作世界模型分类：

- **Latent Action State Imagination**（潜动作状态想象）：在训练期间将世界模型用作紧凑仿真器生成 rollout 以改进策略。样本高效但可能在长 rollout 中累积偏差。代表：Dreamer、AdaWorld、FLARE。

- **Control-Oriented Planning**（控制导向规划）：在推理时将世界模型用作滚动仿真器进行MPC或推理时搜索。计算密集型，依赖精确短期预测。代表：TD-MPC、PIVOT-R。

- **World Action Modeling**（世界动作建模）：通过token化多模态流和自回归或扩散目标统一感知、世界演化和动作生成。代表：Genie Envisioner、WoW。

- **Visual Future Prediction**（视觉未来预测）：学习未来观测的动作条件预测器，并利用视觉 rollout 进行规划和监督。代表：TesserAct、FlowDreamer。

#### 3.1.2 Navigation · 导航

机器人导航对世界模型提出独特挑战，主要要求长距离空间一致性和在动态环境中的鲁棒操作。我们从导航-推理环视角将导航世界模型分为五类：

- **Generative Imagination Navigation**（生成想象导航）：显式模拟未来观测以支持导航规划。代表：NWM、UniWM、MindJourney。

- **Persistent Memory Representation**（持久记忆表征）：维护演化内部状态以解决部分可观测性。代表：RECON、Nav-Morph。

- **Neuro-Symbolic Modeling**（神经符号建模）：用语言或符号约束扩展动力学建模。代表：WMNav、NaVi-WM。

- **Test-Time Adaptation**（测试时适应）：处理不完美先验和新环境。代表：Scale-Infer。

- **Belief-Guided Modeling**（信念引导建模）：将世界模型视为决策充分信念抽象。代表：X-Mobility、Abs-Sim2Real。

#### 3.1.3 Policy Learning · 策略学习

世界模型作为想象引擎、无动作模型和评估代理用于机器人策略学习，使策略能够通过想象交互而非昂贵的真实世界试错来优化。

- **Imagination-Based Optimization**：将世界模型用作优化基质，在想象中直接学习机器人策略。代表：WMPO、World4RL。

- **Action-Free Modeling**：通过世界模型从无标签或弱标签观测序列学习控制策略，无需昂贵显式动作监督。代表：LAWM、PreLAR。

- **Evaluation Proxy**：将世界模型明确作为评估代理仿真器用于策略训练、比较和评估，无需昂贵真实世界 rollout。代表：Ctrl-World、WorldEval。

#### 3.1.4 Locomotion · 运动控制

世界模型最近展示了学习鲁棒运动行为的强潜力，通过显式捕获接触丰富动力学、地形几何和宽范围物理一致性。它们作为结构化预测器重建或预测运动相关状态转换，在复杂约束下实现策略优化。

代表工作包括：WMP学习预测视觉世界模型以为腿控感知接地，显著提高不平坦和部分可观测地形上的鲁棒性；WMR引入重构世界模型，通过强制物理一致潜动力学正则化策略学习，在严重分布偏移下实现稳定人形运动。

### 3.2 World Models for Autonomous Driving · 自动驾驶世界模型

世界模型通过建模交通动力学和智能体交互促进自动驾驶系统，使车辆能够在不确定环境中预测未来场景并相应规划动作。

我们从世界模型在决策环中的参与程度的新视角重新分析该领域：

- **Predictive Modeling**（预测建模）：将世界模型作为环境预测器，从过去观测预测未来世界状态，不以自车动作或控制命令为条件。代表：Copilot4D、UNO、UniWorld。

- **Action-Conditioned Imagination**（动作条件想象）：通过以自车动作、轨迹或高层命令为条件来扩展未来世界演变，支持反事实推理。代表：GAIA-1、Drive-WM。

- **Decision-Centric Integration**（决策中心集成）：将世界模型嵌入决策环，使用想象 rollout 评估动作、引导规划或更新策略。代表：Think2Drive、DriveVLA、AdaWM。

### 3.3 World Models for Science · 科学世界模型

科学世界模型将焦点从交互中心模拟转向复杂部分可观测系统的数据驱动科学建模。

- **Social and Socioeconomic Systems**（社会和经济社会系统）：将社会系统形式化为可学习的集体动力学和智能体交互模型。代表：SocioVerse、SWM-AP。

- **Physical and Natural Sciences**（物理和自然科学）：将世界模型作为数据驱动、物理约束的仿真器，建模自然科学中的系统。CellFlux通过流匹配实现细胞动力学的连续时间模拟；ODesign将生物分子相互作用设计框架为世界建模用于生成分子探索。在医疗中，支持肿瘤演变建模、射线照片世界模型和手术过程建模。

### 3.4 World Models for Virtual Game Simulation · 虚拟游戏模拟世界模型

虚拟游戏模拟是世界模型自然且历史重要的应用，因为游戏提供完全可观测和交互式环境。

- **2D Pixel-Level Observation Prediction**（2D像素级观测预测）：大多数现有游戏世界模型专注于在像素级直接预测未来观测。代表：DIAMOND（Atari）、GameNGen（实时交互游戏）、Oasis（序列宇宙建模）。

- **3D Mesh-Level Observation Prediction**（3D网格级观测预测）：越来越多兴趣于在显式3D几何表征（如网格）上操作的世界模型。HyuanWorld 1.0从文本或图像生成可探索交互式3D世界；Matrix-3D实现全向可探索3D世界生成与全局一致空间结构。

### 3.5 World Models for GUI-Based Agents · 基于GUI代理的世界模型

世界模型显著增强基于图形用户界面（GUI）代理，通过启用界面动力学的预测模拟，使代理能够规划、评估替代方案并在执行前评估动作。

- **Web Agents**（Web代理）：Web导航因大状态空间和延迟奖励带来独特挑战。WebDreamer利用LLM作为隐式Web世界模型，通过模拟 rollout 展示基于模型的规划。代表：WebDreamer、WebEvolver、WALL-E 2.0。

- **Operating Systems & Desktop Agents**（操作系统和桌面代理）：为智能体配备操作系统或桌面应用程序的内部仿真器。NeuralOS建模OS级动力学用于预执行预测规划；ViMo为移动和桌面应用程序构建生成视觉世界模型。

### 3.6 Interpretable and Trustworthy World Models · 可解释可信世界模型

除经验成功外，近期研究审查世界模型的理论基础，聚焦于其涌现因果结构和关键任务中的安全保证。

- **Interpretability**（可解释性）：一些理论研究提示内部世界模型对泛化到长期目标（超越归纳偏差）是必要的。尽管Transformer可以学习与因果结构对齐的表征，但高预测准确性不保证真正的内部模拟，因为模型可能依赖在干预下失效的捷径相关性。

- **Self-Evolutionary Learning**（自演化学习）：为发展真正的内部模拟，需要大量环境交互。由于真实世界数据收集成本极高，近期工作采用自演化学习，引入自验证、自奖励和自博弈等内部机制。这些机制使世界模型在无外部监督的环境中保持稳定持续优化。

- **Safety-Oriented Trustworthiness**（安全导向可信性）：尽管缩放定律表明增加容量改善表征稳定性，但不能确保对分布偏移或对抗扰动的鲁棒性，也不能克服部分可观测设置中的理论限制。

### 3.7 Limitations of WMs in Downstream Applications · 世界模型在下游应用中的局限性

尽管世界模型在下游应用中取得有前景的收益，但仍存在显著挑战。首先，世界模型的训练目标主要聚焦于重建或生成等表征指标，而下游应用强调决策质量和策略学习有效性。其次，现有世界模型普遍缺乏对因果结构的显式建模，增加了闭环交互和长期推理中错误累积和预测偏移的敏感性。此外，世界模型受推理和规划的计算和延迟成本约束，阻碍了直接在机器人或车载系统等边缘设备上部署。

---

## 4. BENCHMARK OF WORLD MODELS · 世界模型基准

### 4.1 Benchmark Datasets & Evaluation Metrics · 基准数据集与评估指标

#### 4.1.1 Pretrained Video Benchmarks · 预训练视频基准

- **WebVid-10M**: 10M网络视频-字幕对，用于文本-视频预训练。核心指标：Recall@K, MedR。
- **Panda-70M**: 自动为70M视频片段生成字幕。核心指标：Recall@K, FVD, CLIPSim。
- **Ego4D**: 添加长程自我中心视频与丰富注释。核心指标：Recall@K, mAP, Accuracy。
- **WorldScore**: 使用多步下一场景协议评估仿真，报告可控性、质量和动力学聚合及分解指标。核心指标：WS-S, WS-D, CCon, OCon。

#### 4.1.2 Benchmarks on Downstream Tasks · 下游任务基准

**机器人**：Open X-Embodiment（跨机器人轨迹）——SR；Room-Across-Room（导航）——SR, NE, PL；Meta-World（多任务）——SR。

**自动驾驶**：NuScenes——mAP, NDS, AMOTA；ACT Bench——ADE, FDE。

**科学**：JUMP Cell Painting——FID；HCC-TACE-Seg——AP, F1-score, JI, recall。

**游戏模拟**：ALE——MedS, NS；MineRL——Episode return。

**GUI代理**：OSWorld——SR；WindowsAgentArena——SR。

#### 4.1.3 General Metrics for World Models · 世界模型的通用指标

- **Generalization（泛化性）**：测量跨域泛化能力 G = E[f(x)] - E[f(x')]，其中 x 和 x' 分别来自训练和测试分布。

- **Causal Reasoning（因果推理）**：给定干预集合 I，使用反事实干预算子 do(i) 测量因果推理能力 C = Ei~I[D(y, y')]。

- **Long-Horizon Consistency（长期一致性）**：对于多步执行任务，比较真实轨迹与想象轨迹之间的增量偏差，评估现有基础世界模型的长期一致性 H。

### 4.2 Physics Engines & Simulation Platforms · 物理引擎与仿真平台

有效的仿真依赖能够复制真实世界属性的物理引擎。

| 仿真器 | 主焦点 | 典型功能 | 关键特性 | 开源 | 软体 | GPU加速 |
|--------|--------|----------|----------|------|------|--------|
| Bullet | 接触丰富机器人 | 广泛使用、软体模块 | 广泛使用 | Y | Y | P |
| Simbody | 高保真生物力学 | 高精度多体动力学 | 多体建模 | Y | N | N |
| PhysX | 可扩展机器人 | 行业级后端 | FEM模块 | Y | Y | Y |
| Gazebo | 导航、多机器人 | ROS集成 | 系统仿真 | Y | D | D |
| MuJoCo | 控制基准、操作 | 控制导向 | MJX加速 | Y | L | P |
| Isaac Gym | 大规模并行rollout | 张量API | GPU闭环 | N | L | Y |
| Genesis | 具身AI训练 | 多后端 | 高吞吐量 | Y | P | Y |

### 4.3 Performance Comparison · 性能比较

在WorldScore基准上的比较显示，TeleWorld实现最强和最均衡的性能，在WS-S、WS-D、3D一致性、光度一致性、语义一致性和主观质量等关键指标上领先，表明优越视觉保真度和时间一致性。

3D方法（如Text2Room、WonderJourney）在可控性相关指标上显著领先，但在运动相关指标上接近零分，凸显动态场景建模的局限性。相比之下，基于视频的模型（如Gen-3、VideoCrafter2）展示更好的运动精度和平滑度，但在细粒度可控性上表现较差。

---

## 5. CHALLENGES & FUTURE DIRECTIONS · 挑战与未来方向

### 5.1 Scientific Modeling · 科学建模

现有方法通常聚焦于拟合观测数据分布以改进视觉保真度、可控性或运动真实性，导致生成视觉似然rollout同时违反物理定律。未来研究应聚焦于不仅提供预测能力而且提供强解释力的科学建模。

在科学建模中，知识通过显式符号形式（如方程和形式关系）表达，独立于特定数据集、实验或观察者。有前景的方向是整合符号和神经组件、强制硬物理约束（如守恒定律），以及开发奖励因果发现和可证伪性而非单纯重建的协议。

### 5.2 Long-Horizon Consistency & Causal Reasoning · 长期一致性与因果推理

保持长期时间跨度上的一致性仍然是世界模型的主要障碍。预测误差累积导致视觉漂移、破坏物理交互或不真实未来状态。许多世界模型依赖相关模式而非因果理解，限制其在闭环或多步rollout中的可靠性。

未来在分层时间建模和因果表征学习方面的进展可能改善长期稳定性。纳入状态抽象、记忆和因果干预的显式机制可能使世界模型能够推理超越短期相关性。

### 5.3 Grounding in Physical and Semantic Constraints · 物理和语义约束的接地

尽管视觉合成令人印象深刻，许多世界模型缺乏物理定律和语义结构的接地，导致不可似然运动、不一致对象交互和语义不一致的场景演变。

未来研究方向包括整合物理感知先验、可微分仿真器或符号知识，以及将神经表征与结构化语义图或以对象为中心模型结合以改进物理似然性和可解释性。

### 5.4 Generalization & Scalability in Real-World · 真实世界的泛化与可扩展性

大多数当前世界模型在窄域内训练和评估，引发对其跨环境、任务和具体形态泛化的担忧。此外，训练大规模世界模型的高计算和数据需求阻碍了可扩展性和真实世界部署。

未来研究可能探索在多样化多模态交互数据上训练的基础世界模型，实现广泛泛化。此外，数据高效学习、参数高效微调和持续学习策略可能对可扩展性至关重要。

---

## 6. CONCLUSIONS · 结论

This survey presents a systematic review of WMs in artificial intelligence. We introduce a unified definition and categorize existing methods into four paradigms: observation-level generative, latent-space, RL-based, and object-centric WMs, and review their applications across robotics, autonomous driving, scientific discovery, virtual game simulation, GUI-based agents, as well as interpretability and trustworthiness.

本综述对人工智能中的世界模型提供了系统综述。我们引入统一定义并将现有方法分为四类范式：观测级生成、潜空间、RL驱动和以对象为中心的世界模型，并综述了它们在机器人、自动驾驶、科学发现、虚拟游戏模拟、基于GUI的代理以及可解释性和可信性方面的应用。

We also summarize benchmark datasets, evaluation metrics, simulation platforms, and comparative results. Moreover, we identify key challenges limiting the deployment and generalization of WMs, including scientific modeling, long-horizon consistency, controllability, robustness, evaluation limitations, and transfer across tasks and embodiments.

我们还总结了基准数据集、评估指标、仿真平台和比较结果。此外，我们确定了限制世界模型部署和泛化的关键挑战，包括科学建模、长期一致性、可控性鲁棒性、评估局限性和跨任务及具体形态的迁移。

We have also discussed potential directions that emphasize integrated modeling, scalable training, principled benchmarking, and real-world validation. This survey serves as a foundation for advancing more generalizable and trustworthy WMs.

我们还讨论了强调集成建模、可扩展训练、有原则基准测试和真实世界验证的潜在方向。本综述为推进更具泛化性和可信性的世界模型奠定了基础。

Looking ahead, WMs should move beyond scaling predictive accuracy toward establishing physical consistency and explanatory structure, with internal representations examinable against physical laws and invariances. Rather than manually encoding physical laws, WMs are trained on large-scale data to autonomously learn representations and predictive capabilities of the physical world through self-evolutionary learning. Advancing toward this goal requires tighter integration of learning, dynamics, and causality, shifting world modeling from large-scale statistical interpolation toward a scientific modeling framework.

展望未来，世界模型应超越扩展预测准确性，转向建立物理一致性和解释结构，使内部表征可根据物理定律和不变性进行检查。世界模型不是手动编码物理定律，而是在大规模数据上训练，通过自演化学习自主学习物理世界的表征和预测能力。推进这一目标需要学习、动力学和因果性的更紧密整合，将世界建模从大规模统计插值转向科学建模框架。

---

*本文参考来源：*
*[1] Jiahua Dong et al., "Learning to Model the World: A Survey of World Models in Artificial Intelligence," Preprints.org, 2026.*
*[其余参考文献见原文，共117条，详见 https://www.preprints.org/manuscript/10.20944/preprints202603.0739.v1]*
