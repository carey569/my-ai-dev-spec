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
| `{{COVERAGE_CMD}}` | Run tests with coverage |

## Tech Stack

- **Language**: {{PRIMARY_LANGUAGE}}
- **Framework**: {{FRAMEWORK}}
- **Package Manager**: {{PACKAGE_MANAGER}}
- **Test Framework**: {{TEST_FRAMEWORK}}
- **CI/CD**: {{CI_PLATFORM}}

## Architecture

**Pattern**: {{ARCHITECTURE}}

```
{{DIRECTORY_TREE}}
```

## Spec-Driven Development Rules

This project follows spec-driven development with change lifecycle tracking.
AI agents MUST:

1. **Read before modify** — Never change code you haven't read
2. **Follow the constitution** — Check `.spec/constitution.md`
3. **Propose changes** — For significant work, create a proposal in `.spec/changes/`
4. **Delta specs** — Track changes as ADDED/MODIFIED/REMOVED
5. **Regression test every bug** — Write failing test before fixing
6. **Evidence required** — Show actual test output, not "it works"
7. **Follow existing patterns** — Consistency over personal preference
8. **Minimum viable change** — One concern per commit
9. **Document sync** — When updating any document, identify and update all documents that reference or depend on the changed content. Common relationships include but are not limited to:
   - `CLAUDE.md` ↔ `.spec/project-context.md` (tech stack, conventions)
   - `.spec/constitution.md` ↔ `.spec/workflow.md` (governance ↔ workflow rules)
   - `.spec/specs/*.md` ↔ `.spec/changes/` (specs ↔ delta changes)
   - Design docs / ADRs ↔ specs and implementation
   - Any document referencing another by path or content

## Development Workflow

### Quick Flow (< 30 min, single module)
1. Write failing test
2. Implement minimum fix/change
3. Verify: test passes + full suite passes
4. Commit with descriptive message

### Full Method (features, cross-module, API changes)
1. Create proposal: `.spec/changes/[name]/proposal.md`
2. Write delta specs (ADDED/MODIFIED/REMOVED)
3. Design (if architecture affected)
4. Break into tasks
5. TDD implement each task
6. Review against specs
7. Archive: merge delta specs into `.spec/specs/`

### Scale Decision
| Signal | Track |
|--------|-------|
| Bug with known cause | Quick Flow |
| Single file change | Quick Flow |
| New feature | Full Method |
| API change | Full Method |
| Cross-module work | Full Method |
| DB schema change | Full Method |

## Code Style

- {{LINT_CONVENTION}}
- {{FORMAT_CONVENTION}}
- Boy Scout Rule: improve one small thing when touching a file, no more
- Do NOT refactor in feature branches

## High-Churn Files

{{HIGH_CHURN_FILES}}

## Key Files

- `.spec/constitution.md` — Project governance principles
- `.spec/project-context.md` — Tech stack, conventions, gotchas
- `.spec/workflow.md` — Development workflow guide
- `.spec/specs/` — Living specifications
- `.spec/changes/` — Active change proposals
- `.spec/prompts/` — Role-based AI prompt templates
