# 8 Claude Code Hooks That Automate What You Keep Forgetting

## 作者信息
- **作者**：darkzodchi (@zodchiii)
- **平台**：X (Twitter)
- **发布时间**：2026年4月3日
- **原始链接**：https://x.com/i/status/2040000216456143002
- **浏览量**：111万+

## 核心内容

### 问题
你告诉 Claude Code 做某件事，但它没做：
- 你说格式化代码——它没做
- 你说别动那个文件——它动了
- 你说完成前运行测试——它忘了

**原因：CLAUDE.md 是建议，Claude 大约只遵循 80%。Hooks 则不同——它们是自动触发的。**

### Hooks 如何工作

两种主要类型：
- **PreToolUse**：Claude 做某事前运行，可以阻止（返回 exit code 2）
- **PostToolUse**：Claude 做某事后运行，可以运行清理/格式化/测试/日志

### 8个 Claude Code Hooks

**1. 自动格式化每个文件**
每次写入/编辑后自动运行 Prettier。

**2. 阻止危险命令**
阻止 `rm -rf`、`git reset --hard`、`DROP TABLE` 等危险操作。

**3. 保护敏感文件**
阻止编辑 .env、package-lock.json、*.pem 等文件。

**4. 每次编辑后运行测试**
代码变更后自动运行测试套件，失败时 Claude 立即修复。

**5. PR 前必须测试通过**
阻止测试失败的 PR 创建。

**6. 自动 lint 并报告错误**
ESLint 检查，违规时 Claude 立即修复。

**7. 记录每个命令**
时间戳记录 Claude 运行的所有命令，便于调试。

**8. 每次任务完成后自动提交**
Claude 停止工作时自动 git commit，保持提交原子化。

### 关键洞察

好用的 Claude Code 和极好用的区别不在于模型或提示词，而在于 **Hooks**。

---

## 数据亮点
- 浏览量：111万+
- 转发：1,607
- 评论：126
- 点赞：8,194
