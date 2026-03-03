# {{PROJECT_NAME}}

{{ONE_LINE_DESCRIPTION}}

> Migration: {{LEGACY_TECH_STACK}} → {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}
> This file serves as the AI behavioral guide during migration.

## Project Structure

- **Legacy Codebase**: `{{LEGACY_DIR}}`
- **Target Codebase**: `{{TARGET_DIR}}` (this directory)
- **Approach**: {{REFACTOR_APPROACH}}

## Commands — New Architecture

| Command | Description |
|---------|-------------|
| `{{INSTALL_CMD}}` | Install dependencies |
| `{{DEV_CMD}}` | Start development server |
| `{{BUILD_CMD}}` | Build for production |
| `{{TEST_CMD}}` | Run tests |
| `{{LINT_CMD}}` | Lint and format check |

## Commands — Legacy (if still running)

| Command | Description |
|---------|-------------|
| `{{LEGACY_DEV_CMD}}` | Start legacy dev server |
| `{{LEGACY_TEST_CMD}}` | Run legacy tests |

## Tech Stack

### New Architecture
- **Language**: {{PRIMARY_LANGUAGE}}
- **Framework**: {{FRAMEWORK}}
- **Package Manager**: {{PACKAGE_MANAGER}}
- **Test Framework**: {{TEST_FRAMEWORK}}

### Legacy (Being Replaced)
- {{LEGACY_TECH_STACK}}

## Refactor Goals

**Why**: {{REFACTOR_MOTIVATION}}
**Target**: {{TARGET_STATE}}
**Priority**: {{PRIORITY_MODULES}}

## Spec-Driven Migration Rules

This project is undergoing an incremental migration. AI agents MUST:

1. **Constitution first** — Check `.spec/constitution.md` (feature parity is non-negotiable)
2. **Characterize before migrate** — Write characterization tests for legacy before touching it
3. **Delta specs for everything** — Track ADDED/MODIFIED/REMOVED in `.spec/changes/`
4. **New patterns only** — Follow NEW architecture patterns; never replicate legacy anti-patterns
5. **No features during migration** — Migration branches contain ONLY migration work
6. **Always have rollback** — Feature flags for every migrated module
7. **Evidence required** — Prove feature parity with actual test output
8. **Check migration status** — See `.spec/project-context.md` for module migration tracker
9. **Document sync** — When updating any document, identify and update all documents that reference or depend on the changed content. Common relationships include but are not limited to:
   - `CLAUDE.md` ↔ `.spec/project-context.md` (tech stack, migration tracker)
   - `.spec/constitution.md` ↔ `.spec/workflow.md` (governance ↔ migration workflow)
   - `.spec/specs/legacy/*.md` ↔ `.spec/specs/feature-parity.md` (characterization ↔ parity checklist)
   - `.spec/changes/migrate-*` ↔ `.spec/specs/` (delta changes ↔ specs)
   - `.spec/intent.md` ↔ `.spec/constitution.md` (refactor goals ↔ principles)
   - Design docs / ADRs ↔ specs and implementation
   - Any document referencing another by path or content

## Migration Workflow (Per Module)

```
1. Characterize: write specs + tests for legacy behavior
2. Propose: create change in .spec/changes/migrate-[module]/
3. Implement: TDD against characterization tests
4. Verify: feature parity check with evidence
5. Rollout: feature flag → gradual → bake period
6. Archive: remove legacy, merge specs
```

## Architecture — New (Target)

**Pattern**: {{ARCHITECTURE}}

```
{{NEW_DIRECTORY_TREE}}
```

## Key Files

- `.spec/constitution.md` — Migration governance (feature parity, rollback, etc.)
- `.spec/project-context.md` — Dual context (legacy + new) + migration tracker
- `.spec/workflow.md` — Migration workflow phases
- `.spec/specs/legacy/` — Characterization specs for legacy modules
- `.spec/specs/feature-parity.md` — Feature parity checklist
- `.spec/changes/` — Active migration proposals
- `.spec/prompts/` — Role-based AI prompt templates
