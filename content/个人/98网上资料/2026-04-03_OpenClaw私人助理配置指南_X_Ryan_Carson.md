# How to turn your OpenClaw into the world's best assistant

## 作者信息
- **作者**：Ryan Carson (@ryancarson)
- **平台**：X (Twitter)
- **发布时间**：2026年4月3日
- **原始链接**：https://x.com/i/status/2039786704731541903
- **浏览量**：28.1万

## 核心内容

### 主要功能
- 帮你安排所有会议（解析Calendly链接并自动预约）
- 每15分钟检查一次邮箱，告诉你哪些邮件需要回复
- 主动跟进未回复的邮件
- 监控日历，预警冲突和即将到来的事项
- 从一个markdown任务清单管理你的一天
- 提前准备今日任务（把到期事项推到"今日"）
- 自动去重任务
- 识别客户回复并更新Google Sheets
- 更新CRM状态
- 研究供应商并联系安排会议
- 有需要才推送，无消息则保持安静

### 项目结构
```
clawchief/
├── README.md
├── skills/
│   ├── business-development/
│   ├── daily-task-manager/
│   ├── daily-task-prep/
│   └── executive-assistant/
├── workspace/
│   ├── HEARTBEAT.md
│   ├── TOOLS.md
│   └── tasks/current.md
└── cron/jobs.template.json
```

### 八步安装指南

**Step 1**: 确保OpenClaw已安装并正常工作

**Step 2**: 先配置好GOG（Gmail搜索、Calendar读取、Google Sheets元数据读取）

**Step 3**: 安装skills到~/.openclaw/skills/
- executive-assistant
- business-development
- daily-task-manager
- daily-task-prep

**Step 4**: 安装workspace文件到~/.openclaw/workspace/
- HEARTBEAT.md
- TOOLS.md
- tasks/current.md

**Step 5**: 创建私人上下文文件
- AGENTS.md
- SOUL.md
- USER.md
- IDENTITY.md
- MEMORY.md
- memory/

**Step 6**: 替换所有占位符
- 所有者名称
- 助手名称
- 邮箱地址
- 时区等

**Step 7**: 配置cron任务
- executive assistant sweep
- daily task prep
- daily business-development sourcing

**Step 8**: 验证安装

### 核心文件说明

**HEARTBEAT.md**: 定义助手需要主动检查的事项（重要新邮件、即将到来的日历事件、任务列表跟进）

**TOOLS.md**: 本地环境特定笔记（偏好的邮箱账号、Google Sheets使用笔记、浏览器配置指导）

**tasks/current.md**: 唯一的canonical任务清单，让助手看一个实时真相来源而不是猜历史对话

### 核心理念

> I didn't get the world's best assistant by asking OpenClaw better questions.
> I got it by giving OpenClaw a better operating system.

通用助手之所以通用，是因为配置不足。好的助手是有观点的、具体的、深度适配一个人实际工作方式的。

---

## 数据亮点
- 浏览量：28.1万
- 转发：701
- 评论：74
- 点赞：32
