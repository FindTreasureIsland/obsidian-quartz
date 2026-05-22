---
title: 什么是 Vibe Design？教你如何利用stitch一句话生成一整套UI页面
author: "小八 (@IceBearMiner)"
date: 2026-03-19T15:15:00
source: "https://x.com/IceBearMiner/status/2034529278625501627"
tags:
  - twitter
  - article
---

# 什么是 Vibe Design？教你如何利用stitch一句话生成一整套UI页面

**作者**: 小八 (@IceBearMiner)
**时间**: 2026-03-19T15:15:00
**来源**: [原始链接](https://x.com/IceBearMiner/status/2034529278625501627)

---

作为一个谷歌死忠粉，他家产品尤其是stitch和NotebookLM我是特别喜爱啊

所以看到这次stitch这么出圈非常高兴，这里给大家介绍介绍stitch这个产品是做什么的以及怎么更好的使用它

简单说，Stitch 就是"你说，它画"。告诉它你想要什么界面，它直接给你出设计稿，还支持导出到 Figma、AI Studio 等工具里。

---

## 三大更新亮点

这次更新主要有三个亮点我很喜欢，不仅重构了整个UI，还支持了无限画布

**1. 语音交互**

现在打开麦克风直接对着它说想法就行，Stitch 会一口气生成一系列设计图。

**2. 实时预览**

生成的 UI 不再是一张死图。拿这个播放器UI举例，你能直接点按钮、看交互，实打实先体验一遍。

**3. 统一并且复用风格**

你可以让 Stitch **读取现有网站的配色**，提取后自动生成设计稿，也能导出为 DESIGN.md 文件。

如果你已经有自己项目的 DESIGN.md，直接导入 Stitch 即可保持风格一致。

Google 还特地起了个名叫 **Vibe Design**。现在你甚至可以用**一句提示词生成整个 App 流程**，包含多个页面和主题。比如下面这条提示词：

> Create a mobile e-commerce app with home, product detail, cart, and checkout screens

---

## Stitch SDK

这里要强推一下 **Stitch SDK**——可以理解为 Stitch 的 CLI 版本，专门给 Agent 调用的。你不需要手动去网页端对话，让 Agent 根据项目需求自动调用 Stitch 就行。API Key 在这里创建，还能查看每日剩余额度。

这几天基于 SDK**做了一个套壳Agent**：
- 仅需提供后端 API 文档
- 自行选择/导入主题（或你自己的 DESIGN.md）
- 一键生成对应的前端页面

后续会开源，敬请期待。

---

## NotebookLM CLI

这里再推荐自己写的一个NotebookLM cli项目：让agent能自动化操作NotebookLM

自己利用NotebookLM cli搭配stitch sdk打造了属于自己的每日播客app和web

**网站原理如下：**
1. NotebookLM调研+生成播客
2. 利用whisper转字幕实现自动推送
3. github上传到vercel
4. 音频自动推送到cloudflare R2并转换成URL
5. 把URL塞进页面实现全自动推送

为啥多此一举呢？因为音频比较大，R2免费的容量能省不少事

现在已经集成到自己的龙虾，只需要提供一个主题，剩下基本全程丢给NotebookLM干了，节省token的同时效果还好

所有项目链接统一放评论区，感兴趣的可以去试试。有问题也欢迎评论区交流

---

## 图片

![Image 1](https://pbs.twimg.com/media/HDwYcl_bcAAAM0r?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HDwNPeqbsAA034c?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HDwNM4pbAAELOau?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HDwNaqqa4AAQ7Xf?format=jpg&name=medium)

![Image 5](https://pbs.twimg.com/media/HDwNzqubwAAA1Of?format=jpg&name=medium)

![Image 6](https://pbs.twimg.com/media/HDwN2NtboAA_GlQ?format=jpg&name=large)

![Image 7](https://pbs.twimg.com/media/HDwOVHIbEAAq8TP?format=jpg&name=medium)

![Image 8](https://pbs.twimg.com/media/HDwOS4JboAAl-mc?format=jpg&name=medium)

![Image 9](https://pbs.twimg.com/media/HDwOYVHbQAARbHj?format=jpg&name=large)

