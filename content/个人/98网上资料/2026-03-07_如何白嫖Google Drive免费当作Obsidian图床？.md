---
title: 如何白嫖Google Drive免费当作Obsidian图床？
author: "实践哥MinLi (@MinLiBuilds)"
date: 2026-03-06 16:33
source: "https://x.com/MinLiBuilds/status/2029958621208228143"
tags:
  - twitter
  - article
---

# 如何白嫖Google Drive免费当作Obsidian图床？

**作者**: 实践哥MinLi (@MinLiBuilds)
**时间**: 2026-03-06 16:33
**来源**: [原始链接](https://x.com/MinLiBuilds/status/2029958621208228143)

---

订阅 Gemini Pro 之后，Google 送了 2TB 的 Drive 空间。日常用不了多少，闲着也是浪费。

与此同时，写 Obsidian 笔记一直有个痛点：粘贴截图只能存本地，换设备就裂图，发博客更是灾难。各种图床要么收费，要么随时跑路。

直到最近推出了Google Workspace CLI(gws) ，终于可以在命令行直接操作 Drive 了。两件事一碰——2TB 空间 + 命令行上传 = 完美图床。

于是我写了 gbed：一个 200 多行的本地代理，让 Obsidian 粘贴图片时自动上传到 Google Drive，返回直链，无缝插入笔记。开源链接我会贴到文章后面。

## 工作原理

gbed 的核心思路很简单，简单来说，就是在本地起一个 HTTP 服务，接收图片上传请求，调用 gws 命令行工具把图片传到 Google Drive，然后返回一个可公开访问的直链。

整个数据流如下：

```
Obsidian (粘贴图片) → obsidian-image-uploader 插件 (HTTP POST) → gbed 本地服务 (http://127.0.0.1:52323/upload) → gws drive files create (上传至 Google Drive) → gws drive permissions create (设置为公开可读) ← 返回 {"url": "https://lh3.googleusercontent.com/d/FILE_ID"} ← 自动将 ![](url) 插入到 Markdown 文档中
```

从粘贴图片到插入链接，整个过程对用户来说是无感知的，体验和使用任何其他图床完全一致。

上传后的图片通过 https://lh3.googleusercontent.com/d/{FILE_ID} 这个 Google 的直链格式对外访问，不需要登录，浏览器直接渲染，非常适合作为 Markdown 图片链接使用。

## 快速上手

前置：安装 Google Workspace CLI 命令行工具 gws，可以帮我们用命令行访问谷歌所有资源，安装时我们只要勾选 googledrive 的权限。

安装：

npm install -g @minlibuilds/gbed

启动：

gbed

首次运行会自动在 Google Drive 创建 obsidian-images 文件夹。支持 gbed -d 后台运行，gbed --stop 停止。

配置 Obsidian 插件：

在 Obsidian 中安装 obsidian-image-uploader 插件，设置如下：

- Api Endpoint：http://127.0.0.1:52323/upload
- Upload Body：{"image": "$FILE"}
- Image Url Path：url

配置完成后，在 Obsidian 中粘贴图片就会自动上传并插入链接了。

## 为什么选择 Google Drive

稳定、免费、Google 基础设施、全球 CDN、数据掌控、有 gwc 作为控制。

最大的优点是：你的数据始终在你自己的 Google Drive 里。图床服务可能跑路，但 Google Drive 不太会。

## 总结

gbed 是一个很小的工具，核心逻辑只有两百多行代码。它做的事情也很简单——在 Obsidian 和 Google Drive 之间搭一座桥。但正是这种「刚好够用」的小工具，往往最能解决实际痛点。

Google Workspace CLI 的出现，让我们可以用命令行直接操作 Google 全家桶，gbed 只是其中一个应用场景。如果你也在用 Google 生态，不妨想想还能用 gws 做些什么有趣的事情。

项目地址：github.com/limin112/gbed

安装命令：npm install -g @minlibuilds/gbed

---

## 图片

![Image 1](https://pbs.twimg.com/media/HCvZ30NboAAUcd4?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HCvZDm4aUAMBbC5?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HCsl3jZaUAAYSnc?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HCvZoG4aUAIMo02?format=jpg&name=medium)

