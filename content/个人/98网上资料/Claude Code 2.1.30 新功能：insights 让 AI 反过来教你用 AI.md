---
title: "Claude Code 2.1.30 新功能：/insights 让 AI 反过来教你用 AI"
source: "https://mp.weixin.qq.com/s/khFij4uoSOD6Wgnfh-rxiw"
author:
  - "[[老罗聊 AI]]"
published:
created: 2026-02-07
description: "大家好我是老罗。昨天我在终端敲了 /insights，然后等了几秒。一份完整的 HTML 报告生成了，直接在浏览器打开。"
tags:
  - "clippings"
---
原创 老罗聊 AI *2026年2月4日 21:20*

大家好我是老罗。

昨天我在终端敲了 `/insights` ，然后等了几秒。

一份完整的 HTML 报告生成了，直接在浏览器打开。

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicUfNfrlnLI0nD0XEofJk5SficOwSvXShqrIaAViaxaicYDPCCEc0cmO2z2Q/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicUFjNfRKaPSyEasOmCq2Rx4SJDLz27ibYGxaibNvvHLLPhGCfxR0XuD81A/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

> “
> 
> 这是 **Claude Code 2.1.30** 版本推出的新功能。

看到这个功能的时候，我第一反应是：这玩意儿早就该有了。

你想啊，咱们每天都在用 Claude Code，但你真的知道自己用得怎么样吗？

- 是不是经常让 AI 做重复的事情？
- 有没有每次都要重新解释你的需求？
- 那些高级功能（Skills、MCP、Task Agents），你真的在用吗？

今天老罗就带你：

1. 看看我的真实使用报告（数据不会骗人）
2. AI 给我指出的 3 个大问题
3. Reddit 社区的高手们怎么用 Claude Code
4. 从"工具"到"教练"，AI 的新角色

**咱们不看虚的，直接上数据。**

## 01\. 我的 26 天：2140 个会话，10756 条消息

**官方核心观点：** `/insights` 就是你的"数字体检报告"，让 AI 告诉你它的观察。

先看一眼我的数据（时间跨度：2026-01-07 到 2026-02-02）：

| 统计项 | 数值 |
| --- | --- |
| 会话数 | 2,140 |
| 消息数 | 10,756 |
| 代码行数变化 | +1,139,346 / -214,723 |
| 操作文件数 | 10,801 |
| 使用天数 | 19 天 |

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicUH77HpVibl2ByGLFCNfeNSGP1nmicnuKTibq5KcHDsLcL31qKV6jDQNv2w/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

平均每天 **566 条消息** ，这数字我自己看了都吓一跳。

### 我主要在做什么？

报告直接把我的工作分成了 5 类：

**1\. 技术文档编写（~5 次会话）**

- 编写 API 文档、架构设计文档
- 主题包括各种 AI 工具的集成方案
- **问题** ：经常查资料多、写正文少，需要我打断

**2\. 项目结构优化（~2 次会话）**

- 分析文件夹结构、数据流
- 生成技术选型建议
- **问题** ：第一次推荐太理论化，我纠正后才调整

**3\. Spring Boot 项目（~1 次会话）**

- 创建了 4 个依赖任务
- Java 写了 14,710 行，TypeScript 5,834 行

**4\. 任务管理（~1 次会话）**

- TodoWrite 用了 10,079 次
- **问题** ：任务 1 阻塞后，不知道该继续还是换个思路

**5\. 平台集成纠正（~1 次会话）**

- **经典案例** ：Claude 建议我用 Tg，我纠正说"我用微信"

这个"Telegram 事件"被报告单独拎出来了，在文末的"有趣发现"部分：

> “
> 
> "The Telegram Hallucination - Claude tried to build a Telegram bot for a user who doesn't use Tg, and had to be redirected to WeChat apps instead"

### 我用得最多的工具

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicUsZESAaEQB1GomZOPZJuibEaicwbHSTiaH0lYmdzLQE9B58mgQ3GUFUnyw/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

Bash 用得最多，说明我经常让 AI 帮我执行命令、跑脚本。

**老罗心得：**

看到这些数据，我才意识到自己有多依赖 Claude Code。

但问题也很明显： **我花了太多时间在"研究"上，而不是"产出"上。**

就像报告说的：我 55% 的会话都是"部分完成"或"大部分完成"，只有 1 个会话是"完全完成"。

这是什么意思？就是我经常开个头，然后跑路了。

## 02\. AI 给我指出的 3 个大问题

报告不是只给你看数据，它真的在分析你的问题。

### 问题 1：31 次被误解

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicU95uomBnuibBDjDXqibe1rNGBSNq7SsicSAEhGHK83VMYaiaLicQ6Y9AP2iaQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

**摩擦类型：Misunderstood Request**

这是我的头号问题，报告直接给了 2 个真实案例：

**案例 1：Telegram 事件**

- Claude 建议：用 Telegram 做集成
- 我的纠正：我用微信生态，不用 Telegram
- 原因：Claude 不了解我的平台偏好

**案例 2：技术选型偏差**

- Claude 推荐：最新最火的技术栈
- 我的反馈：我要稳定可落地的方案
- 原因：没有提前明确我的技术偏好

报告给出的解决方案：

> “
> 
> **直接复制到 CLAUDE.md：** "When recommending technical solutions, prioritize stable, production-ready options over trending technologies."

### 问题 2：过度研究，不直接写

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicUiaC0AnANOibxdJib3DTfEp8G2F2cbQ9j3DuOuuyrLs6BtzeDgCvT59ibTQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

**摩擦类型：Research-Action Imbalance**

报告指出了我的一个致命问题：

> “
> 
> "Claude repeatedly fetched content without producing any actual writing until you had to restate the request with additional context"

翻译成人话就是：我让 Claude 写技术文档，它一直给我查资料，就是不写正文。

然后报告给了个非常具体的建议：

> “
> 
> **复制这个到 Claude Code：** "When creating content from web sources: Read maximum 3 sources, then immediately write the full article. Don't iterate on research more than twice before producing actual content."

**老罗心得：**

这个问题我之前就有感觉，但没想到这么严重。

现在我每次让 AI 生成文档，都会加一句： **"最多查 3 个资料，然后直接开始写，不要一直查。"**

效率立马上去了。

### 问题 3：任务经常做一半

![图片](https://mmbiz.qpic.cn/mmbiz_png/r4yzysZaluCTBQbTUR47eRIbVQtEFAicUQwagKbAjvB5OerAEbsyDZFApjiaYuIKHf6jfmsrSUFbXtGetichpf5Ag/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6)

**摩擦类型：Incomplete Task Execution**

报告发现我的会话结局分布：

- 完全没实现：4 个
- 部分完成：29 个
- 大部分完成：23 个
- 完全完成： **1 个**

这就是说，我 52 个会话里，只有 1 个是真正做完的。

其他都留了尾巴。

**原因分析：**

- 我经常在中途发现方向不对，切换到新任务
- 或者做到一半觉得"够用了"，就停了
- 还有就是被别的事情打断，再也没回来

报告建议我： **"建立明确的完成标准，并在输出符合需求时给反馈。"**

意思就是：你要告诉 AI "做到什么程度才算完"，而不是做到一半觉得行就行。

## 03\. Reddit 社区的高手怎么用

看完报告，我去 Reddit 的 r/ClaudeCode 看了眼大家的讨论，发现几个高手技巧：

### 1\. Hierarchical CLAUDE.md

根目录放项目级规则，子目录放模块特定规则，Claude 会自动加载对应上下文。

**例子：**

```
project/
├── CLAUDE.md          # 项目级：代码风格
├── backend/
│   ├── CLAUDE.md      # 后端特定：ORM 规则
│   └── ...
└── frontend/
    ├── CLAUDE.md      # 前端特定：组件规范
    └── ...
```

### 2\. /compact 命令

上下文太长时，自动压缩并释放窗口。对话久了敲一次，确实丝滑。

### 3\. Skills 就是 Markdown

就是个 Markdown 文件加 YAML 头，超简单：

```
---
description: API 文档助手
---

# API Documentation Skill
当用户要求编写文档时，提供完整示例...
```

**老罗心得：**

这些高手不是在"用"Claude Code，是在"定制"它。

## 04\. 从"工具"到"教练"：AI 的新角色

这才是 `/insights` 最有意思的地方。

以前的 AI，是你问它答，像个工具。

现在的 AI，会分析你的使用习惯，告诉你：

> “
> - 你应该试试 Custom Skills，减少重复解释
> - 你的数据库查询可以连 MCP，让 AI 直接访问
> - 用 Task Agents 并行工作，别让一个任务堵住全部

这已经不是"工具"了，这是"教练"。

**工具 vs 教练：**

| 工具 | 教练 |
| --- | --- |
| 你问，它答 | 它主动发现问题 |
| 你怎么用都行 | 它告诉你怎么用更好 |
| 不了解你的习惯 | 学习你的模式，优化建议 |
| 被动响应 | 主动改进 |

**更重要的是：** 报告给出的建议都是"可复制的"。

比如报告说我 31 次被误解，它直接给了 3 条可以复制到 `CLAUDE.md` 的规则：

```
When recommending technical solutions, prioritize stable, production-ready options over trending technologies.

Always confirm the target platform before assuming integrations - default to WeChat Mini Programs and apps, not Telegram.

When asked to create documentation based on web sources, read and analyze the sources first, then immediately begin writing. Limit research iterations to 2-3 cycles before producing output.
```

**一条命令复制过去，以后就不会再犯同样的错误。**

这就是"教练"的价值： **不是批评你哪里错了，而是帮你建立一个系统，让你不再犯错。**

## 总结：让 AI 帮你用 AI

今天咱们聊了 `/insights` 这个功能，核心就一个观点：

**AI 不只是你的工具，它可以是你的教练。**

通过它的分析，你可以：

1. **看到真实的自己** ：数据不会骗人，你的使用习惯一目了然
2. **发现隐形问题** ：31 次误解、过度研究、任务烂尾，这些都是你自己很难察觉的
3. **获得可操作的改进** ：不是空泛的建议，是直接能复制的配置和规则
4. **学习社区最佳实践** ：Reddit 的高手们，还有很多技巧等着你

**2026 年，会"用 AI"和"让 AI 教你怎么用 AI"的程序员，差距会越来越大。**

前者把 AI 当工具，后者把 AI 当教练。

## 🎁 粉丝福利

老罗整理了一套「Claude Code 高手工具包」：

**📦 包含：**

- ✅ 我的 `CLAUDE.md` 模板（包含技术偏好、平台约定）
- ✅ `/insights` 报告分析清单（手把手教你读懂报告）
- ✅ Reddit 社区 10 个高级技巧整理
- ✅ Custom Skill 示例（API 文档 + 代码审查）
- ✅ MCP Servers 配置模板（PostgreSQL + 微信）

**获取方式：** 在公众号后台回复「 **CC教练** 」，我把完整工具包发给你！

**你最想用 Claude Code 做什么？** 评论区告诉我，呼声高的下期直接出教程！

**往期硬核推荐：**  

👉 [Claude Code + Agent Skills + MCP 实战：一句"看看微博"自动总结全网热搜！](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg==&mid=2247483786&idx=1&sn=61029fda8a99193e7946a0b834ae8b90&scene=21#wechat_redirect)

👉 [被迫改名！Moltbot 10天狂飙10万Star，手机远程指挥电脑干活真香！](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg==&mid=2247484135&idx=1&sn=4efb55212b9cbe8a0b9eac72d09c39a2&scene=21#wechat_redirect)

👉 [我愿称之为2026年最强SKILL，AI替你操作浏览器，每天省2小时](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg==&mid=2247483994&idx=1&sn=3a0420a0c95914a5d503cfba0944c81d&scene=21#wechat_redirect)

👉 [官方终于出手！Claude Code 上下文优化来了，我再教你一招"无限续航"](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg==&mid=2247483908&idx=1&sn=1fc6f3c2b81a3f9669a4664da972701a&scene=21#wechat_redirect)

👉 [Claude Code 创作者 Boris：我已 100% 用 AI 写代码，这 10 个技巧公开了](https://mp.weixin.qq.com/s?__biz=MzYyMzc4NjU0Mg==&mid=2247484177&idx=1&sn=3d91d0c06328db8e01314c5b44874aa1&scene=21#wechat_redirect)

**关于作者：** 我是老罗，一个用代码改变世界的程序员。专注 AI 工具实战分享，让每个人都能享受 AI 红利。关注我，一起用技术创造价值！

  

作者提示: 个人观点，仅供参考

继续滑动看下一个

老罗聊 AI

向上滑动看下一个