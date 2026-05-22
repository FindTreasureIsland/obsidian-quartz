# 用Claude Code + XCrawl 在推上学习大V们的观点

## 作者信息
- **作者**：Mr Panda (@PandaTalk8)
- **平台**：X (Twitter)
- **发布时间**：2026年4月3日
- **原始链接**：https://x.com/PandaTalk8/status/2039972807833219415

## 核心内容

### 背景
把X上一些大V们的发表内容下载下来用AI分析一遍，学习他们高观点和他们的思维。

利用XCrawl在Claude Code整理Karpathy的发表内容。

Andrej Karpathy——前Tesla AI总监、OpenAI创始团队成员、Stanford PhD——可能是X上最值得关注的AI思想家。他的每一条推文都能引发行业讨论。问题是：他发了几百条推文，你不可能一条条翻。

---

### 工具准备：XCrawl

XCrawl是一个能将搜索结果和网站内容转换为LLM友好格式的工具，可以非常友好地与AI Agent协同工作。

**安装XCrawl CLI：**
```bash
# 方式一：全局安装（推荐）
npm install -g @xcrawl/cli

# 方式二：免安装直接用
npx -y @xcrawl/cli@0.0.7 --help
```

**登录认证：**
```bash
# 浏览器登录（推荐，自动弹出授权页面）
xcrawl login --browser

# 或者用API Key登录
xcrawl login --api-key <YOUR_API_KEY>

# 确认登录成功
xcrawl status
```
新账户送1,000个免费credits，不需要绑卡。

**把XCrawl包装成Claude Code Skill：**
直接在Claude Code里说："帮我把xcrawl包装成一个Claude Code Skill"，Claude Code会自动帮你创建配置文件。

---

### 五步流程

**第一步：搜索目标博主的内容**
```
xcrawl search "site:x.com karpathy" --limit 20 --country US --language en --json
```

**第二步：按话题细化搜索**
```
用xcrawl分别搜索Karpathy关于以下话题的推文，每个话题10条：
- AI编程
- AI Agent
- AI教育与创业
- LLM思维模型
```

**第三步：抓取重点推文全文**
"刚才搜到的Karpathy推文里，把最有价值的几条全文抓下来"

**第四步：批量采集多个博主**
"用同样的方法，帮我采集以下博主关于AI的推文，每人20条：
@dotey、@AndrewYNg、@levie、@MatthewBerman"

**第五步：整理分析，生成报告**
"把刚才采集的所有博主推文数据整理一下，按话题分类，每个话题提取top 5最有价值的观点，生成一份《AI行业观点周报》"

---

### Karpathy核心观点摘录

**AI编程变革：**
- "过去两个月AI编程发生了质变，不是渐进的"
- "作为程序员，我从未感到如此落后"——AI工具像"外星人递过来的工具，没有说明书"
- "2025年AI跨过了用英语写程序的能力门槛"
- 支持"context engineering"取代"prompt engineering"

**AI Agent：**
- 让AI Agent连续跑两天，改了700处代码，发现20个改进
- "Agent失败源于用户指令差，不是模型能力"
- 称AI Agent目前是"slop"，但问题10年内可解

**创业与教育：**
- Eureka Labs融资$180M
- 对学校教育委员会："你永远无法检测AI做作业"
- 发布AI职业影响评分工具

**思维模型：**
- "别把LLM当实体，把它当模拟器"
- "Software 2.0：能自动化你能验证的一切"

---

### 完整流程
1. 在Claude Code里说你想了解谁、什么话题
2. Claude Code自动调用XCrawl搜索采集
3. 继续说"抓取重点推文全文"（可选）
4. 继续说"整理分析，生成报告"
5. 一份结构化的观点报告自动保存到本地

五步下来，全程10分钟——只需要说话，不需要打开终端、不需要敲命令、不需要手动整理。

---

## 数据亮点
- 浏览量：3,393
- 转发：28
- 评论：2
- 点赞：1
