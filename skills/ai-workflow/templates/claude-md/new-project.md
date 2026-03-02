# {{PROJECT_NAME}}

{{ONE_LINE_DESCRIPTION}}

> This file serves as the AI behavioral guide for this project.
> Inspired by OpenSpec's AGENTS.md and BMAD's project-context.md.

## Commands

| Command | Description |
|---------|-------------|
| `{{INSTALL_CMD}}` | Install dependencies |
| `{{DEV_CMD}}` | Start development server |
| `{{BUILD_CMD}}` | Build for production |
| `{{TEST_CMD}}` | Run tests |
| `{{LINT_CMD}}` | Lint and format check |

## Tech Stack

- **Language**: {{PRIMARY_LANGUAGE}}
- **Framework**: {{FRAMEWORK}}
- **Package Manager**: {{PACKAGE_MANAGER}}
- **Test Framework**: {{TEST_FRAMEWORK}}

## Architecture

**Pattern**: {{ARCHITECTURE}}

```
{{DIRECTORY_TREE}}
```

## Project Vision

**What**: {{PROJECT_VISION}}
**For**: {{TARGET_USERS}}
**Problem**: {{CORE_PROBLEM}}

Key capabilities:
{{KEY_FEATURES}}

## Spec-Driven Development Rules

This project follows spec-driven development. AI agents MUST:

1. **Spec before code** — Read or create a spec in `.spec/specs/` before implementing
2. **Follow the constitution** — Check `.spec/constitution.md` for project principles
3. **TDD always** — Write failing test → implement → verify pass → refactor
4. **Evidence required** — Show actual command output, not "it should work"
5. **Mark ambiguities** — Use `[NEEDS CLARIFICATION]` for unclear requirements
6. **Minimum viable change** — Smallest change that delivers value
7. **Update context** — Update `.spec/project-context.md` when new patterns emerge

## Development Workflow

### For New Features (Full Method)
1. Write spec in `.spec/specs/[feature-name]/spec.md` (Given/When/Then scenarios)
2. Get spec approval
3. Create implementation plan with tasks
4. TDD implement each task
5. Review against spec
6. Commit

### For Small Tasks (Quick Flow)
1. Note the change briefly
2. Write failing test
3. Implement
4. Verify with evidence
5. Commit

### Scale Decision
- < 30 min estimated → Quick Flow
- Crosses module boundaries → Full Method
- New API endpoint → Full Method
- Config/typo fix → Quick Flow

## Code Style

- {{LINT_CONVENTION}}
- {{FORMAT_CONVENTION}}
- {{TYPE_CHECK_CONVENTION}}
- Follow existing patterns — consistency over personal preference

## Key Files

- `.spec/constitution.md` — Project governance principles
- `.spec/project-context.md` — Detailed tech stack and conventions
- `.spec/workflow.md` — Development workflow guide
- `.spec/specs/` — Living specifications
- `.spec/prompts/` — Role-based AI prompt templates
