# Project Context: {{PROJECT_NAME}}

> Last updated: {{DATE}}
> Migration: {{LEGACY_TECH_STACK}} → {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}
> This file maintains dual context: legacy understanding + new architecture.
> (Inspired by OpenSpec's project.md and BMAD's project-context.md)

## Tech Stack — New Architecture

| Component | Choice | Version |
|-----------|--------|---------|
| Language | {{PRIMARY_LANGUAGE}} | {{LANGUAGE_VERSION}} |
| Framework | {{FRAMEWORK}} | {{FRAMEWORK_VERSION}} |
| Package Manager | {{PACKAGE_MANAGER}} | — |
| Test Framework | {{TEST_FRAMEWORK}} | — |
| CI/CD | {{CI_PLATFORM}} | — |

## Tech Stack — Legacy (Being Replaced)

| Component | Choice |
|-----------|--------|
| {{LEGACY_TECH_STACK_TABLE}} |

## Architecture — New (Target)

**Pattern**: {{ARCHITECTURE}}

```
{{NEW_DIRECTORY_TREE}}
```

### Key Design Decisions (New)
{{NEW_DESIGN_DECISIONS}}

## Architecture — Legacy (Reference)

```
{{LEGACY_DIRECTORY_TREE}}
```

### Legacy Module Map
{{LEGACY_MODULE_MAP}}

### Hidden Business Logic (Legacy)

Discovered during analysis — behaviors that are NOT obvious from reading the code:

{{HIDDEN_BUSINESS_LOGIC}}

`[NEEDS CLARIFICATION]` — Continue discovering hidden logic during each module migration.

## Coding Conventions — New Architecture

### Required Patterns
- {{NEW_PATTERNS}}

### Forbidden Patterns (Legacy Anti-patterns to NOT Replicate)
- {{FORBIDDEN_PATTERNS}}

## Domain Knowledge

### Refactor Context

**Motivation**: {{REFACTOR_MOTIVATION}}
**Target State**: {{TARGET_STATE}}
**Pain Points**: {{PAIN_POINTS}}

### Business Terminology
{{DOMAIN_TERMINOLOGY}}

### Business Rules
{{BUSINESS_RULES}}

## Integration Points

### APIs (External Consumers)
{{EXTERNAL_API_CONSUMERS}}

### Databases
{{DATABASE_DETAILS}}

### Data Migration Notes
{{DATA_MIGRATION_NOTES}}

## Migration State

**Priority Order**: {{PRIORITY_MODULES}}
**Must Preserve**: {{MUST_PRESERVE}}

| Module | Status | Feature Parity |
|--------|--------|----------------|
| {{MIGRATION_STATUS_TABLE}} |

## Critical Implementation Rules

1. Follow the constitution at `.spec/constitution.md`
2. Characterization tests FIRST — never migrate without capturing current behavior
3. Feature parity is non-negotiable — verify every behavior from the checklist
4. No new features in migration branches — migration work ONLY
5. Always have rollback — feature flags for every migrated module
6. New architecture patterns only — never replicate legacy anti-patterns
7. Update this file after each module migration
8. Mark legacy-specific knowledge with `[LEGACY]` prefix
