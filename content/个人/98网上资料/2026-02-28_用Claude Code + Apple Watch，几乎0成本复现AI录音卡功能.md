---
title: 用Claude Code + Apple Watch，几乎0成本复现AI录音卡功能
author: "柯基是猫猫"
date: 2026-02-28
source: "https://note.mowen.cn/detail/AUz3E91k_M_qZt_WfD23e"
tags:
  - mowen
  - 墨问
  - claude-code
  - apple-watch
  - AI录音卡
---

# 用Claude Code + Apple Watch，几乎0成本复现AI录音卡功能

**作者**: 柯基是猫猫
**时间**: 2026-02-28
**来源**: [原始链接](https://note.mowen.cn/detail/AUz3E91k_M_qZt_WfD23e)

---

10 | 用Claude Code + Apple Watc...
柯基是猫猫
2026-02-28 创建
10 | 用Claude Code + Apple Watch ，几乎0成本复现AI录音卡功能
我一直觉得，语音输入是一种特别好的、可以随时随地记录自己灵感的方式。
现在市面上出现了一些 AI 录音卡设备，比如得到的GetSeed AI 录音卡我觉得他们的产品设计逻辑还是很棒的，可以通过一个物理按键来开启和结束记录，音频会被自动上传到云端，通过 AI 转写生成笔记，然后还能做进一步的操作。
我自己平时的录音设备是 Apple Watch Ultra。它同样有一个 物理按键 Action Button，可以按一下就开启语音备忘录，然后再按一下终止录音。
我觉得它作为一个输入设备，已经可以非常完美地替代 AI 录音卡。
今天我用了两个小时的时间，让Claude Code打工，基于 Apple Watch Ultra 和 Mac 完美地复现了整个流程。
整个流程的实现方式和AI录音卡的逻辑还是非常相似的：
我需要做的就是抬起手腕，按一下Action Button， 对着手表说话，再按一下停止，随后，对应的内容就会自动转化成一条结构化的语音记录，并保存在我 Obsidian 当天日记的一个模块中。
实现的效果大概是这样的
1 它做了什么
整套系统串起了这样一条链路：
Apple Watch 录音
    ↓
iPhone / iCloud 自动同步到 Mac
    ↓
后台检测到新的录音文件
    ↓
语音转文字（豆包大模型语音 API）
    ↓
AI 结构化处理（标题 / 摘要 / 待办 / 整理后的文字）
    ↓
自动写入 Obsidian 当天日记
一条语音变成了：一个精炼的标题、一段摘要、提取出来的待办事项、以及原始转写（供回溯）。
2 为什么选择这套方案
市面上有很多语音笔记 App，但它们的问题是：数据被锁在了另一个 App 里。
我已经在用 Obsidian 做日记，我不需要"又一个笔记 App"，我需要的是让语音记录直接流入我现有的工作流。
这套系统的设计原则就是：
- 不引入新 App：用 Apple 原生的语音备忘录录音，用 Obsidian 做笔记，中间的脏活由后台守护进程干
- 不需要手动操作：录完就不用管了，后台自动处理
- 数据完全属于你：所有笔记都是本地 Markdown 文件，没有中间商
3 扩展性
这套系统天然具备很强的扩展性，因为每个模块都是独立的。
我可以自由地选择使用什么样的 AI，自由地设计输出结构；同时也可以非常自由地更换，将其写入到 Obsidian、flomo 还是墨问上。
同时，基于已经转录和结构化的文字，甚至还可以做进一步的每日、每周、每月内容的分析、归纳和总结。
这里面的每一步都是完全可控的，而你需要付出的成本仅仅只有语音转写和 AI 处理的 token 成本。
4 这是一个幸福的时代
用 Claude Code 做完之后，我突然领悟到，其实这是一个非常幸福的时代。
你完全可以用非常低的成本，去做一个只满足自己需求的软件，而这一点在过去是不可想象的。
17
3
9
墨东东，池建强，Steve，michael，微凉，QianTalk，智慧搬运工，墨东东，愤毛阿青
墨东东，池建强，Steve，michael，微凉，QianTalk，智慧搬运工，墨东东，愤毛阿青
(2)
呼唤小墨
愤毛阿青
1 小时前
0
但是我的apple watch 经常没电🪫[撇嘴]
池建强
24 分钟前
0
回复 愤毛阿青：换苹果表啊

---

## 图片

![图片 1](https://priv-sdn-001.mowen.cn/mo/file/meta/14/32/98/2015427766794035201.png?Expires=1772470249&OSSAccessKeyId=LTAI5tE16jzdfWCPVBmyB5Nn&Signature=ukdY9uKMsJKkwtbcHK3zWmP5KZQ%3D&response-expires=Mon%2C%2002%20Mar%202026%2016%3A50%3A49%20GMT&x-oss-process=image%2Fresize%2Cw_240)

![图片 2](https://priv-sdn-001.mowen.cn/mo/file/meta/76/69/96/2027738182736187393.png?Expires=1772371831&OSSAccessKeyId=LTAI5tE16jzdfWCPVBmyB5Nn&Signature=lBo%2BMpI87H4voKRpmXd1v8JyuOY%3D&response-expires=Sun%2C%2001%20Mar%202026%2013%3A30%3A31%20GMT&x-oss-process=image%2Fresize%2Cw_1200)

![图片 3](https://priv-sdn-001.mowen.cn/user/avatar/original/SL/HJ/SLHJ6XTP_enPqYDuizVH-/528a52b4d88d5289288946066bfc0b42.jpg?Expires=1772586490&OSSAccessKeyId=LTAI5tE16jzdfWCPVBmyB5Nn&Signature=o2MDY%2BY3hhkWIrEcpN5GuCXqIN8%3D&response-expires=Wed%2C%2004%20Mar%202026%2001%3A08%3A10%20GMT&x-oss-process=image%2Fresize%2Cw_240)

![图片 4](https://priv-sdn-001.mowen.cn/mo/file/meta/31/07/94/1841511909496111105.jpg?Expires=1772527798&OSSAccessKeyId=LTAI5tE16jzdfWCPVBmyB5Nn&Signature=ngPhIQar2ufu88ZhUds1e1SjhsU%3D&response-expires=Tue%2C%2003%20Mar%202026%2008%3A49%3A58%20GMT&x-oss-process=image%2Fresize%2Cw_240)

