# 抽丝剥茧：深度解析 Hermes Agent 万字系统提示词（System Prompt）构成

**作者**：岚叔 @LufzzLiz
**发布日期**：2026年4月15日
**原文链接**：https://x.com/LufzzLiz/status/2044258384556556743
**浏览量**：2万

---

## 0、准备阶段

如果你需要自己上手实践一下，可以看下岚叔的操作方式。

也很简单，要想完整分享，就需要完整的将 Hermes agent 发给模型的提示词全量导出。这里使用岚叔自己开发的神器 model-box: https://github.com/cclank/modelbox ，可以导出各种 agent 的提示词

安装部署直接让你的 hermes 照着项目 README.md 文档做即可，注意选择 mock 模式启动即可。

使用方式：如图，启动后，我们使用 /models 切换到 modelbox 即可。

长期关注过岚叔的都知道，这个是我们 debug 出完整系统提示词的神器，之前我们做了 openclaw 完整系统提示词解读，可见岚叔之前的文章。

---

## 一、系统提示词组成结构

首先我们剥开源码可以看见：Prompt Builder 位于 agent/prompt_builder.py，负责组装系统提示——身份定义、平台提示、技能索引、上下文文件。所有函数无状态，由 AIAgent._build_system_prompt() 调用拼接各模块。

**总结如下：**

```
┌─────────────────────────────────────────────┐
│ 1. SOUL.md — Agent 身份/人格                   │
│ 2. 记忆使用指南 — Memory 工具使用规范            │
│ 3. MEMORY — 持久化记忆快照（冻结）              │
│ 4. USER PROFILE — 用户画像快照（冻结）          │
│ 5. Skills 索引 — 全量技能列表                   │
│ 6. AGENTS.md — 项目级开发指南                   │
│ 7. 会话元数据 — 时间/模型/Provider              │
│ 8. 平台提示 — Telegram 特定行为                 │
│ 9. 会话上下文 — 来源/群组/投递选项              │
└─────────────────────────────────────────────┘
```

**总字符数：~36,700 chars（~10K tokens）**，看到这我有点震惊，居然和 openclaw 一样都过万了？！

---

## 第一层：SOUL.md — Agent 身份（~500 chars）

来自 ~/.hermes/SOUL.md，定义 Agent 人格。这个文件是我们自己定义的。

---

## 第二层：Memory 使用指南（~600 chars）

硬编码在 _build_system_prompt() 中，告诉模型如何使用 memory 工具：

- 用 memory 工具保存持久事实（用户偏好、环境细节、工具特性）
- 不要保存任务进度，完成日志（用 session_search 回忆）
- 发现非平凡工作流 → 保存为 Skill
- 使用中发现 Skill 过时 → 立即用 skill_manage(action='patch') 修复

---

## 第三层：MEMORY 快照（~3,725/4,000 chars，93% 满）

冻结快照，会话内不变。包含 7 个主题板块。

默认 profile 路径：~/.hermes/memories/MEMORY.md

---

## 第四层：USER PROFILE 快照（~682/1,375 chars，49%）

也是我们自定义的文件，每个人不一样。

默认 profile 路径：~/.hermes/memories/USER.md

也是冻结快照，描述用户是谁。

---

## 第五层：Skills 索引（~5,000 chars）

震惊了吧，skill 索引居然 5000 chars。

完整技能分类列表，涵盖 ~80+ 个 Skill，按分类组织：每个只展示名称 + 描述前缀（截断），模型需要时调用 skill_view(name) 加载完整内容。

---

## 第六层：AGENTS.md — 项目开发指南（~20,300 chars，被截断到 14K+4K）

4K + 4K 代表啥：AGENTS.md 原文（20,360 chars）

- 单文件上限：20,000 chars
- 截断比例：头部 70%（14K），尾部 30%（无显式定义，即剩余部分约 4-6K）
- AGENTS.md 有 20,360 chars，超了 360 chars，所以中间被砍了一小段

这样设计的原因是：文件开头通常最重要（目录结构、核心 API），结尾也有价值（注意事项、测试），中间往往是细节可以牺牲。

可以看到，这是 hermes-agent 仓库根目录的 AGENTS.md，占了系统提示的近一半。

**内容包括：**
- 项目结构：完整目录树 + 文件职责说明
- 文件依赖链：registry → tools → model_tools → run_agent
- AIAgent 类：构造参数、chat() 和 run_conversation() 接口、核心循环伪代码
- CLI 架构：Rich/prompt_toolkit、KawaiiSpinner、Slash Command Registry
- 添加工具的三步指南：tools/your_tool.py → model_tools.py → toolsets.py
- 添加配置：DEFAULT_CONFIG + OPTIONAL_ENV_VARS + 三种配置加载器
- 完整的皮肤自定义 API
- 6 个已知坑（硬编码路径、simple_term_menu Bug、ANSI 转义泄漏等）
- 测试指南：pytest 命令

**岚叔认为：** 如果你不是开发 Hermes，或者不做 Hermes 的升级维护啥，那么这将近 5k 的 token 可以不用。

最佳方式：告诉 hermes：请将主 agent cwd 配置为～，然后重启。

补充说明：关于这个路径你可以自己选择哈，当然你也可以自定义 AGENTS.md，没必要把那一大坨都加进去。

hermes 的 AGENTS.md 与 OpenClaw 的区别很大，前者是项目级别，OpenClaw 是全局的。

---

## 第七层：会话元数据（~200 chars）

加上模型自我认知指令："When asked what model you are, always answer based on this information"

---

## 第八层：平台提示 — Telegram（~200 chars）

这一层叫平台提示：比如岚叔用的 telegram，会传 telegram 相关提示，如果是 discord 就传 discord 的，这块 Hermes 做的很好，不同平台的定制化告诉了模型。

- 不使用 Markdown（Telegram 不渲染）
- 媒体文件投递方式：MEDIA:/path/to/file
- 图片 URL 用 ![alt](url) 会自动作为原生照片发送

---

## 第九层：会话上下文元信息（~400 chars）

系统提示词最后一段：告诉模型"你现在在哪"：

- 来源：Telegram 群 "爱马仕小分队"，thread 205
- 会话类型：多用户线程，消息带 [sender name] 前缀
- 已连接平台：local + telegram
- 当前 chat：telegram Home (ID: xxx')
- 定时任务投递选项：origin / local / telegram

---

## 系统提示词之后的内容

### 1. 对话消息

这里是我们与 hermes 每轮对话内容，都会放到这里。

### 2. 工具列表（30个）

这 30 个工具就是按需加载后的结果，Hermes 总共注册了 51 个工具，但会话只加载了 30 个。

**缺少的工具包括：**

| 未加载 | 原因 |
|---|---|
| mcp_*（3个） | 没配 MCP server |
| rl_*（10个） | RL 训练工具集，未启用 |
| homeassistant_*（4个） | 未配 Home Assistant |
| image_generation | 未配图像生成 API Key |
| mixture_of_agents | MoA 工具集未启用 |
| send_message | 可能当前平台配置未启用 |

**筛选机制：** 在 model_tools.py 的 _discover_tools() 里，通过 check_fn（检查 API Key 是否存在）和 enabled_toolsets/disabled_toolsets 来决定最终加载哪些工具。

---

## 优化效果

**优化前（4月13日）：** 36,700 chars
**优化后（4月15日）：** 明显减少

---

## 后记

本文通过导出全量 Hermes 提示词发现，里面有一些玄机：

1. **Skill 问题**：Hermes 是有很好的 skill 自进化逻辑，但是也会造成 skill 泛滥的问题，这个估计后面得需要考虑优化。

2. **AGENTS.md 文件加载问题**：如果你的 Hermes 是默认启动的，那么很可能会加载进 ~/.hermes/hermes-agent/AGENTS.md，这个文件太大了，大到都被截断了。足足有 5k token 之多，需要按岚叔的方式优化下。当然，省事的话可以直接缩减这个文件也可以，但是要注意后续可能会因为更新被覆盖。

---

*最后更新：2026-04-15*
