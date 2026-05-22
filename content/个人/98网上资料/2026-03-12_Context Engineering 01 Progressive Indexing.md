---
title: "Context Engineering 01: Progressive Indexing"
author: "TRAE (@Trae_ai)"
date: 2026-03-12 11:54
source: "https://x.com/Trae_ai/status/2032062710939320559"
tags:
  - twitter
  - article
---

# Context Engineering 01: Progressive Indexing

**作者**: TRAE (@Trae_ai)
**时间**: 2026-03-12 11:54
**来源**: [原始链接](https://x.com/Trae_ai/status/2032062710939320559)

---

Context Engineering 01: Progressive Indexing

In the era of AI coding, model capabilities are rapidly converging. The true differentiator is no longer which model you use, but how well you engineer its context.

Just as a human developer must understand the business background, technical architecture, and historical design decisions to produce high-quality code, an AI Agent depends equally on well-curated context to generate code that aligns with real-world enterprise requirements.

Context Engineering is not simply a matter of "throwing code at the AI." It is a systematic discipline encompassing how to identify critical information, how to structurally organize project-level and module-level context, how to precisely deliver the most relevant information within a finite token window, and how to continuously refine that context as the project evolves.

In the following sections, we explore how the introduction of Progressive Indexing addresses this challenge. This design avoids context window overflow and information noise: the key lies not in relying on ever-larger context windows, but in mastering the right patterns of human–AI collaboration.

## 1. Why Is Business Context Management Necessary?

In complex software projects, the codebase alone often fails to encapsulate the entirety of business logic. A significant portion of critical business semantics, constraints, and decision rationale resides outside the code, scattered across various artifacts. This creates an information gap.

Without effective management of this "business context," AI Agents face formidable challenges when attempting to comprehend and implement requirements.

The pain points manifest in the following areas:

1. Code Cannot Fully Express Business Semantics

Many business rules are not implemented through explicit code logic but are instead driven by configuration. This implicit association is virtually impossible for a code-reading Agent to discover independently.

Consequently, the Agent may "reinvent" an erroneous implementation simply because it is unaware of the existing logic.

2. The Information Gap from PRD to TRD

Product Requirements Documents (PRDs) focus on "what to build," while Technical Design Documents (TRDs) focus on "how to build it." Between the two lies a substantial cognitive gap.

Engineers must draw upon their understanding of system architecture, legacy constraints, and the technology stack to translate a PRD into an actionable technical design. Without this "default knowledge" as input, an Agent similarly struggles to independently bridge the gap from requirements to a technical solution.

3. The Absence of Tacit Knowledge

Within any engineering team, there exists a wealth of implicit and commonly understood rules: architectural boundaries, module responsibilities, naming conventions, and unwritten agreements.

This tacit knowledge is rarely reiterated explicitly during each development cycle, yet it is essential for ensuring collaboration efficiency and code quality.

Therefore, to enable AI coding tools like TRAE to participate more effectively and accurately in technical design and development, it is essential to provide it with a mechanism for systematically and structurally understanding and leveraging this business context.

## 2. Why Introduce Progressive Indexing?


Having established the importance of providing business context, an intuitive approach would be to feed all relevant documentation (e.g., Wikis, TRDs, architecture diagrams) directly to the Agent.

While this brute-force strategy is straightforward, it quickly encounters several bottlenecks:

- Context Window Limitations: LLMs operate within finite context windows. As project documentation grows, loading all content at once inevitably leads to token overflow, rendering the task unexecutable.
- Prohibitive Cost and Latency: The inclusion of vast amounts of irrelevant information significantly increases token consumption, leading to higher costs and longer response times, ultimately diminishing development efficiency.
- Information Noise: Excessive information introduces noise that impairs the Agent's judgment. The model must search for information in a large number of unrelated content, which paradoxically may cause it to miss the core points, resulting in designs that deviate from expectations.

To address these challenges, we drew inspiration from the Progressive Disclosure philosophy employed by Anthropic Skills and designed a Progressive Indexing mechanism.

The core principle is "load on demand, read in layers." Rather than flooding the context with all available information, the Agent is guided to begin with a lightweight "table of contents" and then precisely locate and retrieve only the most relevant information based on the task at hand.

This approach ensures that the Agent can access the necessary business knowledge while maximizing the conservation of context resources, striking an optimal balance between efficiency and effectiveness.

## 3. How to Generate and Organize the Index?


The implementation of progressive indexing relies on a standardized document structure and a set of governing rules. It organizes business context into two distinct layers: Metadata and Content.

### 1. Two-Layer Structure: Metadata + Content

Each standalone business logic document (e.g., <model-config-context.md>) comprises two components:

Layer 1: Metadata (YAML Frontmatter)

Located at the top of each markdown file as a YAML snippet, the metadata contains only two core fields:

- <name>: A unique identifier for the business logic, using lowercase letters, numbers, and hyphens.
- <description>: A concise summary of the document's core content and applicable scenarios, enabling the Agent to determine when it needs to read the document.

The key advantage of metadata is its extremely lightweight nature, incurring minimal loading cost. The Agent can preload the metadata of all business documents at startup, thereby gaining a comprehensive overview of the project's available knowledge base.

Layer 2: Content (Markdown Body)

The main body following the YAML frontmatter uses markdown to provide detailed elaboration of specific business logic, code locations, design decisions, and important considerations.

This content is only read on demand when the Agent determines, based on the user's request and the metadata, that the document is relevant. This significantly reduces the token overhead per request.

Example YAML:
---
name: model-version-modes
description: "Defines how server matches IDE versionCode and plugin versionRule to select effective app/function configs; read when adding version-gated configs or debugging config not taking effect."
---

# v2 and Max Model Determination Rules

## Determination Objectives
- Given an IDEFunctionConfig or its DetailConfigItem, determine whether it is a v2 model or a Max model
- Used for consistent display and behavioral control across front-end and back-end (prompts, context length, interaction flow)

## v2 Determination Signals
- Model layer (any match triggers v2 classification): - DetailConfigItem.ModelName contains __v2

## Max Determination Signals
- Display layer - IDEFunctionConfig.DisplayConfig.MaxMode == true
- Model layer (any match triggers Max classification): - DetailConfigItem.ModelName contains __max

### 2. <project_rules.md> as the Index Manifest

To enable the Agent to discover and utilize these business documents, we introduce a dedicated XML block, <available_business_logic>, within the project's <.TRAE/project_rules.md>.

This XML block serves as the index manifest for all available business documents. It consists of multiple <business_logic> entries, each containing the name, description, and other metadata extracted from the corresponding document's YAML frontmatter, along with a <location> tag pointing to the file's physical path.

### 3. Maintenance Strategy

This index manifest can be automatically generated and updated via a script. The script traverses all .md files within the <.TRAE/business-logic/>, parses their YAML frontmatter, and consolidates the metadata along with file paths into the <available_business_logic> block in <project_rules.md>.

Through this approach, we achieve automation and standardization of business context management. Developers need only create or update business logic documents according to the prescribed format, and the index manifest will remain synchronized automatically.


## 4. How to Utilize Business Context in TRAE?


With the progressive indexing mechanism in place, we can guide TRAE to efficiently leverage this context during routine tasks such as technical design and TRD generation. The Builder Mode in TRAE, with its robust instruction-following capabilities, is particularly well-suited for this scenario.

The typical workflow:

1. Startup and Index Loading

When the TRAE Agent begins processing a new request, it first loads the contents of <.TRAE/project_rules.md>. At this point, the metadata (<name> and <description>) of all business documents within the <available_business_logic> block enters the Agent's context, providing it with a global overview of the project's documented business knowledge.

2. Requirement Analysis and Index Matching

When a user submits a requirement (e.g., "I need to support Max mode billing in the B2B scenario"), the Agent analyzes the keywords within the request (such as "B2B," "Max mode," "billing") and cross-references them against the description of all business documents held in memory.

If a document's description demonstrates high relevance to the requirement, the Agent flags it as a document to be retrieved.

3. On-Demand Retrieval of Detailed Content

After identifying the relevant business documents, the Agent uses the read tool, referencing the <location> path from the index manifest, to retrieve the full content of these documents.

At this stage, the detailed business logic, code locations, and important considerations are fully loaded into the context.

4. Context-Informed Solution Generation

Armed with comprehensive business knowledge, the Agent proceeds to generate the technical design (TRD).

Since it has already internalized key insights such as how to determine Max mode and where the B2B billing pipeline entry point is located, the resulting design is far more grounded in reality, avoiding speculative or uninformed proposals.

5. Citation and Validation

Within the TRD, the Agent explicitly cites the business documents it referenced and bases its design on the information contained therein.

For example, it specifies the exact files and code locations that require modification, or recommends where to add new fields within a configuration structure, rather than producing a vague, non-actionable proposal.

Through this workflow, TRAE transcends the role of a tool that blindly reads code. It becomes an intelligent assistant capable of proactively consulting, comprehending, and applying accumulated institutional knowledge, thereby delivering substantially greater value in the context of complex software projects.

Follow TRAE on X for the latest news and visit trae.ai to experience the future of coding today.

---

## 图片

![Image 1](https://pbs.twimg.com/media/HDMz0xBaAAA_Zzc?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HDM0TxDbIAAcG-0?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HDNTzxta4AANbYM?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HDNQLRybQAUUvYD?format=jpg&name=medium)

![Image 5](https://pbs.twimg.com/media/HDNSAYtaIAAnWza?format=jpg&name=medium)

![Image 6](https://pbs.twimg.com/media/HDNSKGtbQAA8o5N?format=png&name=medium)

![Image 7](https://pbs.twimg.com/media/HDNRuP0bQAAGMyT?format=png&name=large)

