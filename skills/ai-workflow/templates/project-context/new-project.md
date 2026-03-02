# Project Context: {{PROJECT_NAME}}

> Last updated: {{DATE}}
> This file is the "worldview" for AI agents working on this project.
> (Inspired by OpenSpec's project.md and BMAD's project-context.md)

## Tech Stack

| Component | Choice | Version |
|-----------|--------|---------|
| Language | {{PRIMARY_LANGUAGE}} | {{LANGUAGE_VERSION}} |
| Framework | {{FRAMEWORK}} | {{FRAMEWORK_VERSION}} |
| Package Manager | {{PACKAGE_MANAGER}} | — |
| Build Tool | {{BUILD_TOOL}} | — |
| Test Framework | {{TEST_FRAMEWORK}} | — |
| Linting | {{LINT_TOOLS}} | — |
| Formatting | {{FORMAT_TOOLS}} | — |
| Type Checking | {{TYPE_CHECK}} | — |

## Architecture

**Pattern**: {{ARCHITECTURE}}

```
{{DIRECTORY_TREE}}
```

### Key Design Decisions

{{DESIGN_DECISIONS}}

`[NEEDS CLARIFICATION]` — Add initial ADRs as architecture decisions are made.

## Coding Conventions

### Naming
- {{NAMING_CONVENTIONS}}

### File Organization
- {{FILE_ORGANIZATION}}

### Error Handling
- {{ERROR_HANDLING_PATTERN}}

### Logging
- {{LOGGING_PATTERN}}

## Project Goals

{{PROJECT_VISION}}

**Target Users**: {{TARGET_USERS}}
**Core Problem**: {{CORE_PROBLEM}}
**Success Criteria**: {{SUCCESS_CRITERIA}}

## Domain Knowledge

{{DOMAIN_CONTEXT}}

## Constraints

{{PROJECT_CONSTRAINTS}}

## Integration Points

`[NEEDS CLARIFICATION]` — Document external APIs, databases, and services as they are added.

## Critical Implementation Rules

1. Follow the constitution at `.spec/constitution.md` for all decisions
2. Write specs before code — use `.spec/specs/` for all feature specifications
3. TDD: write failing test → implement → verify pass → refactor
4. Every command in CLAUDE.md must be copy-paste ready
5. Update this file when new conventions or patterns are established
