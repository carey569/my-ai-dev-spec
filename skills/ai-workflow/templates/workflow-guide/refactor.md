# {{PROJECT_NAME}} — Spec-Driven Migration Workflow

> Generated: {{DATE}} | Type: **Refactor** | Stack: {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}
> Migration: {{LEGACY_TECH_STACK}} → {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}
> Methodology: BMAD story-driven + OpenSpec delta specs + Superpowers TDD

---

## Refactor Objectives

**Motivation**: {{REFACTOR_MOTIVATION}}
**Target State**: {{TARGET_STATE}}
**Success Criteria**: {{SUCCESS_CRITERIA}}

Priority migration order:
{{PRIORITY_MODULES}}

---

## Phase 1: Legacy Analysis & Constitution

**Goal**: Understand legacy, establish new governance

- [ ] Document all legacy capabilities as characterization specs
- [ ] Map dependencies and integration points
- [ ] Identify hidden business logic
- [ ] Create feature parity checklist (`.spec/specs/feature-parity.md`)
- [ ] Validate characterization specs cover `.spec/intent.md` "Must Preserve" items
- [ ] Ratify constitution for new architecture
- [ ] Create dual project context (legacy + new)

**Gate**: Every module has a characterization spec. Constitution ratified.

**Prompts**: `analyst-brainstorm.md` → `analyst-legacy.md`

---

## Phase 2: Architecture Design

**Goal**: Target architecture with migration strategy

- [ ] Design new architecture with ADRs
- [ ] Choose migration strategy (Strangler Fig recommended)
- [ ] Define module migration order
- [ ] Design data migration strategy (reversible)
- [ ] API compatibility plan
- [ ] Implementation readiness: PASS / CONCERNS / FAIL

**Gate**: Architecture approved. Migration order defined. Readiness: PASS.

**Prompt**: `architect-design.md`

---

## Phase 3: Infrastructure

**Goal**: New skeleton + reference migration

- [ ] Set up new project with CI/CD
- [ ] Feature flag system operational
- [ ] Compatibility/adapter layer
- [ ] Complete ONE module migration as reference

**Gate**: Reference module migrated and verified.

---

## Phase 4: Incremental Migration

**Per-module cycle** (repeat for each module):

### 4a. Characterize
- [ ] Verify characterization specs complete
- [ ] Write characterization tests (pass against legacy)

### 4b. Specify
- [ ] Create proposal: `.spec/changes/migrate-[module]/proposal.md`
- [ ] Write delta specs: ADDED / MODIFIED / REMOVED
- [ ] Update feature parity checklist

### 4c. TDD Implement
- [ ] New implementation following new patterns
- [ ] TDD: RED → GREEN → REFACTOR
- [ ] Pass ALL characterization tests
- [ ] Deploy behind feature flag

### 4d. Verify
- [ ] Feature parity evidence (actual test output)
- [ ] Performance benchmark: new ≥ old
- [ ] Integration tests pass

### 4e. Rollout
- [ ] Gradual: 10% → 50% → 100%
- [ ] Bake period (minimum 1 week)

### 4f. Archive
- [ ] Remove feature flag + legacy code
- [ ] Merge delta specs into main specs
- [ ] Update migration tracker

**Prompts**: `dev-migration.md` → `qa-feature-parity.md`

---

## Phase 5: Completion

- [ ] All modules migrated
- [ ] Feature parity 100% verified
- [ ] Legacy code removed
- [ ] Documentation updated
- [ ] Performance report: old vs new

---

## Module Migration Tracker

| Module | Status | Parity |
|--------|--------|--------|
| {{MODULE_TRACKER_ROWS}} |

Statuses: `pending` → `analyzing` → `testing-legacy` → `implementing` → `verifying` → `rolled-out` → `archived`

---

## Rollback Plan

| Level | Trigger | Action |
|-------|---------|--------|
| Feature flag | Module regression | Toggle to legacy |
| Deploy | Multiple issues | Revert deployment |
| Data | Migration issue | Restore backup |
| Full | Systemic failure | All traffic to legacy |

---

## Strict Rules

1. Characterize before migrate
2. Feature parity is non-negotiable
3. No features during migration
4. Always have rollback
5. Evidence for every milestone
6. Delta specs for every change

---

## AI Prompt Usage Guide

| Phase | Prompt |
|-------|--------|
| Legacy analysis | `.spec/prompts/analyst-legacy.md` |
| Architecture | `.spec/prompts/architect-design.md` |
| Migration plan | `.spec/prompts/dev-migration.md` |
| Implementation | `.spec/prompts/dev-implement.md` + `dev-tdd.md` |
| Feature parity | `.spec/prompts/qa-feature-parity.md` |
| Code review | `.spec/prompts/qa-review.md` |
