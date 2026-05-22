# Harness Engineering 在讨论什么：三个 Scaling 维度的统一框架

## 来源信息
- **平台**：yage.ai（鸭哥每日手记）
- **发布日期**：2026-03-30
- **原始链接**：https://yage.ai/share/harness-engineering-scalability-20260330.html

## 核心内容

### 1. 一个词，三件事

2026年第一季度，OpenAI、Cursor和Anthropic先后发布了各自在agent-first软件开发上的实践报告。三篇文章都被归入同一个术语：harness engineering。但它们讲的几乎是三件完全不同的事：

- **OpenAI**的harness engineering：环境设计——文档体系、架构约束、可观测性基础设施
- **Cursor**的self-driving codebases：协调架构——几百个agent同时工作，怎么分工、并行、收敛
- **Anthropic**的harness design for long-running apps：运行时纠偏——一个agent连续跑几小时，怎么保持方向和质量

### 2. 地基：三家收敛到的共同判断

1. **人类核心工作从写代码转向设计agent的工作环境**——人类的杠杆点在于创造让agent能可靠工作的条件
2. **知识必须版本化、可发现、存在于repo中**——Codex看不到的等于不存在
3. **约束比指令有效**——约束是可执行的、确定性的
4. **完美主义是吞吐量的敌人**——纠错比等待便宜

### 3. 三个 Scaling 维度

#### 3.1 时间 Scalability：让一个Agent连续跑几小时
**问题**：长时间运行会引发方向漂移和自评失真
**Anthropic解法**：三角色架构（Planner-Generator-Evaluator）
- Planner：把需求扩展成完整产品spec
- Generator：按spec实现功能
- Evaluator：用Playwright验证产出是否达标

**成果**：数字音频工作站运行约4小时，成本$124

#### 3.2 空间 Scalability：让几百个Agent并行工作
**问题**：能否通过投入10倍计算获得10倍有意义吞吐量
**Cursor解法**：递归Planner-Worker架构
- 根Planner拥有整个项目范围
- Worker在独立repo副本上工作
- 写handoff提交给Planner

**成果**：峰值约1000 commits/hour

#### 3.3 交互 Scalability：让人用最少的介入steer大量Agent工作
**OpenAI Symphony**：把人机交互从"写prompt并触发"简化为"写ticket并移动状态"

### 4. 三个维度之间的关系

- **空间scaling会放大时间scaling中的问题**：几百个agent同时漂移、每个都在自我合理化，错误以并行度倍数积累
- **交互scaling依赖时间和空间scaling的成熟度**
- **三家共同发现**：模型选择对角色的适配比预期更重要

### 5. 框架能帮你做什么

判断harness engineering讨论的质量：
- 它在解决哪个维度的scaling？
- 时间（让agent跑更久）、空间（让更多agent一起跑）、交互（让人更省力地steer）

---

## 参考来源
- Ryan Lopopolo, "Harness engineering: leveraging Codex in an agent-first world", OpenAI, 2026-02-11
- Wilson Lin, "Towards self-driving codebases", Cursor, 2026-02-05
- Wilson Lin, "Scaling long-running autonomous coding", Cursor, 2026-01-14
- Prithvi Rajasekaran, "Harness design for long-running application development", Anthropic, 2026-03-24
- OpenAI, Symphony, 2026-03-05
