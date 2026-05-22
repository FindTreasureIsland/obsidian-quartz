---
title: "OpenClaw 实战：用 AI Agent 做企业运维自动化"
author: "安仔 (@geekshellio)"
date: 2026-03-01 07:30
source: "https://x.com/geekshellio/status/2028010025927774278"
tags:
  - twitter
  - article
  - AI
  - OpenClaw
  - 运维自动化
  - 案例分享
---

# OpenClaw 实战：用 AI Agent 做企业运维自动化

**作者**: 安仔 (@geekshellio)
**时间**: 2026-03-01 07:30
**来源**: [原始链接](https://x.com/geekshellio/status/2028010025927774278)

---

过完个年，上班后才意识到，公司网络设备越来越多了，每天早上第一件事就是检查设备状态。

一开始还好，就十几台设备，SSH 登录、跑几条命令、看看日志，半小时搞定。但设备一多，问题就来了。

## 每天要检查的东西

- Ping 通不通？
- 网卡绑定状态正常吗？
- OSPF 邻居建立了吗？
- 设备在监控平台上显示正常吗？

**流程是这样的：**
1. SSH 登录每台设备
2. 手动执行命令
3. 复制日志到 Excel
4. 打开浏览器截图
5. 粘贴到文档
6. 重复 30 遍

一套流程下来，至少 2 小时。更要命的是，这事儿每天都要做。周末也不能停，因为设备不会因为你休息就不出问题。

## 试过传统自动化的问题

我试过写 Shell 脚本自动化，但遇到几个问题：

### 问题 1：异常处理太复杂

设备登录有时候会卡住，有时候密码过期，有时候网络抖动。每种情况都要写 if-else，代码越写越长，维护成本越来越高。

### 问题 2：浏览器操作很难自动化

有些检查必须看 Web 界面（比如 OSPF 邻居状态、LibreNMS 监控平台）。用 Selenium 写自动化脚本，光是处理登录、等待页面加载、定位元素，就要写几百行代码。

### 问题 3：结果汇总很麻烦

日志要写入飞书表格，截图要粘贴到文档。飞书 API 不支持直接插入图片，只能手动粘贴。自动化到一半又变成手动了。

## 为什么想到用 OpenClaw

其实之前看到 OpenClaw 刚发布时，当时没太在意，觉得又是一个 AI 聊天工具。

直到看到它内置的 browser 工具演示：可以自动打开网页、登录、点击、截图、复制到剪贴板。我突然意识到，这不就是我需要的吗？

传统自动化脚本的问题在于：你要预判所有可能的情况，写死每一步的处理逻辑。

但 OpenClaw 不一样，你只需要告诉它「去检查这些设备，把结果写到表格里」，它自己会想办法完成：
- SSH 登录失败了？它会重试
- 页面加载慢了？它会等
- 元素找不到了？它会换个方式定位

**这才是真正的自动化。**

---

## AI 自动化 vs 传统自动化：本质区别

很多人会问：这和写 Shell 脚本，用 Ansible、Puppet 有什么区别？

### 区别在于：决策能力

**传统自动化：规则驱动**

```bash
if [ $status -eq 0 ]; then
    echo "成功"
else
    echo "失败"
fi
```

你要提前定义好所有规则。遇到新情况，就要改代码。

| 优点 | 缺点 |
|------|------|
| 执行速度快 | 维护成本高 |
| 结果可预测 | 适应性差 |
| 适合标准化流程 | 无法处理模糊需求 |

**AI 自动化：目标驱动**

```
去检查这些设备，把结果写到表格里
```

你只需要告诉它目标，它自己决定怎么做。

| 优点 | 缺点 |
|------|------|
| 适应性强 | 执行速度慢 |
| 维护成本低 | 结果有一定随机性 |
| 可以处理模糊需求 | 成本高 |

## 什么时候用 AI 自动化？

**适合 AI 自动化：**
- 流程复杂，异常情况多
- 需要跨多个工具（SSH + 浏览器 + API）
- 需要人工判断的环节（比如「截图看起来正常吗？」）
- 频率不高，但很重要（比如每天一次的设备巡检）

**适合传统自动化：**
- 流程简单，标准化执行
- 频率高（比如每秒几千次）
- 对速度和成本敏感
- 结果必须 100% 可预测

---

## 用 OpenClaw 搭建自动化系统

我写了一个 Skill（OpenClaw 的扩展能力），让它自动完成整个流程。

### 1. SSH 自动登录 + 抓日志

设备需要两级认证（先 admin 再 root），手动登录很烦。用 expect 脚本自动化：

```bash
#!/usr/bin/expect
spawn ssh admin@192.168.1.100
expect "password:"
send "admin_password\r"
expect "$ "
send "login\r"
expect "Username:"
send "root\r"
expect "Password:"
send "root_password\r"
expect "# "
send "tail -n 10 /var/log/ping.log\r"
expect "# "
send "exit\r"
```

OpenClaw 调用这个脚本，拿到日志内容，直接写入飞书表格。

### 2. 浏览器自动截图

有些检查需要看 Web 界面（比如 OSPF 邻居状态、LibreNMS 监控平台）。

OpenClaw 的 browser 工具可以：
1. 打开设备管理页面
2. 自动登录
3. 执行筛选操作（比如只看 Network 类型设备）
4. 全页截图
5. 复制到剪贴板
6. 打开飞书表格
7. 定位到指定单元格
8. Cmd+V 粘贴

整个过程完全自动化，不需要人工干预。

### 3. 结果写入飞书表格

所有测试结果统一写入飞书 Sheets：

| 列 | 内容 |
|----|------|
| A 列 | 设备名称（Router-A、Router-B、Switch-C） |
| B 列 | 测试项（Ping，Bonding、OSPF） |
| C 列 | 状态（待审阅/成功/失败） |
| D 列 | 证据（文本日志或截图） |

> 注意：这是飞书的传统电子表格文档，不是多维表格。多维表格才支持 API 调用直接插入图片。

---

## 核心架构

整个系统由四个核心模块组成：
- SSH 自动化（expect）
- OpenClaw Skill
- 浏览器自动化（browser tool）
- 飞书 API（结果写入）

### 代码结构

```
bashdevice-check/
├── SKILL.md              # Skill 说明文档
├── check.sh              # 主入口脚本
├── config.sh             # 配置文件（设备 IP、密码、表格 ID）
├── lib/
│   ├── ssh-helper.sh     # SSH 连接封装
│   ├── feishu-api.sh     # 飞书 API 封装
│   └── browser-helper.sh # 浏览器操作封装
└── tests/
    ├── router-tests.sh   # 路由器设备测试
    ├── switch-tests.sh   # 交换机设备测试
    └── firewall-tests.sh # 防火墙设备测试
```

### 关键代码片段

**SSH 抓日志：**

```bash
test_ping() {
  local device_ip="$1"
  local row_num="$2"

  # SSH 登录并执行命令
  local log_content=$(expect ssh-login.exp "$device_ip" "tail -n 10 /var/log/ping.log")

  # 写入飞书表格
  update_feishu_cell "$row_num" "C" "待审阅"
  update_feishu_cell "$row_num" "D" "$log_content"
}
```

**浏览器截图：**

```bash
test_ospf() {
  local device_ip="$1"
  local row_num="$2"

  # 打开设备管理页面
  openclaw browser open "https://$device_ip/admin/ospf"

  # 登录
  openclaw browser type "username" "admin"
  openclaw browser type "password" "admin_password"
  openclaw browser click "login_button"

  # 截图
  openclaw browser screenshot "/tmp/ospf.png"

  # 复制到剪贴板
  osascript -e "set the clipboard to (read (POSIX file \"/tmp/ospf.png\") as JPEG picture)"

  # 打开飞书表格并粘贴
  openclaw browser open "https://feishu.cn/sheets/xxx"
  openclaw browser click "cell_D$row_num"
  openclaw browser press "Cmd+V"

  # 写入状态
  update_feishu_cell "$row_num" "C" "待审阅"
}
```

### 使用方式

```bash
# 测试单个设备的单个项目
bash check.sh test router-a ping

# 测试单个设备的所有项目
bash check.sh test router-a all

# 运行所有设备的所有测试
bash check.sh run-all

# 创建新的日期标签页并运行测试
bash check.sh run-all --new-tab
```

---

## 变成 Skill 的好处

把这套流程封装成 OpenClaw Skill 之后，最大的好处是可以定时自动执行。

**现在的设置：**
- 每天早上 8:30 自动运行一次
- 等同事 9 点上班的时候，飞书表格里已经有最新的测试结果了

### 实际效果

| 时间 | 操作 |
|------|------|
| 8:30 | OpenClaw 自动执行检查 |
| 8:35 | 所有设备检查完成，结果写入飞书 |
| 9:00 | 同事上班，打开飞书直接看结果 |
| 9:05 | 发现问题，立即处理 |

以前是同事上班后，我才开始检查，发现问题已经 9:30 了。现在问题在上班前就发现了，节省了至少半小时响应时间。

### 多环境复用

Skill 的另一个好处是可以复用。我们有测试环境、预发布环境、生产环境，每个环境都要做设备巡检。

```bash
# 测试环境
bash check.sh run-all --config config-test.sh

# 预发布环境
bash check.sh run-all --config config-staging.sh

# 生产环境
bash check.sh run-all --config config-prod.sh
```

甚至可以给不同环境设置不同的定时任务：

| 环境 | 检查频率 |
|------|----------|
| 测试环境 | 每天 1 次（早上 8:30） |
| 预发布环境 | 每天 2 次（早上 8:30、下午 2:30） |
| 生产环境 | 每天 4 次（8:30、12:30、16:30、20:30） |

---

## 实际效果

### 测试结果示例

**文本日志（Ping 测试）：**

```
2026-02-27 12:00:31 T=1 OK=1 LOSS%=0 RTTavg=43ms HILAT=0
2026-02-27 12:01:31 T=1 OK=1 LOSS%=0 RTTavg=42ms HILAT=0
2026-02-27 12:02:31 T=1 OK=1 LOSS%=0 RTTavg=44ms HILAT=0
...
```

**截图（OSPF 邻居）**：显示 2 个 OSPF neighbors（10.181.221.84，10.181.221.85）和 5 条路由。

**截图（LibreNMS 监控）**：显示 14 台 Network 设备（Cisco、Juniper、H3C），全部在线。

### 时间对比

| 方式 | 耗时 |
|------|------|
| 手动操作 | 2 小时 |
| 自动化后 | 5 分钟（全程无人值守） |

**节省了 95% 的时间。**

---

## 踩过的坑

### 1. 飞书 API 不支持直接插入图片

飞书的电子表格 API 只能写文本，不能直接插入图片。

**解决方案**：通过浏览器自动化，模拟人工粘贴操作。

### 2. SSH 两级认证

设备需要先用 admin 登录，再切换到 root。

**解决方案**：用 expect 脚本处理交互式登录。

### 3. 浏览器 SSL 证书警告

设备的 Web 界面用的是自签名证书，浏览器会弹警告。

**解决方案**：OpenClaw 的 browser 工具可以自动处理证书警告。

### 4. 日志格式不统一

不同设备的日志格式不一样，正则表达式很难写。

**解决方案**：直接把原始日志写入表格，不做过滤。人工审阅时再判断。

---

## 可以复制到哪些场景？

这套方法可以用到很多地方：

| 场景 | 应用 |
|------|------|
| 服务器巡检 | 检查 CPU、内存、磁盘、进程状态 |
| 数据库备份验证 | 检查备份文件是否存在，大小是否正常 |
| 网站可用性监控 | 定时访问网站，截图保存 |
| 日志分析 | 从多台服务器抓日志，汇总到一个表格 |
| 合规审计 | 自动收集证据（日志、截图、配置文件） |

**核心思路**：把重复性的人工操作，拆解成「SSH + 浏览器 + API」的组合，让 OpenClaw 自动执行。

---

## 下一步计划

目前只实现了 5 个测试项，还有很多可以做：

- 其他设备的测试（更多路由器、交换机）
- 更多测试项（Syslog、日志上传、NTP、备份文件）
- 异常告警（测试失败时发送通知到企业微信/钉钉）
- 历史记录（每天创建新的标签页，保留历史数据）
- 趋势分析（统计设备故障率、响应时间变化）

### 定时任务的更多玩法

除了每天固定时间执行，还可以：

- **按需触发**：在飞书群里发 /check 命令，立即执行检查
- **故障自愈**：检测到问题后，自动重启服务或切换备用设备
- **智能调度**：根据历史数据，在设备最容易出问题的时间段增加检查频率

这些都是传统自动化脚本很难做到的，但用 OpenClaw 可以很容易实现。

---

## 结语

> OpenClaw 的价值在于「把 AI 当员工，不是当工具」。

传统的自动化脚本，你要写很多代码，处理各种异常情况。用 OpenClaw，你只需要告诉它「去检查这些设备，把结果写到表格里」，它自己会想办法完成。

SSH 登录、浏览器操作、API 调用、剪贴板操作，这些都是 OpenClaw 自带的能力。你只需要把它们组合起来，就能搭出一套完整的自动化系统。

如果你也有类似的重复性工作，可以试试这个思路。代码不需要很复杂，关键是把流程拆清楚，让 AI 一步步执行。

---

## 图片

![Image 1](https://pbs.twimg.com/media/HCTu7nzasAA_IQ-?format=jpg&name=medium)

![Image 2](https://pbs.twimg.com/media/HCTvT1TbcAAVbkc?format=jpg&name=medium)

![Image 3](https://pbs.twimg.com/media/HCTvWssbAAA5KJd?format=jpg&name=medium)

![Image 4](https://pbs.twimg.com/media/HCTve82bEAY7lLJ?format=jpg&name=medium)

![Image 5](https://pbs.twimg.com/media/HCTvhoeaQAAxAtg?format=jpg&name=medium)

![Image 6](https://pbs.twimg.com/media/HCTvj29bEAAqLzz?format=jpg&name=medium)

![Image 7](https://pbs.twimg.com/media/HCTwH0-bEAELJBS?format=jpg&name=medium)

![Image 8](https://pbs.twimg.com/media/HCTwOl-aUAEN7Iq?format=jpg&name=medium)
