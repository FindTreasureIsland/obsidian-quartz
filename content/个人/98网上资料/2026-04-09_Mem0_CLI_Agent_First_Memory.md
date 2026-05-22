# Mem0 CLI — Agent-First Memory from Terminal

## 作者信息
- **作者**：Mem0 (@mem0ai)
- **平台**：X (Twitter)
- **发布时间**：2026年4月8日 23:40
- **原始链接**：https://x.com/mem0ai/status/2041903999520272674
- **浏览量**：1,378

## 核心内容

### Agent正在获得超能力

现在的AI agent已经可以：
- **说话** → ElevenLabs、Vapi
- **发邮件** → AgentMail
- **打电话** → AgentPhone
- **浏览网页** → Browserbase
- **搜索** → Firecrawl、Exa
- **使用SaaS工具** → Composio
- **支付** → GoKite、Paysponge

**加上 Mem0 → agent能记住**

把这些能力拼在一起，你得到的不只是工具，而是一个**数字同事**。

### Mem0 CLI是什么

一个让agent拥有记忆的终端工具。

**安装：**
```bash
npm install -g @mem0/cli
# 或
pip install mem0-cli
```

**添加记忆：**
```bash
mem0 add "Prefers TypeScript" --user-id cli-demo
mem0 add "Always respond in MD format" --agent-id coding-assistant
```

**搜索记忆：**
```bash
mem0 --agent search "preferences" --user-id cli-demo
```

**查看所有记忆：**
```bash
mem0 list --user-id cli-demo
```

### 解决什么问题

目前agent的记忆是个痛点：
- 需要集成SDK
- 需要构建pipeline
- 需要管理Vector DB或Markdown文件
- 需要决定添加什么、忽略什么

Mem0 CLI让这件事变简单——为agent和人类都简单。

---

## 数据亮点
- 浏览量：1,378
- 转发：8
- 评论：37
- 点赞：31
