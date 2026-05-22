# How we built a virtual filesystem for our Assistant

## 来源信息
- **作者**：Dens Sumesh (Mintlify)
- **平台**：Mintlify Blog
- **发布日期**：2026年3月24日
- **原始链接**：https://www.mintlify.com/blog/how-we-built-a-virtual-filesystem-for-our-assistant

## 核心内容

### 问题背景

RAG 很优秀，但在跨页查找精确语法时表现不佳。团队希望 AI 能像浏览代码库一样浏览文档。

**解决思路**：如果每个文档页面是一个文件，每个章节是一个目录，那么 grep、cat、ls、find 这些命令就是 AI 探索文档需要的所有工具。

---

### 容器瓶颈

传统方案是给 AI 一个真实的文件系统——启动隔离沙箱并克隆仓库。但有两个问题：

1. **延迟高**：P90 会话创建时间约 46 秒
2. **成本高**：每月 850,000 次对话，约需 $70,000+/年

---

### ChromaFs 解决方案

**核心思路**：AI 不需要真实的文件系统，只需要文件系统的幻觉。

构建在已有的 Chroma 数据库基础上，拦截 UNIX 命令并将其翻译成对同一数据库的查询。

**效果对比：**
| 指标 | Sandbox | ChromaFs |
|------|---------|----------|
| P90 启动时间 | ~46 秒 | ~100 毫秒 |
| 边际计算成本 | ~$0.0137/次对话 | ~$0（复用现有DB） |
| 搜索机制 | 线性磁盘扫描 | DB 元数据查询 |

---

### 技术实现

**1. 目录树引导**

整个文件树以 gzipped JSON 文档（`__path_tree__`）形式存储在 Chroma collection 中：

```json
{
  "auth/oauth": { "isPublic": true, "groups": [] },
  "auth/api-keys": { "isPublic": true, "groups": [] },
  "internal/billing": { "isPublic": false, "groups": ["admin", "billing"] }
}
```

**2. 访问控制**

使用 `isPublic` 和 `groups` 字段实现细粒度的权限控制：
- 普通用户看不到内部文档路径
- AI 无法访问或引用被剪枝的路径

**3. 页面重组**

文档被分块存储在 Chroma 中，`cat` 命令执行时：
- 获取所有匹配 slug 的块
- 按 chunk_index 排序
- 合并成完整页面

**4. Grep 优化**

两层过滤：
1. **粗粒度过滤（Chroma）**：识别可能包含匹配的文件
2. **细粒度过滤（内存）**：在 Redis 缓存的匹配块上执行正则匹配

---

### 核心优势

- **即时会话创建**：100 毫秒 vs 46 秒
- **零边际计算成本**：复用现有 DB 基础设施
- **内置 RBAC**：无需额外基础设施

---

### 关键洞察

> The agent doesn't need a real filesystem; it just needs the illusion of one.

ChromaFs 用虚拟文件系统替代沙箱，为数千个用户提供文档助手服务，每天处理 30,000+ 次对话。

---

## 延伸阅读
- Docs on autopilot: From zero to self-maintaining with Mintlify
- The state of agent traffic in documentation (March 2026)
