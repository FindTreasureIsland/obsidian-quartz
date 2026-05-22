---
title: 开箱即用、无需折腾的多模态 OpenClaw 来了：MaxClaw 详细深度实测与问题解答
author: "Kevin Ma (@kevinma_dev_zh)"
date: 2026-02-28 17:29
source: "https://x.com/kevinma_dev_zh/status/2027677448025084154"
tags:
  - twitter
  - article
---

# 开箱即用、无需折腾的多模态 OpenClaw 来了：MaxClaw 详细深度实测与问题解答

**作者**: Kevin Ma (@kevinma_dev_zh)
**时间**: 2026-02-28 17:29
**来源**: [原始链接](https://x.com/kevinma_dev_zh/status/2027677448025084154)

---

最近一直在用 MiniMax Agent，发现他们新上了一个基于 OpenClaw 部署叫 MaxClaw 的东西，觉得很不错，实测分享下。

简单说，MaxClaw 就是 MiniMax 帮你托管好的 OpenClaw，直接在网页上点几下就能用。不用自己折腾服务器，也不用配一堆 API Key，对不想在技术细节上花时间的人来说，这个太省心了。

我深度用了用，把实测的体验和一些有意思的发现分享出来。

适用场景：信息搜集与研究、内容生成（写文案、生图、生视频、配音）、文件处理与轻度自动化、每天定时抓取多个信息源生成报告，以及通过 Telegram / 飞书等 IM 工具随时下达任务。

目录
MaxClaw 是什么？
这东西好在哪？
实测中一些有意思的发现
发现一：工具缺失 ≠ 任务失败，它会自己找路
发现二：能装社区 Skill，还自带安全防火墙
发现三：内置多模态能力够用，且可以串联
发现四：对自身环境有清晰认知，会自我诊断
发现五：音频能力打通了，能听也能说
总结
常见问题

MaxClaw 是什么？
一句话：云端托管、一键部署的 OpenClaw。

它把开源 OpenClaw 那些麻烦的部署流程全包了，直接集成在 MiniMax Agent 网页端。买个基础版会员就能用，点几下，几十秒就能跑起来一个 7x24 小时在线的 AI 助手，还自带 50G 云存储。国内版在 agent.minimaxi.com，海外版在 agent.minimax.io。

首先是入口就在 MiniMax Agent 网页左边栏，很显眼。

图 1: 入口就在 MiniMax Agent 网页左边栏，很显眼。
图 2: 选个配置就能开始，新手直接用默认的就行，功能最全。
图 3: 点完部署，等个十几秒，直接就能对话开干了。

这东西好在哪？
玩下来感觉，MaxClaw 最大的好处就是把门槛降到最低，让普通人也能用上强大的 AI Agent。具体说有几点：

1. 零部署、零配置，真·开箱即用
这点是核心。自己装过 OpenClaw 的都知道，从服务器到环境配置，一步出错就得折腾半天。MaxClaw 把这些全免了，点几下鼠标，一个功能完整的云端 AI 助手就绪，对非技术用户非常友好。

2. 成本可控，不用担心 API 账单爆炸
自建 OpenClaw，底层大模型的 API 调用费是个无底洞。MaxClaw 是订阅制，包含在 MiniMax Agent 会员里，内置的图片、视频、音频生成这些功能都没有额外的 API 费用，成本是固定的，用起来很安心

3. 7x24 小时在线，随时待命
它跑在云端，所以你随时都能通过网页或者绑定的 IM 工具找到它。我把网页关了，用 Telegram 照样能使唤它干活，这点很棒。

图 4: 网页关了，Telegram 里照样能收到回复，证明是真·云端运行。

4. 绑定 IM 工具，用起来更顺手
它支持绑定飞书、钉钉、Telegram 这些常用的 IM 工具。绑定过程也很有意思，全程通过对话完成，基本就是复制粘贴几条信息的事。

图 5: 直接跟它说配置 telegram，它就把步骤一条条列出来了。
图 6: 按指引去 Telegram 里找 @BotFather 创建一个 Bot，拿到 Token。
图 7: 把 Token 扔回给 MaxClaw，它自己就配置好了。
图 8: 最后一步，把 Bot 发的配对码再扔给 MaxClaw，就绑上了。整个过程很流畅。
图 9: 绑定后，在 Telegram 里用斜杠指令就能看它都会些啥，很方便。

实测中一些有意思的发现
MiniMax 官方介绍的功能都差不多，我主要分享几个在实际测试中发现的、觉得做得不错的点。

发现一：工具缺失 ≠ 任务失败，它会自己找路
我让它去技能市场装一个叫 openinsider 的技能，用来查美股内部交易数据。结果技能市场里没有。

有意思的是，它没报错，而是直接跑去 OpenInsider 网站，把我要的苹果公司（AAPL）的交易数据给抓了回来，还整理成了表格，顺带做了分析总结。

图 10: 技能市场里没有，它就自己上网找数据，这点很智能。
图 11: 不光给原始数据，还做了二次分析，告诉我这些交易不一定是看空信号。

这点说明它的能力不完全依赖现成的工具。当工具箱里没有锤子的时候，它会自己去找块石头来砸钉子。对信息查询这类需求，这种自适应能力很实用。

发现二：能装社区 Skill，还自带安全防火墙
我用的是海外版，试了下装社区 Skill。整个过程都是对话完成，不用敲命令行。

更让我意外的是，它在安装 Nano Banana Pro 这个图片生成 Skill 时，主动警告我 playbooks.com 上的安装教程有供应链攻击风险，然后绕开了那个有问题的页面，用了官方的 clawhub CLI 来装。这个安全意识不错。

图 12: 它告诉我 playbooks.com 上的安装教程有问题，然后自己换了安全的装法，这个细节加分。

装好配上 API Key，直接就能用中文让它干活了。

图 13: 装好后用中文让它画的太空橘猫，效果不错。

发现三：内置多模态能力够用，且可以串联
图片生成：我用同样的提示词，分别让它用内置模型和刚装的 Nano Banana Pro（Gemini 模型）画了同一张图。对比下来，内置的 MiniMax 模型在写实感和光影层次上甚至更好一些，对大多数人来说完全够用，省了配 API Key 的钱。

图 14: 这是用它内置模型画的，跟图 13 对比，质感更好。

视频生成：我试了下从一句话生成带音乐的短视频，整个流程很顺畅。
1.先用文字生成一张静态图。
2.再让它把静态图变成动态视频。
3.最后让它给视频配上音乐。
每一步都是一句话的事，在一个对话里就能搞定，体验很好。

图 15: 第一步，先按我的描述生成一张静态图。
图 16: 第二步，让图动起来，变成 6 秒的短视频。
图 17: 第三步，一句话给视频配上音乐，搞定。

这种对话即工作流的体验，是它作为集成产品的优势，自己搭的话很难这么顺滑。

发现四：对自身环境有清晰认知，会自我诊断
我问它能不能执行 GitHub CLI 命令，它说没装，但可以帮我装，给了两个选项：apt install gh 或者从 GitHub 官方下载。我说试试，它先尝试了 apt，因为没有 root 权限失败了，然后自动切换成直接下载二进制文件，最终成功装上了 gh 2.66.1。

图 18: apt 因为没有 root 权限失败，它自动切换成下载二进制文件，最终装好了。

我又问了一句能安装 npm 全局安装包吗，它说完全没问题，然后我让它装 codex cli，一下子就装好了，还主动告诉我装在 /tmp 目录下重启会丢失，建议我把 npm 前缀改到 /workspace 下持久化。

图 19: npm 全局安装完全没问题，而且它还主动提醒了持久化的注意事项。

我还让它列出自己的文件目录和权限，它都答得清清楚楚，知道哪里能持久化存东西，哪里重启就没了。这种对自身环境的深度理解，让它在处理一些复杂指令时更可靠。

图 20: 它知道自己的核心配置文件都在 /workspace 里。
图 21: 它很清楚自己能访问哪些目录，不能访问哪些。
图 22: 它还主动整理了各目录的写权限，告诉我东西存哪才安全。

发现五：音频能力打通了，能听也能说
最后试了下音频。结论是：能听也能说。

语音识别：我在 Telegram 里发语音，它能准确识别成文字。
音频生成：让它生成一段英文音频，它直接发回了 mp3 文件。它自己也承认，底层用的是 MiniMax 自家的语音合成服务，不是开源 TTS。

图 23: 让它生成英文音频，直接就发过来了，音质还行。

至于语音回复，它也能做到，但不太稳定，声音也比较机械，这个功能我不太推荐用。

总结
总的来说，MaxClaw 是个好东西。

它把 OpenClaw 这种强大的 AI Agent 框架，做成了一个普通人也能轻松上手的云服务。不用折腾技术细节，开箱即用，成本可控，还内置了不错的的多模态能力。

如果你是开发者或极客，喜欢完全的控制权和深度定制，那还是自己去折腾开源的 OpenClaw。

但如果你是办公室职员、内容创作者，或者任何一个想把 AI Agent 用在实际工作流里，但又不想花时间在技术折腾上的人，MaxClaw 非常值得一试。

可以直接去 MiniMax Agent 官网开通，基础版会员就能用。

常见问题
最后补充几个大家可能关心的问题。

1. 国内版和海外版有什么区别？
两个版本都有专家功能（也就是技能市场），都支持自己安装 Skill、创建 Skill。主要差异是：海外版多了 Team Plan（团队协作套餐），以及可以切换到 Gemini 模型；国内版目前这两个功能都没有。

2. 国内版能访问海外网站吗？
国内版与海外版分别部署于对应地区的节点，国内版在访问需要代理的海外 API 或网站时会受到限制。我用的是海外版，访问 GitHub、OpenInsider 这些海外网站都没问题。

3. 内置搜索用的是什么？能自己换吗？
用的是 MiniMax 官方自研的搜索服务，不是 Brave Search。如果你想接入 Brave，MiniMax 说可以在对话中尝试自行配置，但建议先用 MiniMax 的搜索服务体验一下再说。

4. 视频生成怎么收费？
消耗的是 MiniMax Agent 会员积分，不用额外开别的会员。具体消耗多少，MiniMax 没给明确数字，建议自己用的时候留意下积分变化。

5. 音频回复能用吗？
技术上能做到，但实测下来不太稳定，声音也比较机械，不建议作为主要的交互方式。不过，既然底层已经打通了 MiniMax 自家的语音合成服务，估计 MiniMax 未来会把成熟的 Audio 模型能力集成进来，值得期待。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HCPBxB8aEAA8WDR?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HCO6j6RbcAAsKG2?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HCO6ylYbEAYCaJm?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HCO61VAbEAEEJRm?format=jpg&name=medium)

![Image 5](https://pbs.twimg.com/media/HCO65mabEAI72Kb?format=png&name=900x900)

![Image 6](https://pbs.twimg.com/media/HCO7H8ubEAkEjt7?format=png&name=medium)

![Image 7](https://pbs.twimg.com/media/HCO7WWnbUAA44Yh?format=jpg&name=large)

![Image 8](https://pbs.twimg.com/media/HCO7fKXaUAAxeE1?format=jpg&name=medium)

![Image 9](https://pbs.twimg.com/media/HCO7h26bEAEkOxW?format=jpg&name=medium)

![Image 10](https://pbs.twimg.com/media/HCO7kQHaAAAVmJH?format=jpg&name=medium)

![Image 11](https://pbs.twimg.com/media/HCO7o7bbEAMyDFb?format=jpg&name=large)

![Image 12](https://pbs.twimg.com/media/HCO7rnraQAAzasN?format=jpg&name=large)

![Image 13](https://pbs.twimg.com/media/HCO7vcCbYAACE4M?format=jpg&name=large)

![Image 14](https&name=large://pbs.twimg.com/media/HCO7vcCbYAACE4M?format=jpg&name=large)

![Image 15](https://pbs.twimg.com/media/HCO7yMCbEAMawUT?format=jpg&name=medium)

![Image 16](https://pbs.twimg.com/media/HCO71BrbEAIeOvA?format=jpg&name=medium)

![Image 17](https://pbs.twimg.com/media/HCO79arawAARLBo?format=jpg&name=medium)

![Image 18](https://pbs.twimg.com/media/HCO8MEZbEAUqG9Y?format=jpg&name=medium)

![Image 19](https://pbs.twimg.com/amplify_video_thumb/2027670950498783232/img/QlRKlaofNvxaSxR9.jpg)

![Image 20](https://pbs.twimg.com/media/HCO8SBbaEAEHgjF?format=jpg&name=medium)

![Image 21](https://pbs.twimg.com/media/HCO8fgGbEAENdnX?format=jpg&name=large)

![Image 22](https://pbs.twimg.com/media/HCO8jujbEAUPGcW?format=jpg&name=medium)

![Image 23](https://pbs.twimg.com/media/HCO8s77bAAAQl4q?format=jpg&name=medium)

![Image 24](https://pbs.twimg.com/media/HCO8vg3agAA07YB?format=png&name=900x900)

![Image 25](https://pbs.twimg.com/media/HCO8yKObEAMGyKC?format=jpg&name=medium)

![Image 26](https://pbs.twimg.com/media/HCO81WPbgAA30cV?format=jpg&name=medium)

