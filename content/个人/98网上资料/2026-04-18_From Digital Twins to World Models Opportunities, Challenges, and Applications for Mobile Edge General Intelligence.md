---
title: "From Digital Twins to World Models: Opportunities, Challenges, and Applications for Mobile Edge General Intelligence"
title_zh: "从数字孪生到世界模型：移动边缘通用智能的机遇、挑战与应用"
source: "https://notebooklm.google.com/notebook/8b1ac415-d16a-444e-a50a-ca6099d73923"
author: "Jie Zheng, Dusit Niyato, Changyuan Zhao, Jiawen Kang, Jiacheng Wang"
created: 2026-04-18
tags:
  - "数字孪生"
  - "世界模型"
  - "边缘智能"
  - "EGI"
  - "6G"
  - "clippings"
language: en-zh
---

# 从数字孪生到世界模型：移动边缘通用智能的机遇、挑战与应用

> **本文来源**：系统综述数字孪生向世界模型演进的历程，探讨其在边缘通用智能（EGI）中的核心作用。对比两种范式的根本差异——数字孪生侧重高保真还原与离线分析，世界模型侧重数据驱动抽象与潜空间想象。涵盖 ISCC、语义通信、空地网络、低空无线网络四大应用场景，并提供开放资源与未来研究方向。

---

## Abstract · 摘要

The rapid evolution toward 6G and beyond communication systems is accelerating the convergence of digital twins and world models at the network edge. Traditional digital twins provide high-fidelity representations of physical systems and support monitoring, analysis, and offline optimization. However, in highly dynamic edge environments, they face limitations in autonomy, adaptability, and scalability.

向6G及下一代通信系统的快速演进正在加速数字孪生与世界模型在网络边缘的融合。传统数字孪生提供物理系统的高保真表征，并支持监控、分析和离线优化。然而，在高度动态的边缘环境中，它们面临自主性、适应性和可扩展性方面的局限。

This paper presents a systematic survey of the transition from digital twins to world models and discusses its role in enabling edge general intelligence (EGI). First, the paper clarifies the conceptual differences between digital twins and world models and highlights the shift from physics-based, centralized, and system-centric replicas to data-driven, decentralized, and agent-centric internal models.

本文系统性地综述了从数字孪生向世界模型过渡的历程，并探讨了其在实现边缘通用智能（EGI）中的作用。首先，本文阐明了数字孪生与世界模型之间的概念差异，并强调了从基于物理的、集中式的、以系统为中心的副本，向数据驱动的、去中心化的、以代理为中心的内部模型的转变。

This discussion helps readers gain a clear understanding of how this transition enables more adaptive, autonomous, and resource-efficient intelligence at the network edge.

这一讨论帮助读者清晰理解这一转变如何使网络边缘的智能变得更加自适应、自主且资源高效。

The paper reviews the design principles, architectures, and key components of world models, including perception, latent state representation, dynamics learning, imagination-based planning, and memory.

本文综述了世界模型的设计原则、架构和关键组件，包括感知、潜态表征、动力学学习、基于想象的规划与记忆。

In addition, it examines the integration of world models and digital twins in wireless EGI systems and surveys emerging applications in integrated sensing and communications, semantic communication, air–ground networks, and low-altitude wireless networks.

此外，本文还研究了世界模型与数字孪生在无线EGI系统中的集成，并综述了集成感知与通信、语义通信、空对地网络和低空无线网络中的新兴应用。

Finally, this survey provides a systematic roadmap and practical insights for designing world-model-driven edge intelligence systems in wireless and edge computing environments. It also outlines key research challenges and future directions toward scalable, reliable, and interoperable world models for edge-native agentic AI.

最后，本文为无线与边缘计算环境中设计世界模型驱动的边缘智能系统提供了系统性路线图和实践洞察，并概述了面向可扩展、可靠且可互操作的世界模型的关键研究挑战与未来方向，以实现边缘原生代理AI。

---

## I. INTRODUCTION · 引言

### A. Background · 背景

Edge computing is undergoing a paradigm shift from task-specific edge artificial intelligence (Edge AI) to edge general intelligence (EGI) [1]. EGI represents a new class of intelligent systems deployed close to the physical world, capable of long-term autonomous operation on multiple tasks, environments, and time scales.

边缘计算正在经历一场从特定任务边缘人工智能（Edge AI）向边缘通用智能（EGI）的范式转变[1]。EGI代表了一类新型智能系统，部署于接近物理世界的环境中，具备在多种任务、环境和时间尺度上进行长期自主运行的能力。

EGI enables low-latency or even ultra-low-latency inference while reducing system energy consumption and operational costs, making it well suited for resource-constrained devices and diverse vertical applications [2].

EGI能够实现低延迟乃至超低延迟的推理，同时降低系统能耗和运营成本，使其非常适合资源受限设备和多样化的垂直应用[2]。

Traditional Edge AI is generally considered to have emerged from the development needs of interconnected ecosystems. Its primary objective is to enable the execution of local algorithms near data sources or edge servers, thus supporting applications with stringent requirements of low latency and high data efficiency, such as in-vehicle communication for autonomous driving [3].

传统Edge AI通常被认为是互联生态系统发展需求的产物，其主要目标是在数据源或边缘服务器附近执行本地算法，从而支持对低延迟和高数据效率有严格要求的应用，如自动驾驶的车载通信[3]。

Unlike traditional Edge AI, which focuses on predefined inference tasks, EGI agents can autonomously perceive, reason, and act within dynamic and partially observable environments.

与传统Edge AI专注于预定义推理任务不同，EGI代理能够在动态且部分可观测的环境中自主感知、推理和行动。

---

By executing algorithms directly on edge devices, edge intelligence supports localized data processing and reduces reliance on cloud infrastructure. This approach improves latency and enhances privacy and security, as sensitive data remain within the local environment [4].

通过直接在边缘设备上执行算法，边缘智能支持本地化数据处理，减少了对云基础设施的依赖。这种方法改善了延迟并增强了隐私与安全性，因为敏感数据保留在本地环境中[4]。

Key application scenarios include UAV-enabled communication and sensing networks [5], intelligent transportation systems with autonomous vehicles [6], and industrial infrastructures for smart factories and energy grids [7].

关键应用场景包括无人机支持的通信与感知网络[5]、配备自动驾驶汽车的智能交通系统[6]，以及智能工厂和能源电网的工业基础设施[7]。

In these scenarios, EGI is typically required to operate in close coupling with physical systems under resource constraints and in real time to address dynamic environments. This need for a closed loop of perception, decision-making, and action gives rise to clear embodied characteristics, aligning edge intelligence with the core principles of embodied artificial intelligence.

在这些场景中，EGI通常需要在资源约束下实时与物理系统紧密耦合运行，以应对动态环境。这种感知-决策-行动的闭环需求产生了明确的具身特征，使边缘智能与具身人工智能的核心原则相一致。

Embodied intelligence emphasizes autonomous behavior achieved through perception and interaction with the physical world, and relies on physical simulators and world models to support training, environment representation, and predictive planning, thus advancing agents toward higher levels of autonomy [8].

具身智能强调通过与物理世界的感知和交互来实现自主行为，并依赖物理模拟器和世界模型来支持训练、环境表征和预测规划，从而推动代理向更高自主水平迈进[8]。

---

Achieving high levels of autonomy requires capabilities beyond simple reactive inference. Policies based only on instantaneous perception-to-action mappings typically implemented through end-to-end models are often fragile when faced with environmental changes, partial observability, and action delays.

实现高水平的自主性需要超越简单反应式推理的能力。仅基于瞬时感知到动作映射的策略（通常通过端到端模型实现）在面对环境变化、部分可观测性和动作延迟时往往很脆弱。

Thus, EGI systems must incorporate world models, which are internal representations of the external environment [9].

因此，EGI系统必须纳入世界模型，即外部环境的内部表征[9]。

World models are commonly regarded as essential tools for understanding the current state of an environment and predicting its future evolution. By modeling state transitions, reasoning under uncertainty, and simulating and comparing different action sequences, world models support long-term planning and decision evaluation.

世界模型通常被视为理解环境当前状态和预测其未来演变的重要工具。通过建模状态转换、在不确定性下推理以及模拟和比较不同动作序列，世界模型支持长期规划和决策评估。

World models can simulate complex real-world dynamics [10], while edge intelligence without such models often relies on short-term reactive decisions, making it challenging to ensure reliability and generalization in dynamic or unknown environments.

世界模型可以模拟复杂的现实世界动态[10]，而缺乏此类模型的边缘智能通常依赖短期反应式决策，在动态或未知环境中难以保证可靠性和泛化能力。

---

### B. Motivation and Contribution · 动机与贡献

From early conceptual proposals to recent systematic developments, digital twins have become a main paradigm for representing and modeling physical objects in networked cyber–physical systems [11]. Digital twins are typically implemented in software as high-fidelity virtual counterparts of physical systems, supporting contextual modeling, real-time state synchronization, and secure modular interactions through application programming interfaces (APIs).

从早期的概念提案到近年来的系统性发展，数字孪生已成为网络信息物理系统中表示和建模物理对象的主要范式[11]。数字孪生通常以软件形式实现，作为物理系统的高保真虚拟对应物，通过应用程序编程接口（API）支持上下文建模、实时状态同步和安全模块化交互。

Thus, digital twins can facilitate industrial analysis and decision-making tasks [12]. Built on explicit physical laws, domain-specific equations, and expert rules, digital twins provide substantial value for offline engineering analysis and system design.

因此，数字孪生可以促进工业分析和决策任务[12]。建立在明确的物理定律、特定领域方程和专家规则之上，数字孪生为离线工程分析和系统设计提供了巨大价值。

---

In recent years, digital twins have been widely applied in fields such as robotics, healthcare monitoring, and wireless communications.

近年来，数字孪生已广泛应用于机器人、医疗健康监控和无线通信等领域。

For example, RoboTwin integrates three-dimensional generative foundation models with large language models (LLMs) to generate diverse expert data for dual-arm robotic manipulation, leading to significant performance gains [13].

例如，RoboTwin将三维生成式基础模型与大语言模型（LLM）相结合，生成双臂机器人操作的多样化专家数据，取得了显著的性能提升[13]。

Digital-twin-based models for smart home healthcare monitoring support visual monitoring, health state prediction, and intelligent control [14].

基于数字孪生的智能家居健康监控模型支持视觉监控、健康状态预测和智能控制[14]。

In wireless communication and edge computing systems, digital twins are used for network planning, configuration validation, and what-if analysis. They also enable joint optimization of communication and computing under low-latency and energy-constrained conditions while meeting the model accuracy requirements [15].

在无线通信和边缘计算系统中，数字孪生被用于网络规划、配置验证和假想分析。它们还能够在满足模型精度要求的同时，在低延迟和能源约束条件下实现通信与计算的联合优化[15]。

---

However, digital twin technology still faces several challenges, including complex communication and data integration, limited data availability for machine learning training, high computational costs for high-fidelity modeling, strong dependence on interdisciplinary collaboration, and the lack of unified development and validation frameworks [16].

然而，数字孪生技术仍面临若干挑战，包括复杂的通信和数据集成、机器学习训练数据可用性有限、高保真建模的高计算成本、对跨学科协作的强烈依赖，以及缺乏统一的开发和验证框架[16]。

Traditional digital twin paradigms, which are mainly designed for offline system engineering, are fundamentally misaligned with the requirements of online and autonomous EGI.

主要为离线系统工程设计的传统数字孪生范式，与在线和自主EGI的需求存在根本性的不一致。

This mismatch is further amplified in heterogeneous operational technology environments, where infrastructure differences and missing standards hinder large-scale deployment [11].

在异构运营技术环境中，这种不匹配进一步加剧，基础设施差异和标准缺失阻碍了大规模部署[11]。

Moreover, digital twins often rely heavily on predefined rules and prior assumptions, which limits their generalizability.

此外，数字孪生往往严重依赖预定义规则和先验假设，这限制了其泛化能力。

High-fidelity modeling also struggles to meet the real-time constraints of resource-limited edge devices, and the system-centric modeling perspective tends to overlook the agent's perception, decision-making, and action processes.

高保真建模也难以满足资源受限边缘设备的实时约束，而以系统为中心的建模视角往往忽视了代理的感知、决策和行动过程。

As a result, many existing digital twins remain in the static replica stage, lacking dynamic evolution and intelligent decision-making capabilities [17].

因此，许多现有数字孪生仍停留在静态副本阶段，缺乏动态演化和智能决策能力[17]。

---

To complement and enhance the capabilities of digital twins, world models have gradually emerged and been adopted for similar tasks [18]. Their objective shifts from high-fidelity replication of the physical world to capturing environment evolution that is relevant to decision-making.

为补充和增强数字孪生的能力，世界模型已逐渐兴起并被采用来完成类似任务[18]。其目标从对物理世界的高保真复制，转向捕获与决策相关的环境演化。

This reflects a broader transition from world replication to task-relevant abstraction, from rule-driven to data-driven dynamics, and from a system-centric to an agent-centric modeling perspective.

这反映了一场更广泛的转变：从世界复制到任务相关抽象，从规则驱动到数据驱动动力学，从以系统为中心到以代理为中心的建模视角。

---

World models typically use modern representation learning methods, such as variational autoencoders, to compress high-dimensional sensory input into low-dimensional latent states [9]. Action-conditioned state transitions are then learned in the latent space to support imaginative prediction of future environment dynamics.

世界模型通常使用现代表征学习方法（如变分自编码器）将高维感官输入压缩为低维潜态[9]。然后在潜空间中学习动作条件化状态转换，以支持对未来环境动态的想象性预测。

This paradigm aligns well with the core requirements of EGI, including resource efficiency, imagination-based planning, and close integration with reinforcement learning and control algorithms.

这一范式与EGI的核心需求高度吻合，包括资源效率、基于想象的规划，以及与强化学习和控制算法的紧密集成。

Existing studies have explored world model design from multiple perspectives, including multi-scale variation modeling, controllable prediction, structured reasoning, and dynamics modeling [10].

现有研究已从多个角度探索世界模型设计，包括多尺度变化建模、可控预测、结构化推理和动力学建模[10]。

For example, DriveDreamer-2 generates diverse predictions covering long-tail scenarios in autonomous driving [19]. GLAM improves model-based reinforcement learning by jointly modeling global and local state variations [20].

例如，DriveDreamer-2生成涵盖自动驾驶长尾场景的多样化预测[19]。GLAM通过联合建模全局和局部状态变化来改进基于模型的强化学习[20]。

Drive-OccWorld applies a vision-centric 4D world model to end-to-end autonomous driving planning [21]. SWAP uses world-model-driven entailment graphs for structured reasoning [22][23], and MoSim supports long-horizon physical state prediction through motion dynamics modeling [24].

Drive-OccWorld将视觉中心的4D世界模型应用于端到端自动驾驶规划[21]。SWAP使用世界模型驱动的蕴含图进行结构化推理[22][23]，MoSim通过运动动力学建模支持长期物理状态预测[24]。

Thus, these studies show that by modeling only the environment dynamics related to task objectives and perceptual capabilities, world models can provide key support for long-term autonomy in resource-constrained edge environments.

因此，这些研究表明，通过仅建模与任务目标和感知能力相关的环境动态，世界模型可以为资源受限边缘环境中的长期自主性提供关键支持。

---

This survey reviews the evolution from digital twins to world models through the lens of EGI. Figure 1 outlines the structure of this paper, covering motivation, world models, comparison with digital twins, technical evolution, applications, open resources, and future directions.

本综述通过EGI的视角回顾了从数字孪生到世界模型的演进。图1概述了本文的结构，涵盖动机、世界模型、与数字孪生的比较、技术演进、应用、开放资源和未来方向。

Building on the background and motivation discussed above, the contributions of this work are as follows:

在上述背景和动机的基础上，本文的贡献如下：

- **We provide the first comprehensive review on world models for EGI in wireless and edge systems, and contrast them with traditional digital-twin-centric designs.** We clearly distinguish world-model-centric EGI from conventional digital twin approaches, and outline a new direction for decision-centric modeling and autonomy at the network edge.

- **我们首次全面综述了无线和边缘系统中用于EGI的世界模型，并将其与传统以数字孪生为中心的设计进行对比。** 我们清晰地区分了以世界模型为中心的EGI与传统数字孪生方法，并概述了网络边缘以决策为中心的建模和自主性的新方向。

- **We provide a systematic conceptual comparison and a unifying perspective on digital twins and world models as two complementary, yet fundamentally different, paradigms for modeling the physical world in edge systems.** We highlight key shifts from world replication to decision-oriented abstraction, from rule-driven to data-driven dynamics, and from system-centric to agent-centric modeling, and explain how these shifts effectively match the requirements of EGI.

- **我们对数字孪生和世界模型作为两种互补但根本不同的边缘系统物理世界建模范式提供了系统性的概念比较和统一视角。** 我们强调从世界复制到决策导向抽象、从规则驱动到数据驱动动力学、从系统中心到代理中心建模的关键转变，并解释这些转变如何有效匹配EGI的需求。

- **We establish a taxonomy of world models tailored to wireless and edge scenarios, and decompose them into core components, including representation learning, dynamics modeling, observation and action interfaces, and imagination-based planning.** We review representative methods from machine learning, robotics, and control, and reinterpret them in terms of edge deployment constraints, communication awareness, and integration with existing digital twin infrastructures.

- **我们为无线和边缘场景建立了世界模型的分类体系，并将其分解为核心组件，包括表征学习、动力学建模、观测与动作接口以及基于想象的规划。** 我们综述了来自机器学习、机器人和控制领域的代表性方法，并从边缘部署约束、通信感知和与现有数字孪生基础设施的集成角度重新诠释它们。

- **We demonstrate the potential of world models in edge systems by mapping classical digital twin applications in integrated sensing, communication, and computing (ISCC), semantic communication, air-to-ground network, and low-altitude platforms, and industrial edge infrastructures to their corresponding world model-based counterparts.** We identify key open challenges and outline future research directions, including hybrid physics–data-driven world models, federated world modeling at the edge, multi-agent and multi-scale modeling, and explainable and trustworthy world models for safety-critical EGI.

- **我们通过将经典数字孪生应用（集成感知通信计算（ISCC）、语义通信、空对地网络、低空平台和工业边缘基础设施）映射到对应的世界模型版本，展示了世界模型在边缘系统中的潜力。** 我们确定了关键开放挑战，并概述了未来研究方向，包括混合物理-数据驱动世界模型、边缘联合世界建模、多代理和多尺度建模，以及面向安全关键EGI的可解释可信世界模型。

By organizing existing knowledge and open questions along these dimensions, this survey offers both a conceptual foundation and a practical roadmap for researchers and practitioners moving from digital-twin-centric design toward world-model-centric EGI.

通过沿这些维度组织现有知识和开放问题，本综述为研究人员和实践者提供了从数字孪生中心设计向世界模型中心EGI转变的概念基础和实践路线图。

---

## II. WORLD MODELS · 世界模型

*This section introduces the basic concepts of digital twins and world models, and then discusses their main differences. We further explain how world models can serve as a core enabler for EGI. The detailed framework is shown in Figure 2.*

*本节介绍数字孪生和世界模型的基本概念，然后讨论它们的主要差异。我们进一步解释世界模型如何成为EGI的核心赋能者。详细框架如图2所示。*

### A. Introduction to Digital Twins · 数字孪生简介

Digital twin technology has emerged as a dominant paradigm for modeling physical systems in cyber-physical environments [11].

数字孪生技术已成为信息物理环境中物理系统建模的主要范式[11]。

A digital twin is typically a high-fidelity virtual replica of a physical asset, system, or process governed by physical laws, domain-specific equations, and expert-crafted rules. Digital twins support detailed simulation, performance evaluation, fault diagnosis, and system optimization.

数字孪生通常是受物理定律、特定领域方程和专家规则约束的物理资产、系统或过程的高保真虚拟副本。数字孪生支持详细模拟、性能评估、故障诊断和系统优化。

In wireless and edge systems, digital twins have been widely adopted for tasks such as network planning, configuration validation, interference analysis, and what-if performance evaluation under known operational conditions [14].

在无线和边缘系统中，数字孪生已被广泛采用于网络规划、配置验证、干扰分析以及已知操作条件下的假想性能评估等任务[14]。

For example, network operators use digital twins to explore different base-station deployment strategies, predict coverage and capacity, and test control policies before applying them to the live network.

例如，网络运营商使用数字孪生来探索不同的基站部署策略，预测覆盖范围和容量，并在应用于实时网络之前测试控制策略。

These applications show that explicit physics-based and rule-based models can provide valuable insights into complex edge environments [25].

这些应用表明，显式基于物理和规则的模型可以为复杂边缘环境提供有价值的洞察[25]。

However, the characteristics that make digital twins powerful for offline engineering analysis do not directly meet the needs of online, autonomous EGI agents that must learn, adapt and act continuously in the field.

然而，使数字孪生成为强大离线工程分析工具的特性，并不能直接满足必须在线持续学习、适应和行动的自主EGI代理的需求。

This gap motivates a critical reassessment of how world modeling should be approached for EGI.

这一差距促使我们重新批判性地评估EGI中世界建模应有的方法。

---

### B. Overview of World Models · 世界模型概述

World models are internal simulations of environmental dynamics constructed by intelligent systems [26].

世界模型是由智能系统构建的环境动态内部模拟[26]。

By learning from real-world data and implicit laws, they capture key dynamic properties of the environment, predict future states, and provide agents with the ability to understand, reason about, and plan for the physical world.

通过从现实世界数据和隐式规律中学习，它们捕获环境的关键动态属性，预测未来状态，并为代理提供理解、推理和规划物理世界的能力。

This capability of learning and representing physical dynamics enables world models to excel in computer vision tasks such as video generation.

这种学习和表征物理动态的能力使世界模型能够在视频生成等计算机视觉任务中表现出色。

For instance, by internalizing spatiotemporal relationships from driving data, world models can generate realistic 4D scenes where objects follow consistent physical trajectories and spatial layouts over time, demonstrating their potential as physical simulators for visual content creation [30].

例如，通过内化驾驶数据中的时空关系，世界模型可以生成逼真的4D场景，其中物体随时间遵循一致的物理轨迹和空间布局，展示了其作为视觉内容创建的物理模拟器的潜力[30]。

---

World models are not high-fidelity reproductions of the physical world. Instead, they focus on dynamic aspects that are directly related to agent behavior and build an internal cognitive framework for imaginative reasoning [9].

世界模型并非物理世界的高保真再现。相反，它们专注于与代理行为直接相关的动态方面，并构建用于想象推理的内部认知框架[9]。

This abstraction avoids the computational cost of full-scale replication and makes world models well suited to resource-constrained scenarios such as EGI, where they can offer efficient decision support.

这种抽象避免了全量复制的计算成本，使世界模型非常适合EGI等资源受限场景，在这些场景中它们可以提供高效的决策支持。

Data-driven dynamic modeling is central to the adaptability of world models.

数据驱动的动态建模是世界模型适应性的核心。

Unlike traditional models that depend on preset physical formulas or rule bases, world models automatically extract implicit environmental laws including physical regularities and temporal correlations via unsupervised or self-supervised learning from multi-modal interaction data, such as sensor measurements, action feedback, and environmental observations [18].

与传统模型依赖预设物理公式或规则库不同，世界模型通过从多模态交互数据（如传感器测量、动作反馈和环境观测[18]）中进行无监督或自监督学习，自动提取包括物理规律性和时间相关性在内的隐式环境规律。

For example, in UAV flight scenarios, they can learn the mapping between actions and states from data that reflect channel variations and meteorological interference [18].

例如，在无人机飞行场景中，它们可以从反映信道变化和气象干扰的数据中学习动作与状态之间的映射[18]。

Even when facing previously unseen low-altitude weather conditions, they can still make reasonable predictions based on learned general laws, thereby overcoming the generalization limits of traditional models and flexibly adapting to the dynamics and uncertainty of edge environments.

即使面对先前未见过的低空气象条件，它们仍能基于所学到的通用规律做出合理预测，从而克服传统模型的泛化限制，灵活适应边缘环境的动态性和不确定性。

---

Prospective decision-making and planning are the core objectives of world models [9].

前瞻性决策和规划是世界模型的核心目标[9]。

Rather than responding passively, they follow a prediction–imagination–decision pipeline that gives agents forward-looking cognitive capabilities.

它们不是被动响应，而是遵循预测-想象-决策管道，赋予代理前瞻性认知能力。

World models can simulate multi-step future evolutions of the environment based on the current state and candidate actions, assess the benefits and risks of different action sequences, and optimize decision strategies to avoid short-sighted behavior.

世界模型可以基于当前状态和候选动作模拟环境的多步未来演变，评估不同动作序列的收益和风险，并优化决策策略以避免短视行为。

This property makes them well aligned with the latency, energy, and privacy constraints that define EGI in practice [1], and provides the core support for long-term autonomous and adaptive decision-making at the edge.

这一特性使它们与实践中定义EGI的延迟、能源和隐私约束高度吻合[1]，并为边缘的长期自主和自适应决策提供核心支持。

This adaptability comes from three key design characteristics of world models for edge deployment.

这种适应性源于世界模型用于边缘部署的三个关键设计特征。

The **efficiency** of the world model comes from latent-space abstraction. World models extract decision-relevant information without reconstructing the full environment in high fidelity, thus significantly reducing computation, storage, and communication overhead, which is critical for edge devices [18].

世界模型的**效率**源于潜空间抽象。世界模型在不高保真重建完整环境的情况下提取决策相关信息，从而显著降低计算、存储和通信开销，这对于边缘设备至关重要[18]。

The **agent-centric nature** focuses only on the environmental dynamics that are relevant to the observations and actions of the agent, forming a localized task-oriented cognitive model and avoiding the use of limited resources on redundant information [31].

**以代理为中心的特性**仅关注与代理的观测和动作相关的环境动态，形成本地化任务导向的认知模型，避免将有限资源用于冗余信息[31]。

The **generative imagination capability** uses generative AI techniques to infer the trajectories of scenarios that have not yet occurred, improving sample efficiency and further adapting to the practical requirements of edge scenarios [18].

**生成性想象能力**使用生成式AI技术推断尚未发生的场景轨迹，提高样本效率，并进一步适应边缘场景的实际需求[18]。

Thus, world models learn compact representations of environmental dynamics from data and, through generative imagination and prospective reasoning, provide efficient, autonomous, and adaptive decision support for resource-constrained edge agents.

因此，世界模型从数据中学习环境动态的紧凑表征，并通过生成性想象和前瞻性推理，为资源受限边缘代理提供高效、自主和自适应的决策支持。

They are becoming an indispensable cognitive pillar in the realization of EGI.

它们正在成为实现EGI不可或缺的认知支柱。

---

### C. Differences Between World Models and Digital Twins · 世界模型与数字孪生的差异

Both world models and digital twins aim to model environmental dynamics and support decision-making, but their core logic and application focus are fundamentally different.

世界模型和数字孪生都旨在建模环境动态并支持决策，但它们的核心逻辑和应用重点根本不同。

A world model is an **internal cognitive framework of an agent**. Rather than replicating reality, it distills laws of environmental dynamics that are relevant to agents' actions and decisions [27].

世界模型是**代理的内部认知框架**。它不是复制现实，而是提炼与代理动作和决策相关的环境动态规律[27]。

Without relying on preset physical formulas or rule bases, a world model learns implicit environmental laws in an unsupervised or self-supervised way from multi-modal interaction data and is inherently designed to provide efficient decision support across diverse tasks [34].

不依赖预设物理公式或规则库，世界模型以无监督或自监督方式从多模态交互数据中学习隐式环境规律，其本质设计是为多样化任务提供高效决策支持[34]。

To fit resource-constrained settings in EGI, world models reduce information dimensionality via latent-space abstraction, greatly lowering computation, storage, and communication overhead and avoiding resource use on redundant information.

为适应EGI中的资源受限设置，世界模型通过潜空间抽象降低信息维度，极大地降低计算、存储和通信开销，避免将资源用于冗余信息。

With a focus on optimizing future decisions, they enable agents to perform autonomous, adaptive and long-horizon decision-making in dynamic and uncertain edge environments, and have already shown clear advantages in navigation and related tasks that require accurate perception and decision-making [35].

专注于优化未来决策，它们使代理能够在动态和不确定的边缘环境中执行自主、自适应和长期的决策，并在需要精确感知和决策的导航及相关任务中已显示出明显优势[35]。

---

By contrast, the **core of a digital twin is to build a high-fidelity virtual mirror of a physical entity**, pursuing the accurate correspondence between the virtual and actual systems [28].

相比之下，**数字孪生的核心是构建物理实体的高保真虚拟镜像**，追求虚拟系统与实际系统之间的精确对应[28]。

Its modeling process heavily depends on pre-set physical formulas, rule bases, and rich sensor data, and aims to restore the real system states through physics-based modeling and data fusion [29].

其建模过程严重依赖预设物理公式、规则库和丰富传感器数据，旨在通过基于物理的建模和数据融合来恢复真实系统状态[29]。

This makes digital twins very effective for intelligent asset management. However, such high-fidelity requirements lead to massive data transmission, complex simulations, and large storage demands, impose strict requirements on hardware resources, and typically rely on cloud or high-performance servers.

这使数字孪生非常适合智能资产管理。然而，这种高保真要求导致大量数据传输、复杂模拟和大存储需求，对硬件资源要求严格，通常依赖云或高性能服务器。

Digital twins reside in real-time monitoring of physical entities, reconstruction of historical processes, and diagnosis of potential faults, with an emphasis on knowing the current real-world states.

数字孪生专注于物理实体的实时监控、历史过程重建和潜在故障诊断，重点在于了解当前真实世界状态。

Thus, Digital twins are more suitable for Industry 4.0 manufacturing, urban operation and maintenance, and other scenarios that need fine-grained management, rather than highly resource-constrained edge scenarios.

因此，数字孪生更适合工业4.0制造、城市运营维护和其他需要精细化管理的场景，而非高度资源受限的边缘场景。

---

The essential difference is that digital twins emphasize **restoring reality**, making the states and changes of physical entities observable and knowable, whereas world models emphasize **predicting the future**, making agent decisions more forward-looking and near-optimal through law distillation and imaginative reasoning [27][33].

根本区别在于，数字孪生强调**还原现实**，使物理实体的状态和变化可观测和可知，而世界模型强调**预测未来**，通过规律提炼和想象推理使代理决策更具前瞻性和近最优性[27][33]。

This difference in core orientation allows world models to overcome the strong resource dependence of digital twins and better match the latency, energy, and privacy constraints of edge scenarios, while digital twins remain indispensable in scenarios that require high-fidelity reconstruction.

这种核心导向的差异使世界模型能够克服数字孪生对资源的强依赖，更好地匹配边缘场景的延迟、能源和隐私约束，而数字孪生在需要高保真重建的场景中仍不可或缺。

---

### D. World-Model-Enabled Edge General Intelligence · 世界模型赋能的边缘通用智能

Through leveraging the four core capabilities — imagination, prediction, planning, and reasoning — world models meet the autonomous decision-making needs of EGI under resource constraints and dynamic uncertainty [36].

通过利用想象、预测、规划和推理这四个核心能力，世界模型在资源约束和动态不确定性下满足EGI的自主决策需求[36]。

**Imagination**: Imagination empowers world models to synthesize novel scenarios beyond observed reality, enabling agents to mentally explore hypothetical futures without physical interaction [26].

**想象**：想象赋予世界模型合成超出观测现实的新场景的能力，使代理能够在无需物理交互的情况下在精神上探索假设的未来[26]。

This capability supports creative problem-solving and risk-free experimentation in resource-constrained edge environments.

这种能力支持在资源受限边缘环境中的创造性问题解决和无风险实验。

For example, by leveraging learned visual priors, navigation agents can imagine trajectories in unfamiliar environments from a single input image, predicting future visual observations to plan safe and efficient paths without prior exploration [30].

例如，通过利用学到的视觉先验，导航代理可以从单张输入图像在陌生环境中想象轨迹，预测未来视觉观测以规划安全高效路径而无需事先探索[30]。

**Prediction**: Prediction refers to inferring future environmental states by learning implicit laws from multi-modal interaction data [18].

**预测**：预测指通过从多模态交互数据中学习隐式规律来推断未来环境状态[18]。

In EGI scenarios, a world model can foresee channel-quality fluctuations based on historical channel data and device trajectories, providing time margins for mode switching and power adjustment, and thus helping to avoid link outages [20].

在EGI场景中，世界模型可以基于历史信道数据和设备轨迹预见信道质量波动，为模式切换和功率调整提供时间裕量，从而帮助避免链路中断[20]。

In low-altitude networks, it can fuse historical and real-time weather data to predict short-term changes in wind speed and direction, provide early warnings for UAV flight safety, and mitigate the timeliness limitations of traditional weather forecasts [37].

在低空网络中，它可以融合历史和实时天气数据预测风速和风向的短期变化，为无人机飞行安全提供预警，并减轻传统天气预报的时间局限性[37]。

**Planning**: Planning uses predicted outcomes to simulate multi-step scenario evolution, evaluate candidate actions, and optimize decisions [38].

**规划**：规划使用预测结果模拟多步场景演变，评估候选动作，并优化决策[38]。

When UAVs perform delivery or inspection tasks, the world model can combine weather and channel predictions to plan flight trajectories that balance safety, energy efficiency, and throughput.

当无人机执行投递或巡检任务时，世界模型可以结合天气和信道预测来规划在安全性、能效和吞吐量之间取得平衡的飞行轨迹。

In scenarios with multiple UAVs or clusters of edge nodes, it can dynamically allocate limited computing, storage, and communication resources and adjust allocations based on task load and remaining resources, preventing overload or waste and improving overall system efficiency [38].

在多无人机或边缘节点集群场景中，它可以动态分配有限的计算、存储和通信资源，并根据任务负载和剩余资源调整分配，防止过载或浪费，提高整体系统效率[38]。

EGI requires autonomous decision-making in uncertain environments, and world models enhance this ability through latent-space simulation. For example, Zhang et al. [39] proposes a generative AI and multi-agent policy optimization framework for satellite communication, achieving efficient modeling and adaptive optimization, thereby improving the planning capability of EGI.

EGI需要在不确定环境中进行自主决策，世界模型通过潜空间模拟增强这一能力。例如，张等人[39]提出了一种用于卫星通信的生成式AI和多代理策略优化框架，实现了高效建模和自适应优化，从而提高了EGI的规划能力。

**Reasoning**: Reasoning allows the world model to use learned general laws to handle unknowns and uncertainties at the edge [40].

**推理**：推理使世界模型能够使用学到的通用规律来处理边缘的未知和不确定性[40]。

In vehicular communications, when sudden road works or traffic jams occur, the onboard edge nodes can infer appropriate communication routes and trajectory adjustments by combining real-time road conditions with link states, thus maintaining continuous data delivery and driving safety [41].

在车联网通信中，当突发道路施工或交通拥堵时，车载边缘节点可以结合实时路况与链路状态推断适当的通信路由和轨迹调整，从而保持连续数据传输和驾驶安全[41]。

In industrial edge-device maintenance, a world model can analyze abnormal sensor readings, distinguish between actual faults, interference, and false alarms, and provide accurate support for operations and maintenance decisions, reducing unnecessary production loss [40].

在工业边缘设备维护中，世界模型可以分析异常传感器读数，区分实际故障、干扰和误报，并为运维决策提供准确支持，减少不必要的生产损失[40]。

---

EGI faces challenges such as time-varying channels and dynamic node appearance caused by high-speed mobility.

EGI面临由高速移动引起的时间变化信道和动态节点出现等挑战。

The prediction, planning and reasoning capabilities of world models help ensure link stability, resource optimization, and rapid response to emergencies, thus meeting the low-latency and high-reliability requirements of wireless EGI networks [42].

世界模型的预测、规划和推理能力有助于确保链路稳定性、资源优化和紧急情况快速响应，从而满足无线EGI网络的低延迟和高可靠性要求[42]。

In low-altitude cooperative UAV scenarios, these capabilities jointly support flight safety and mission efficiency, and enable adaptation to the complex conditions of edge environments [20].

在低空协作无人机场景中，这些能力共同支持飞行安全和任务效率，并实现对边缘环境复杂条件的适应[20]。

---

## III. FROM DIGITAL TWIN TO WORLD MODEL · 从数字孪生到世界模型

*This section first introduces the core components of world models and then discusses the key technical shifts that drive the evolution from digital twins to world models.*

*本节首先介绍世界模型的核心组件，然后讨论推动从数字孪生到世界模型演进的关键技术转变。*

### A. Core Components of World Models · 世界模型的核心组件

The perception–prediction–decision of world models is based on the coordinated operation of three core modules: the encoder, the dynamics model, and the decoder.

世界模型的感知-预测-决策基于三个核心模块的协调运行：编码器、动力学模型和解码器。

These modules are tightly coupled and together form an efficient closed-loop workflow [18].

这些模块紧密耦合，共同形成高效的闭环工作流[18]。

**Encoder**: The encoder is the front-end information processing module of the world model and is mainly responsible for compressing high-dimensional data and extracting key features [18].

**编码器**：编码器是世界模型的前端信息处理模块，主要负责压缩高维数据并提取关键特征[18]。

It receives multi-modal, high-dimensional perceptual data such as images and radar signals, removes redundant details via feature extraction algorithms, and preserves core information relevant to agent decision-making.

它接收图像和雷达信号等多模态高维感知数据，通过特征提取算法去除冗余细节，保留与代理决策相关的核心信息。

In this way, it transforms high-dimensional raw data into compact low-dimensional latent states [43].

这样，它将高维原始数据转换为紧凑的低维潜态[43]。

This processing not only greatly reduces the computational overhead of downstream modules (which is important for edge devices), but also provides high-quality input for subsequent structure learning and prediction.

这种处理不仅大大降低了下游模块的计算开销（这对边缘设备很重要），还为后续结构学习和预测提供高质量输入。

**Dynamics model**: The dynamics model is the core engine that allows a world model to learn environmental evolution laws and perform temporal prediction [26].

**动力学模型**：动力学模型是世界模型学习环境演化规律并执行时间预测的核心引擎[26]。

Its main role is to learn the state transition function of the environment so that it can accurately predict the next latent state given the current latent state and the action of agent [44].

其主要作用是学习环境的状态转换函数，以便在给定当前潜态和代理动作的情况下准确预测下一个潜态[44]。

Dynamics models can be broadly divided into deterministic models (such as RNN-based models) and stochastic models (such as the recurrent state-space model, RSSM, which uses both deterministic and stochastic hidden variables), and can be selected according to scenario requirements.

动力学模型可大致分为确定性模型（如基于RNN的模型）和随机模型（如使用确定性和随机隐藏变量的递归状态空间模型RSSM），可根据场景需求选择。

The dynamics model takes the encoder's latent state as input, combines it with the agent's action, and predicts multi-step latent state trajectories, thereby providing crucial trend information to support decision-making [24].

动力学模型以编码器的潜态作为输入，结合代理的动作，预测多步潜态轨迹，从而提供关键趋势信息以支持决策[24]。

**Decoder**: The decoder is the key output module in the closed loop, responsible for mapping the latent states predicted by the dynamics model back to observable quantities [9].

**解码器**：解码器是闭环中的关键输出模块，负责将动力学模型预测的潜态映射回可观测量[9]。

It can reconstruct future environmental observation frames and output reward signals.

它可以重建未来环境观测帧并输出奖励信号。

These outputs can be used to visually verify prediction quality and assess the validity of latent states, and they also serve as an important basis for policy evaluation, helping the system select better decision strategies.

这些输出可用于可视化验证预测质量并评估潜态的有效性，它们还作为策略评估的重要基础，帮助系统选择更好的决策策略。

In addition, the decoder's outputs can be used as feedback signals to update the encoder and the dynamics model, continuously improving feature extraction and state prediction accuracy.

此外，解码器的输出可用作反馈信号来更新编码器和动力学模型，不断改进特征提取和状态预测精度。

This closes the perception–prediction–decision–iteration loop and ensures the integrity and effectiveness of the entire pipeline [19].

这闭合了感知-预测-决策-迭代循环，并确保整个管道的完整性和有效性[19]。

Thus, the progression from digital twin to world model for EGI involves a transition from rule-driven, system-centric world replication to a data-driven, agent-centric abstraction capable of active imagination, as shown in Figure 3 and Table III.

因此，EGI从数字孪生到世界模型的演进涉及从规则驱动的、系统中心的 world replication 向数据驱动的、以代理为中心且具备主动想象能力的 abstraction 的转变，如图3和表III所示。

---

### B. From World Replication to World Abstraction · 从世界复制到世界抽象

The core principle of digital twins is **world replication**. The goal is to construct virtual systems that are highly consistent with the physical world in structure, state, and mechanisms, to support system-level simulation and monitoring [16].

数字孪生的核心原则是**世界复制**。目标是构建在结构、状态和机制上与物理世界高度一致的虚拟系统，以支持系统级模拟和监控[16]。

The modeling objective of world models is **world abstraction**. Instead of pursuing full physical fidelity, world models retain only those environmental dynamics that affect an agent's future cumulative rewards and emphasize decision-relevant information through abstract representations.

世界模型的建模目标是**世界抽象**。世界模型不追求完整的物理保真度，而是仅保留影响代理未来累积奖励的环境动态，并通过抽象表征强调决策相关信息。

For example, the world models framework proposed [26] uses a variational auto-encoder (VAE) to learn low-dimensional latent representations and shows that such latent states alone can support complex control tasks with performance close to that achieved via direct interaction with the real environment.

例如，文献[26]提出的世界模型框架使用变分自编码器（VAE）学习低维潜态表征，并表明仅凭这些潜态就能支持复杂控制任务，性能接近于通过与真实环境直接交互所达到的水平。

The Dreamer family proposed [27] further demonstrates that imaginative rollouts in a learned world model can significantly improve the sample efficiency of policy optimization.

文献[27]提出的Dreamer系列进一步表明，在已学习的世界模型中进行想象性 rollout 可以显著提高策略优化的样本效率[27]。

When the modeling objective shifts toward online decision-making and control for EGI, the criteria for evaluating state representations differ fundamentally from those in traditional systems engineering.

当建模目标转向EGI的在线决策和控制时，评估状态表征的标准与传统系统工程中的标准有根本性不同。

The objective of EGI is to bring general, adaptive, and context-sensitive cognitive capabilities to resource-constrained edge devices. It emphasizes long-term autonomous decision-making in dynamic, uncertain, and partially observable environments, under tight computation, storage, and communication budgets [48].

EGI的目标是为资源受限边缘设备带来通用、自适应和上下文敏感的认知能力。它强调在紧张计算、存储和通信预算下，在动态、不确定和部分可观测环境中的长期自主决策[48]。

In EGI scenarios, maintaining a globally accurate, real-time synchronized replica of the physical world leads to heavy computational and communication overhead and introduces large amounts of information that are irrelevant to current decisions, due to over-detailed physical descriptions [18].

在EGI场景中，维护物理世界的全局准确实时同步副本会导致大量计算和通信开销，并因过度详细的物理描述而引入大量与当前决策无关的信息[18]。

This mismatch reduces the efficiency of decisions per unit of resource.

这种不匹配降低了每单位资源的决策效率。

Furthermore, traditional digital twins rely heavily on prior physical models, which are difficult to maintain in complex and unknown edge environments and often lack sufficient generalization and adaptability.

此外，传统数字孪生严重依赖先验物理模型，这在复杂和未知边缘环境中难以维护，且往往缺乏足够的泛化能力和适应性。

Existing studies indicate that agent decision-making depends on how the environment evolves under the influence of actions rather than on complete reconstruction of physical states, while full replication of the physical world therefore does not produce an optimal state representation for decision-making [49].

现有研究表明，代理决策取决于环境在动作影响下如何演变，而非对物理状态的完整重建，因此物理世界的完全复制并不能产生用于决策的最优状态表征[49]。

Abstraction-based world models show clear advantages for EGI.

基于抽象的世界模型对EGI显示出明显优势。

The core requirement of EGI is to capture the mapping between scheduling or control actions and system performance, rather than to reconstruct the full physical state.

EGI的核心需求是捕获调度或控制动作与系统性能之间的映射，而非重建完整物理状态。

By discarding irrelevant details for decision-making, world models can significantly reduce computation and communication costs on the edge [50].

通过丢弃与决策无关的细节，世界模型可以显著降低边缘的计算和通信成本[50]。

More importantly, by learning environmental dynamics directly from interaction data, world models reduce dependence on precise prior physical models and lay the foundation for strong generalization and long-term autonomy in unknown environments [8][51].

更重要的是，通过直接从交互数据中学习环境动态，世界模型减少了对精确先验物理模型的依赖，为未知环境中的强泛化能力和长期自主性奠定了基础[8][51]。

The evolution from digital twins to world models thus reflects a decision-centered shift in design philosophy. The modeling goal changes from building a high-fidelity replica of the world to constructing an abstract world representation that supports efficient prediction, planning, and learning by agents.

因此，从数字孪生到世界模型的演进反映了设计哲学中以决策为中心的转变。建模目标从构建世界的高保真副本，转变为构建支持代理高效预测、规划和学习的抽象世界表征。

---

### C. From Rule-Driven Dynamics to Data-Driven World Evolution · 从规则驱动动力学到数据驱动世界演化

Traditional digital twin technology is grounded in physics-based mechanistic models, in which environmental evolution is governed by predefined physical laws and system-level equations.

传统数字孪生技术植根于基于物理的机理模型，其中环境演化受预定义物理定律和系统级方程支配。

This rule-driven paradigm provides deterministic descriptions of physical entities through high-fidelity virtual replicas [16].

这一规则驱动范式通过高保真虚拟副本为物理实体提供确定性描述[16]。

World models adopt a **data-driven modeling paradigm**. Using generative AI techniques, they compress environmental dynamics into compact latent spaces.

世界模型采用**数据驱动建模范式**。使用生成式AI技术，它们将环境动态压缩为紧凑潜空间。

By analyzing interaction data between agents and their environments, world models can autonomously learn implicit laws of state transitions and predict future environmental states [26].

通过分析代理与其环境之间的交互数据，世界模型可以自主学习状态转换的隐式规律并预测未来环境状态[26]。

A key characteristic of EGI is the need for long-horizon autonomous decision-making in dynamic, unstructured, and highly uncertain physical environments [52].

EGI的一个关键特性是需要，在动态、非结构化和高度不确定的物理环境中进行长期自主决策[52]。

In practical EGI scenarios, such as UAV networks and intelligent transportation systems [53], fixed rule-based models often fail to capture the long-term evolution of complex systems with sufficient accuracy.

在UAV网络和智能交通系统[53]等实际EGI场景中，固定基于规则的模型往往无法以足够精度捕获复杂系统的长期演变。

This rule-driven nature limits their generalization capability.

这种规则驱动特性限制了其泛化能力。

Since a digital twin operates strictly according to predefined formulas and assumptions, it cannot flexibly adjust its evolution logic when facing unmodeled physical phenomena or unexpected disturbances beyond its design scope.

由于数字孪生严格按预定义公式和假设运行，当面对超出其设计范围的未建模物理现象或意外干扰时，它无法灵活调整其演化逻辑。

In addition, the complex numerical solvers required for high-fidelity physical modeling impose a substantial computational load that conflicts with the limited resources of edge devices.

此外，高保真物理建模所需的复杂数值求解器带来大量计算负载，与边缘设备的有限资源相冲突。

**Data-driven world evolution modeling becomes a key direction for EGI.** EGI agents can continuously refine their internal world models using local interaction data, thus adapting to environmental changes without redesigning physical equations [18].

**数据驱动的世界演化建模成为EGI的关键方向。** EGI代理可以使用本地交互数据不断精炼其内部世界模型，从而在无需重新设计物理方程的情况下适应环境变化[18]。

By performing evolution inference in low-dimensional latent spaces, world models avoid pixel-level simulation of high-dimensional physical entities and significantly reduce computational latency and resource consumption.

通过在低维潜空间执行演化推理，世界模型避免了对高维物理实体的像素级模拟，显著降低计算延迟和资源消耗。

For example, in UAV networks, the aerial network world model, trained in large-scale aerial sequences, trajectories, and semantic labels, can predict semantically plausible long-range scenarios even under unseen meteorological conditions. This supports the dynamic generation of navigation paths that balance obstacle avoidance and high-level semantic objectives [37].

例如，在UAV网络中，在大规模航空序列、轨迹和语义标签上训练的航空网络世界模型，即使在未见过的气象条件下也能预测语义上合理的远程场景。这支持动态生成在障碍物规避和高层语义目标之间取得平衡的导航路径[37]。

The shift from rule-driven to data-driven modeling represents a fundamental evolution of EGI rather than a simple technical improvement. This transition allows the system to move beyond passive reproduction toward proactive prediction within open-world environments.

从规则驱动到数据驱动建模的转变代表了EGI的根本性演进，而非简单的技术改进。这一转变使系统能够从被动再现走向开放世界环境中的主动预测。

---

### D. Action-Conditioned Prediction and Imagination · 动作条件化预测与想象

As EGI evolves from basic perception to complex autonomous decision-making, the objective of modeling shifts from describing current states to reasoning about the consequences of actions [54].

随着EGI从基本感知发展到复杂自主决策，建模目标从描述当前状态转向推理动作的后果[54]。

From this viewpoint, digital twins and world models represent two distinct predictive paradigms: the former focuses on parameter-driven offline simulation, whereas the latter supports action-conditioned online imagination.

从这个视角看，数字孪生和世界模型代表了两种截然不同的预测范式：前者专注于参数驱动的离线模拟，而后者支持动作条件化在线想象。

Traditional digital twins are designed mainly for system monitoring and performance evaluation. Their predictive mechanisms are typically based on passive simulation of environmental dynamics.

传统数字孪生主要为系统监控和性能评估而设计。其预测机制通常基于环境动态的被动模拟。

Given an initial state and boundary conditions, a digital twin carries out deterministic simulations to forecast system trajectories.

给定初始状态和边界条件，数字孪生执行确定性模拟来预测系统轨迹。

Agent actions are often treated as external input or configuration parameters, rather than as intrinsic drivers of system evolution [55].

代理动作通常被视为外部输入或配置参数，而非系统演化的内在驱动因素[55]。

By contrast, world models use an **action-conditioned prediction mechanism** that explicitly models the agent's actions as key variables in state transitions.

相比之下，世界模型使用**动作条件化预测机制**，将代理动作明确建模为状态转换中的关键变量。

Since trial-and-error interaction in the physical world is often costly, world models allow agents to conduct imaginative trajectory rollouts in a compact latent space.

由于物理世界中的试错交互通常代价高昂，世界模型允许代理在紧凑潜空间中进行想象性轨迹 rollout。

Without directly interacting with the real environment, an agent can rapidly simulate multiple candidate action sequences inside the model and evaluate their cumulative long-term rewards [9].

无需直接与真实环境交互，代理可以在模型内快速模拟多个候选动作序列并评估其累积长期奖励[9]。

In EGI scenarios, edge devices are constrained by limited computing, storage, and communication resources, while EGI tasks often involve long time horizons and limited rewards [56].

在EGI场景中，边缘设备受限于有限的计算、存储和通信资源，而EGI任务通常涉及长时域和有限奖励[56]。

Agents must therefore compare many potential decision paths under stringent cost constraints, which is difficult to achieve efficiently with prediction schemes based on high-fidelity simulation.

因此，代理必须在严格成本约束下比较许多潜在决策路径，这在使用基于高保真模拟的预测方案时难以高效实现。

World models perform action-conditioned prediction and imagination in low-dimensional latent spaces. This avoids pixel-level simulation of high-dimensional physical states, greatly reducing computational complexity while preserving essential dynamics for decision-making.

世界模型在低维潜空间执行动作条件化预测和想象。这避免了对高维物理状态的像素级模拟，大大降低计算复杂度，同时保留决策所需的基本动态。

In autonomous driving, for example, FSDrive [57] employs a world model as a predictor to generate future imagined scenes in latent space that jointly capture spatial and temporal structure, thereby enabling trajectory planning and policy evaluation without explicit pixel-level physical simulation.

例如在自动驾驶中，FSDrive[57]使用世界模型作为预测器，在潜空间生成联合捕获时空结构的未来想象场景，从而实现无需显式像素级物理模拟的轨迹规划和策略评估。

By shifting prediction from system-level reproduction to action-driven evaluation of future outcomes, world models provide a more efficient and scalable decision-support paradigm for edge intelligence.

通过将预测从系统级再现转向动作驱动的未来结果评估，世界模型为边缘智能提供了更高效和可扩展的决策支持范式。

---

### E. Agent-Centric and Localized World Modeling · 以代理为中心和本地化世界建模

Digital twin technology originated in large-scale system engineering contexts such as Industry 4.0 and smart cities, and its design philosophy is inherently system-centric [46].

数字孪生技术源于工业4.0和智慧城市等大规模系统工程背景，其设计哲学本质上是系统中心的[46]。

By constructing a global virtual replica of the entire physical system, digital twins aim to reproduce the states of physical entities, their structural relationships, and their evolution from a holistic perspective, thereby supporting system-level analysis, simulation, and management.

通过构建整个物理系统的全局虚拟副本，数字孪生旨在从整体视角再现物理实体的状态、其结构关系及其演化，从而支持系统级分析、模拟和管理。

World models adopt an **agent-centric and localized modeling paradigm**.

世界模型采用**以代理为中心和本地化建模范式**。

Agent-centric modeling means that a world model does not try to reconstruct the full objective physical world. Instead, it serves as an internal cognitive component of the agent [58].

以代理为中心的建模意味着世界模型不试图重建完整的客观物理世界，而是作为代理的内部认知组件[58]。

The model is defined by the agent's sensing capabilities, action space, and task objectives, and captures only the environmental dynamics that are relevant to the agent's observations and actions.

模型由代理的感知能力、动作空间和任务目标定义，仅捕获与代理观测和动作相关的环境动态。

Through localized modeling, world models learn implicit evolution patterns and retain only local dynamics that directly affect current decisions [59].

通过本地化建模，世界模型学习隐式演化模式，仅保留直接影响当前决策的本地动态。

Thus, the size of the model is decoupled from the overall environmental complexity, allowing resource-constrained edge devices to perform complex environment modeling tasks.

因此，模型大小与整体环境复杂性解耦，允许资源受限边缘设备执行复杂环境建模任务。

In EGI scenarios that require continuous autonomous decision-making and online adaptation, the primary challenge of an agent is not only to precisely reconstruct the environment, but also to quickly understand local conditions, predict the consequences of actions, and make effective decisions under partial observability [60].

在需要持续自主决策和在线适应的EGI场景中，代理的主要挑战不仅是精确重建环境，还要快速理解本地条件、预测动作后果，并在部分可观测性下做出有效决策[60]。

For edge-deployed agents, sensing range, communication capability, and computational resources are limited, and the global state of the environment is generally neither fully observable nor practically maintainable [48].

对于边缘部署的代理，感知范围、通信能力和计算资源有限，环境全局状态通常既非完全可观测也非实际可维护[48]。

The agent-centric and localized nature of world models closely matches the fundamental requirements of EGI [61].

世界模型的以代理为中心和本地化特性与EGI的根本需求高度匹配[61]。

This modeling paradigm reduces the complexity of model construction and maintenance, making online learning and continuous updates on edge devices more feasible.

这种建模范式降低了模型构建和维护的复杂性，使边缘设备上的在线学习和持续更新更加可行。

It supports a deep integration with decision-making methods such as reinforcement learning and model predictive control, allowing the world model to function as an internal part of the agent's decision process rather than an external simulation tool.

它支持与强化学习和模型预测控制等决策方法的深度集成，使世界模型作为代理决策过程的内部部分而非外部模拟工具运行。

Localized world models offer better scalability and robustness in typical EGI scenarios characterized by multi-agent operation, non-stationary environments, and incomplete information [62].

本地化世界模型在典型的多代理运行、非平稳环境和信息不完整的EGI场景中提供更好的可扩展性和鲁棒性[62]。

By shifting from system-centric to agent-centric modeling, world models focus on local dynamics directly relevant to individual decisions. This shift not only reduces resource consumption at the edge, but also provides essential internal support for efficient prediction, reasoning, and autonomous decision-making in dynamic physical environments.

通过从系统中心转向代理中心建模，世界模型专注于与个体决策直接相关的本地动态。这种转变不仅降低了边缘的资源消耗，还为动态物理环境中高效预测、推理和自主决策提供了必要的内部支持。

---

### F. Summary of the World Model Paradigm · 世界模型范式总结

This section has examined the paradigm shift from digital twins to world models. This transition redefines physical-world modeling from fidelity-oriented replication to decision-oriented abstraction, establishing a more suitable cognitive modeling framework for resource-constrained EGI.

本节考察了从数字孪生到世界模型的范式转变。这一转变将物理世界建模从保真度导向复制重新定义为决策导向抽象，为资源受限的EGI建立了更合适的认知建模框架。

Therefore, we summarize the key characteristics of the world model paradigm in four dimensions:

因此，我们从四个维度总结世界模型范式的关键特征：

1. **Decision-Oriented Abstract Modeling**: With high-fidelity physical replication of digital twins, world models abstract the environment in a decision-oriented manner by learning compact latent representations that preserve only the dynamics relevant to an agent's future rewards. This abstraction reduces model dimensionality and computational overhead, making world models well suited for resource-constrained edge devices [26].

   **决策导向抽象建模**：与数字孪生的高保真物理复制不同，世界模型以决策导向方式抽象环境，通过学习仅保留与代理未来奖励相关动态的紧凑潜态表征。这种抽象降低了模型维度和计算开销，使世界模型非常适合资源受限边缘设备[26]。

2. **Data-Driven Evolutionary Learning**: Rule-driven digital twins that rely on predefined physical equations, world models use data-driven generative modeling to learn state transition dynamics from agent–environment interactions. This approach captures complex dynamics that are difficult to describe analytically and supports continual learning, enabling the model to adapt to environmental changes and unexpected disturbances [18].

   **数据驱动演化学习**：与依赖预定义物理方程的规则驱动数字孪生不同，世界模型使用数据驱动生成建模从代理-环境交互中学习状态转换动态。这种方法捕获难以解析描述的复杂动态，并支持持续学习，使模型能够适应环境变化和意外干扰[18]。

3. **Action-Conditioned Imaginative Reasoning**: World models incorporate agent actions into state transitions through action-conditioned prediction. By iterating one-step predictions, they enable imagination-based reasoning in latent space to evaluate future trajectories under different actions. This allows agents to assess long-term effects without real-world interaction, supporting forward planning and improving sample efficiency [51].

   **动作条件化想象推理**：世界模型通过动作条件化预测将代理动作纳入状态转换。通过迭代单步预测，它们在潜空间中实现基于想象的推理，以评估不同动作下的未来轨迹。这使代理能够在无需真实世界交互的情况下评估长期效果，支持前瞻性规划并提高样本效率[51]。

4. **Agent-Centric Local Modeling**: As an internal cognitive component, a world model is shaped by the agent's perception, action space, and task goals, and captures only the local dynamics the agent can observe and influence. This agent-centric design decouples model complexity from the global environment, reduces the reliance on global state synchronization, and supports heterogeneous and collaborative deployment in distributed edge systems [9].

   **以代理为中心的本地建模**：作为内部认知组件，世界模型由代理的感知、动作空间和任务目标塑造，仅捕获代理可以观测和影响的本地动态。这种以代理为中心的设计将模型复杂性与全局环境解耦，减少对全局状态同步的依赖，并支持分布式边缘系统中的异构协作部署[9]。

In EGI, the world model paradigm provides a coherent and practical framework for environmental modeling. With replacing digital twins in system-level analysis, world models complement them by supporting internal cognition and decision-making of agents.

在EGI中，世界模型范式为环境建模提供了连贯实用的框架。在系统级分析中取代数字孪生，世界模型通过支持代理的内部认知和决策来补充它们。

This enables edge agents to achieve continuous autonomy and long-term adaptation in dynamic, partially observable, and resource-constrained environments, marking a shift from task-specific automation to more general autonomous intelligence.

这使边缘代理能够在动态、部分可观测和资源受限环境中实现持续自主和长期适应，标志着从特定任务自动化向更通用自主智能的转变。

---

## IV. APPLICATIONS · 应用

*This section discusses the application of world models to integrated sensing, communication, and computing (ISCC), semantic communication, air-to-ground networks, and low-altitude wireless networks.*

*本节讨论世界模型在集成感知通信计算（ISCC）、语义通信、空对地网络和低空无线网络中的应用。*

### A. Integrated Sensing, Communication, and Computing · 集成感知、通信与计算

Integrated sensing, communication, and computation (ISCC) is a key application in edge intelligence. Its objective is to orchestrate the end-to-end optimization of these resources under strict edge constraints, thereby maximizing system performance in connectivity-centric scenarios [63].

集成感知通信与计算（ISCC）是边缘智能的关键应用。其目标是在严格边缘约束下协调这些资源的端到端优化，从而在以连接为中心的场景中最大化系统性能[63]。

Digital twins and world models jointly support deep synergy among the three ISCC pillars. The digital twin provides offline verification for sensing-data calibration, communication-link planning and computational-resource pre-allocation, whereas the world model dynamically adjusts, in an online fashion, sensing frequency, communication-protocol parameters and computation-offloading policies.

数字孪生和世界模型共同支持三大ISCC支柱的深度协同。数字孪生为感知数据校准、通信链路规划和计算资源预分配提供离线验证，而世界模型以在线方式动态调整感知频率、通信协议参数和计算卸载策略。

The two mechanisms are functionally complementary and together form a cohesive co-design paradigm.

两种机制在功能上互补，共同形成有凝聚力的协同设计范式。

The **principal value of the digital twin** lies in its ability to perform offline, system-level modeling and validation of sensing accuracy, link quality, and resource allocation [64].

**数字孪生的主要价值**在于其执行感知精度、链路质量和资源分配的离线系统级建模和验证的能力[64]。

By constructing a high-fidelity virtual replica of the physical system, the twin exploits predefined physical models and rules to run simulations. In industrial-edge deployment scenarios, it accurately reproduces sensor coverage, wireless signal attenuation, and compute-node capacity distributions, enabling ex-ante evaluation of various resource-scheduling policies [65].

通过构建物理系统的高保真虚拟副本，孪生体利用预定义物理模型和规则运行模拟。在工业边缘部署场景中，它精确再现传感器覆盖、无线信号衰减和计算节点容量分布，实现各种资源调度策略的事前评估[65]。

This high-fidelity emulation offers reliable evidence for offline resource allocation and task scheduling, eliminates the risks and overhead of direct experimentation on real hardware, and constitutes an indispensable tool during the ISCC design phase.

这种高保真仿真为离线资源分配和任务调度提供可靠证据，消除了在真实硬件上直接实验的风险和开销，并构成ISCC设计阶段不可或缺的工具。

The **world model focuses on online, dynamic co-optimization** of sensing, communication, and computation, thereby accommodating the volatility and uncertainty inherent to edge environments.

**世界模型专注于感知、通信和计算的在线动态协同优化**，从而适应边缘环境固有的波动性和不确定性。

Its core advantage is prospective planning and real-time adaptation conditioned on the instantaneous system's state [66].

其核心优势是基于即时系统状态的前瞻性规划和实时适应[66]。

The world model employs data-driven approaches to learn the latent dependencies between the three functions using multi-modal interaction data [67].

世界模型使用数据驱动方法利用多模态交互数据学习三项功能之间的潜依赖关系[67]。

To achieve this, an encoder first compresses high-dimensional data into low-dimensional latent states, extracting critical information to reduce overhead. Next, a dynamics module tracks environmental changes and captures temporal dependencies. Finally, a decoder maps these predicted states back to observable quantities, completing the sense-predict-decide loop.

为实现这一点，编码器首先将高维数据压缩为低维潜态，提取关键信息以降低开销。然后动力学模块跟踪环境变化并捕获时间依赖。最后解码器将这些预测状态映射回可观测量，完成感知-预测-决策循环。

In ISCC scenarios for UAV swarms, the model forecasts communication traffic and computational-resource variations induced by alternative trajectory adjustments, enabling proactive cooperative strategies [68].

在无人机集群的ISCC场景中，模型预测由替代轨迹调整引起的通信流量和计算资源变化，实现主动协作策略[68]。

In industrial-edge contexts, it adaptively tunes sensor sampling rates, communication protocol configurations, and offloading fractions, dynamically balancing competing objectives [69].

在工业边缘环境中，它自适应调整传感器采样率、通信协议配置和卸载比例，动态平衡竞争目标[69]。

This online adaptability exactly compensates for the inability of offline digital-twin optimization to cope with environmental dynamics.

这种在线适应性恰好弥补了离线数字孪生优化无法应对环境动态的不足。

In physical layer security, the prediction and generation abilities of world models have shown great potential. The APEG [70] framework uses generative AI and diffusion models to achieve high-accuracy and adaptive physical layer authentication in dynamic environments.

在物理层安全中，世界模型的预测和生成能力显示出巨大潜力。APEG[70]框架使用生成式AI和扩散模型在动态环境中实现高精度自适应物理层认证。

The synergy between digital twins and world models propels ISCC from offline static optimization to online dynamic self-adaptive optimization [18].

数字孪生与世界模型之间的协同推动ISCC从离线静态优化转向在线动态自适应优化[18]。

Exploiting high-fidelity physical mapping and offline deduction, the digital twin delivers precise calibration benchmarks for sensing, dependable link-planning evidence for communication, and rational resource pre-allocation schemes for computation.

利用高保真物理映射和离线推理，数字孪生为感知提供精确校准基准，为通信提供可靠链路规划证据，为计算提供合理资源预分配方案。

Leveraging data-driven predictive modeling and online decision making, the world model continuously refines sensing frequency, communication parameter configurations and computation-offloading strategies at run time [71], achieving online co-alignment of sensing, communication and computation.

利用数据驱动预测建模和在线决策，世界模型在运行时持续优化感知频率、通信参数配置和计算卸载策略[71]，实现感知、通信和计算的在线协同对齐。

Collectively, the integration of digital twins and world models breaks down silos-based subsystem optimization, endowing ISCC with both the reliability of offline planning and the agility of online adaptation.

总体而言，数字孪生与世界模型的集成打破了基于孤岛的子系统优化，赋予ISCC离线规划的可靠性和在线适应的敏捷性。

Specifically, digital twin-integrated frameworks achieve 33% end-to-end latency reduction and a 30% reduction in tail latency at a mere 2–7% energy cost [64], while world models enable dynamic parameter adjustment of 15–20% lower execution latency [69], ultimately enhancing system stability and efficiency in complex edge scenarios.

具体而言，数字孪生集成框架实现端到端延迟降低33%，尾延迟降低30%，仅消耗2-7%的额外能耗[64]，而世界模型实现执行延迟降低15-20%的动态参数调整[69]，最终在复杂边缘场景中增强系统稳定性和效率。

---

### B. Semantic Communication · 语义通信

Semantic communication is widely recognized as a key technique for next-generation 6G networks because it focuses on the efficient transmission of semantic essence and core intent [86].

语义通信被广泛认为是下一代6G网络的关键技术，因为它专注于语义本质和核心意图的高效传输[86]。

By conveying semantic meaning rather than raw bits, it breaks the throughput ceiling of conventional schemes and remains efficient under limited bandwidth or hostile channels, thus providing a key enabler for resource-constrained intelligent networking [87].

通过传输语义含义而非原始比特，它突破了传统方案的吞吐量上限，并在有限带宽或恶劣信道下保持高效，从而为资源受限的智能网络提供关键赋能[87]。

The digital twin is responsible for offline pre-optimization and parameter calibration of semantic policies, whereas the world model performs online adaptation by tracking end-to-end dynamics and continuously refining encoding, transmissions, and decoding.

数字孪生负责语义策略的离线预优化和参数校准，而世界模型通过跟踪端到端动态并持续优化编码、传输和解码来执行在线适应。

The two actors therefore operate in a complementary offline design and an online evolution loop.

因此两种机制在互补的离线设计和在线演化循环中运行。

The **digital twin, operating within semantic communication**, concentrates on noise-prone channels, priority-aware semantic priority and the stringent requirement for guaranteed recognition accuracy, thereby enabling offline pre-optimization and calibration of core transmission parameters [72].

**在语义通信中运行的数字孪生**专注于噪声信道、优先级感知语义优先级和保证识别精度的严格要求，从而实现核心传输参数的离线预优化和校准[72]。

By learning intrinsic semantic features and their interaction rules, the digital twin proactively simulates the suitability of candidate encoding or transmission schemes.

通过学习固有语义特征及其交互规则，数字孪生主动模拟候选编码或传输方案的适用性。

The digital twin tests the semantic-loss rate of a specific code under complex noise and measures the delivery delay of critical intent messages, then refines semantic recognition and reconstruction algorithms accordingly.

数字孪生测试特定编码在复杂噪声下的语义损失率，测量关键意图消息的传输延迟，然后相应地优化语义识别和重建算法。

Priority assignment is calibrated against latency budgets [72], while channel adaptation is tuned to counteract time-varying channel fading [73].

优先级分配根据延迟预算进行校准[72]，而信道适应被调整以对抗时变信道衰落[73]。

This targeted offline optimization intrinsically improves reliability and efficiency, mitigates semantic distortion or intent loss, and lays a stable foundation for deployment, especially in scenarios where business demands are static and semantic rules are well defined [74].

这种有针对性的离线优化本质上提高可靠性和效率，减轻语义失真或意图丢失，并为部署奠定稳定基础，特别是在业务需求静态且语义规则定义良好的场景中[74]。

The **world model focuses on the real-time capture of dynamic variations** along the entire semantic link. Without assuming preset channel parameters, it autonomously learns the latent relationship between semantic content, instantaneous channel state and user demand from massive live data and performs end-to-end optimization [75][76].

**世界模型专注于实时捕获**整个语义链路的动态变化。在不假设预设信道参数的情况下，它从大量实时数据中自主学习语义内容、即时信道状态和用户需求之间的潜关系，并执行端到端优化[75][76]。

The world model first compresses semantic data in the encoder to eliminate redundancy. It then adapts modulation and power during transmission to mitigate fading and, finally, corrects semantic distortion at the decoder to preserve the original intent.

世界模型首先在编码器中压缩语义数据以消除冗余。然后在传输过程中调整调制和功率以减轻衰落，最后在解码器中纠正语义失真以保留原始意图。

Its lightweight design enables its deployment on edge nodes, facilitating an efficient and robust cloud-edge-terminal architecture [77].

其轻量化设计使其能够部署在边缘节点上，促进高效稳健的云-边缘-终端架构[77]。

In the offline phase, the digital twin generates semantic priority tables, code modulation settings, and channel protection parameters [74]. During online operation, the world model dynamically updates these parameters to adapt to real-time noise, traffic, and resource conditions.

在离线阶段，数字孪生生成语义优先级表、编码调制设置和信道保护参数[74]。在在线运行期间，世界模型动态更新这些参数以适应实时噪声、流量和资源条件。

This interaction ensures that the end-to-end system maintains near-optimal performance automatically, thus delivering the intended information with stability and efficiency [75].

这种交互确保端到端系统自动维持近乎最优的性能，从而稳定高效地传递预期信息[75]。

Semantic communication empowered by world models provides a scalable and reliable architecture for next-generation intelligent networks.

由世界模型赋能的语义通信为下一代智能网络提供了可扩展且可靠的架构。

---

### C. Air-to-Ground Networks · 空对地网络

Air-to-Ground (A2G) networks integrate satellites, high-altitude platforms, and UAVs to form a three-dimensional space-air–ground (SAG) communication and computing architecture, providing fundamental support for wide-area connectivity, low-latency services, and edge intelligence.

空对地（A2G）网络整合卫星、高空平台和无人机，形成三维空-天-地（SAG）通信和计算架构，为广域连接、低延迟服务和边缘智能提供基础支持。

However, highly dynamic aerial topologies, heterogeneous network resources, and stringent ultra-low-latency requirements pose significant challenges to efficient resource allocation and task offloading [88].

然而，高度动态的空基拓扑、异构网络资源和严格的超低延迟要求对高效资源分配和任务卸载提出重大挑战[88]。

Digital twins focus on global modeling of the multi-layer air–space–ground network structure and resource constraints, enabling system-level optimization for cross-layer resource scheduling and task offloading.

数字孪生专注于多层空-天-地网络结构和资源约束的全局建模，支持跨层资源调度和任务卸载的系统级优化。

Digital twins support system-level resource management and computation offloading in A2G scenarios by constructing high-fidelity virtual replicas of SAG networks.

数字孪生通过构建SAG网络的高保真虚拟副本来支持A2G场景中的系统级资源管理和计算卸载。

Hevesli et al. [78] developed a digital twin-based framework for air–ground cooperation in the 6G industrial Internet of Things, where a virtual network replica is used for real-time state prediction.

Hevesli等人[78]开发了一个用于6G工业物联网空地协作的基于数字孪生的框架，其中使用虚拟网络副本来进行实时状态预测。

Gong et al. [79] proposed a SAG digital twin integrated blockchain architecture for air–space–ground heterogeneous networks, enabling centralized digital twins to perform global resource scheduling and ensure globally optimal task allocation.

Gong等人[79]为空-天-地异构网络提出了SAG数字孪生集成区块链架构，使集中式数字孪生能够执行全局资源调度并确保全局最优任务分配。

As local environment simulators for A2G edge nodes, world models emphasize the relationships between aerial agent actions and local link and airspace states, supporting short-term prediction under partial observability.

作为A2G边缘节点的本地环境模拟器，世界模型强调航空代理动作与本地链路和空域状态之间的关系，在部分可观测性下支持短期预测。

Zhang et al. [37] proposed an aerial network world model that encodes historical link states, flight trajectories, and control actions into compact latent representations, allowing path selection to be simulated in latent space.

Zhang等人[37]提出了一种航空网络世界模型，将历史链路状态、飞行轨迹和控制动作编码为紧凑潜态表征，允许在潜空间中模拟路径选择。

Lu et al. [81] integrate edge interaction data with aerial and satellite sensing information, enabling world models to learn action-conditioned spatial state evolution and perform predictive inference before link fluctuations occur, thereby reducing the dependence of aerial nodes on frequent synchronization with centralized controllers.

Lu等人[81]将边缘交互数据与航空和卫星感知信息集成，使世界模型能够学习动作条件化空间状态演化，并在链路波动发生前执行预测推理，从而减少航空节点对与集中控制器频繁同步的依赖。

Zhang et al. [89] propose an integrated air–ground edge–cloud framework that improves multi-modal AI inference under limited bandwidth and outperforms both cloud-only and edge-only schemes.

Zhang等人[89]提出了一种集成空-地边缘云框架，在有限带宽下改进多模态AI推理，性能优于纯云和纯边缘方案。

In A2G networks, digital twins and world models exhibit clear functional separation.

在A2G网络中，数字孪生和世界模型表现出明确的功能分离。

Digital twins act as **global operational mappings and planning centers** for A2G networks, addressing how the general system should be configured [80].

数字孪生作为A2G网络的**全局运营映射和规划中心**，解决总体系统应如何配置的问题[80]。

World models serve as **local cognition and decision engines** for aerial edge agents, determining which actions should be taken under current local airspace and link conditions.

世界模型作为航空边缘代理的**本地认知和决策引擎**，确定在当前本地空域和链路条件下应采取哪些动作。

Together, they form a **hierarchical optimization framework** that spans from system-level planning to link-level adaptive control.

共同形成从系统级规划到链路级自适应控制的**分层优化框架**。

---

### D. Low-Altitude Wireless Networks · 低空无线网络

Low-Altitude wireless networks (LAWNs) are composed of platforms such as UAVs and electric vertical take-Off and landing (eVTOLs), typically operating below an altitude of 3000 m.

低空无线网络（LAWN）由无人机和电动垂直起降（eVTOL）等平台组成，通常在3000米以下高度运行。

In these networks, highly unstructured environments, strong uncertainty, and strict computation and energy constraints on board make global planning and fast local response equally important [90].

在这些网络中，高度非结构化环境、强不确定性以及严格的机载计算和能源约束使全局规划和快速本地响应同等重要[90]。

Digital twins enable global awareness of aerial platform states by constructing high-fidelity virtual replicas of LAWNs and provide macroscopic guidance for large-scale resource scheduling.

数字孪生通过构建LAWN的高保真虚拟副本来实现航空平台状态的全局感知，并为大规模资源调度提供宏观指导。

World models act as **embodied cognition onboard aerial platforms**. Using imagination in latent space, they empower UAVs with real-time local control capabilities, such as obstacle avoidance, short-term channel prediction, and action refinement in complex environments [91].

世界模型作为**航空平台上的具身认知**。利用潜空间想象，它们赋予无人机实时本地控制能力，如障碍物规避、短期信道预测和复杂环境中的动作优化[91]。

The framework combines offline digital twin guidance with online world modeling in a hierarchical closed-loop architecture.

该框架在分层闭环架构中结合离线数字孪生指导和在线世界建模。

In LAWNs, constrained airspace, dense node deployment, and complex interference conditions motivate the use of digital twins for global situational awareness [82][83].

在LAWN中，受限空域、密集节点部署和复杂干扰条件促使使用数字孪生进行全局态势感知[82][83]。

By integrating virtual replicas of urban 3D models, building distributions, wireless propagation environments, and UAV operational states, digital twins support system-level optimization of UAV trajectory planning, task assignment, and resource scheduling.

通过集成城市3D模型、建筑物分布、无线传播环境和无人机运行状态的虚拟副本，数字孪生支持无人机轨迹规划、任务分配和资源调度的系统级优化。

Xie et al. [82] proposed a UAV application framework in which multiple tasks in the digital twin are coordinated by a task manager and interact with physical UAVs, enabling intelligent operation and management of real UAV networks.

Xie等人[82]提出了一个无人机应用框架，其中数字孪生中的多个任务由任务管理器协调并与物理无人机交互，实现真实无人机网络的智能运营和管理。

Wang et al. [83] developed a digital replica of aerial networks to jointly design power control, task partitioning, and computation resource allocation.

Wang等人[83]开发了航空网络的数字副本，以联合设计功率控制、任务划分和计算资源分配。

**World models act as local embodied decision-makers at the UAV edge.** They enable real-time prediction of channel dynamics and environmental disturbances to generate fine-grained control policies.

**世界模型作为无人机边缘的本地具身决策者。** 它们支持信道动态和环境干扰的实时预测，以生成细粒度控制策略。

Bar et al. [35] proposed a navigation world model based on the conditional diffusion transformer architecture, which predicts future visual observations conditioned on navigation actions, allowing UAVs to imagine flight trajectories in unfamiliar environments from a single input image and to perform online path planning under complex dynamic constraints.

Bar等人[35]提出了一种基于条件扩散Transformer架构的导航世界模型，它预测以导航动作为条件的未来视觉观测，使无人机能够从单张输入图像在陌生环境中想象飞行轨迹，并在复杂动态约束下执行在线路径规划。

For more challenging dynamic obstacle avoidance tasks, Diehl et al. [84] proposed the 4D occupancy flow world model, which estimates and decomposes scene occupancy flow from sparse laser radar observations, completes instance shapes, and predicts their temporal evolution.

对于更具挑战性的动态障碍物规避任务，Diehl等人[84]提出了4D占据流世界模型，从稀疏激光雷达观测中估计和分解场景占据流，完成实例形状并预测其时间演化。

This predictive capability enables UAVs to anticipate the motion of low-altitude objects and make sub-second safe avoidance decisions while maintaining communication link stability, without relying on frequent synchronization with centralized digital twins.

这种预测能力使无人机能够预见低空物体的运动，在保持通信链路稳定性的同时做出亚秒级安全规避决策，而无需依赖与集中式数字孪生的频繁同步。

In addition, reconfigurable intelligent surfaces (RIS) introduce extra degrees of freedom for signal reflection in LAWNs. By learning implicit mappings among position, phase configuration, and channel quality, world models support end-to-end policy optimization without explicitly constructing analytical channel models [85].

此外，可重构智能表面（RIS）在LAWN中引入了信号反射的额外自由度。通过学习位置、相位配置和信道质量之间的隐式映射，世界模型支持端到端策略优化，而无需显式构建分析信道模型[85]。

In practical LAWNs deployments, digital twins provide offline or quasi-online trajectory planning and resource configuration from a global network perspective, offering macroscopic guidance that defines task boundaries and long-term objectives.

在实际LAWN部署中，数字孪生从全局网络角度提供离线或准在线轨迹规划和资源配置，提供定义任务边界和长期目标的宏观指导。

World models operate onboard aerial nodes, generating real-time policies based on local perception and action feedback to dynamically adjust navigation maps and pre-defined trajectories [92].

世界模型在航空节点上运行，基于本地感知和动作反馈生成实时策略，动态调整导航地图和预定义轨迹[92]。

This collaborative architecture ensures both continuous network coverage and efficient resource utilization at the system level, while enabling edge nodes to autonomously adapt to transient environmental changes, forming a hierarchical control framework that combines global topology optimization with local link-level adaptation.

这种协作架构确保系统级的持续网络覆盖和高效资源利用，同时使边缘节点能够自主适应瞬态环境变化，形成将全局拓扑优化与本地链路级适应相结合的分层控制框架。

---

## V. OPEN RESOURCES PROJECT · 开放资源项目

*This section provides related open-source projects of digital twin, world model, and EGI across various fields.*

*本节提供数字孪生、世界模型和EGI在各个领域的相关开源项目。*

### A. Digital Twin Framework · 数字孪生框架

Digital twins have advanced in multiple dimensions, including generation, behavior modeling, robust tracking, platform support, and object reconstruction.

数字孪生在多个维度上取得了进展，包括生成、行为建模、鲁棒跟踪、平台支持和对象重建。

**Deep Learning Tools for Digital Twin Generation**: Deep learning has become a key tool for digital twin generation. FaceChain [93] is a deep learning framework to generate human portraits that preserve identity. It uses decoupled training and face-related perceptual understanding models to extract ID features, combined with Classifier-Free Guidance and models such as DamoFD [107] and M2FP [108]. The framework supports high-quality controllable portrait generation with custom style training and pose control, producing realistic outputs.

**用于数字孪生生成的深度学习工具**：深度学习已成为数字孪生生成的关键工具。FaceChain[93]是一个生成保持身份的人像的深度学习框架。它使用解耦训练和面部相关感知理解模型来提取ID特征，结合无分类器引导和DamoFD[107]及M2FP[108]等模型。该框架支持自定义风格训练和姿态控制的高质量可控人像生成，产出逼真结果。

**LLM-enhanced Digital Twin Frameworks**: Large language models provide new capabilities for building digital twins with personalized behaviors. PsyDT [94] is an LLM-based framework to build digital twins of psychological counselors with personalized styles. It uses dynamic one-shot learning to capture counselor linguistic patterns and therapy techniques, synthesizing multi-turn dialogues to fine-tune the model for personalized counseling behavior.

**LLM增强数字孪生框架**：大语言模型为构建具有个性化行为的数字孪生提供新能力。PsyDT[94]是一个基于LLM的框架，用于构建具有个性化风格的心理咨询师数字孪生。它使用动态一次性学习来捕获咨询师语言模式和治疗方法，综合多轮对话以微调模型实现个性化咨询行为。

**Robust Digital Twin Tracking**: Robust pose estimation under sensor noise is essential for reliable digital twin tracking in mobile environments. DTTDNet [95] addresses this problem by introducing a robust six-degrees-of-freedom (6DoF) pose estimation network for mobile environments. Built on a Transformer, it uses geometric feature filtering and Chamfer Distance loss to enhance robustness to depth noise. Experiments on DTTD-Mobile show that DTTDNet achieves 60.74 on the ADD metric, outperforming existing methods by at least 4.32, and remaining stable across noise levels.

**鲁棒数字孪生跟踪**：传感器噪声下的鲁棒姿态估计对于移动环境中可靠的数字孪生跟踪至关重要。DTTDNet[95]通过引入用于移动环境的鲁棒六自由度（6DoF）姿态估计网络来解决此问题。它构建在Transformer之上，使用几何特征过滤和Chamfer距离损失来增强对深度噪声的鲁棒性。DTTD-Mobile上的实验表明，DTTDNet在ADD指标上达到60.74，比现有方法至少高出4.32，且在噪声水平上保持稳定。

**Composable and Reusable Digital Twin Platform**: Platform-based solutions reduce complexity and enhance reusability in digital twin systems. DTaaS [96] offers a composable platform that centrally manages assets—models, data, functions, and tools—and supports building digital twins as services, integrating storage, computing, communication, monitoring, and task execution.

**可组合和可重用数字孪生平台**：基于平台的解决方案降低了数字孪生系统的复杂性并增强了可重用性。DTaaS[96]提供了一个可组合平台，集中管理资产——模型、数据、功能和工具——并支持将数字孪生构建为服务，集成存储、计算、通信、监控和任务执行。

**Digital Twins for Articulated Object Reconstruction**: Recent studies have explored digital twins to model the structure and motion of articulated objects. Ditto [97] constructs digital twins of real-world articulated objects through interactive perception. Using visual observations before and after interaction, it reconstructs part-level geometry and estimates articulation models with implicit neural representations. The method is category-agnostic and supports real-world reconstruction and physical simulation.

**用于铰接对象重建的数字孪生**：近期研究探索了用数字孪生建模铰接对象的结构和运动。Ditto[97]通过交互感知构建真实世界铰接对象的数字孪生。它利用交互前后视觉观测重建零件级几何，并使用隐式神经表征估计铰接模型。该方法与类别无关，支持真实世界重建和物理模拟。

These works demonstrate advances in digital twins across generation, personalized behavior, robust tracking, platform-based management, and modeling of complex objects. They improve the accuracy, controllability, and reusability of digital twins, supporting the application of EGI in perception, reasoning, and autonomous decision-making.

这些工作展示了数字孪生在生成、个性化行为、鲁棒跟踪、平台管理和复杂对象建模方面的进展。它们提高了数字孪生的准确性、可控性和可重用性，支持EGI在感知、推理和自主决策中的应用。

---

### B. World Model Framework · 世界模型框架

World models provide a framework for representing and predicting complex environments. They combine multimodal perception, decision-making, planning, and simulation capabilities. These models help agents act and learn efficiently across long tasks, high-dimensional spaces, and multiple domains, supporting applications in AI and robotics.

世界模型为表征和预测复杂环境提供了框架。它们结合多模态感知、决策、规划和模拟能力。这些模型帮助代理在长时任务、高维空间和多个领域中高效行动和学习，支持AI和机器人应用。

**LLM-enhanced World Model Frameworks**: Multimodal models with extended context have shown significant progress in recent years. Building on these advances, LWM [98] enables cross-modal understanding and generation of text, images, and videos while handling long-context inputs. It excels in long-text retrieval, long-video understanding, and text-to-image/video tasks, while retaining short-context capabilities and providing an open-source training pipeline.

**LLM增强世界模型框架**：具有扩展上下文的多模态模型近年来取得了重大进展。在此基础上，LWM[98]在处理长上下文输入的同时实现文本、图像和视频的跨模态理解和生成。它在长文本检索、长视频理解和文本转图像/视频任务方面表现出色，同时保持短上下文能力并提供开源训练管道。

**World Model-Driven RL for Multi-Domain Tasks**: General-purpose reinforcement learning (RL) has advanced rapidly. DreamerV3 [27] is a world model-based algorithm with robustness techniques such as normalization, Kullback-Leibler (KL) divergence balancing, and sym-log/symexp transformations. It adapts to 150+ tasks across eight domains without tuning, learns efficiently via unsupervised reconstruction and actor–critic methods, outperforms PPO and MuZero [109] algorithms on benchmarks, and offers flexible model size and replay ratio for practical cross-domain use.

**世界模型驱动的多领域任务强化学习**：通用强化学习（RL）发展迅速。DreamerV3[27]是一个基于世界模型的算法，具有归一化、KL散度平衡和sym-log/symexp变换等鲁棒性技术。它无需调优即可适应八个领域的150多项任务，通过无监督重建和演员-评论家方法高效学习，在基准测试中优于PPO和MuZero[109]算法，并为实际跨领域使用提供灵活模型大小和回放比率。

**Cross-Domain Applications of World Models**: Interactive simulation platforms have advanced rapidly with video generation and world modeling. LingBot-World [99] provides an open-source platform for multi-domain simulations. It integrates a hierarchical semantic engine, multi-stage training, and mixture-of-experts (MoE) architecture to deliver high-fidelity, long-term, low-latency environments, supporting prompt-driven events, agent training, and 3D reconstruction.

**世界模型的跨领域应用**：交互式仿真平台随着视频生成和世界建模快速发展。LingBot-World[99]为多领域模拟提供了一个开源平台。它集成分层语义引擎、多阶段训练和专家混合（MoE）架构，提供高保真、长期、低延迟环境，支持提示驱动事件、代理训练和3D重建。

**Visual and Long-Horizon World Models**: Recent RL research has focused on world model-driven approaches for sample-efficient learning. IRIS [100] builds a world model with a discrete autoencoder and autoregressive Transformer for learning in imagination. Trained on simulated trajectories with real data, it performs pixel-level prediction, reward and termination estimation, adapts to complex visual environments, and outperforms humans in Atari 100k games.

**视觉和长期世界模型**：近期RL研究聚焦于世界模型驱动的方法以实现样本高效学习。IRIS[100]构建了具有离散自编码器和自回归Transformer的世界模型，用于在想象中学习。它在使用真实数据训练的模拟轨迹上执行像素级预测、奖励和终止估计，适应复杂视觉环境，并在Atari 100k游戏中超越人类。

**Efficient Robot Learning with World Models**: Efficient robot learning depends on scalable data and robust task generalization. GigaBrain-0 [101] uses data generated by world models to build a vision-language-action (VLA) foundation model, reducing the reliance on real robot data. With RGB-depth-map (RGBD) modeling and embodied chain-of-thought supervision, it reasons about geometry, object states, and long-horizon dependencies, achieving robust performance in dexterous and mobile tasks.

**使用世界模型的高效机器人学习**：高效机器人学习依赖于可扩展数据和鲁棒任务泛化。GigaBrain-0[101]使用世界模型生成的数据来构建视觉-语言-动作（VLA）基础模型，减少对真实机器人数据的依赖。结合RGBD建模和具身思维链监督，它对几何、物体状态和长期依赖进行推理，在灵巧和移动任务中实现鲁棒性能。

These studies highlight the role of world models in supporting EGI. By enabling reasoning, planning, simulation, and robot learning, they improve efficiency and generalization, supporting robust perception, decision-making, and autonomous action in complex, multi-domain environments.

这些研究强调了世界模型在支持EGI中的作用。通过实现推理、规划、模拟和机器人学习，它们提高效率和泛化，支持在复杂多域环境中的鲁棒感知、决策和自主行动。

---

### C. Edge Artificial Intelligence Framework · 边缘人工智能框架

EGI faces the challenge of efficient, personalized learning and inference across distributed heterogeneous devices. Integrating world models, personalized federated learning, resource-aware scheduling, and knowledge distillation improves efficiency, generalization, and supports diverse intelligent applications.

EGI面临在分布式异构设备上高效个性化学习和推理的挑战。集成世界模型、个性化联邦学习、资源感知调度和知识蒸馏提高了效率、泛化能力，并支持多样化智能应用。

**EGI with Communication-Efficient Federated Learning**: Reducing communication and enabling personalization are critical for federated learning on edge devices. LotteryFL [102] uses the Lottery Ticket hypothesis to train and transmit client-specific subnetworks, lowering communication overhead while supporting personalized models. Experiments on non-IID datasets show improved accuracy and efficiency, with real-time deployment demonstrated on edge devices.

**通信高效联邦学习的EGI**：减少通信和实现个性化对于边缘设备上的联邦学习至关重要。LotteryFL[102]使用彩票假设来训练和传输客户端特定子网络，降低通信开销同时支持个性化模型。非IID数据集上的实验显示精度和效率提升，边缘设备上已演示实时部署。

**Resource-Aware EGI Frameworks**: EGI applications require low latency and high energy efficiency. Neurosurgeon [103] uses layer-level neural network partitioning to coordinate edge and cloud computing resources. The framework predicts performance and dynamically adapts to hardware, architecture, and network conditions, achieving improved efficiency and throughput.

**资源感知EGI框架**：EGI应用需要低延迟和高能效。Neurosurgeon[103]使用层级别神经网络分区来协调边缘和云计算资源。该框架预测性能并动态适应硬件、架构和网络条件，实现效率和吞吐量的改进。

**Communication-Efficient FL for EGI**: Efficient and personalized learning is critical for edge devices. FedCache [104] uses a knowledge cache on the server to provide relevant information to client models and applies ensemble distillation. The framework supports heterogeneous devices and asynchronous interactions, achieving significant communication efficiency gains while maintaining performance comparable to state-of-the-art methods.

**EGI通信高效联邦学习**：高效和个性化学习对边缘设备至关重要。FedCache[104]在服务器上使用知识缓存向客户端模型提供相关信息，并应用集成蒸馏。该框架支持异构设备和异步交互，在保持与最先进方法相当的性能的同时实现显著的通信效率提升。

**Balancing Model Drift and Inference in EGI**: Managing computation and maintaining accuracy are key to practical edge intelligence. ORRIC [105] models resource competition between retraining and inference and dynamically adapts resource allocation. It improves long-term inference accuracy while balancing drift-related losses and optimizing computational resources and latency.

**EGI中平衡模型漂移和推理**：管理计算和保持精度是实际边缘智能的关键。ORRIC[105]对再训练和推理之间的资源竞争建模，并动态适应资源分配。它在平衡漂移相关损失和优化计算资源与延迟的同时提高长期推理精度。

**Self-Distilled FL for Edge Devices**: Edge computing applications require efficient and personalized model training. pFedSD [106] is a personalized federated learning framework for edge computing. It uses self-knowledge distillation to retain client historical models and guide local training, improving personalization and convergence while supporting non-IID data, heterogeneous models, and preserving privacy with low system overhead.

**用于边缘设备的自蒸馏联邦学习**：边缘计算应用需要高效个性化的模型训练。pFedSD[106]是用于边缘计算的个性化联邦学习框架。它使用自知识蒸馏来保留客户端历史模型并指导本地训练，在支持非IID数据、异构模型和保持隐私的同时以低系统开销提高个性化和收敛性。

These studies highlight the importance of communication-efficient, resource-aware, and personalized strategies in edge environments. By reducing overhead, managing model drift, optimizing inference, and supporting diverse devices, they provide a solid basis for efficient and reliable EGI systems.

这些研究强调了通信高效、资源感知和个性化策略在边缘环境中的重要性。通过减少开销、管理模型漂移、优化推理和支持多样化设备，它们为高效可靠的EGI系统提供了坚实基础。

---

## VI. FUTURE DIRECTIONS · 未来方向

Advancing world models for EGI requires realism, adaptability, and efficiency in dynamic and constrained environments. Edge systems need models that combine physical knowledge with data-driven learning, support continual adaptation, and operate at different spatial and temporal scales.

推进用于EGI的世界模型需要在动态和受限环境中实现逼真性、适应性和效率。边缘系统需要结合物理知识与数据驱动学习、支持持续适应并在不同时空尺度上运行的模型。

### A. Hybrid Physics-Driven and Data-Driven World Models · 混合物理驱动与数据驱动世界模型

Future work should investigate hybrid architectures that combine explicit physical knowledge (e.g., radio propagation models, mobility laws, power constraints) with learned latent dynamics.

未来工作应研究将显式物理知识（如无线电传播模型、移动性规律、功率约束）与学习到的潜动态相结合的混合架构。

Purely data-driven world models often struggle with extrapolation under sparse, non-stationary, or shifted data, and their generalization and scalability in complex real-world robotic scenarios remain in question [110].

纯数据驱动的世界模型在稀疏、非平稳或偏移数据下的外推方面往往遇到困难，且其在复杂真实机器人场景中的泛化性和可扩展性仍存疑问[110]。

In contrast, purely physics-based digital twins can be brittle and computationally expensive.

相比之下，纯基于物理的数字孪生可能脆弱且计算昂贵。

Promising directions include physics-informed latent spaces, generative models regularized by conservation laws [111], and differentiable simulators coupled with neural world models.

有前景的方向包括物理约束潜空间、受守恒定律正则化的生成模型[111]，以及与神经世界模型耦合的可微分模拟器。

For EGI, such hybrid designs can improve robustness and interpretability while remaining lightweight enough for deployment at the edge.

对于EGI，这种混合设计可以提高鲁棒性和可解释性，同时保持足够轻量以部署在边缘。

### B. Federated World Modeling at the Edge · 边缘联合世界建模

EGI requires world models that evolve as environments, traffic patterns, and hardware conditions change.

EGI需要随环境、流量模式和硬件条件变化而演进的世界模型。

Future research should address continual and lifelong learning of world models under strict resource and privacy constraints, so that intelligent systems can retain existing knowledge while continuously acquiring and integrating new information [112].

未来研究应解决在严格资源和隐私约束下世界模型的持续和终身学习，使智能系统能够在持续获取和整合新信息的同时保留现有知识[112]。

This includes mechanisms for online adaptation without catastrophic forgetting, efficient model versioning across heterogeneous edge nodes, and federated learning protocols tailored to world-model training (e.g., regularizing latent dynamics to improve agent behavior [113]).

这包括无灾难性遗忘的在线适应机制、跨异构边缘节点的高效模型版本控制，以及专为世界模型训练定制的联邦学习协议（如正则化潜动态以改进代理行为[113]）。

Handling non-IID data, enabling communication-efficient aggregation, and supporting privacy-preserving updates will be central challenges.

处理非IID数据、实现通信高效聚合和支持隐私保护更新将是核心挑战。

### C. Multi-Agent and Multi-Scale World Models · 多代理和多尺度世界模型

Edge scenarios such as 6G, air-to-ground networks, and low-altitude operations inherently involve many interacting agents (devices, base stations, UAVs, vehicles) evolving across multiple temporal and spatial scales.

6G、空对地网络和低空运营等边缘场景本质上涉及许多跨多个时间和空间尺度演化的交互代理（设备、基站、无人机、车辆）。

Future research should explore world models that capture multi-agent interactions (e.g., via graph-structured agent-level interaction modules [114]) and multi-scale processes (fast wireless-channel fluctuations vs. slower mobility and traffic patterns).

未来研究应探索捕获多代理交互（如通过图结构代理级交互模块[114]）和多尺度过程（快速无线信道波动与较慢移动性和流量模式）的世界模型。

Agent-centric models with interactive perception capabilities can support decentralized collaboration among distributed edge nodes, enable predicting emergent behaviors, and facilitate cooperative planning.

具有交互感知能力的以代理为中心模型可以支持分布式边缘节点间的去中心化协作，实现对涌现行为的预测，并促进协作规划。

Decentralized agents may form collusion through covert communication [115], highlighting the need to move beyond single-agent, local-view world models and to develop mechanisms for effective decentralized planning.

去中心化代理可能通过隐蔽通信形成共谋[115]，这凸显了需要超越单代理局部视角世界模型，并开发有效去中心化规划的机制。

### D. Explainable and Trustworthy World Models · 可解释可信世界模型

As EGI systems are deployed in high-stakes environments, it is crucial that their decisions are understandable, reliable, and trustworthy.

随着EGI系统部署在高风险环境中，其决策可理解、可靠和可信至关重要。

Current world models, often based on deep neural networks, tend to act as black boxes, making failures difficult to interpret and diagnose [116].

当前世界模型通常基于深度神经网络，往往作为黑箱运行，使故障难以解释和诊断[116]。

A key research direction is the development of explainable artificial intelligence (XAI) techniques tailored to world models. Potential approaches include methods to visualize the model's imagined futures, to identify which environmental features are most influential for its predictions, and to quantify uncertainty in its forecasts.

关键研究方向是开发专为世界模型定制的可解释人工智能（XAI）技术。潜在方法包括可视化模型想象未来的方法，识别对其预测影响最大的环境特征，以及量化其预测中的不确定性。

Building trust also requires mechanisms to detect out-of-distribution conditions and to decide when the world model should not be used for planning, as such detection is a key component of trusted machine learning systems [117] and enables graceful degradation, conservative fallback strategies, or safe human or rule-based intervention.

建立信任还需要检测分布外条件和决定何时不应使用世界模型进行规划的机制，因为这种检测是可信机器学习系统的关键组成部分[117]，并支持优雅降级、保守回退策略或安全的人工或基于规则的干预。

---

## VII. CONCLUSION · 结论

This survey has outlined a unified perspective on the transition from digital twins to world models for EGI.

本综述概述了从数字孪生到EGI世界模型的统一视角。

Digital twins remain indispensable for high-fidelity engineering analysis, lifecycle management, and system-level optimization.

数字孪生在工程高保真分析、生命周期管理和系统级优化方面仍然不可或缺。

However, their reliance on explicit modeling, centralized computation, and continuous synchronization limits their suitability for autonomous and real-time operations at the edge.

然而，它们对显式建模、集中计算和持续同步的依赖限制了其在边缘自主和实时运行中的适用性。

World models address these limitations by learning compact, action-conditioned representations of the environment and by enabling imagination-based planning and self-supervised adaptation.

世界模型通过学习紧凑、动作条件化的环境表征以及实现基于想象的规划和自监督适应来应对这些限制。

This survey has reviewed core architectures and algorithms for world models, their coupling with communication, sensing, and control, and their emerging role in future wireless networks and cyber–physical systems.

本综述综述了世界模型的核心架构和算法、其与通信、感知和控制的耦合，以及它们在未来无线网络和信息物理系统中的新兴角色。

We have also highlighted open issues, including hybrid physics–data integration, federated and continual world modeling under non-IID edge data, multi-agent and multi-scale modeling, as well as safety, explainability, and standardization.

我们还强调了开放问题，包括混合物理-数据集成、在非IID边缘数据下的联邦和持续世界建模、多代理和多尺度建模，以及安全性、可解释性和标准化。

These challenges define a rich research agenda for the coming years.

这些挑战为未来数年定义了丰富的研究议程。

Thus, the synergistic use of digital twins and world models is expected to provide a key technological pillar for robust, efficient, and intelligent edge systems in 6G and beyond.

因此，数字孪生和世界模型的协同使用有望为6G及更高版本中稳健、高效和智能的边缘系统提供关键技术支柱。

---

*本文参考来源：*
*[1] H. Chen et al., "Towards edge general intelligence via large language models," IEEE Network, 2025.*
*[其余参考文献见原文]*
