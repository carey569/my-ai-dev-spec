# ai-dev-spec

AI 开发工作流生成器插件（Claude Code Plugin）。根据项目类型（新建 / 维护 / 重构）和代码库深度分析，自动生成定制化的规范驱动（Spec-Driven）AI 开发配置。

综合了 [Spec-Kit](https://github.com/spec-kit)、[OpenSpec](https://github.com/openspec)、[Superpowers](https://github.com/superpowers) 和 [BMAD Method](https://github.com/bmad-method) 四大框架的最佳实践。

## 功能概览

| 输入 | 输出 |
|------|------|
| 项目路径（或当前目录） | `CLAUDE.md` — AI 行为指南 + 项目上下文 |
| 项目类型（可选，支持自动推断） | `.spec/constitution.md` — 项目治理宪法 |
| 代码库分析数据 | `.spec/project-context.md` — 技术栈、架构、约定 |
| 用户意图描述 | `.spec/workflow.md` — 分阶段开发工作流 |
| | `.spec/intent.md` — 项目意图文档（新建/重构） |
| | `.spec/specs/` — 活文档规范工作区 |
| | `.spec/changes/` — 变更追踪（维护/重构） |
| | `.claude/skills/*/SKILL.md` — 14 个项目级 AI Skills |

### 支持的项目类型

- **new**（0→1）— 全新项目，从规范到实现
- **maintenance** — 已有项目的持续开发与维护
- **refactor** — 遗留系统重构/迁移（支持原地重构和全新目录两种方式）

## 安装

### 从 Git 仓库安装

```shell
# 1. 添加仓库作为 marketplace
/plugin marketplace add carey569/my-ai-dev-spec

# 2. 安装插件
/plugin install ai-dev-spec@ai-dev-spec
```

支持多种 Git 来源：

```shell
# GitHub（owner/repo 格式）
/plugin marketplace add carey569/my-ai-dev-spec

# HTTPS
/plugin marketplace add https://github.com/carey569/my-ai-dev-spec.git

# SSH
/plugin marketplace add git@github.com:carey569/my-ai-dev-spec.git

# 指定分支或标签
/plugin marketplace add https://github.com/carey569/my-ai-dev-spec.git#v1.0.0
```

### 从本地目录安装

```shell
# 1. 克隆仓库
git clone https://github.com/carey569/my-ai-dev-spec.git

# 2. 添加本地 marketplace
/plugin marketplace add ./ai-dev-spec

# 3. 安装
/plugin install ai-dev-spec@ai-dev-spec-marketplace
```

### 开发调试

```shell
claude --plugin-dir ./ai-dev-spec
```

## 使用方法

安装后，在 Claude Code 中用自然语言触发即可：

```
生成AI工作流
```

```
generate AI workflow for this project
```

```
帮我分析这个项目并生成开发配置
```

也可以带参数指定项目类型和路径：

```
生成AI工作流 refactor /path/to/legacy-project
```

### 工作流程

1. **输入收集** — 确定项目路径和类型
2. **代码库分析** — 自动分析技术栈、架构、测试、Git 历史等
3. **类型确认** — 确认或推断项目类型（new / maintenance / refactor）
4. **意图收集** — 通过自由描述或引导式问答收集项目目标（new / refactor）
5. **模板加载** — 读取方法论文档和输出模板
6. **文件生成** — 替换占位符，生成所有配置文件
7. **验证汇总** — 检查生成完整性，提供后续操作建议

### 生成的 Skills（14 个）

**通用 Skills（7 个）**：

| Skill | 说明 |
|-------|------|
| `analyst` | 需求发现与头脑风暴（BMAD Analyst） |
| `pm` | 规范编写，Given/When/Then 场景（BMAD PM） |
| `architect` | 技术设计与任务分解（BMAD Architect） |
| `adr` | 架构决策记录（Spec-Kit ADR） |
| `dev` | 规范驱动实现（BMAD Dev + Superpowers） |
| `tdd` | TDD 红绿重构循环（Superpowers） |
| `qa` | 全面代码审查（BMAD QA） |

**项目专用 Skills（7 个）**：

| Skill | 说明 |
|-------|------|
| `scaffold` | 项目脚手架 |
| `bugfix` | Bug 诊断与修复 |
| `dep-update` | 依赖管理与升级 |
| `incident` | 事故响应 |
| `legacy-analyze` | 遗留代码分析 |
| `migrate` | 模块迁移 |
| `parity-check` | 功能对等性验证 |

所有 14 个 Skills 会生成到每个项目中，无论项目类型。

## 项目结构

```
ai-dev-spec/
├── .claude-plugin/
│   ├── plugin.json              # 插件清单
│   └── marketplace.json         # Marketplace 索引
├── skills/
│   └── ai-workflow/
│       ├── SKILL.md             # 核心编排逻辑（7 个阶段）
│       ├── scripts/
│       │   └── analyze_codebase.py  # 代码库分析脚本（纯 Python3 标准库）
│       ├── references/
│       │   ├── spec-driven-principles.md   # 四大框架综合方法论
│       │   ├── analysis-guide.md           # 分析数据解读与类型推断
│       │   ├── workflow-new-project.md     # 新建项目工作流方法论
│       │   ├── workflow-maintenance.md     # 维护项目工作流方法论
│       │   └── workflow-refactor.md        # 重构项目工作流方法论
│       └── templates/
│           ├── claude-md/          # CLAUDE.md 输出模板（3 类型）
│           ├── constitution/       # 项目治理宪法模板（3 类型）
│           ├── project-context/    # 项目上下文模板（3 类型）
│           ├── workflow-guide/     # 工作流文档模板（3 类型）
│           ├── intent/             # 意图文档模板（new / refactor）
│           └── commands/           # Skills 模板
│               ├── common/         #   通用（7 个）
│               ├── new-project/    #   新建项目（1 个）
│               ├── maintenance/    #   维护项目（3 个）
│               └── refactor/       #   重构项目（3 个）
├── CLAUDE.md                    # 插件自身的开发规范
└── README.md
```

## 方法论

本插件综合了四个规范驱动开发框架的核心理念：

| 框架 | 核心贡献 |
|------|----------|
| **Spec-Kit** | Constitution（治理宪法）、ADR、规范流水线 |
| **OpenSpec** | Delta Specs（ADDED/MODIFIED/REMOVED 变更追踪）、生命周期管理 |
| **Superpowers** | TDD 强制执行、证据驱动验证 |
| **BMAD Method** | 角色代理（PM/Architect/Dev/QA）、规模自适应（Quick Flow / Full Method） |

**核心原则**：

1. **先规范后代码** — 没有规范不写实现
2. **宪法治理** — 不可违反的项目原则
3. **渐进式上下文** — 分层、按需加载的上下文文件
4. **TDD 强制** — 测试先行，用证据验证
5. **文档联动** — 更新任何文档时同步更新关联文档

## 开发规范

面向插件本身的开发：

- 分析脚本仅使用 Python3 标准库，不依赖第三方包
- SKILL.md 使用祈使句式（非第二人称）
- 模板中使用 `{{PLACEHOLDER}}` 格式的占位符
- 引用插件内文件使用 `${CLAUDE_PLUGIN_ROOT}` 变量
- 文档联动更新（详见 [CLAUDE.md](CLAUDE.md)）

## License

MIT
