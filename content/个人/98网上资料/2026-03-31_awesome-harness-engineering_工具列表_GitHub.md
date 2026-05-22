# awesome-harness-engineering：最全的Harness Engineering资源库

> 项目：walkinglabs/awesome-harness-engineering
> GitHub：https://github.com/walkinglabs/awesome-harness-engineering
> Stars：834 | Forks：43

## 核心内容

Harness Engineering = 为 AI Agent 制作可靠工具的工程实践

> "Harness engineering sits at the intersection of context engineering, evaluation, observability, orchestration, safe autonomy, and software architecture."

翻译成人话：**怎么让 AI Agent 在真实工作流中更靠谱？**

这个仓库收录了最全的 Harness Engineering 相关资源：文章、实战手册、 benchmarks、规格说明、开源项目。

## 内容分类

### 1.  Courses & Learning Resources
学习路径和实战课程

### 2. Foundations
必读基础文章，包括：
- OpenAI 的 Harness Engineering field report
- Anthropic 的 long-running agents 核心文章
- LangChain 的 Agent Harness 解剖
- Thoughtworks 的 Harness Engineering 框架

### 3. Context, Memory & Working State
上下文管理和记忆系统，包括：
- Anthropic 的 context window 管理指南
- Manus 的 Context Engineering 实战 playbook
- OpenHands 的 Context Condensensation 设计

### 4. Constraints, Guardrails & Safe Autonomy
安全约束和自主控制，包括：
- Anthropic 的 Claude Code 安全实践
- OpenHands 的 Prompt Injection 防护指南
- HumanLayer 的 12 Factor Agents 原则

### 5. Specs, Agent Files & Workflow Design
规格设计和 Workflow，包括：
- AGENTS.md 格式（repo 本地指令）
- GitHub Spec Kit
- 12 Factor Agents / 12 Factor AgentOps

### 6. Evals & Observability
评测和可观测性，包括：
- OpenAI 的 Agent evals 实践指南
- OpenHands 的 Skill 评测 playbook
- Trace grading 方法论

### 7. Benchmarks
各种 benchmark 测试，包括：
- SWE-bench（软件工程任务）
- OSWorld（真机电脑使用）
- WebArena（网页自动化）
- GAIA（通用 AI 助手）
- Agent Arena（AI Agent 排行榜）
- WildClawBench（OpenClaw 实战 benchmark）

### 8. Runtimes, Harnesses & Reference Implementations
运行时和参考实现，包括：
- SWE-agent
- Anthropic Claude Agent SDK
- Inngest AgentKit

---

## 核心观点

> "Generic agent tooling is out of scope unless the page directly covers harness design, context management, evaluation, runtime control, or other reliability-critical harness primitives."

筛选标准很明确：**只收跟可靠性相关的核心实践，不收泛泛的 AI 工具介绍。**

---

## 数据统计
- ⭐ 834 Stars
- 🍴 43 Forks
- 📚 8大分类
