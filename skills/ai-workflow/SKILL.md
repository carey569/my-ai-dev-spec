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
| | `.claude/skills/*/SKILL.md` — project-specific skills (scaffold, bugfix, migrate...) |
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

### Special Handling for Refactor Projects

Refactor projects typically involve two directories:
- **Legacy directory**: The existing codebase to be refactored
- **Target directory**: A new, clean directory for the refactored code

**If refactor type is detected or specified:**
1. Ask the user to clarify the refactor approach:
   - **Option A**: "In-place refactor" — Refactor within the existing directory (legacy code remains alongside new code)
   - **Option B**: "Clean slate refactor" — Create a new directory for refactored code (recommended)

2. **If Option B (Clean slate) is chosen:**
   - Ask for the target directory path for the refactored project
   - If not provided, suggest: `{legacy-dir}-refactored` or `{legacy-dir}-v2`
   - Verify the target directory is empty or doesn't exist yet
   - Store both paths:
     - `LEGACY_DIR`: The directory being analyzed (source of truth for characterization)
     - `TARGET_DIR`: Where AI workflow configs will be generated
   - Generate all output files in `TARGET_DIR`, not `LEGACY_DIR`

3. **If Option A (In-place) is chosen:**
   - Use the current directory as both legacy and target
   - Warn about potential conflicts with existing files

## Phase 2: Codebase Analysis

Read `references/analysis-methodology.md` and execute each analysis step
on the **source directory** (legacy directory for refactor projects)
using built-in tools (Glob, Grep, Read, Bash for git commands only).

Collect all data fields defined in the methodology for use in template
placeholder substitution (Phase 5-6).

**For refactor projects with clean slate approach:**
- Analyze `LEGACY_DIR` to understand the existing system
- Generate configs in `TARGET_DIR`
- Include legacy analysis data in the generated configs

Handle edge cases:
- **Empty directory**: If no source files found (total_files = 0), skip
  analysis steps and proceed with `new` type.
- **Not a git repository**: Skip Step 6 (git metrics). Record git fields
  as "N/A".
- **Large repository (1000+ files)**: Focus on root-level config files and
  top 2 levels of directory structure for architecture recognition. Use
  extension distribution for file statistics instead of per-file counting.

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

[For refactor projects only]
Refactor Setup:
  Legacy:      [LEGACY_DIR]
  Target:      [TARGET_DIR]
  Approach:    [In-place / Clean slate]
```

## Phase 3: Project Type Determination

Read `references/analysis-guide.md` for inference logic.

**If type provided via arguments**: Confirm alignment with analysis.
**If type NOT provided**: Present inference with top 3 signals, ask user to confirm.

Wait for confirmation before proceeding.

## Phase 4: Intent Collection

> **Applies to**: `new` and `refactor` only. Skip this phase for `maintenance`.

> **SCOPE BOUNDARY**: This phase collects intent data ONLY for populating
> `{{INTENT_*}}` placeholders in configuration templates. Record the user's
> answers as-is — do NOT design architecture, propose migration strategies,
> evaluate technical trade-offs, or begin actual project work. Keep every
> response focused on data collection and move to Phase 5 immediately after
> confirmation.

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

**Free-form mode**: Present a single open prompt.

For **new** projects:
> Tell me about this project — what are you building, who is it for,
> what problem does it solve, and what constraints should I know about?

For **refactor** projects:
> Briefly describe: what is the refactor motivation, what should the target state
> look like, what are the main pain points, and what constraints should I know about?
> (Keep it high-level — detailed architecture design comes later when you use the
> generated workflow.)

Parse the response to extract structured fields matching the intent template placeholders.
Ask a follow-up only if critical fields (Vision/Motivation, Success Criteria) are missing.
Do NOT elaborate on, evaluate, or expand the user's answers — simply record them.

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

**Additional context for refactor projects:**
- If "clean slate" approach was chosen, remind user that configs will be generated in the target directory
- Emphasize the importance of characterization specs for the legacy system
- Ask if there's existing documentation about the legacy system that should be referenced

### Step 4: Confirm Intent Summary

Present a structured summary of collected intent data. Ask the user to confirm or edit.
Format the summary matching the intent template structure (`templates/intent/{type}.md`).

Once confirmed, store the intent data for use in Phase 6 template generation.

> **REMINDER — PROCEED TO PHASE 5**: Intent collection is complete. The purpose
> of this skill is to **generate AI workflow configuration files**, not to execute
> the refactoring itself. Proceed immediately to Phase 5 (Load References and
> Templates) and then Phase 6 (Generate Output Files). Do NOT start designing
> architecture, planning migration, or doing any actual project work.

> **Fallback**: If the user chose "Skip" or any intent placeholder remains empty after collection,
> replace it with `[NEEDS CLARIFICATION]` and append a hint directing to `.spec/intent.md`.

## Phase 5: Load References and Templates

> **CHECKPOINT**: All user input has been collected (Phases 1-4). From this point
> forward, the task is purely mechanical: read templates, substitute placeholders,
> and write output files. No further user interaction is needed until the final
> summary in Phase 7.

Based on confirmed type, read in this order:

1. `references/spec-driven-principles.md` — core methodology (always read)
2. `references/workflow-{type}.md` — type-specific workflow methodology
3. `templates/constitution/{type}.md` — constitution template
4. `templates/project-context/{type}.md` — project-context template
5. `templates/claude-md/{type}.md` — CLAUDE.md template
6. `templates/workflow-guide/{type}.md` — workflow document template
7. `templates/commands/common/*.md` — common skill templates (all types)
8. `templates/commands/{type}/*.md` — type-specific skill templates
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

**IMPORTANT**: For refactor projects with "clean slate" approach, generate ALL files in `TARGET_DIR`, not `LEGACY_DIR`.

### Output 0: `.spec/intent.md` (new/refactor only, when intent was collected)

Generate from `templates/intent/{type}.md`, replacing all `{{INTENT_*}}` placeholders
with collected intent data. Only generate this file if intent was collected in Phase 4.
If the user skipped intent collection, do not generate this file.

For any `{{INTENT_*}}` placeholder that was not collected, replace with
`[NEEDS CLARIFICATION]` and append: `— Define in .spec/intent.md`.

**For refactor projects with clean slate:**
- Generate in `TARGET_DIR/.spec/intent.md`
- Include `{{LEGACY_DIR}}` placeholder with the path to the legacy codebase
- Add a note: "Legacy codebase location: [LEGACY_DIR] — Reference for characterization specs"

### Output 1: `CLAUDE.md` (project root) — HIGHEST PRIORITY

Combines OpenSpec's AGENTS.md (AI behavioral guidelines) with BMAD's
project-context.md (implementation rules). This is the single most impactful
file for AI collaboration quality.

- **If exists**: Read existing, show diff, ask before modifying. Offer merge or replace.
- **If not exists**: Generate from template, show preview before writing.

**For refactor projects:**
- Generate in `TARGET_DIR/CLAUDE.md`
- Include a section referencing the legacy codebase location
- Add refactor-specific rules (e.g., "Always check feature parity", "Write characterization specs first")

### Output 2: `.spec/constitution.md`

Project governance document inspired by Spec-Kit's Constitution:
- Core principles with rationale
- Non-negotiable rules (testing, code style, security)
- For new projects: establish principles proactively
- For existing projects: extract principles from codebase analysis

**For refactor projects:**
- Generate in `TARGET_DIR/.spec/constitution.md`
- Include refactor-specific articles:
  - "Feature parity is non-negotiable"
  - "Characterization tests before migration"
  - "Incremental migration (strangler fig pattern)"
  - "Always have rollback capability"
  - "No new features during migration"

### Output 3: `.spec/project-context.md`

Detailed project context inspired by OpenSpec's project.md and BMAD's project-context.md:
- Tech stack with exact versions
- Architectural patterns and conventions
- Business domain terminology
- Integration constraints
- Critical implementation rules

**For refactor projects:**
- Generate in `TARGET_DIR/.spec/project-context.md`
- Include dual context section:
  - **Legacy System**: Tech stack, architecture, pain points (from analysis)
  - **Target System**: New tech stack, new architecture, improvements
- Add migration strategy overview

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

**For refactor projects with clean slate:**
- Generate in `TARGET_DIR/.spec/specs/README.md`
- Create subdirectories:
  - `TARGET_DIR/.spec/specs/legacy/` — Characterization specs for legacy system
  - `TARGET_DIR/.spec/specs/target/` — Target specs for new system
  - `TARGET_DIR/.spec/specs/feature-parity.md` — Feature parity checklist
- Include instructions for writing characterization specs
- Add note: "Legacy codebase at: [LEGACY_DIR] — Reference when writing characterization specs"

### Output 6: `.spec/changes/README.md` (maintenance and refactor only)

Initialize the change tracking directory following OpenSpec's model:
- How to propose changes (proposal.md)
- How to write delta specs (ADDED/MODIFIED/REMOVED)
- How to archive completed changes

### Output 7: `.claude/skills/` directory

Generate project-level skills as `.claude/skills/*/SKILL.md` files.

**Common skills (all types) — generated from `templates/commands/common/`:**
- `analyst` — Discovery and brainstorming (BMAD Analyst)
- `pm` — Spec writing with Given/When/Then (BMAD PM)
- `architect` — Technical design and task breakdown (BMAD Architect)
- `adr` — Architecture Decision Records (Spec-Kit)
- `dev` — Spec-driven implementation (BMAD Dev + Superpowers)
- `tdd` — TDD red-green-refactor cycle (Superpowers)
- `qa` — Comprehensive code review (BMAD QA)

**Project-specific skills (all types get ALL skills below):**
- `scaffold` — Project scaffolding (from `templates/commands/new-project/`)
- `bugfix` — Bug diagnosis and fix (from `templates/commands/maintenance/`)
- `dep-update` — Dependency management (from `templates/commands/maintenance/`)
- `incident` — Incident response (from `templates/commands/maintenance/`)
- `legacy-analyze` — Legacy code analysis (from `templates/commands/refactor/`)
- `migrate` — Module migration (from `templates/commands/refactor/`)
- `parity-check` — Feature parity verification (from `templates/commands/refactor/`)

For each skill template:
1. Read ALL common skills from `templates/commands/common/*.md`
2. Read ALL project-specific skills from:
   - `templates/commands/new-project/*.md`
   - `templates/commands/maintenance/*.md`
   - `templates/commands/refactor/*.md`
3. Replace `{{PLACEHOLDER}}` variables with actual analysis data:
   - `{{PROJECT_NAME}}` → actual project name
   - `{{TEST_CMD}}` → actual test command
   - `{{BUILD_CMD}}` → actual build command
   - `{{LINT_CMD}}` → actual lint command
   - `{{INSTALL_CMD}}` → actual install command
4. Write to `target-project/.claude/skills/{name}/SKILL.md`

**IMPORTANT**: Generate ALL skills (common + all project-specific) regardless of project type. Every project gets all 14 skills.

**Backward Compatibility:**
- If `.claude/commands/` exists in target project, preserve it and warn about migration
- If `.claude/skills/` exists, preserve existing skills
- Warn user if any skill names conflict

## Phase 7: Verification and Summary

### Step 1: Verify All Skills Generated

After generating all files, verify that ALL 14 skills were created successfully:

**Expected skills (must all exist):**
1. `.claude/skills/analyst/SKILL.md`
2. `.claude/skills/pm/SKILL.md`
3. `.claude/skills/architect/SKILL.md`
4. `.claude/skills/adr/SKILL.md`
5. `.claude/skills/dev/SKILL.md`
6. `.claude/skills/tdd/SKILL.md`
7. `.claude/skills/qa/SKILL.md`
8. `.claude/skills/scaffold/SKILL.md`
9. `.claude/skills/bugfix/SKILL.md`
10. `.claude/skills/dep-update/SKILL.md`
11. `.claude/skills/incident/SKILL.md`
12. `.claude/skills/legacy-analyze/SKILL.md`
13. `.claude/skills/migrate/SKILL.md`
14. `.claude/skills/parity-check/SKILL.md`

Use Glob to check: `target-project/.claude/skills/*/SKILL.md`

If any skills are missing:
- Report which skills are missing
- Attempt to regenerate the missing skills
- If regeneration fails, warn the user and provide manual instructions

### Step 2: Present Summary

After verification, present:

1. **Created files list** with one-line descriptions
2. **Available skills** table showing all 14 generated skills:
   - **Common skills** (7): analyst, pm, architect, adr, dev, tdd, qa
   - **Project-specific skills** (7): scaffold, bugfix, dep-update, incident, legacy-analyze, migrate, parity-check
3. **Recommended first actions** (3-5 steps) based on project type:
   - `new`: "Review intent.md → Ratify constitution.md → Ask me to 'write a spec for [feature]' → Ask me to 'design [feature]' → Ask me to 'implement [feature] with TDD'"
   - `maintenance`: "Verify project-context.md → Ask me to 'fix [bug]' or 'add [feature]'"
   - `refactor`:
     - **Clean slate approach**: "Review intent.md → Verify legacy codebase location → Ask me to 'analyze [legacy-module]' → Ask me to 'write characterization specs for [module]' → Ask me to 'migrate [module]' → Ask me to 'verify parity for [module]'"
     - **In-place approach**: "Review intent.md → Ask me to 'analyze [module]' → Ask me to 'refactor [module]' → Ask me to 'verify parity for [module]'"
4. **Refactor-specific notes** (if applicable):
   - "All configs generated in: [TARGET_DIR]"
   - "Legacy codebase at: [LEGACY_DIR]"
   - "Start by characterizing the legacy system before writing new code"
   - "Use the legacy-analyze skill to understand existing modules"
   - "Use the migrate skill for incremental module migration"
   - "Use the parity-check skill to verify feature parity after migration"
5. **Skill invocation note**: "Skills activate automatically based on your requests. Use natural language - no slash commands needed."
6. **Scale guidance**: When to use Quick Flow vs Full Method
7. **Iteration reminder**: All .spec/ files are living documents; update as the project evolves

---

## Reference Files

- **`references/spec-driven-principles.md`** — Synthesized principles from Spec-Kit, OpenSpec, Superpowers, BMAD
- **`references/analysis-methodology.md`** — Step-by-step codebase analysis using built-in tools
- **`references/analysis-guide.md`** — Analysis data interpretation and type inference matrix
- **`references/workflow-new-project.md`** — Spec-driven 0→1 methodology
- **`references/workflow-maintenance.md`** — Brownfield-first maintenance methodology
- **`references/workflow-refactor.md`** — Delta-spec-driven refactoring methodology

## Template Files

- **`templates/intent/{type}.md`** — Intent document templates (new/refactor only)
- **`templates/constitution/{type}.md`** — Project governance templates
- **`templates/project-context/{type}.md`** — Project context templates
- **`templates/claude-md/{type}.md`** — CLAUDE.md output templates
- **`templates/workflow-guide/{type}.md`** — Workflow document templates
- **`templates/commands/common/*.md`** — Common skill templates (analyst, pm, architect, adr, dev, tdd, qa)
- **`templates/commands/new-project/*.md`** — New project skill templates (scaffold)
- **`templates/commands/maintenance/*.md`** — Maintenance skill templates (bugfix, dep-update, incident)
- **`templates/commands/refactor/*.md`** — Refactor skill templates (legacy-analyze, migrate, parity-check)
