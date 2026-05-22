---
title: Macmini x OpenClaw 保姆级配置教程(全网最简单)
author: "雪踏乌云 (@Pluvio9yte)"
date: 2026-02-28T00:59:00+08:00
source: "https://x.com/Pluvio9yte/status/2027428387937996998"
tags:
  - twitter
  - article
---

# Macmini x OpenClaw 保姆级配置教程(全网最简单)

**作者**: 雪踏乌云 (@Pluvio9yte)
**时间**: 2026-02-28T00:59:00+08:00
**来源**: [原始链接](https://x.com/Pluvio9yte/status/2027428387937996998)

---

如果你也想把 Macmini 变成 24h 在线的 私人秘书，这篇就是保姆级喂饭教程！

前期准备：
任何一家的大模型调用的 base url 和 key(附免费和低价方案)
Clash Verge(或其他工具) + 翻墙节点
UU远程(提供远程桌面)

步骤 1：安装依赖
OpenClaw 需要 Homebrew 和 Node.js 等工具。
打开 终端（Terminal），运行以下命令：
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

安装 Node.js
brew install nodejs

步骤2：安装Claude Code
这是我们最重要的一步，因为假如后面出现任何问题，我们都可以让 Claude Code 修复 OpenClaw
npm install -g @anthropic-ai/claude-code

然后直接导入 Claude Code 的环境变量
export ANTHROPIC_BASE_URL="你的提供商链接"
export ANTHROPIC_AUTH_TOKEN="你的API密钥"

这里介绍一下我的 半公益Claude站 clawstoken.com 15块钱100美金
渠道目前是 AWS Kiro 逆向，假如用户多后续会上满血 Claude Max
因为是半公益且只有我一个人维护，所以主打一个低价但是不稳定
(Sonnet模型目前可用性为90% Opus模型不稳定)
需要可以联系我，目前为了稳定暂时每天只开放2000美金售卖额度。

步骤3：安装 OpenClaw
curl -fsSL https://openclaw.ai/install.sh | bash

安装脚本完成后，在终端继续运行：
openclaw onboard

步骤4：配置OpenClaw
这里也是我们最重要的一步，有如下两个选择
1)假如你有下列模型的管订账号，直接选择跳转登录即可
2)假如你没有下列模型的官订账号，则进行如下配置：
我们跳过模型的秘钥选择(因为大部分人包括我都没有管订账号)，所以后面让Claude Code给我们自己配置第三方。
如下图，直接选择最后一步跳过。
后面的选择根据我们自己的需要，一步步配置即可。

步骤5：配置 Telegram 或 Discord
假如上一步我们没有选择模型，则直接将我们模型提供商的URL和Key给Claude Code，并发送下面的提示词：
“这是我的URL和Key，帮我配置OpenClaw”

步骤6：配置 Telegram 或 Discord(先提前配好翻墙环境)
这里Telegram会简单一些，Discord则是比较麻烦。如果使用TG，大概配置需要花费3分钟，Discord则需要10分钟

这里我的选择是 Telegram，因为添加新龙虾很简便：
在搜索栏搜索 @BotFather ，然后点击开始对话，如下图所示
如果没有消息，则发送 /start ，开始对话。
然后进行下图的配置，直接抄作业即可 (第二步名称可以自定义，第三步必须是英文名，并且以_bot结尾)。

然后拿到如图所示的Token，直接发给Claude Code，附带如下提示词：
“这是我的Telegram Bot 的 Token，帮我配置到 OpenClaw 中”

等待配置完成后，直接点击上图中下面返回的链接，就能够对话了。

到这里基本就配置完成可以对话了，下面是额外配置，但是非必须

配置1：网络代理 (假如上面配置完成后还不能对话)
这里还是使用你的翻墙软件，并且导入订阅链接后，打开TUN模式。
然后给Claude Code发送这段话：
“帮我配置OpenClaw的环境，使其适配目前的网络代理”

Claude Code 配置完成后，你的龙虾就能够翻墙了。

配置2：大模型
目前龙虾中最为强力的模型还是Claude的Sonnet和Opus，如果你是土豪，可以直接买中转站的原生Claude Max，但是大部分OpenClaw的用量其实一天有保底100美金。

所以这里推荐我的逆向半公益站和免费站AnyRouter，AnyRouter目前只能使用Linuxdo登录了，每天签到赠送25$，我的公益站提供逆向AWS的Claude Sonnet模型，便宜不稳定，15元100刀。

但是也有其他的选择，比如说GPT-5(来自Codex)、GLM-5、MiniMAX、Kimi等，效果会差一点

配置3：UU远程

下载UU远程，安装到Macmini上，然后在我们经常用的电脑上也安装一个，如图所示

好处是：
1. 手机\电脑都能够操控Macmini远程桌面(不需要显示器了)
2. OpenClaw挂掉了，我们随时能够通过远程桌面的Claude Code来重启OpenClaw

看到这里了，相信大家都能顺利配置好OpenClaw，欢迎关注我 @Pluvio9yte ，祝大家都能够顺利获得自己的 私人秘书！

---

## 图片

![Image 1](https://pbs.twimg.com/media/HCLLD4kXgAAghUS?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HCLYoDOXUAc32To?format=png&name=900x900)

![Image 3](https://pbs.twimg.com/media/HCLbaHyXUAsB1Us?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HCLddSKa0AAuuTz?format=jpg&name=medium)

