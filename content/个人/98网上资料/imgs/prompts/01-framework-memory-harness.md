---
illustration_id: 01
type: framework
style: blueprint
references: []
---

Memory is Harness - Agent架构对比图

技术蓝图风格框架图，对比两种架构设计模式。中文标注。

STRUCTURE: 左右分栏对比 + 底部隐喻注解

左侧面板 - 插件式架构（Plugin Approach）：
- 外层大框：Agent（智能体）
- Agent内部：Context Window（上下文窗口）
- Agent外部：Memory Plugin（内存插件）通过虚线箭头连接
- 标注：「Memory 作为外部插件」→「无法管理Context」
- 颜色：浅灰底，深灰框，虚线连接

右侧面板 - Harness架构（Harness Approach）：
- 外层大框：Harness（框架/底盘）
- Harness内部包含：
  1. Agent（智能体）核心
  2. Memory & Context Management（内存与上下文管理）作为内置核心能力
  3. 标注：「Context Management 是 Harness 的核心职责」
- 颜色：浅蓝底(#BFDBFE)，深蓝框(#1E3A5F)，实线连接

底部注解区域：
- 汽车与驾驶的隐喻：
  「驾驶 ≠ 汽车插件 | 驾驶 = 汽车的核心能力」
  「Memory ≠ Agent插件 | Memory = Harness的核心能力」
- 以虚线分隔

ZONES:
- Zone 1（左）: 插件式架构示意
- Zone 2（右）: Harness式架构示意
- Zone 3（下）: 核心隐喻总结

COLORS（严格蓝图配色）:
- 背景: #FAF8F5（蓝图纸白）
- 网格: #E5E5E5（浅灰格线）
- 主文字: #334155（深板岩）
- 主强调: #2563EB（工程蓝）
- 副强调: #1E3A5F（藏蓝）
- 填充: #BFDBFE（浅蓝）
- 警示: #F59E0B（琥珀色，用于「错误/问题」标注）

STYLE: 严格蓝图风格
- 细线等宽线条，工程图纸质感
- 网格背景叠加
- 90度直角连接线
- 标注文字用工程蓝图字体
- 精确几何形状
- 无手绘感、无有机曲线

ASPECT: 16:9
