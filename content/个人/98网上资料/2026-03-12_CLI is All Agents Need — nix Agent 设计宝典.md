---
title: CLI is All Agents Need — *nix Agent 设计宝典
author: "yan5xu (@yan5xu)"
date: 2026-03-12 04:15
source: "https://x.com/yan5xu/status/2031947154911351159"
tags:
  - twitter
  - article
---

# CLI is All Agents Need — *nix Agent 设计宝典

**作者**: yan5xu (@yan5xu)
**时间**: 2026-03-12 04:15
**来源**: [原始链接](https://x.com/yan5xu/status/2031947154911351159)

---

CLI is All Agents Need — *nix Agent 设计宝典

4148.7万

Why a single run(command) outperforms sprawling tool catalogs

当所有人在为 Agent 设计复杂的函数调用框架时，我发现：一个 run(command="...") 就够了。

本文由 AI Agent 协作完成，但每一个设计决策、每一次生产踩坑、以及把它们提炼成原则的思考过程，都是本人完成的。

为什么是 *nix

Unix 在 50 年前做了一个设计决策：一切皆文本流。

程序之间不交换复杂的二进制结构，不共享内存对象——它们通过文本管道沟通。小工具各司其职，通过 | 组合成强大的工作流。程序用 --help 描述自己，用 exit code 报告成败，用 stderr 传递错误上下文。

LLM 在 50 年后做了一个几乎相同的决策：一切皆 token。

它只理解文本，只输出文本。它的"思考"是文本，它的"行动"是文本，它从世界获得的反馈也必须是文本。

这两个决策跨越半个世纪，从完全不同的出发点，收敛到了同一个接口模型。

Unix 为人类终端操作者设计的文本系统——cat、grep、pipe、exit code、man page——对 LLM 来说不是"也能用"，而是天然适配。

LLM 在工具使用这件事上，本质就是一个终端操作者，只不过它比任何人类都快，而且它的训练数据里有大量 shell 命令与 CLI 用例。

这就是 *nix Agent 的核心哲学：不发明新的工具接口，把 Unix 已经验证了 50 年的设计直接交给 LLM。

为什么只有一个 run

单工具假说

主流 Agent 框架给 LLM 一堆独立工具：

bashtools: [search_web, read_file, write_file, run_code, send_email, ...]

LLM 每次调用前要做工具选择——用哪个？参数怎么填？工具越多，选择越难，准确率越低。认知负荷花在了"选工具"上，而不是"解决问题"上。

我的做法：一个 run(command="...")，所有能力通过 CLI 命令暴露。

run(command="cat notes.md")
run(command="cat log.txt | grep ERROR | wc -l")
run(command="see screenshot.png")
run(command="memory search 'deployment issue'")
run(command="clip sandbox bash 'python3 analyze.py'")

LLM 仍然需要选择"用什么命令"，但这和"从 15 个不同 schema 的工具中选一个"是完全不同的认知任务。命令选择是在一个统一的 namespace 里做字符串组合——而函数选择是在多个不相关的 API 间做模式切换。

LLM 的 CLI 母语

为什么 CLI 命令比结构化函数调用更适合 LLM？因为 LLM 的训练数据里，CLI 是最密集的工具使用范式。

GitHub 上数十亿行代码充满了：

bash

# README 里的安装指南
pip install -r requirements.txt && python main.py

# CI/CD 里的构建脚本
make build && make test && make deploy

# Stack Overflow 里的解决方案
cat /var/log/syslog | grep "Out of memory" | tail -20

我不需要教 LLM 如何使用 CLI——它已经会了。这种熟悉度是概率性的、模型相关的，但在主流模型上经验证非常可靠。

对比两种方式完成同一个任务：

任务：读取日志文件，找出错误行数

函数调用方式（3 次 tool call）：
1. read_file(path="/var/log/app.log") → 返回完整文件
2. search_text(text=<entire file>, pattern="ERROR") → 返回匹配行
3. count_lines(text=<matched lines>) → 返回数字

CLI 方式（1 次 tool call）：
run(command="cat /var/log/app.log | grep ERROR | wc -l")
→ "42"

一次调用替代三次。不是因为做了特殊优化——而是 Unix 管道天然支持组合。

让管道和链式执行成为可能

光有一个 run 不够。如果 run 只能执行单条命令，LLM 还是要多次调用才能完成组合任务。

所以我在命令路由层实现了一个链式解析器（parseChain），支持四种 Unix 操作符：

|   管道：前一个命令的 stdout 作为后一个的 stdin
&&  与链：前一个成功才执行后一个
||  或链：前一个失败才执行后一个
;   顺序：无论前一个成败都执行后一个

有了这个机制，LLM 的每一次 tool call 都可以是一个完整的工作流：

bash

# 一次 tool call：下载 → 查看
curl -sL $URL -o data.csv && cat data.csv | head 5

# 一次 tool call：读文件 → 过滤 → 排序 → 取前 10
cat access.log | grep "500" | sort | head 10

# 一次 tool call：尝试 A，失败则尝试 B
cat config.yaml || echo "config not found, using defaults"

N 个命令 × 4 种操作符，组合空间急剧扩大。而在 LLM 看来，这只是一个字符串——它已经从训练数据里学会了怎么写。

命令行就是 LLM 的母语工具接口。

启发式设计：让 CLI 引导 Agent 顺滑工作

单工具 + CLI 解决了"用什么"的问题，但 Agent 还需要知道"怎么用"。它没有搜索引擎，没有同事可以问。

我通过三个递进的设计手段，让 CLI 自身成为 Agent 的导航系统。

手段一：渐进式 --help 自发现

一个设计良好的 CLI 工具，用户不需要读文档就能上手——因为 --help 告诉了一切。我把同样的理念用在 Agent 身上，并且做成了渐进式披露：

Agent 不需要一次加载所有文档，而是按需逐层深入。

第零层：Tool Description → 命令列表注入

run 工具的 description 在每次对话开始时动态生成，列出当前所有已注册命令的一行摘要：

plaintext

Available commands:
  cat    — Read a text file. For images use 'see'. For binary use 'cat -b'.
  see    — View an image (auto-attaches to vision)
  ls     — List files in current topic
  write  — Write file. Usage: write <path> [content] or stdin
  grep   — Filter lines matching a pattern (supports -i, -v, -c)
  memory — Search or manage memory
  clip   — Operate external environments (sandboxes, services)
  ...

Agent 从第一轮就知道有哪些能力，但不需要知道每个命令的所有参数——那会浪费上下文。

注： 命令列表全量注入 vs 按需发现，随着命令增多这里存在上下文预算的权衡。目前还在探索更优的平衡方式，欢迎讨论。

第一层：command（无参数）→ 命令用法

Agent 对某个命令感兴趣时，直接调用它。没给参数？命令返回自己的用法：

plaintext

→ run(command="memory")
[error] memory: usage: memory search|recent|store|facts|forget

→ run(command="clip")
  clip list                              — list available clips
  clip <name>                            — show clip details and commands
  clip <name> <command> [args...]         — invoke a command
  clip <name> pull <remote-path> [name]   — pull file from clip to local
  clip <name> push <local-path> <remote>  — push local file to clip

​现在 Agent 知道 memory 有五个子命令，clip 可以 list/pull/push。只花了一次调用，没有多余信息。

第二层：command subcommand（缺参数）→ 具体参数

Agent 决定用 memory search，但不确定参数格式？继续深入：

plaintext

→ run(command="memory search")
[error] memory: usage: memory search <query> [-t topic_id] [-k keyword]

→ run(command="clip sandbox")
  Clip: sandbox
  Commands:
    clip sandbox bash <script>
    clip sandbox read <path>
    clip sandbox write <path>
  File transfer:
    clip sandbox pull <remote-path> [local-name]
    clip sandbox push <local-path> <remote-path>

渐进式披露：概览（注入）→ 用法（探索）→ 参数（深入）。 Agent 按需探索，每一层只获取当前需要的信息量。这和把所有文档塞进 system prompt 是完全不同的思路。

system prompt 里塞 3000 字的工具文档，大部分信息在大部分时候都用不到——白白占用上下文预算。渐进式 help 让 Agent 自己决定什么时候需要更多信息。

这也要求每个命令、每个子命令都必须有完整的 help 输出。不仅是给人看的，更是给 Agent 看的。一条好的 help 能让 Agent 一步到位，一条缺失的 help 意味着一次盲猜。

手段二：Error Message 纠偏

Agent 不可能永远走对路。关键不是阻止它犯错，而是让每个错误都指向正确方向。

传统 CLI 的错误信息给人看——人可以 Google。Agent 不能 Google。

所以要求每个错误同时包含"出了什么问题"和"该怎么做"：

传统 CLI：
  $ cat photo.png
  cat: binary file (standard output)
  → 人会 Google "how to view image in terminal"

我的设计：
  [error] cat: binary image file (182KB). Use: see photo.

---

## 图片

_无图片_
