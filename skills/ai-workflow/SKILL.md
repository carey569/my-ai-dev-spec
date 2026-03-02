---
name: ai-workflow
description: Generate AI development workflow configurations by analyzing codebase. Use when user asks to "generate AI workflow", "create development workflow", "set up AI development", "generate CLAUDE.md", "create project configuration", "analyze project for AI workflow", "spec-driven development setup", "规范驱动开发", "生成AI工作流", "创建开发工作流", "项目AI配置", "生成开发流程", or wants to configure a project for optimal AI-assisted spec-driven development. Analyzes codebase architecture, tech stack, quality infrastructure, and git history. Produces spec-driven AI configurations based on Spec-Kit, OpenSpec, Superpowers, and BMAD Method best practices. Supports project types new (0→1), maintenance, and refactor.
version: 2.0.0
---

# AI Workflow Generator (Spec-Driven)

Generate spec-driven AI development configurations by analyzing a project's
codebase. Synthesizes best practices from Spec-Kit (GitHub), OpenSpec,
Superpowers, and BMAD Method into customized project configurations.

## Quick Reference

| Input | Output |
|-------|--------|
| Project path (or cwd) | `CLAUDE.md` — AI behavioral guidelines + project context |
| Optional: project type | `.spec/constitution.md` — project governance principles |
| Codebase analysis | `.spec/project-context.md` — tech stack, conventions, constraints |
| | `.spec/workflow.md` — phased spec-driven development workflow |
| | `.claude/commands/*.md` — role-based slash commands (/tdd, /qa, /bugfix...) |
| | `.spec/specs/` — living specification workspace |
| | `.spec/changes/` — change tracking (maintenance/refactor) |

Supported types: `new` (0→1), `maintenance` (ongoing development), `refactor` (rewrite/restructure)

---

## Methodology

This skill synthesizes four leading spec-driven development frameworks.
Read `references/spec-driven-principles.md` for the full synthesis.

**Key principles applied:**
1. **Spec before code** — never implement without a specification (all four frameworks)
2. **Constitution** — non-negotiable project governance (Spec-Kit)
3. **Progressive context** — layered, load-on-demand context files (BMAD, OpenSpec)
4. **Role-based agents** — PM, Architect, Dev, QA personas for prompts (BMAD)
5. **TDD enforcement** — test-first, verify-with-evidence (Superpowers)
6. **Delta specs** — ADDED/MODIFIED/REMOVED tracking for existing codebases (OpenSpec)
7. **Scale-adaptive** — Quick Flow for small tasks, Full Method for features (BMAD)

---

## Phase 1: Input Collection

Parse `$ARGUMENTS` for optional parameters:
- Explicit type: `new` / `maintenance` / `refactor` (aliases: `0to1`, `maint`, `maintain`, `refac`)
- Explicit path: any valid directory path (defaults to cwd)
- Natural language: extract intent from free-form input

If no arguments provided, ask the user:
1. Which project directory to analyze (default: current working directory)
2. Whether they know the project type or prefer automatic inference

## Phase 2: Codebase Analysis

Execute the analysis script:

```bash
python3 "${CLAUDE_PLUGIN_ROOT}/skills/ai-workflow/scripts/analyze_codebase.py" TARGET_PATH
```

Capture JSON output. Handle edge cases:
- **Empty directory**: `total_files: 0`. Proceed with `new` type.
- **Script failure**: Fall back to manual analysis using Glob and Grep tools.
- **No Python3**: Perform manual analysis by reading key config files.

Present summary to user:

```
Project Analysis Summary
========================
Tech Stack:    [language] / [frameworks] / [package manager]
Architecture:  [pattern] ([confidence]%)
Scale:         [total files] files, [total lines] lines
Quality:       Testing: [framework] ([count] files) | CI: [platform] | Lint: [tools]
Git:           [commits] commits, [age] days, [contributors] contributors
Documentation: README [✓/✗] | CLAUDE.md [✓/✗] | API docs [✓/✗]
```

## Phase 3: Project Type Determination

Read `references/analysis-guide.md` for inference logic.

**If type provided via arguments**: Confirm alignment with analysis.
**If type NOT provided**: Present inference with top 3 signals, ask user to confirm.

Wait for confirmation before proceeding.

## Phase 4: Intent Collection

> **Applies to**: `new` and `refactor` only. Skip this phase for `maintenance`.

Collect user intent to populate intent-specific placeholders across all output templates.
This produces richer, more accurate configurations compared to relying solely on codebase analysis.

### Step 1: Check for Existing Intent in Arguments

Scan `$ARGUMENTS` for intent signals (e.g., "I want to build a ...", "We're migrating because ...").
If found, extract structured data and present for confirmation. If confirmed, skip to Step 4.

### Step 2: Offer Collection Mode

Detect the conversation language and use the same language for all prompts below.

Present three options:

1. **Free-form input** — "Describe your project in your own words and I'll extract the key details"
2. **Guided questions** — "I'll ask 7 short questions to understand your goals"
3. **Skip** — "Proceed without intent collection (placeholders will show `[NEEDS CLARIFICATION]`)"

### Step 3: Collect Intent

**Free-form mode**: Present a single open prompt:

> Tell me about this project — what are you building (or migrating), who is it for,
> what problem does it solve, and what constraints should I know about?

Parse the response to extract structured fields matching the intent template placeholders.
Ask a follow-up only if critical fields (Vision/Motivation, Success Criteria) are missing.

**Guided mode (new project)** — ask sequentially, one at a time:

1. What is your one-sentence vision for this project?
2. Who are the primary users or audience?
3. What core problem does this project solve?
4. What are the 3-5 key features or capabilities?
5. How will you measure success? (metrics, milestones, or outcomes)
6. What constraints exist? (timeline, tech mandates, team size, budget)
7. Any domain-specific terminology or context I should know?

**Guided mode (refactor)** — ask sequentially, one at a time:

1. What is the primary motivation for this refactor?
2. What does the target state look like? (architecture, quality, performance)
3. What are the biggest pain points with the current system?
4. Which modules or areas should be migrated first?
5. What must be preserved exactly as-is? (APIs, behaviors, contracts)
6. What constraints exist? (timeline, budget, team, compatibility)
7. How will you measure success for this refactor?

### Step 4: Confirm Intent Summary

Present a structured summary of collected intent data. Ask the user to confirm or edit.
Format the summary matching the intent template structure (`templates/intent/{type}.md`).

Once confirmed, store the intent data for use in Phase 6 template generation.

> **Fallback**: If the user chose "Skip" or any intent placeholder remains empty after collection,
> replace it with `[NEEDS CLARIFICATION]` and append a hint directing to `.spec/intent.md`.

## Phase 5: Load References and Templates

Based on confirmed type, read in this order:

1. `references/spec-driven-principles.md` — core methodology (always read)
2. `references/workflow-{type}.md` — type-specific workflow methodology
3. `templates/constitution/{type}.md` — constitution template
4. `templates/project-context/{type}.md` — project-context template
5. `templates/claude-md/{type}.md` — CLAUDE.md template
6. `templates/workflow-guide/{type}.md` — workflow document template
7. `templates/commands/common/*.md` — common command templates (all types)
8. `templates/commands/{type}/*.md` — type-specific command templates
9. `templates/intent/{type}.md` — intent document template (new/refactor only)

Type mapping: `new` → `new-project`, `maintenance` → `maintenance`, `refactor` → `refactor`

### Customization Rules

When generating output from templates:
- Replace ALL `{{PLACEHOLDER}}` variables with actual analysis data
- Use actual commands, file paths, framework names from analysis
- Remove sections that don't apply to the detected tech stack
- Add sections for patterns not covered by the base template
- Make every command copy-paste ready with the actual package manager
- Include project-specific observations (monorepo, unusual patterns, etc.)
- For maintenance/refactor: incorporate git metrics (high-churn files, recent patterns)
- Mark unresolvable sections with `[NEEDS CLARIFICATION]` (Spec-Kit convention)
- For `{{INTENT_*}}` placeholders: if intent was not collected, replace with `[NEEDS CLARIFICATION]` + hint pointing to `.spec/intent.md`

## Phase 6: Generate Output Files

### Output 0: `.spec/intent.md` (new/refactor only, when intent was collected)

Generate from `templates/intent/{type}.md`, replacing all `{{INTENT_*}}` placeholders
with collected intent data. Only generate this file if intent was collected in Phase 4.
If the user skipped intent collection, do not generate this file.

For any `{{INTENT_*}}` placeholder that was not collected, replace with
`[NEEDS CLARIFICATION]` and append: `— Define in .spec/intent.md`.

### Output 1: `CLAUDE.md` (project root) — HIGHEST PRIORITY

Combines OpenSpec's AGENTS.md (AI behavioral guidelines) with BMAD's
project-context.md (implementation rules). This is the single most impactful
file for AI collaboration quality.

- **If exists**: Read existing, show diff, ask before modifying. Offer merge or replace.
- **If not exists**: Generate from template, show preview before writing.

### Output 2: `.spec/constitution.md`

Project governance document inspired by Spec-Kit's Constitution:
- Core principles with rationale
- Non-negotiable rules (testing, code style, security)
- For new projects: establish principles proactively
- For existing projects: extract principles from codebase analysis

### Output 3: `.spec/project-context.md`

Detailed project context inspired by OpenSpec's project.md and BMAD's project-context.md:
- Tech stack with exact versions
- Architectural patterns and conventions
- Business domain terminology
- Integration constraints
- Critical implementation rules

### Output 4: `.spec/workflow.md`

Phased development workflow synthesized from all four frameworks:
- Spec-Kit's pipeline: Spec → Plan → Tasks → Implement
- BMAD's scale tracks: Quick Flow vs Full Method decision criteria
- Superpowers' gates: mandatory design → plan → TDD implement
- OpenSpec's lifecycle: propose → specify → implement → archive

### Output 5: `.spec/specs/README.md`

Initialize the living specification directory:
- For `new`: explain spec-first approach, provide spec writing guide
- For `maintenance`: document existing capabilities as specs
- For `refactor`: set up characterization specs for legacy + target specs for new

### Output 6: `.spec/changes/README.md` (maintenance and refactor only)

Initialize the change tracking directory following OpenSpec's model:
- How to propose changes (proposal.md)
- How to write delta specs (ADDED/MODIFIED/REMOVED)
- How to archive completed changes

### Output 7: `.claude/commands/` directory

Generate slash commands as `.claude/commands/*.md` files. Each file becomes a
`/command` that users invoke directly (e.g., `/tdd implement login module`).

Source templates are in `templates/commands/`. For each command template:
1. Read the template file
2. Replace `{{PLACEHOLDER}}` variables with actual analysis data
3. Write to `target-project/.claude/commands/[name].md`

**Common commands (all types) — from `templates/commands/common/`:**
- `/analyst` — Discovery and brainstorming (BMAD Analyst)
- `/pm` — Spec writing with Given/When/Then (BMAD PM)
- `/architect` — Technical design and task breakdown (BMAD Architect)
- `/adr` — Architecture Decision Records (Spec-Kit)
- `/dev` — Spec-driven implementation (BMAD Dev + Superpowers)
- `/tdd` — TDD red-green-refactor cycle (Superpowers)
- `/qa` — Comprehensive code review (BMAD QA)

**Type-specific commands — from `templates/commands/{type}/`:**
- **new**: `/scaffold` — project scaffolding
- **maintenance**: `/bugfix` — bug diagnosis, `/dep-update` — dependency management, `/incident` — incident response
- **refactor**: `/legacy-analyze` — legacy code analysis, `/migrate` — module migration, `/parity-check` — feature parity verification

If `.claude/commands/` already exists in target project, preserve existing commands
and only add new ones. Warn user if any command names conflict.

## Phase 7: Summary and Next Steps

After generating all files, present:

1. **Created files list** with one-line descriptions
2. **Available commands** table showing all generated `/commands` with descriptions
3. **Recommended first actions** (3-5 steps) based on project type:
   - `new`: "Review intent.md → Ratify constitution.md → `/pm` to write your first spec → `/architect` to design → `/tdd` to implement"
   - `maintenance`: "Verify project-context.md → `/bugfix` for bugs or `/pm` + `/dev` for features"
   - `refactor`: "Review intent.md → `/legacy-analyze` a module → `/migrate` it → `/parity-check` to verify"
4. **Scale guidance**: When to use Quick Flow vs Full Method
5. **Iteration reminder**: All .spec/ files are living documents; update as the project evolves

---

## Reference Files

- **`references/spec-driven-principles.md`** — Synthesized principles from Spec-Kit, OpenSpec, Superpowers, BMAD
- **`references/analysis-guide.md`** — Analysis JSON interpretation and type inference matrix
- **`references/workflow-new-project.md`** — Spec-driven 0→1 methodology
- **`references/workflow-maintenance.md`** — Brownfield-first maintenance methodology
- **`references/workflow-refactor.md`** — Delta-spec-driven refactoring methodology

## Template Files

- **`templates/intent/{type}.md`** — Intent document templates (new/refactor only)
- **`templates/constitution/{type}.md`** — Project governance templates
- **`templates/project-context/{type}.md`** — Project context templates
- **`templates/claude-md/{type}.md`** — CLAUDE.md output templates
- **`templates/workflow-guide/{type}.md`** — Workflow document templates
- **`templates/commands/common/*.md`** — Common command templates (analyst, pm, architect, adr, dev, tdd, qa)
- **`templates/commands/{type}/*.md`** — Type-specific command templates
