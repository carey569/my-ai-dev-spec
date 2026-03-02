# Project Context: {{PROJECT_NAME}}

> Last updated: {{DATE}}
> Repository: {{TOTAL_COMMITS}} commits, {{CONTRIBUTORS}} contributors, {{REPO_AGE}} days old
> This file captures the "unobvious" knowledge about this codebase.
> (Inspired by OpenSpec's project.md and BMAD's project-context.md)

## Tech Stack

| Component | Choice | Version |
|-----------|--------|---------|
| Language | {{PRIMARY_LANGUAGE}} | {{LANGUAGE_VERSION}} |
| Framework | {{FRAMEWORK}} | {{FRAMEWORK_VERSION}} |
| Package Manager | {{PACKAGE_MANAGER}} | — |
| Build Tool | {{BUILD_TOOL}} | — |
| Test Framework | {{TEST_FRAMEWORK}} | — |
| CI/CD | {{CI_PLATFORM}} | — |
| Linting | {{LINT_TOOLS}} | — |
| Formatting | {{FORMAT_TOOLS}} | — |

## Architecture

**Pattern**: {{ARCHITECTURE}}

```
{{DIRECTORY_TREE}}
```

### Module Responsibilities

{{MODULE_DESCRIPTIONS}}

### Data Flow

{{DATA_FLOW_DESCRIPTION}}

## Coding Conventions (Observed)

### Patterns to Follow
- {{OBSERVED_PATTERNS}}

### Patterns to Avoid
- {{ANTI_PATTERNS_OBSERVED}}

### Naming Conventions
- {{NAMING_CONVENTIONS}}

### File Organization
- {{FILE_ORGANIZATION_RULES}}

## Domain Knowledge

### Business Terminology
{{DOMAIN_TERMINOLOGY}}

### Business Rules
{{BUSINESS_RULES}}

## Integration Points

### Internal Services
{{INTERNAL_INTEGRATIONS}}

### External APIs
{{EXTERNAL_INTEGRATIONS}}

### Databases
{{DATABASE_DETAILS}}

## High-Churn Files (Frequently Modified)

{{HIGH_CHURN_FILES}}

These files change frequently and deserve extra attention during reviews.

## Known Gotchas

{{GOTCHAS}}

## Critical Implementation Rules

1. Follow the constitution at `.spec/constitution.md`
2. Read existing code before modifying — never change code you haven't read
3. Follow existing patterns — consistency over personal preference
4. Propose changes through `.spec/changes/` with delta specs
5. Regression test for every bug fix
6. Evidence-based completion — show actual test/build output
7. Update this file when new conventions or gotchas are discovered
