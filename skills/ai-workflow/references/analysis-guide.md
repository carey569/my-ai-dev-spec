# Analysis Interpretation Guide

> Analysis data is collected by following `analysis-methodology.md` using
> built-in tools (Glob, Grep, Read, Bash). This guide explains how to
> interpret the collected data and map it to template placeholders.

How to read the analysis data and make customization decisions.

## File Statistics Interpretation

| total_files | Implication |
|-------------|-------------|
| 0 | Empty project — strong "new" signal |
| 1-15 | Very small — likely new or micro-project |
| 15-100 | Small-medium — could be any type |
| 100-500 | Medium — likely maintenance or refactor |
| 500+ | Large — definitely not new |

## Tech Stack → Customization Mapping

### Node.js / TypeScript

| Detected | CLAUDE.md should include |
|----------|--------------------------|
| package manager: pnpm/yarn/npm/bun | Correct install/run commands |
| framework: Next.js | App Router patterns, SSR/SSG notes, `next dev`/`next build` |
| framework: React | Component patterns, hooks guidelines, state management |
| framework: Express/Fastify | Route patterns, middleware chain, error handling |
| framework: NestJS | Module/Controller/Service pattern, DI conventions |
| build tool: vite/webpack | Dev server command, build output path |
| testing: jest/vitest | Test command, coverage command, mock patterns |
| linting: eslint + prettier | Format-on-save setup, lint command |

### Python

| Detected | CLAUDE.md should include |
|----------|--------------------------|
| package manager: poetry/pip/uv | Install and venv commands |
| framework: Django | `manage.py` commands, migration workflow, app structure |
| framework: Flask/FastAPI | Route patterns, request handling, ASGI/WSGI |
| testing: pytest | Test command, fixture patterns, conftest usage |
| linting: ruff/flake8 | Lint and format commands |
| type checking: mypy | Type checking command, stub handling |

### Go

| Detected | CLAUDE.md should include |
|----------|--------------------------|
| go modules | `go mod tidy`, `go build`, `go test` commands |
| framework: Gin/Echo/Fiber | Router patterns, middleware, context handling |
| testing: built-in | `go test ./...`, table-driven test patterns |

### Rust

| Detected | CLAUDE.md should include |
|----------|--------------------------|
| cargo | `cargo build`, `cargo test`, `cargo clippy` commands |
| framework: Actix/Axum/Rocket | Handler patterns, extractors, middleware |

### Java/Kotlin (JVM)

| Detected | CLAUDE.md should include |
|----------|--------------------------|
| build: maven | `mvn clean install`, `mvn test` |
| build: gradle | `./gradlew build`, `./gradlew test` |
| framework: Spring | Bean patterns, annotation conventions, profiles |

## Architecture Pattern → Workflow Implications

| Pattern | Workflow emphasis |
|---------|-------------------|
| mvc | Organize by model/controller/view layers; test each layer independently |
| layered | Service layer boundaries; dependency direction (upper → lower) |
| ddd | Bounded contexts; domain model purity; anti-corruption layers |
| spa-frontend | Component hierarchy; state management; routing; API integration |
| api-server | Route organization; middleware chain; request validation; error responses |
| serverless | Function isolation; cold start considerations; deployment per-function |
| monorepo | Cross-package quality gates; shared dependency management; affected-package testing |

## Type Inference Scoring Matrix

| Signal | new | maintenance | refactor |
|--------|-----|-------------|----------|
| total_files = 0 | +5 | — | — |
| total_files < 15 | +3 | — | — |
| Not a git repo | +2 | — | — |
| total_commits < 10 | +3 | — | — |
| repo_age < 14 days | +2 | — | — |
| No test files | +1 | — | — |
| No CI/CD | +1 | — | — |
| total_commits > 100 | — | +2 | — |
| contributors > 1 | — | +2 | — |
| CI/CD present | — | +2 | — |
| coverage config exists | — | +1 | — |
| test_files > 10 | — | +2 | — |
| repo_age > 90 days | — | +1 | — |
| CHANGELOG exists | — | +1 | — |
| "refactor/migrate" in 3+ recent commits | — | — | +3 |
| "refactor/migrate" in 1-2 recent commits | — | — | +1 |
| legacy/deprecated directories | — | — | +3 |
| parallel old/new structures | — | — | +3 |
| migration directories | — | — | +2 |

**Confidence calculation**: `0.5 + (lead over second place * 0.1)`, capped at 0.95.

## Template Placeholder Reference

Standard placeholders used across all templates:

| Placeholder | Source (methodology step) |
|-------------|--------------------------|
| `{{PROJECT_NAME}}` | Last segment of SOURCE_PATH |
| `{{PRIMARY_LANGUAGE}}` | Step 2: language with most code lines |
| `{{FRAMEWORK}}` | Step 2: first detected framework |
| `{{PACKAGE_MANAGER}}` | Step 2: detected package manager |
| `{{INSTALL_CMD}}` | Step 2: derived from package manager |
| `{{DEV_CMD}}` | Step 2: from scripts field or framework convention |
| `{{BUILD_CMD}}` | Step 2: from scripts field or framework convention |
| `{{TEST_CMD}}` | Step 2: from test framework + package manager |
| `{{LINT_CMD}}` | Step 2: from lint tools + package manager |
| `{{ARCHITECTURE}}` | Step 4: highest-scoring pattern |
| `{{DIRECTORY_TREE}}` | Step 1: formatted directory tree |
| `{{KEY_FILES}}` | Step 4: entry points + Step 6: high-churn files |
| `{{TEST_FRAMEWORK}}` | Step 3: detected test framework |
| `{{CI_PLATFORM}}` | Step 3: detected CI platform |
| `{{TOTAL_FILES}}` | Step 1: total file count |
| `{{TOTAL_COMMITS}}` | Step 6: commit count |
| `{{CONTRIBUTORS}}` | Step 6: contributor count |
| `{{REPO_AGE}}` | Step 6: days since first commit |

## Intent Placeholder Reference

Placeholders populated from user intent collection (Phase 4). Applicable to `new` and `refactor` types only. When intent is not collected (skipped or `maintenance` type), replace with `[NEEDS CLARIFICATION]` + guidance hint.

### New Project Intent Placeholders

| Placeholder | Source | Description |
|-------------|--------|-------------|
| `{{PROJECT_VISION}}` | Intent Q1: Vision | One-sentence project vision statement |
| `{{CORE_PROBLEM}}` | Intent Q2: Problem | The core problem this project solves |
| `{{TARGET_USERS}}` | Intent Q3: Users | Primary target user personas |
| `{{KEY_FEATURES}}` | Intent Q4: Features | Bulleted list of key capabilities |
| `{{SUCCESS_CRITERIA}}` | Intent Q5: Success | Measurable success criteria |
| `{{PROJECT_CONSTRAINTS}}` | Intent Q6: Constraints | Technical, business, or timeline constraints |
| `{{DOMAIN_CONTEXT}}` | Intent Q7: Domain | Domain-specific terminology and context |

### Refactor Intent Placeholders

| Placeholder | Source | Description |
|-------------|--------|-------------|
| `{{REFACTOR_MOTIVATION}}` | Intent Q1: Motivation | Why this refactor is being undertaken |
| `{{TARGET_STATE}}` | Intent Q2: Target | Desired end-state architecture or quality |
| `{{PAIN_POINTS}}` | Intent Q3: Pain points | Current pain points driving the refactor |
| `{{PRIORITY_MODULES}}` | Intent Q4: Priority | Ordered list of modules to migrate first |
| `{{MUST_PRESERVE}}` | Intent Q5: Preserve | Behaviors, APIs, or contracts that must not change |
| `{{SUCCESS_CRITERIA}}` | Intent Q6: Success | Measurable success criteria for the refactor |
| `{{PROJECT_CONSTRAINTS}}` | Intent Q7: Constraints | Technical, business, or timeline constraints |
