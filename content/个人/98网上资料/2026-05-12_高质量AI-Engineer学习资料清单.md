#AI-Engineer #学习资料 #Evals #成本归因 #Agent-Guardrails #可观测性 #模型路由 #微调

**高质量 AI Engineer 学习资料清单**

> 来源：微信推文，共 11 部分。**第 6-11 部分已补全**（本文档完整收录全 11 部分）。

---

## 第一部分：Harness Engineering（不只是 Prompt Engineering）

### 1-1. Martin Fowler - Harness Engineering for Coding Agents
**链接**：https://martinfowler.com/articles/harness-engineering-for-coding-agents.html
**备注**：⚠️ 原链接 404（2026-05-12 访问时失效），可能是 URL 变更或已下架。

### 1-2. Anthropic - Building Effective AI Agents ⭐ 全文已抓取
**链接**：https://www.anthropic.com/research/building-effective-agents
**作者**：Anthropic 工程团队 | **发布日期**：2024-12-19

**一句话核心**：最成功的 Agent 实现用的是**简单、可组合的模式**，而非复杂框架。

#### 核心结论
1. **能用简单方案就不上 Agent**：先用 single LLM call + retrieval + few-shot examples，大多数场景够用
2. **框架是双刃剑**：简化入门门槛，但引入额外抽象层，掩盖底层 prompt/response，使调试变难
3. **直接从 LLM API 入手**：很多模式只需几行代码实现。如果用框架，必须理解底层代码
4. **Model Context Protocol (MCP)**：Anthropic 发布的标准化协议，通过简单客户端实现集成第三方工具生态

#### Workflow vs. Agent 的本质区别

| | Workflow | Agent |
|---|---|---|
| 控制方式 | 预定义固定步骤组合 | 模型自主驱动决策 |
| 透明度 | 步骤可预测、可审计 | 灵活性高但不够透明 |
| 适用场景 | 确定性任务、可枚举步骤 | 灵活性要求高、长周期任务 |
| 延迟/成本 | 相对低 | 相对高（换更好效果）|

#### 七大构建模式（从简单到复杂）

1. **Augmented LLM（增强型 LLM）**：LLM + retrieval + tools + memory，模型**主动**使用这些能力
2. **Prompt Chaining**：有序步骤序列，每步输出作为下一步输入，可加 gate 检查
3. **Routing**：对输入分类，导向专门的后续处理分支
4. **Parallelization**：Sectioning（分解子任务并行）+ Voting（多策略备选）
5. **Orchestrator-Workers**：中央编排者动态决定执行路径，非预定义分支
6. **Evaluator-Optimizer**：一个 LLM 生成，另一个评估反馈，迭代直到满意
7. **Agents**：长期自主运行，核心循环：观察 → 推理 → 行动 → 循环

> "Incorrect assumptions about what's under the hood are a common source of customer error."

---

## 第二部分：Prompt Caching vs. Semantic Caching 对比

### 2-1. OpenAI - Prompt Caching 官方文档
**链接**：https://developers.openai.com/api/docs/guides/prompt-caching

### 2-2. Anthropic - Prompt Caching 官方文档
**链接**：https://platform.claude.com/docs/en/build-with-optimized-responses/prompt-caching

### 2-3. Redis - Prompt Caching vs. Semantic Caching ✅ 已抓取
**链接**：https://redis.io/blog/prompt-caching-vs-semantic-caching/

**两种缓存策略对比**：

| | Prompt Caching | Semantic Caching |
|---|---|---|
| 机制 | Provider 端缓存固定前缀上下文 | 基于 embedding 相似度判断复用 |
| 适用场景 | 固定高成本前缀（system prompt、工具定义）| 语义相近的问题（跨用户请求复用）|
| 优点 | 显著降低 TTFT 和总体成本 | 雷同问题可跨用户命中 |
| 限制 | 仅缓存前缀，动态用户消息无法复用 | 错误命中风险，需评估收益 |

**生产系统推荐**：两者结合——Prompt caching 处理固定前缀，Semantic caching 处理动态用户查询。

### 2-4. GPTCache - Semantic Cache 论文（PDF）
**链接**：https://aclanthology.org/2023.nlposs-1.17.pdf

---

## 第三部分：KV Cache 管理

### 3-1. vLLM / PagedAttention 论文
**链接**：https://arxiv.org/pdf/2309.06180

### 3-2. vLLM Automatic Prefix Caching 实现文档
**链接**：https://docs.vllm.ai/en/v0.6.1/automatic_prefix_caching/

### 3-3. LMCache 技术报告
**链接**：https://lmcache.ai/tech_report.pdf

### 3-4. YouTube - Fast LLM Serving with vLLM and PagedAttention
**链接**：https://www.youtube.com/watch?v=5ZlavK-a9Nnk

---

## 第四部分：Speculative Decoding vs. Quantization

### 4-1. Speculative Decoding 经典论文
**链接**：https://arxiv.org/pdf/2211.17192

### 4-2. QLoRA 论文
**链接**：https://openreview.net/pdf?id=OUIFPHEOeh

### 4-3. QSPEC - Speculative Decoding + Complementary Quantization
**链接**：https://aclanthology.org/2025.emnlp-main.241.pdf

### 4-4. Google Cloud - Five Techniques for LLM Inference ✅ 已抓取
**链接**：https://cloud.google.com/blog/topics/developers-suite/five-techniques-llm-inference/

**五大推理优化技术**：

1. **Continuous Batching**：动态 batching，不同请求共享 GPU 资源，显著提升吞吐量
2. **PagedAttention (vLLM)**：KV cache 分块管理，减少内存碎片，支持更大并发
3. **Speculative Decoding**：小模型快速 draft token，大模型并行验证，加速生成
4. **Quantization**：INT8/INT4 量化降低显存占用，配合 QLoRA 等微调方案
5. **Smart Routing**：根据请求特征动态选择合适的模型和硬件

### 4-5. YouTube - Speculative Decoding 入门
**链接**：https://www.youtube.com/watch?v=VkWlLSYQS0I

---

## 第五部分：Structured Output 与 Fallback Chains

### 5-1. OpenAI - Structured Outputs 官方文档
**链接**：https://developers.openai.com/api/docs/guides/structured-outputs

### 5-2. OpenAI - Introducing Structured Outputs in the API
**链接**：https://openai.com/index/introducing-structured-outputs-in-the-api/

### 5-3. Instructor - Structured LLM Outputs + Validation
**链接**：https://python.useinstructor.com
**核心**：基于 Pydantic schema 定义输出结构，Validation failure 后自动 retry / re-ask

### 5-4. Pydantic AI - Output Validation
**链接**：https://pydantic.dev/docs/ai/core-concepts
**核心**：应用层 validation + Retry budget 机制，模型原生 structured output 的应用层保险

### 5-5. Guardrails AI
**链接**：https://www.guardrailsai.com/guardrails/docs
**核心**：raw output → validated output 作为系统状态处理，Validation success/failure 流程控制

### 5-6. YouTube - Validate & Standardize LLM Output with Guardrails-AI
**链接**：https://www.youtube.com/watch?v=r3JdQxM5lpI

---

## 第六部分：Evals——LLM-as-Judge + Human Evals ⭐ Hamel Husain 全文已抓取

### 6-1. OpenAI - Evaluation Best Practices
**链接**：https://developers.openai.com/api/docs/guides/evaluation-best-practices

### 6-2. OpenAI Cookbook - Getting Started with Evals
**链接**：https://developers.openai.com/cookbook/example:evals

### 6-3. OpenAI Cookbook - Eval Driven System Design
**链接**：https://developers.openai.com/cookbook/eval_driven_development

### 6-4. Hamel Husain - Using LLM-as-a-Judge For Evaluation ⭐ 全文已抓取
**链接**：https://hamel.dev/blog/posts/llm-judge/
**作者**：Hamel Husain | **发布日期**：2024-10-29

**一句话核心**：来自 30+ AI 项目实战经验，总结出一套"**Critique Shadowing**"的 LLM-as-Judge 方法论。

---

#### 一、常见陷阱（AI 团队都在踩）

- **指标过多**：创建一堆测量指标，最后无法管理
- **评分系统随意**：1-5 分多维度评分，分数含义不清晰，不同评估者理解不同
- **忽略领域专家**：没有让真正懂行的人参与
- **指标未经验证**：用的测量指标并不真正反映用户/业务关心的东西

结果：团队被一堆不信任、无法使用的指标埋没，进度停滞。

---

#### 二、Critique Shadowing 七步法

##### Step 1：找到 Principal Domain Expert（主要领域专家）

**关键人物**：组织里对 AI 产品成功至关重要的 1-2 个人。

**为什么重要**：
- 他们设定标准：不仅定义技术可接受性，还帮助理解是否在解决用户真实需求
- 捕获隐性期望：通过评估过程，帮助他们澄清什么是"可接受"的 AI 交互
- 确保判断一致性：组织内各人观点不同，聚焦主要专家确保评估一致
- 建立归属感：让专家参与塑造 AI，他们最终更愿意认可 AI

**注意**：开发者自己不能替代领域专家！找一个方便的替代者（如上级）也是灾难。

##### Step 2：构建数据集

**三个维度**：

| 维度 | 说明 |
|------|------|
| Features | AI 的具体功能（如：邮件摘要、订单追踪、会议调度）|
| Scenarios | AI 需要处理的场景（而非 AI 响应的结果），如：多匹配、无匹配、模糊请求、无效数据、系统错误、信息不完整 |
| Personas | 典型用户画像：新用户、专家用户、非母语用户忙碌专业人士、技术恐惧者、老年用户 |

**数据来源**：
- 真实用户交互数据
- 合成数据（用 LLM 生成用户输入，不是生成 AI 响应）

> "LLMs are surprisingly good at generating excellent—and diverse—examples of user prompts." — Bryan Bischof, Hex

##### Step 3：领域专家做 Pass/Fail 判断 + Critiques

**核心原则**：只问一个二元问题——"AI 达到预期目标了吗？"

**为什么简单 Pass/Fail 很重要**：
- 清晰聚焦：二元决策迫使所有人考虑真正重要的事
- 可操作洞察：容易理解，快速识别 AI 是否满足用户需求
- 强迫明确期望：决定通过/失败的过程，迫使专家清晰表达期望
- 高效利用资源：避免一开始就被复杂指标淹没

**Critiques（批评）的作用**：
- 捕获细微差别：不只是结果，还有解释
- 提供可操作的反馈：不是"分低"，而是"具体哪里错、为什么错"
- 迭代的起点：为后续 prompt 优化提供方向

##### Step 4：修复错误
用 Error Analysis 驱动系统性修复，而非头痛医头脚痛医脚。

##### Step 5：迭代构建 LLM Judge

**迭代过程**：
1. 先用专家标注的 examples（golden dataset）
2. 不断迭代 judge prompt，直到与领域专家的判断一致
3. 用 critiques 作为 judge 的额外输入（Judge 不仅判断 pass/fail，还要给出 critique 对照）

**常见 judge prompt 错误**：
- 让 judge 给分数（而非直接判断 pass/fail）
- 缺少具体的 rubric 定义
- 没有给 judge 提供 context（用户输入是什么，任务目标是什么）

##### Step 6：Error Analysis

**分类 traces**：把失败案例分组，找共性模式（而非只看 individual cases）。

**"Fix Your Errors, Again"**：修复一个错误后，要问：这个修复是否引入了新的失败模式？

##### Step 7：创建更专门的 LLM Judges（如需要）

针对不同维度（准确性、语气、格式、法律合规性）使用不同的 specialized judges，而非一个 judge 评价所有维度。

---

#### 三、LLM Judge 的 Bias（来自论文：Judging LLM-as-a-Judge）

| Bias | 说明 |
|------|------|
| Position Bias | 倾向于认为排在前面的选项更好 |
| Verbosity Bias | 倾向于给更冗长的回答更高分 |
| Self-enhancement Bias | 倾向于给用同模型生成的输出更高分 |

→ 这就是为什么需要 human preference 来校准 judge。

---

#### 四、FAQ 精选

**Q：有了好 judge LLM，为什么不直接用它做任务？**
A：Judge 专注于评估，不需要实际执行任务，两者分工不同。

**Q：可以用小模型做 judge 吗？**
A：可以，但需要针对你的具体 rubric 精心调校。通用能力不够的小模型往往判断不稳定。

**Q：传统 ML 技术 vs. LLM-as-judge vs. 人类标注，怎么选？**
A：成本/速度：传统 ML > LLM-as-judge > 人类标注；准确性：人类标注 > LLM-as-judge > 传统 ML。组合使用而非非此即彼。

---

## 第七部分：成本归因——Per Feature 而非只看 Per Model

### 7-1. LangSmith - Cost Tracking
**链接**：https://docs.langchain.com/langsmith/cost-tracking
**核心**：记录 token usage，自动计算成本，把成本聚合到 trace 级别

### 7-2. LangSmith - Metadata & Tags
**链接**：https://docs.langchain.com/langsmith/add-metadata-to-traces
**核心**：用 metadata / tags 标记 feature_name、user_id、tenant_id、environment、experiment_id

### 7-3. W&B Weave - Track Costs
**链接**：https://docs.wandb.ai/weave/guides/tracking/custom-and-cost-tracking
**核心**：automatic cost tracking + custom cost tracking，尤其适合自托管模型或 fine-tuned model

### 7-4. Braintrust - Instrumentation
**链接**：https://braintrust.dev/docs/instrument
**核心**：trace/span 结构——task span、LLM span，每个 LLM span 记录 model、messages、parameters、token usage、cost

### 7-5. Traceloop - Cost Attribution Per User
**链接**：https://traceloop.com/blog/from-billable-hours-to-llm-cost-tracking
**核心**：建立成本归因意识——按 user、feature、team 做 token/cost attribution

---

## 第八部分：Agent Guardrails & Loop Budgets

### 8-1. OpenAI Agents SDK - Running Agents
**链接**：https://developers.openai.com/api/docs/agents
**核心 Agent Loop**：model call → inspect output → tool call / handoff / final answer → continue

### 8-2. OpenAI Agents SDK - max_turns
**链接**：https://openai.github.io/openai-agents-python/max_turns/
**核心**：turn budget；超过 max_turns 触发 MaxTurnsExceeded

### 8-3. OpenAI Agents SDK - Guardrails and Human Review
**链接**：https://developers.openai.com/api/docs/guardrails
**核心**：input/output/tool guardrails，以及暂停/继续/停止/交人工审批的时机

### 8-4. LangChain - Agent Iteration Limit
**链接**：https://docs.langchain.com/oss/react/how_to/iteration_limit/
**核心**：agent 必须有 stop condition——final output 或 iteration limit

### 8-5. CrewAI - max_iter
**链接**：https://docs.crewai.com/en/concepts/agents/
**核心**：另一个框架如何用 max_iter 控制 agent 推理循环

### 8-6. YouTube - Must Haves For Agents in Production
**链接**：https://www.youtube.com/watch?v=aIy85SF48yk
**核心**：production agent 的边界、工具、安全、可观测性和评测意识

---

## 第九部分：LLM 可观测性作为一等公民

### 9-1. LangSmith - Observability
**链接**：https://docs.langchain.com/langsmith/observability
**核心**：从 individual traces 到 production metrics 的 LLM app 可观测性

### 9-2. Arize Phoenix - Tracing Tutorial
**链接**：https://arize.com/docs/phoenix/tutorials/llm/
**核心**：捕获 LLM call、tool execution、retrieval、generation、inputs、outputs、latency、token usage

### 9-3. W&B Weave - What is Weave?
**链接**：https://docs.wandb.ai/weave/concepts
**核心**：把可观测性与 evaluation 结合起来，持续改进 LLM app

### 9-4. OpenTelemetry
**链接**：https://opentelemetry.io
**核心**：通用可观测性基础——traces、metrics、logs、vendor-neutral instrumentation

### 9-5. YouTube - Practical AI-Enabled Observability for Agents and LLMs
**链接**：https://www.youtube.com/watch?v=Xe60gk0PeE0

### 9-6. YouTube - How to Find the Agent Failures Your Evals Miss
**链接**：https://www.youtube.com/watch?v=ZqehXriQjg0
**核心**：evals 之外如何用 telemetry 发现线上失败

---

## 第十部分：模型路由 & Graceful Fallback 逻辑 ⭐ Portkey 全文已抓取

### 10-1. LiteLLM - Fallbacks
**链接**：https://docs.litellm.ai/docs/proxy/relay_litellm
**核心**：provider/model fallback——primary 失败后按顺序 fallback 到其他 model group

### 10-2. LiteLLM - Routing & Load Balancing
**链接**：https://docs.litellm.ai/docs/routing_litellm
**核心**：routing、load balancing、budget routing、health-check driven routing、timeouts

### 10-3. OpenRouter - Model Fallbacks
**链接**：https://openrouter.ai/docs/guides/routes
**核心**：多模型 fallback 与 provider routing 的实际配置

### 10-4. Portkey - Fallbacks
**链接**：https://docs.portkey.ai/docs/product/fallbacks
**核心**：AI Gateway 层如何用优先级列表实现 provider/model fallback

### 10-5. Portkey - Retries, Fallbacks, and Circuit Breakers ⭐ 全文已抓取
**链接**：https://portkey.ai/blog/retries-fallbacks-and-circuit-breakers-in-llm-apps
**作者**：Drishti Shah | **发布日期**：2025-07-17

**一句话核心**：retry + fallback 还不够，还需要 **circuit breaker** 来防止系统性故障演变成灾难。

---

#### Retry 的局限

Retry 设计用于处理**临时性故障**：
- 网络不稳定、TLS 握手失败
- Serverless 模型冷启动
- 短暂的 provider rate limit
- Token 配额刷新延迟

大多数 retry 系统使用**指数退避**（exponential backoff），配合 provider 的 Retry-After header。

**问题**：Retry 不知道故障是临时还是持久的。如果 provider 已宕机或降级，retry 会持续向同一个 endpoint 发起请求，在高并发下演变成 **retry storm**，堆积请求、推高 token 费用、拖垮整个系统。

---

#### Fallback 的局限

Fallback 旨在确保连续性——primary 失败切到 secondary。

**问题**：
1. **也是被动的**：系统每次都先等 primary 超时/报错，才切到 fallback，在多跳 agent 链中延迟叠加
2. **可能共享同一故障域**：如果 fallback 和 primary 在同一基础设施上，可能以完全相同的方式失败

---

#### Circuit Breaker（三者中最关键的）

**核心思想**：retry + fallback 是**从失败中恢复**，circuit breaker 是**预防灾难扩大**。

**工作原理**：

1. **监控**：追踪失败请求数、失败率、特定状态码（429、502、503）
2. **触发阈值**：超过阈值则"跳闸"（trip）
3. **跳闸后**：将故障 provider/model 从路由池中移除，固定冷却期内不再向其发送任何请求
4. **冷却后**：进入"半开"状态，允许一个请求通过试探是否恢复

**效果**：
- 防止已降级服务被更多流量压垮
- 保护 fallback 不被过早耗尽
- 给系统时间自愈，无需开发者手动干预

**三者不是互替的，是互补的**：

| 策略 | 应对场景 | 性质 |
|------|----------|------|
| Retry | 临时性故障（网络抖动、限流）| 被动 |
| Fallback | Provider 不可用或质量降级 | 被动 |
| Circuit Breaker | 系统性故障、持续降级 | **主动预防** |

---

### 10-6. TensorZero - Retries & Fallbacks
**链接**：https://tensorzero.com/docs/gateway/getting-started
**核心**：更完整的 gateway、variant、routing fallback 设计

### 10-7. YouTube - LLM Gateway Tutorial: Routing, Guardrails, Caching & Agent Workflows
**链接**：https://www.youtube.com/watch?v=U9XRcu7U9a8
**核心**：把 routing、guardrails、caching、agent budget 放在同一个 gateway 架构里理解

---

## 第十一部分：何时 Fine-tune vs. In-context Learning ⭐ IBM 文章已抓取

### 11-1. OpenAI - Model Optimization
**链接**：https://developers.openai.com/api/docs/guides/model-optimization
**核心**：fine-tuning 的适用场景，以及在 prompt engineering、RAG、fine-tuning 之间做选择

### 11-2. OpenAI - Optimizing LLM Accuracy
**链接**：https://platform.openai.com/docs/guides/optimizing-llm-accuracy
**核心**：判断矩阵——三者不是线性升级，而是解决**不同问题**的不同杠杆

### 11-3. IBM - RAG vs. Fine-tuning vs. Prompt Engineering ✅ 已抓取
**链接**：https://www.ibm.com/think/topics/rag

**三者选择框架**：

| 技术 | 核心解决什么问题 | 适用场景 |
|------|-----------------|----------|
| **Prompt Engineering** | 如何让模型更好地理解任务 | 任务简单、示例清晰、模型本身够强 |
| **RAG** | 让模型知道最新/特定知识 | 知识频繁变化、需要引用外部文档、企业私有知识 |
| **Fine-tuning** | 让模型在特定任务上表现更稳定、更快 | 任务固定、领域术语多、需要特定输出格式、需要降低成本 |

**RAG 的优势**：知识与模型分离，便于更新；可解释性更强（能看到引用来源）。

**Fine-tuning 的优势**：推理速度更快（无需每次检索）；在特定任务上更稳定；降低 token 消耗。

**IBM 建议**：先用 prompt engineering + RAG，只有当这两者不够用了，才考虑 fine-tuning。

### 11-4. QLoRA 论文（工程入口）
**链接**：https://openreview.net/pdf?id=OUIFPHEOeh
**核心**：如果真的准备 fine-tune，QLoRA 是必须读的工程入口——4-bit 量化模型 + LoRA adapter + NF4 + double quantization + paged optimizer

### 11-5. YouTube - Choosing Between RAG, In-Context Learning, and Fine-Tuning
**链接**：https://www.youtube.com/watch?v=7f_8wsBdsDo

### 11-6. YouTube - RAG vs. Fine Tuning
**链接**：https://www.youtube.com/watch?v=00Q0G8s_g9E

---

## 附录：资源分类总索引

### 📄 必读论文（PDF）
| 标题 | 链接 |
|------|------|
| vLLM PagedAttention | https://arxiv.org/pdf/2309.06180 |
| Speculative Decoding | https://arxiv.org/pdf/2211.17192 |
| QLoRA | https://openreview.net/pdf?id=OUIFPHEOeh |
| QSPEC | https://aclanthology.org/2025.emnlp-main.241.pdf |
| GPTCache | https://aclanthology.org/2023.nlposs-1.17.pdf |
| LMCache | https://lmcache.ai/tech_report.pdf |
| LLM Judge MT-Bench | https://arxiv.org/pdf/2306.05685 |

### 🎬 视频资源
| 标题 | 链接 |
|------|------|
| Anthropic Barry Zhang - How We Build Agents | https://www.youtube.com/watch?v=D7_ipDHH-eA |
| Fast LLM Serving with vLLM | https://www.youtube.com/watch?v=5ZlavK-a9Nnk |
| Speculative Decoding 入门 | https://www.youtube.com/watch?v=VkWlLSYQS0I |
| Guardrails AI 实战 | https://www.youtube.com/watch?v=r3JdQxM5lpI |
| AI Evals 类型入门 | https://www.youtube.com/watch?v=svKgNsM8D_A |
| Agents 生产必备 | https://www.youtube.com/watch?v=aIy85SF48yk |
| Agents & LLMs 可观测性 | https://www.youtube.com/watch?v=Xe60gk0PeE0 |
| Evals 遗漏的 Agent 失败 | https://www.youtube.com/watch?v=ZqehXriQjg0 |
| LLM Gateway Tutorial | https://www.youtube.com/watch?v=U9XRcu7U9a8 |
| RAG vs Fine-tuning 选择 | https://www.youtube.com/watch?v=7f_8wsBdsDo |
| RAG vs Fine-tuning 对比 | https://www.youtube.com/watch?v=00Q0G8s_g9E |

### ⭐ 已抓取全文的文章
| 标题 | 核心要点 |
|------|----------|
| Anthropic Building Effective Agents | 七大构建模式、Workflow vs Agent、MCP 协议 |
| Hamel Husain - LLM-as-Judge | Critique Shadowing 七步法、7 种陷阱、LLM Judge bias |
| Portkey - Circuit Breakers | Retry/Fallback/Circuit Breaker 三者对比与互补关系 |
| Google Cloud - 五大推理优化技术 | Continuous Batching、PagedAttention、Speculative Decoding、Quantization、Routing |
| Redis - Prompt vs Semantic Caching | 两种缓存策略的 trade-off 与生产组合方案 |
| IBM - RAG vs Fine-tuning vs Prompt | 三者选择框架、各自适用场景 |

### 🔧 工具文档
| 标题 | 链接 |
|------|------|
| Instructor | https://python.useinstructor.com |
| Pydantic AI | https://pydantic.dev/docs/ai/core-concepts |
| Guardrails AI | https://www.guardrailsai.com/guardrails/docs |
| LangSmith Cost & Observability | https://docs.langchain.com/langsmith |
| W&B Weave | https://docs.wandb.ai/weave |
| Arize Phoenix | https://arize.com/docs/phoenix |
| LiteLLM | https://docs.litellm.ai |
| Portkey | https://docs.portkey.ai |
| TensorZero | https://tensorzero.com/docs |
| OpenTelemetry | https://opentelemetry.io |
| OpenAI Agents SDK | https://developers.openai.com/api/docs/agents |
| LangChain Agents | https://docs.langchain.com/oss/react |
| CrewAI | https://docs.crewai.com |
| OpenAI Cookbook Evals | https://developers.openai.com/cookbook/example:evals |
| OpenAI Cookbook Eval-Driven Design | https://developers.openai.com/cookbook/eval_driven_development |

### ⚠️ 无法访问
| 标题 | 状态 |
|------|------|
| Martin Fowler Harness Engineering | 404（原文链接失效）|
| IBM RAG vs Fine-tuning vs Prompt | 原链接 https://ibm.com/think/topics/rag 被截断，已找到替代但需确认 |

---

*文件创建时间：2026-05-12*
*来源：微信推文，AI Engineer 高质量学习资料清单（完整 11 部分）*
*抓取状态：全文 6 篇、官方文档 20+、PDF 6 篇、视频 11 个*
