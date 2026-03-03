# ai-dev-spec

AI 开发工作流生成器插件。根据项目类型（新建/维护/重构）和代码库深度分析，自动生成定制化的 AI 开发配置。

## 项目结构

- `.claude-plugin/` — Plugin 清单
- `skills/ai-workflow/` — 核心 Skill
  - `SKILL.md` — 编排逻辑
  - `scripts/analyze_codebase.py` — 代码库分析脚本
  - `references/` — 工作流方法论文档
  - `templates/` — 输出模板
    - `claude-md/` — CLAUDE.md 模板
    - `constitution/` — 宪法模板
    - `project-context/` — 项目上下文模板
    - `workflow-guide/` — 工作流文档模板
    - `commands/` — Slash 命令模板（生成到目标项目 `.claude/commands/`）

## 开发规范

- 分析脚本仅使用 Python3 标准库，不依赖第三方包
- SKILL.md 使用祈使句式（非第二人称）
- 模板中使用 `{{PLACEHOLDER}}` 格式的占位符
- 引用插件内文件使用 `${CLAUDE_PLUGIN_ROOT}` 变量
- 文档联动更新：修改任何文档时，检查并同步更新所有关联文档。关联关系包括：
  - `SKILL.md` ↔ `references/*.md`：编排逻辑引用的方法论
  - `SKILL.md` ↔ `templates/**/*.md`：编排逻辑引用的模板
  - `templates/` 同类型文件互相关联（如 `constitution/refactor.md` ↔ `workflow-guide/refactor.md`）
  - `CLAUDE.md` ↔ `SKILL.md`：项目结构描述与实际编排逻辑
