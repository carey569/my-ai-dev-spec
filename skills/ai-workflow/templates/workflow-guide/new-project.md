# {{PROJECT_NAME}} — Spec-Driven Development Workflow

> Generated: {{DATE}} | Type: **New Project (0→1)** | Stack: {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}
> Methodology: Spec-Kit + Superpowers + BMAD + OpenSpec synthesis

---

## Project Objectives

**Vision**: {{PROJECT_VISION}}
**Success Criteria**: {{SUCCESS_CRITERIA}}

Key features to deliver:
{{KEY_FEATURES}}

---

## Phase 1: Constitution and Context

**Goal**: Establish governance and development environment

- [ ] Ratify `.spec/constitution.md` (review each article)
- [ ] Complete `.spec/project-context.md` (fill `[NEEDS CLARIFICATION]` items)
- [ ] Set up {{PACKAGE_MANAGER}} and install dependencies
- [ ] Configure {{LINT_TOOLS}} with auto-fix on save
- [ ] Create CI pipeline ({{CI_RECOMMENDATION}})
- [ ] Verify: `{{INSTALL_CMD}}`, `{{DEV_CMD}}`, `{{TEST_CMD}}`, `{{LINT_CMD}}` all work

**Gate**: Constitution ratified. Commands documented and working. CI passes.

---

## Phase 2: Specification

**Goal**: Define WHAT the system does (not HOW)

- [ ] Write specs for core features in `.spec/specs/[feature]/spec.md`
- [ ] Use Given/When/Then scenarios for acceptance criteria
- [ ] Mark ambiguities with `[NEEDS CLARIFICATION]`
- [ ] Define data models and API contracts
- [ ] Trace each spec back to a goal in `.spec/intent.md`
- [ ] Review specs against constitution
- [ ] Stakeholder approval

**Gate**: All features specified. No unresolved `[NEEDS CLARIFICATION]`.

**Prompt**: Use `.spec/prompts/pm-requirements.md`

---

## Phase 3: Architecture and Planning

**Goal**: Define HOW the system will be built

- [ ] Create architecture document with ADRs
- [ ] Verify architecture against constitution
- [ ] Break specs into ordered tasks
- [ ] Update `project-context.md` with architecture decisions
- [ ] Implementation readiness check: PASS / CONCERNS / FAIL

**Gate**: Architecture documented. Task breakdown complete. Readiness: PASS.

**Prompt**: Use `.spec/prompts/architect-design.md`

---

## Phase 4: Foundation Implementation

**Goal**: Working skeleton with reference implementation

- [ ] Create directory structure per architecture
- [ ] Write first test (verify test infra works)
- [ ] Implement reference vertical slice (TDD)
- [ ] Set up pre-commit hooks
- [ ] Document all commands in CLAUDE.md

**Gate**: Reference implementation passes tests. CI passes. Evidence provided.

**Prompt**: Use `.spec/prompts/dev-implement.md` + `.spec/prompts/dev-tdd.md`

---

## Phase 5: Core Implementation

**Goal**: All features implemented per spec

For each task batch (3-5 tasks):
- [ ] Read the spec
- [ ] Write failing tests from spec scenarios (RED)
- [ ] Implement minimum code (GREEN)
- [ ] Refactor (REFACTOR)
- [ ] Verify against spec (evidence required)
- [ ] QA review checkpoint

**Gate**: All spec scenarios pass. Coverage > 70%. No critical issues.

---

## Phase 6: Documentation and Deployment

- [ ] Complete README
- [ ] API documentation
- [ ] Deployment configuration
- [ ] Final review of all `.spec/` files

**Gate**: New contributor can onboard from documentation alone.

---

## Scale Tracks

| Situation | Track | Process |
|-----------|-------|---------|
| New feature | Full Method | Spec → Plan → TDD → Review |
| Small utility | Quick Flow | Test → Implement → Verify |
| Architecture decision | Full Method | ADR → Review → Document |
| Config change | Quick Flow | Change → Verify → Commit |

---

## AI Prompt Usage Guide

| Phase | Prompt |
|-------|--------|
| Discovery | `.spec/prompts/analyst-brainstorm.md` |
| Requirements | `.spec/prompts/pm-requirements.md` |
| Architecture | `.spec/prompts/architect-design.md` |
| Implementation | `.spec/prompts/dev-implement.md` |
| TDD cycle | `.spec/prompts/dev-tdd.md` |
| Scaffolding | `.spec/prompts/dev-scaffold.md` |
| ADR creation | `.spec/prompts/architect-adr.md` |
| Code review | `.spec/prompts/qa-review.md` |
