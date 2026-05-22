---
title: 看完 Anthropic Academy 13 门课后，我对OpenClaw系统做了17个改动
author: "xiyu (@ohxiyu)"
date: 2026-03-02 20:20
source: "https://x.com/ohxiyu/status/2028445432729506095"
tags:
  - openclaw
  - anthropic
  - claude
  - agent
  - prompt-engineering
---

# 看完 Anthropic Academy 13 门课后，我对openclaw 系统做了 17 个改动

**作者**: xiyu (@ohxiyu)
**时间**: 2026年3月2日 20:20
**来源**: [原始链接](https://x.com/ohxiyu/status/2028445432729506095)

---

Anthropic 开放了免费的 Academy 课程，13 门，从 Prompt Engineering 到 MCP 到 Claude Code，全覆盖。

完整提示词 -- 复制发给你的openclaw

别收藏了。打开你的配置文件，现在就改

---

## 一、最大收获：Adaptive Thinking（省钱 30-50%）

这是 ROI 最高的一个改动。五分钟改完，立刻省钱。

我之前用的是固定 thinking budget：
```
{"thinking": {"type": "enabled", "budget_tokens": 32000}}
```

问题很明显——不管你问"现在几点"还是"帮我做个深度分析"，都烧同样的 thinking tokens。Opus 不便宜，这个浪费很痛。

Opus 4.6 已经废弃了 type，推荐的新写法：
```
{ "thinking": {"type": "adaptive"}, "output_config": {"effort": "high"} }
```

核心区别：Claude 自己判断需要多少思考。简单问题可能 0 thinking tokens，复杂问题全力以赴。

effort 参数有三档：low / medium / high，控制思考上限。

**关键洞察：不同 Agent 应该用不同 effort。**

- **low**：日常对话、状态查询、简报生成、消息路由。这些任务不需要深度推理，low 就够了。
- **medium**：内容写作、日常监控，信息整合。需要一定思考但不复杂。
- **high**：深度分析、代码生成、财务计算、复杂决策。这些钱不能省。

我的系统里有多个 Agent 各司其职，改完之后路由 Agent 用 low，分析 Agent 用 high，写作 Agent 用 medium。整体 thinking token 消耗直接降了大概三到四成。

💡 **操作建议**：如果你的系统只有一个 effort 配置，今天就按任务类型拆分。这是最快见效的优化。

---

## 二、Think Tool：Agent 系统的隐藏武器

这个是课程里让我最意外的。

**先说区别：**
- Extended Thinking 是调用前思考
- Think Tool 是调用间思考

Extended Thinking 发生在 Claude 生成回复之前，一次性完成。但在多 Agent 场景里，Claude 经常需要连续调用多个工具——先查数据，再分析，再写入。工具调用之间，Claude 没有"暂停思考"的机制。

Think Tool 解决的就是这个问题。它就是一个普通的工具定义：
```
{ "name": "think", "description": "Use this tool to think through complex problems step by step before taking action. Call this when you need to reason about which tool to use, verify your approach, or plan multi-step operations.", "input_schema": { "type": "object", "properties": { "thought": { "type": "string", "description": "Your step-by-step reasoning" } }, "required": ["thought"] } }
```

没有任何 handler——调用它不执行任何代码，纯粹是给 Claude 一个"思考缓冲区"。但 Anthropic 实测发现，加了这个工具后，policy 遵循率和多步骤任务的准确性显著提升。

**哪些 Agent 该加 Think Tool？**

- ✅ 路由/调度类 Agent（需要判断任务该给谁）
- ✅ 分析/研究类 Agent（需要多步推理）
- ✅ 代码类 Agent（需要逻辑验证）
- ✅ 涉及权限/安全检查的 Agent
- ❌ 纯创意输出的 Agent（写文章，写推文）
- ❌ 单步操作的 Agent（查天气、记账）

**Think Tool vs Extended Thinking，怎么选？**

不是二选一。它们互补：
- Extended Thinking：处理请求前的整体规划
- Think Tool：工具调用链中的步骤间推理

我的做法是两个都开。路由 Agent 用 effort + Think Tool，分析 Agent 用 effort + Think Tool。

---

## 三、Prompt Engineering 实战：5 个立即可用的技巧

课程 9 章内容，浓缩成 5 个我实际用到的。

### 3.1 XML 标签分离指令与数据

之前我的 Skill 文件（类似 system prompt 的模块化配置）把指令和参考数据混在一起。Claude 经常搞混"这是让我做的事"和"这是给我参考的数据"。

改成 XML 标签后清晰多了：
```
<instructions> 你是一个财务分析 Agent。分析以下数据并给出建议。 输出格式：先结论，再数据支撑，最后风险提示。 </instructions> <reference_data> {{动态注入的数据}} </reference_data>
```

Claude 对 XML 标签的解析极其可靠。这不是什么新技术，但实际动手改的人不多。

### 3.2 Speaking for Claude（Output Prefill）

与其说"请用 JSON 格式输出"，不如直接在 assistant 消息里预填开头：
```
Assistant: {"analysis": "
```

Claude 会自然接续，格式错误率大幅降低。

这个技巧在 API 调用中很容易实现——messages 数组最后加一个 role 的消息，内容就是你想让 Claude 接续的开头。

### 3.3 Few-shot 示例的正确姿势

对格式要求严格的输出（比如固定格式的简报、特定风格的推文），1-2 个示例效果远超长篇描述：
```
<examples>
<example>
<input>分析苹果 Q3 财报</input>
<output>
📊
Apple Q3 FY2025
- 营收：$XX B（+X% YoY）
- 关键：服务业务占比首次超过 XX%
- 风险：中国市场持续承压
</output>
</example>
</examples>
```

关键：示例要覆盖边界情况，不要只给"完美示例"。

### 3.4 防幻觉指令（一句话就够）

对涉及事实查询的 Agent（情报类、财务类、研究类），在 system prompt 里加一句：

> 如果你不确定某个数据或事实，明确说"我不确定"或"需要验证"。错误信息比没有信息更危险。

就这一句。简单，但很多人不加，然后被 Claude 自信满满的幻觉坑到。

### 3.5 System Prompt 分层

这是我改动最大的一个。之前的 system prompt 试图一次性塞入所有指令，结果越靠后的规则越容易被忽略。

Anthropic 建议的分层结构：
```
<critical_rules> 绝对不能违反的规则（安全、权限、格式） </critical_rules>
<standard_rules> 日常行为规范 </standard_rules>
<reference> 参考信息，按需使用 </reference>
```

优先级从上到下递减。核心身份和关键安全规则放最前面，参考资料放最后。

另一个建议：可缓存的静态内容放前面，动态内容放后面。这样配合 Prompt Caching（下面会讲），静态部分只需要传一次。

---

## 四、MCP 的 90% 你没用到

如果你在用 MCP（Model Context Protocol），大概率只用了 Tools、Resources、Prompts 这三个核心原语。但 MCP 还有三个高级特性，大多数人完全没碰过。

### 4.1 Sampling：Server 反向调 LLM

这个最让我兴奋。

正常流程是 client 调 server 的工具。Sampling 反过来——MCP server 可以请求 client 端帮它调 LLM。server 本身不需要持有任何 API key。

场景很多：
- MCP server 处理数据时需要 AI 辅助分类
- 自动摘要、自动标注
- server 端做决策需要 LLM 判断

架构优势：AI 成本和复杂度集中在 client 端管理，server 保持轻量。

### 4.2 Roots：目录声明

正式声明哪些目录对 LLM 可见：
```
{ "roots": [ {"uri": "file:///path/to/workspace", "name": "Project Root"} ] }
```

比起让 LLM 自己摸索文件结构，Roots 提供明确的访问边界。安全性和效率都更好。

### 4.3 Elicitation：向用户提问

MCP server 可以主动向用户提问，获取额外信息：
```
{ "method": "elicitation/create", "params": { "message": "请确认要执行此操作吗？", "requestedSchema": { "type": "object", "properties": { "confirm": {"type": "boolean"} } } } }
```

当 server 需要用户确认或补充信息时，不用让 LLM 转述，直接问用户。

💡 这三个特性能不能用，取决于你的 MCP client 框架是否支持。建议先查文档确认，再决定要不要投入时间。

---

## 五、从 Claude Code 学到的 Agent 模式

Claude Code 课程不长，但里面几个 Agent 模式很实用。

### 5.1 并行 Subagent

之前我的系统是串行的——一个任务 spawn 一个子 Agent，等完成了再下一个。

Claude Code 的思路：识别可并行的子任务，同时 spawn。

```
任务：生成周报
├── Agent A → 收集各渠道数据（并行）
├── Agent B → 分析趋势变化（并行）
└── 主 Agent → 等 A+B 完成 → 汇总输出
```

改动不大，但复杂任务的完成时间能缩短不少。

### 5.2 自动重试

子 Agent 失败后自动重试一次，不惊扰用户：
- 第一次失败 → 自动重试（附上错误信息帮助修正）
- 第二次失败 → 上报用户 + 错误详情
- 永远不重试：涉及资金转账、消息发送、数据删除的操作

这个规则很简单，但能大幅减少人工干预。

### 5.3 上下文压缩

长对话 session 的上下文会不断膨胀。Claude Code 有个 compact 模式——自动压缩历史对话，保留关键信息。

对于需要长时间运行的 Agent（比如项目管理类、持续监控类），上下文压缩是必须的。否则跑着跑着就超 context window 了。

---

## 六、我的改动清单（17 项，按 ROI 排序）

### 🔴 5 分钟见效

1. **切换 Adaptive Thinking**
   — 把 type 改成 adaptive，配上 effort 参数。立省 30-50% thinking tokens。

2. **添加 Think Tool**
   — 给路由，分析、代码、监控类 Agent 加上面那个 JSON 定义。零成本，显著提升多步推理准确性。

3. **按 Agent 配置 Effort 级别**
   — 日常 low，创作 medium，分析 high。不要一刀切。

### 🟡 需要改文件

4. **Skill 文件 XML 标签重构**
   — 所有 Skill 文件用 `<instructions>` / `<examples>` / `<reference>` 分离。

5. **System Prompt 分层重构**
   — 核心身份 + 关键规则放最顶部，用 `<critical_rules>` 包裹。参考信息用 `<reference>` 放底部。

6. **添加 Few-shot 示例**
   — 对格式敏感的输出（简报、推文等），加 1-2 个示例。

7. **防幻觉指令**
   — 所有涉及事实查询的 Agent 加一句。

8. **Think Tool 使用指引**
   — 在相关 Agent 的 system prompt 里加一句"在复杂决策和多步操作前使用 think tool"。

9. **System Prompt 精简**
   — 审计所有 Agent 的 system prompt 大小，超长的砍掉冗余，核心指令前置。

### 🟢 需要调研

10. **Prompt Caching** — 检查你的框架是否已对 system prompt 自动启用缓存。如果没有，手动加 cache_control。cache hit 只收 1/10 价格。

11. **MCP Sampling** — 检查你的 MCP client 是否支持 sampling capability。如果支持，MCP server 就能反向调 LLM。

12. **MCP Roots** — 配置目录声明，明确文件访问边界。

13. **并行 Subagent** — 改路由逻辑，识别可并行的子任务。

14. **自动重试机制** — 子 Agent 第一次失败自动重试，第二次再上报。

15. **上下文压缩** — 对长 session Agent 启用 compact 模式（取决于框架支持）。

16. **MCP Elicitation** — 让 MCP server 能直接向用户提问。

17. **Assistant Prefill** — 在 API 调用中预填 assistant 消息开头，引导输出格式。

---

## 结尾

13 门课，一下午看完。但看完不等于学到，学到不等于改进。

**改进 = 学习 + 动手。**

这 17 个改动里，前 3 个五分钟就能搞定，改完立刻省钱。如果你也在跑多 Agent 系统，建议今天就改。

---

*来源: X @ohxiyu*
