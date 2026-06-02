# Claude Skill 完全构建指南

> 来源：Anthropic官方文档 | 版本：2026年1月

---

## 总论

### 什么是Skill？

**Skill（技能）**是一组 instructions（指令）的集合——以简单的文件夹形式封装——用于教授 Claude 如何处理特定的任务或工作流。Skill 是自定义 Claude 以满足特定需求的最强大方式之一。与其每次对话都重新解释您的偏好、流程和领域专业知识，不如一次性教会 Claude，并在此后的每次交互中受益。

Skill 在您拥有**可重复的工作流程**时特别强大，例如：

- 根据规格生成前端设计
- 使用一致的方法论进行研究
- 创建遵循团队风格指南的文档
- 编排多步骤流程

它们与 Claude 的内置功能（如代码执行和文档创建）配合良好。对于构建 MCP 集成的用户，Skill 增加了另一个强大的层次，帮助将原始的工具访问转变为可靠、优化的工作流。

### 两条学习路径

- **构建独立 Skill？** 专注于基础、规划和设计章节（1-2类）。
- **增强 MCP 集成？** "Skills + MCP"部分和第三章适合您。

两条路径共享相同的技术要求，但您可以选择与您的用例相关的内容。

### 您将学到什么

- Skill 结构的技术要求和最佳实践
- 独立 Skill 和 MCP 增强工作流的模式
- 我们在各种用例中看到的有效模式
- 如何测试、迭代和分发您的 Skill

### 谁应该阅读本指南

- 希望 Claude 遵循特定工作流程的开发者
- 希望 Claude 遵循特定工作流程的高级用户
- 希望标准化 Claude 在整个组织中工作方式的团队

### 您将获得什么

到本指南结束时，您将能够在一个坐姿内构建一个可用的 Skill。预计需要约15-30分钟来构建和测试您的第一个工作 Skill。

---

## 第一章：基础

### 1.1 什么是 Skill？

一个 Skill 包含：

- **SKILL.md（必需）**：包含 YAML frontmatter 的 Markdown 格式指令
- **scripts/（可选）**：可执行代码（Python、Bash 等）
- **references/（可选）**：按需加载的文档
- **assets/（可选）**：模板、字体、图标等输出中使用的资源

### 1.2 核心设计原则

#### 渐进式披露（Progressive Disclosure）

Skill 使用三级系统：

**第一级（YAML frontmatter）**：始终加载到 Claude 的系统提示中。提供足够的信息让 Claude 知道何时应该使用每个 Skill，而无需将所有内容加载到上下文中。

**第二级（SKILL.md 正文）**：当 Claude 认为 Skill 与当前任务相关时加载。包含完整的指令和指导。

**第三级（链接文件）**：Skill 目录内绑定的额外文件，Claude 可以选择仅在需要时导航和发现。

这种渐进式披露最大程度减少 token 使用，同时保持专业能力。

#### 可组合性（Composability）

Claude 可以同时加载多个 Skill。您的 Skill 应该与其他 Skill 良好配合，而不是假设它是唯一可用的功能。

#### 可移植性（Portability）

Skill 在 Claude.ai、Claude Code 和 API 中工作相同。创建一次 Skill，它就可以在所有表面上工作，无需修改，只要环境支持 Skill 所需的任何依赖。

### 1.3 对于 MCP 构建者：Skill + 连接器

#### 厨房类比

- **MCP** 提供专业厨房：访问工具、食材和设备
- **Skill** 提供食谱：关于如何创造有价值内容的分步说明

一起使用，它们使用户能够完成复杂的任务，而不需要自己弄清楚每一个步骤。

#### 它们如何协同工作

| MCP（连接性）                                       | Skill（知识）                  |
| --------------------------------------------------- | ------------------------------ |
| 将 Claude 连接到您的服务（Notion、Asana、Linear等） | 教 Claude 如何有效使用您的服务 |
| 提供实时数据访问和工具调用                          | 捕获工作流和最佳实践           |
| Claude 能做什么                                     | Claude 应该如何做              |

#### 为什么这对您的 MCP 用户很重要

**没有 Skill 的情况：**

- 用户连接了您的 MCP 但不知道接下来要做什么
- 支持工单询问"如何用您的集成做X"
- 每次对话都从头开始
- 结果不一致，因为用户每次提示都不同
- 当真正问题是工作流指导时，用户责怪您的连接器

**有 Skill 的情况：**

- 预构建的工作流在需要时自动激活
- 一致、可靠的工具使用
- 最佳实践嵌入每次交互中
- 您的集成学习曲线更低

---

## 第二章：规划与设计

### 2.1 从用例开始

在编写任何代码之前，确定您的 Skill 应该实现的2-3个具体用例。

**良好的用例定义示例：**

```
用例：项目冲刺规划
触发：用户说"帮我规划这个冲刺"或"创建冲刺任务"
步骤：
1. 从 Linear（通过 MCP）获取当前项目状态
2. 分析团队速率和容量
3. 建议任务优先级
4. 创建带有适当标签和估算的任务
结果：规划好的冲刺，包含创建的任务
```

**问自己：**

- 用户想要完成什么？
- 这需要什么多步骤工作流？
- 需要哪些工具（内置或 MCP）？
- 应该嵌入什么领域知识或最佳实践？

### 2.2 常见 Skill 用例类别

在 Anthropic，我们观察到三个常见的用例类别：

#### 类别1：文档和资产创建

**用途：** 创建一致、高质量的输出，包括文档、演示文稿、应用程序、设计、代码等

**真实示例：** frontend-design skill

> "Create distinctive, production-grade frontend interfaces with high design quality. Use when building web components, pages, artifacts, posters, or：\*\*

- applications."

\*\*关键技术嵌入式风格指南和品牌标准

- 模板结构确保输出一致
- 成品质量检查清单
- 无需外部工具——使用 Claude 的内置功能

#### 类别2：工作流自动化

**用途：** 受益于一致方法论的多步骤流程，包括跨多个 MCP 服务器的协调。

**真实示例：** skill-creator skill

> "Interactive guide for creating new skills. Walks the user through use case definition, frontmatter generation, instruction writing, and validation."

**关键技术：**

- 带验证关卡的分步工作流
- 常见结构模板
- 内置审查和改进建议
- 迭代改进循环

#### 类别3：MCP 增强

**用途：** 增强 MCP 服务器提供的工具访问的工作流指导。

**真实示例：** sentry-code-review skill（来自 Sentry）

> "Automatically analyzes and fixes detected bugs in GitHub Pull Requests using Sentry's error monitoring data via their MCP server."

**关键技术：**

- 协调多个 MCP 顺序调用
- 嵌入领域专业知识
- 提供用户通常需要指定的上下文
- 常见 MCP 问题的错误处理

### 2.3 定义成功标准

#### 定量指标

- **Skill 在90%的相关查询上触发**
  - 测量方法：运行10-20个应该触发 Skill 的测试查询。跟踪自动加载与需要明确调用次数。

- **工作流在 X 次工具调用内完成**
  - 测量方法：比较启用和未启用 Skill 的同一任务。计算工具调用数和消耗的总 token 数。

- **每个工作流 0 次失败的 API 调用**
  - 测量方法：在测试运行期间监控 MCP 服务器日志。跟踪重试率和错误代码。

#### 定性指标

- **用户不需要提示 Claude 下一步做什么**
  - 评估方法：在测试期间，注意您需要多少次重定向或澄清。向 beta 用户询问反馈。

- **工作流完成无需用户纠正**
  - 评估方法：运行相同请求3-5次。比较输出的结构一致性和质量。

- **新用户可以在首次尝试时完成任务**
  - 评估方法：可以让新用户在最少指导下完成任务吗？

---

## 第三章：技术要求

### 3.1 文件结构

```
your-skill-name/
├── SKILL.md                 # 必需 - 主要 Skill 文件
├── scripts/                 # 可选 - 可执行代码
│   ├── process_data.py     # 示例
│   └── validate.sh         # 示例
├── references/              # 可选 - 文档
│   ├── api-guide.md         # 示例
│   └── examples/            # 示例
└── assets/                  # 可选 - 模板等
    └── report-template.md   # 示例
```

### 3.2 YAML Frontmatter：最重要的部分

YAML frontmatter 是 Claude 决定是否加载您的 Skill 的方式。

#### 最小必需格式

```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

#### 字段要求

**name（必需）：**

- 仅限 kebab-case
- 无空格或大写
- 应与文件夹名称匹配

**description（必需）：**

- 必须包含两者：
  - Skill 做什么
  - 何时使用（触发条件）
- 少于1024个字符
- 不包含 XML 标签（< 或 >）
- 包含用户可能说的具体任务
- 如相关，提及文件类型

**license（可选）：**

- 如使 Skill 开源则使用
- 常用：MIT、Apache-2.0

**compatibility（可选）：**

- 1-500个字符
- 指示环境要求：例如预期产品、所需系统包、网络访问需求等

**metadata（可选）：**

- 任何自定义键值对
- 建议：author、version、mcp-server

#### 关键规则

**安全限制：**

- Frontmatter 中禁止：
  - XML 尖括号（< >）
  - 名称中包含"claude"或"anthropic"的 Skill（保留）

**原因：** Frontmatter 出现在 Claude 的系统提示中。恶意内容可能注入指令。

### 3.3 编写有效的 Skill 指令

#### 描述字段

根据 Anthropic 工程博客："这个元数据...提供足够的信息让 Claude 知道何时应该使用每个 Skill，而无需将所有内容加载到上下文。"这是渐进式披露的第一级。

**结构：**
[做什么] + [何时使用] + [关键能力]

**好的描述示例：**

```yaml
# 好 - 具体且可操作
description: Analyzes Figma design files and generates developer handoff documentation. Use when user uploads .fig files, asks for "design specs", "component documentation", or "design-to-code handoff".

# 好 - 包含触发短语
description: Manages Linear project workflows including sprint planning, task creation, and status tracking. Use when user mentions "sprint", "Linear tasks", "project planning", or asks to "create tickets".

# 好 - 清晰的价值主张
description: End-to-end customer onboarding workflow for PayFlow. Handles account creation, payment setup, and subscription management. Use when user says "onboard new customer", "set up subscription", or "create PayFlow account".
```

**坏的描述示例：**

```yaml
# 太模糊
description: Helps with projects.

# 缺少触发条件
description: Creates sophisticated multi-page documentation systems.

# 太技术化，没有用户触发
description: Implements the Project entity model with hierarchical relationships.
```

#### 编写主指令

在 frontmatter 之后，用 Markdown 编写实际指令。

**推荐结构：**

```markdown
# Your Skill Name

## Instructions

### Step 1: [First Major Step]

Clear explanation of what happens.

### Step 2: [Second Major Step]

Another clear explanation.

## Examples

### Example 1: [common scenario]

User says: "[what user says]"
Actions:

1. [action 1]
2. [action 2]
   Result: [what happens]

## Troubleshooting

### [Common Issue]

Error: [error message]
Cause: [why it happens]
Solution: [how to fix]
```

#### 最佳实践

**要具体且可操作：**

✅ 好：

```
Run `python scripts/validate.py --input {filename}` to check data format.
If validation fails, common issues include:
- Missing required fields (add them to the CSV)
- Invalid date formats (use YYYY-MM-DD)
```

❌ 坏：

```
Validate the data before proceeding.
```

**包含错误处理：**

```markdown
## Common Issues

### MCP Connection Failed

If you see "Connection refused":

1. Verify MCP server is running: Check Settings > Extensions
2. Confirm API key is valid
3. Try reconnecting: Settings > Extensions > [Your Service] > Reconnect
```

**明确引用捆绑资源：**

```markdown
Before writing queries, consult `references/api-patterns.md` for:

- Rate limiting guidance
- Pagination patterns
- Error codes and handling
```

**使用渐进式披露：**

保持 SKILL.md 专注于核心指令。将详细文档移到 `references/` 并链接到它。

---

## 第四章：测试与迭代

### 4.1 测试级别

Skill 可以在不同严格程度下进行测试：

- **手动测试（Claude.ai）**：直接运行查询并观察行为。快速迭代，无需设置。
- **脚本测试（Claude Code）**：自动化测试用例，以在更改时进行可重复验证。
- **编程测试（通过 skills API）**：构建评估套件，系统地对定义的测试集运行。

选择符合您质量要求和无障碍需求的方。法。在小团队内部使用的 Skill 与部署到数千企业用户的 Skill 有不同的测试需求。

### 4.2 推荐的测试方法

基于早期经验，有效的 Skill 测试通常涵盖三个方面：

#### 1. 触发测试

**目标：** 确保您的 Skill 在正确的时间加载。

**测试用例：**

应该触发：

- "Help me set up a new ProjectHub workspace"
- "I need to create a project in ProjectHub"
- "Initialize a ProjectHub project for Q4 planning"

不应该触发：

- "What's the weather in San Francisco?"
- "Help me write Python code"
- "Create a spreadsheet"（除非 ProjectHub Skill 处理表格）

#### 2. 功能测试

**目标：** 验证 Skill 产生正确的输出。

**测试用例：**

- 生成的输出有效
- API 调用成功
- 错误处理有效
- 边缘情况被覆盖

**示例：**

```
测试：创建包含5个任务的项目
给定：项目名称"Q4 Planning"，5个任务描述
当：Skill 执行工作流
那么：
- 项目在 ProjectHub 中创建
- 5个任务以正确属性创建
- 所有任务链接到项目
- 无 API 错误
```

#### 3. 性能比较

**目标：** 证明 Skill 相对于基线改进结果。

使用"定义成功标准"中的指标。以下是比较可能的样子：

**无 Skill 的基线：**

- 用户每次都提供指令
- 15条往复消息
- 3次需要重试的失败 API 调用
- 消耗 12,000 tokens

**有 Skill 的情况：**

- 自动工作流执行
- 仅需2个澄清问题
- 0次失败的 API 调用
- 消耗 6,000 tokens

### 4.3 使用 skill-creator Skill

skill-creator Skill——通过插件目录在 Claude.ai 中可用或供 Claude Code 下载——可以帮助您构建和迭代 Skill。如果您有 MCP 服务器并知道您的顶级2-3个工作流，您可以在一个坐姿内构建和测试一个功能性 Skill——通常在15-30分钟内。

**创建 Skill：**

- 从自然语言描述生成 Skill
- 生成格式正确的 SKILL.md 及 frontmatter
- 建议触发短语和结构

**审查 Skill：**

- 标记常见问题（模糊描述、缺失触发、结构问题）
- 识别过度/不足触发风险
- 根据 Skill 声明的目的建议测试用例

**迭代改进：**

- 使用您的 Skill 并遇到边缘情况或失败后，将这些例子带回给 skill-creator
- 例如："使用本聊天中识别的问题和解决方案来改进 Skill 处理[特定边缘情况]的方式"

### 4.4 基于反馈迭代

Skill 是活的文档。计划基于以下内容进行迭代：

**触发不足的信号：**

- Skill 不在应该加载时加载
- 用户手动启用它
- 关于何时使用它的支持问题
- 解决方案：在描述中添加更多细节和细微差别——这可能包括特别技术术语的关键字

**触发过多的信号：**

- Skill 为无关查询加载
- 用户禁用它
- 对目的混淆
- 解决方案：添加负面触发条件，更加具体

---

## 第五章：分发与共享

### 5.1 当前分发模型（2026年1月）

#### 个人用户如何获取 Skill

1. 下载 Skill 文件夹
2. 压缩文件夹（如需要）
3. 通过 Settings > Capabilities > Skills 上传到 Claude.ai
4. 或放入 Claude Code skills 目录

#### 组织级 Skill

管理员可以部署工作区范围的 Skill（2025年12月18日发布）

- 自动更新
- 集中管理

### 5.2 开放标准

我们发布了 Agent Skills 作为开放标准。与 MCP 类似，我们相信 Skill 应该在工具和平台之间可移植——无论您使用 Claude 还是其他 AI 平台，同一个 Skill 都应该工作。不过，有些 Skill 旨在充分利用特定平台的能力；作者可以在 Skill 的 compatibility 字段中注明这一点。我们一直在与生态系统成员合作制定标准，并对早期采用感到兴奋。

### 5.3 通过 API 使用 Skill

对于编程用例——例如构建利用 Skill 的应用程序、代理或自动化工作流——API 提供对 Skill 管理和执行的直接控制。

**关键能力：**

- `/v1/skills` 端点用于列出和管理 Skill
- 通过 `container.skills` 参数将 Skill 添加到 Messages API 请求
- 通过 Claude Console 进行版本控制和管理
- 与 Claude Agent SDK 配合用于构建自定义代理

#### 何时通过 API vs Claude.ai 使用 Skill

| 用例                      | 最佳表面                |
| ------------------------- | ----------------------- |
| 最终用户直接与 Skill 交互 | Claude.ai / Claude Code |
| 开发期间手动测试和迭代    | Claude.ai / Claude Code |
| 个人的、临时的工作流      | Claude.ai / Claude Code |
| 应用程序编程使用 Skill    | API                     |
| 生产规模部署              | API                     |
| 自动化管道和代理系统      | API                     |

### 5.4 推荐的分发方法

**1. 托管在 GitHub**

- 公开仓库用于开源 Skill
- 清晰的 README 和安装说明
- 使用示例和屏幕截图

**2. 在您的 MCP 仓库中记录**

- 从 MCP 文档链接到 Skill
- 解释一起使用两者的价值
- 提供快速入门指南

**3. 创建安装指南**

```markdown
# 安装 [Your Service] Skill

1. 下载 Skill：
   - 克隆仓库：`git clone https://github.com/yourcompany/skills`
   - 或从 Releases 下载 ZIP

2. 安装到 Claude：
   - 打开 Claude.ai > Settings > skills
   - 点击"Upload skill"
   - 选择 Skill 文件夹（压缩）

3. 启用 Skill：
   - 切换到 [Your Service] Skill
   - 确保您的 MCP 服务器已连接

4. 测试：
   - 询问 Claude："在 [Your Service] 中设置新项目"
```

### 5.5 定位您的 Skill

您如何描述您的 Skill 决定用户是否理解其价值并实际尝试它。

**专注于成果，而不是功能：**

✅ 好：

> "The ProjectHub skill enables teams to set up complete project workspaces in seconds — including pages, databases, and templates — instead of spending 30 minutes on manual setup."

❌ 坏：

> "The ProjectHub skill is a folder containing YAML frontmatter and Markdown instructions that calls our MCP server tools."

**突出 MCP + Skill 的故事：**

> "Our MCP server gives Claude access to your Linear projects. Our skills teach Claude your team's sprint planning workflow. Together, they enable AI-powered project management."

---

## 第六章：模式与故障排除

### 6.1 常见模式

这些模式来自早期采用者和内部团队创建的 Skill。它们代表我们看到的常见方法，而不是 prescriptive 模板。

#### 模式1：顺序工作流编排

**使用场景：** 用户需要特定顺序的多步骤流程。

**示例结构：**

```markdown
## Workflow: Onboard New Customer

### Step 1: Create Account

Call MCP tool: `create_customer`
Parameters: name, email, company

### Step 2: Setup Payment

Call MCP tool: `setup_payment_method`
Wait for: payment method verification

### Step 3: Create Subscription

Call MCP tool: `create_subscription`
Parameters: plan_id, customer_id (from Step 1)

### Step 4: Send Welcome Email

Call MCP tool: `send_email`
Template: welcome_email_template
```

**关键技术：**

- 明确的步骤顺序
- 步骤之间的依赖关系
- 每个阶段的验证
- 故障回滚说明

#### 模式2：多 MCP 协调

**使用场景：** 工作流跨越多个服务。

**示例：设计到开发交接**

```markdown
## Phase 1: Design Export (Figma MCP)

1. Export design assets from Figma
2. Generate design specifications
3. Create asset manifest

## Phase 2: Asset Storage (Drive MCP)

1. Create project folder in Drive
2. Upload all assets
3. Generate shareable links

## Phase 3: Task Creation (Linear MCP)

1. Create development tasks
2. Attach asset links to tasks
3. Assign to engineering team

## Phase 4: Notification (Slack MCP)

1. Post handoff summary to #engineering
2. Include asset links and task references
```

**关键技术：**

- 清晰的阶段分离
- MCP 之间的数据传递
- 移动到下一阶段前的验证
- 集中式错误处理

#### 模式3：迭代改进

**使用场景：** 输出质量通过迭代改进。

**示例：报告生成**

```markdown
## Iterative Report Creation

### Initial Draft

1. Fetch data via MCP
2. Generate first draft report
3. Save to temporary file

### Quality Check

1. Run validation script: `scripts/check_report.py`
2. Identify issues:
   - Missing sections
   - Inconsistent formatting
   - Data validation errors

### Refinement Loop

1. Address each identified issue
2. Regenerate affected sections
3. Re-validate
4. Repeat until quality threshold met

### Finalization

1. Apply final formatting
2. Generate summary
3. Save final version
```

**关键技术：**

- 明确的quality标准
- 迭代改进
- 验证脚本
- 知道何时停止迭代

#### 模式4：上下文感知工具选择

**使用场景：** 相同结果，不同工具取决于上下文。

**示例：智能文件存储**

```markdown
## Smart File Storage

### Decision Tree

1. Check file type and size
2. Determine best storage location:
   - Large files (>10MB): Use cloud storage MCP
   - Collaborative docs: Use Notion/Docs MCP
   - Code files: Use GitHub MCP
   - Temporary files: Use local storage

### Execute Storage

Based on decision:

- Call appropriate MCP tool
- Apply service-specific metadata
- Generate access link

### Provide Context to User

Explain why that storage was chosen
```

**关键技术：**

- 明确的决策标准
- 后备选项
- 选择透明

#### 模式5：领域特定智能

**使用场景：** 您的 Skill 增加了超越工具访问的专业知识。

**示例：金融合规**

```markdown
## Payment Processing with Compliance

### Before Processing (Compliance Check)

1. Fetch transaction details via MCP
2. Apply compliance rules:
   - Check sanctions lists
   - Verify jurisdiction allowances
   - Assess risk level
3. Document compliance decision

### Processing

IF compliance passed:

- Call payment processing MCP tool
- Apply appropriate fraud checks
- Process transaction
  ELSE:
- Flag for review
- Create compliance case

### Audit Trail

- Log all compliance checks
- Record processing decisions
- Generate audit report
```

**关键技术：**

- 嵌入逻辑的专业知识
- 行动前的合规性
- 全面的文档
- 明确的治理

### 6.2 故障排除

#### Skill 无法上传

**错误：** "Could not find SKILL.md in uploaded folder"

**原因：** 文件名不是精确的 SKILL.md

**解决方案：**

- 重命名为 SKILL.md（区分大小写）
- 验证：`ls -la` 应显示 SKILL.md

#### 错误：Invalid frontmatter

**常见错误：**

```yaml
# 错误 - 缺少分隔符
name: my-skill
description: Does things

# 错误 - 未闭合引号
name: my-skill
description: "Does things"

# 正确
---
name: my-skill
description: Does things
---
```

#### 错误：Invalid skill name

**原因：** 名称包含空格或大写

```yaml
# 错误
name: My Cool Skill

# 正确
name: my-cool-skill
```

#### Skill 不触发

**症状：** Skill 从不自动加载

**修复：**
修改您的 description 字段。请参阅"描述字段"部分了解好/坏示例。

**快速检查清单：**

- 是否太模糊？（"Helps with projects" 不行）
- 是否包含用户实际会说的触发短语？
- 如相关，是否提及相关文件类型？

**调试方法：**
询问 Claude："什么时候会使用 [skill name] Skill？" Claude 会引用 description。根据缺失的内容进行调整。

#### Skill 触发过于频繁

**症状：** Skill 为无关查询加载

**解决方案：**

1. **添加负面触发**

```yaml
description: Advanced data analysis for CSV files. Use for statistical modeling, regression, clustering. Do NOT use for simple data exploration (use data-viz skill instead).
```

2. **更加具体**

```yaml
# 太宽泛
description: Processes documents

# 更具体
description: Processes PDF legal documents for contract review.
```

3. **澄清范围**

```yaml
description: PayFlow payment processing for e-commerce. Use specifically for online payment workflows, not for general financial queries.
```

#### 指令不被遵循

**症状：** Skill 加载但 Claude 不遵循指令

**常见原因：**

1. **指令太冗长**
   - 保持指令简洁
   - 使用项目符号和编号列表
   - 将详细参考移到单独文件

2. **指令被埋没**
   - 将关键指令放在顶部
   - 使用 ## Important 或 ## Critical 标题
   - 如需要可以重复关键点

3. **语言模糊**

```yaml
# 坏
Make sure to validate things properly

# 好
CRITICAL: Before calling create_project, verify:
- Project name is non-empty
- At least one team member assigned
- Start date is not in the past
```

**高级技术：** 对于关键验证，考虑捆绑执行检查的脚本，而不是依赖语言指令。代码是确定性的；语言解释不是。

#### MCP 连接问题

**症状：** Skill 加载但 MCP 调用失败

**检查清单：**

1. **验证 MCP 服务器已连接**
   - Claude.ai: Settings > Extensions > [Your Service]
   - 应显示"Connected"状态

2. **检查认证**
   - API 密钥有效且未过期
   - 正确授予权限/范围
   - OAuth 令牌已刷新

3. **独立测试 MCP**
   - 询问 Claude 直接调用 MCP（不带 Skill）
   - 例如："使用 [Service] MCP 获取我的项目"
   - 如果这失败，问题在 MCP 而不是 Skill

4. **验证工具名称**
   - Skill 引用正确的 MCP 工具名称
   - 检查 MCP 服务器文档
   - 工具名称区分大小写

#### 大上下文问题

**症状：** Skill 似乎变慢或响应质量下降

**原因：**

- Skill 内容太大
- 同时启用的 Skill 太多
- 加载所有内容而不是渐进式披露

**解决方案：**

1. **优化 SKILL.md 大小**
   - 将详细文档移到 references/
   - 链接到参考而不是内联
   - 保持 SKILL.md 少于 5,000 字

2. **减少启用的 Skill**
   - 评估是否同时启用了超过 20-50 个 Skill
   - 建议选择性启用
   - 考虑相关功能的 Skill"包"

---

## 第七章：资源与参考

### 7.1 官方文档

**Anthropic 资源：**

- 最佳实践指南
- Skills 文档
- API 参考
- MCP 文档

**博客文章：**

- 介绍 Agent Skills
- 工程博客：为现实世界装备代理
- Skills 解释
- 如何为 Claude 创建 Skills
- 通过 Skills 改进前端设计

### 7.2 工具和实用程序

**skill-creator Skill：**

- 内置在 Claude.ai 中，可用于 Claude Code
- 可以从描述生成 Skill
- 提供审查和建议
- 使用："使用 skill-creator 帮助我构建一个 Skill"

**验证：**

- skill-creator 可以评估您的 Skill
- 询问："审查这个 Skill 并建议改进"

### 7.3 示例 Skill

**公共 Skill 仓库：**

- GitHub: anthropics/skills
- 包含您可以自定义的 Anthropic 创建的 Skill

**推荐参考：**

- 文档 Skill - PDF、DOCX、PPTX、XLSX 创建
- 示例 Skill - 各种工作流模式
- 合作伙伴 Skill 目录 - 来自各种合作伙伴的 Skill，如 Asana、Atlassian、Canva、Figma、Sentry、Zapier 等

---

## 附录A：快速检查清单

### 上传前

**测试触发：**

- ✅ 在明显的任务上触发
- ✅ 在改写的请求上触发
- ✅ 验证不在无关主题上触发

**功能测试通过：**

- ✅ 工具集成工作（如适用）
- ✅ 压缩为 .zip 文件

### 开始前

- ✅ 确定了2-3个具体用例
- ✅ 确定了工具（内置或 MCP）
- ✅ 审查了本指南和示例 Skill
- ✅ 规划了文件夹结构

### 开发期间

- ✅ 文件夹命名为 kebab-case
- ✅ SKILL.md 文件存在（精确拼写）
- ✅ YAML frontmatter 有 --- 分隔符
- ✅ name 字段：kebab-case，无空格，无大写
- ✅ description 包含 WHAT 和 WHEN
- ✅ 无 XML 标签（< >）
- ✅ 指令清晰且可操作
- ✅ 包含错误处理
- ✅ 提供示例
- ✅ 引用清晰链接

### 上传后

- ✅ 在实际对话中测试
- ✅ 监控触发不足/过度
- ✅ 收集用户反馈
- ✅ 迭代 description 和指令
- ✅ 在 metadata 中更新版本

---

## 附录B：YAML Frontmatter 参考

### 必需字段

```yaml
---
name: skill-name-in-kebab-case
description: What it does and when to use it. Include specific trigger phrases.
---
```

### 所有可选字段

```yaml
---
name: skill-name
description: [required description]

# 可选：开源许可证
license: MIT

# 可选：限制工具访问
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"

# 可选：自定义字段
metadata:
  author: Company Name
  version: 1.0.0
  mcp-server: server-name
  category: productivity
  tags: [project-management, automation]
  documentation: https://example.com/docs
  support: support@example.com
---
```

### 允许的内容

- 任何标准 YAML 类型（字符串、数字、布尔值、列表、对象）
- 自定义元数据字段
- 长描述（最多1024个字符）

### 禁止的内容

- XML 尖括号（< >）——安全限制
- YAML 中的代码执行（使用安全的 YAML 解析）
- 带有"claude"或"anthropic"前缀的 Skill 名称（保留）

---

## 附录C：完整 Skill 示例

完整的、生产就绪的 Skill 示例演示了本指南中的模式：

- **文档 Skill** - PDF、DOCX、PPTX、XLSX 创建
- **示例 Skill** - 各种工作流模式
- **合作伙伴 Skill 目录** - 来自各种合作伙伴的 Skill，如 Asana、Atlassian、Canva、Figma、Sentry、Zapier 等

这些仓库保持更新，并包含超出本指南范围的额外示例。将它们克隆下来，为您的用例修改它们，并将它们用作模板。

---

_本文档根据 Anthropic 官方《The Complete Guide to Building Skills for Claude》整理，版本截至2026年1月。_
