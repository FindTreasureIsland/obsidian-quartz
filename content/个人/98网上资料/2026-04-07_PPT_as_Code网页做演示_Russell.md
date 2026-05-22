# PPT as Code：用网页高效做出比PPT还惊艳的演示文稿

## 作者信息
- **作者**：Russell (@Russell3402)
- **平台**：X (Twitter)
- **发布时间**：2026年4月4日 21:57
- **原始链接**：https://x.com/i/status/2040428571064484221
- **浏览量**：32万+

## 核心内容

### 问题定义
传统PPT的痛点：
- AI生成的PPT太丑，排版问题太多
- 修着修着发现还不如自己做
- 时间花在和工具拉扯上，而不是表达上

### PPT as Code的底层模型
演示系统只需要这五件事：
1. **container** — 演示容器，也就是舞台
2. **slides** — 每一页内容
3. **index** — 当前页索引
4. **controls** — 按钮、键盘、分页器、URL
5. **motion** — 切换时怎么动

### 底层技术栈
- transform + transition
- scroll-snap
- History API
- WAAPI (Web Animations API)
- View Transition API
- reveal.js

### 核心观点
> 把一次性的演示文件，变成一套可复用、可迭代、可扩展的内容资产。

### 框架选择
- 最小版本：原生 HTML + CSS + JS
- 进阶：reveal.js（Markdown支持、auto-animate、fragments）

### 设计系统
做好网页PPT需要先定四件事：
1. 字体系统
2. 颜色系统
3. 间距系统
4. 组件系统

### 金句
> 代码会越来越像材料，prompt会越来越像起点，但对结构、节奏、可讲性和可维护性的判断，才是最难被替代的部分。

---

## 数据亮点
- 浏览量：32万+
- 转发：205
- 评论：815
- 点赞：1,757
