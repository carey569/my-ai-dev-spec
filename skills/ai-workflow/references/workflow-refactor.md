# Refactor Project Spec-Driven Workflow

Synthesizes: BMAD's story-driven migration with agent personas, OpenSpec's
delta specs for tracking changes, Superpowers' TDD and evidence-based verification,
Spec-Kit's constitutional governance for the new architecture.

## Philosophy

> "Refactoring is surgery on a living system. Characterize before you cut." — Adapted from BMAD

Migrate incrementally with specifications as the bridge between old and new.
Every behavior must be captured as a spec before migration, verified after migration,
and tracked with delta specs throughout.

---

## Phase 1: Legacy Analysis and Constitution (Week 1)

*BMAD Agents: Analyst + Architect*

### Objectives
- Complete understanding of the legacy system
- Feature parity baseline established
- New architecture constitution ratified

### Checklist
- [ ] **Analyst**: Brainstorm and document all legacy capabilities
  - Entry points, side effects, edge cases, hidden business logic
  - Create `.spec/specs/legacy/[module]/spec.md` for each module
  - Use characterization spec format (capture current behavior, even if imperfect)
- [ ] **Analyst**: Map dependency graph and integration points
- [ ] **Architect**: Draft constitution for new architecture
  - Article: Feature parity is non-negotiable
  - Article: Characterization tests before migration
  - Article: Incremental migration (strangler fig)
  - Article: Always have rollback
  - Article: No new features during migration
- [ ] Create feature parity checklist: `.spec/specs/feature-parity.md`
- [ ] Create `project-context.md` with dual context (legacy + new)
- [ ] Define success criteria for the refactor

### Quality Gate
- Every legacy module has a characterization spec
- Feature parity checklist is complete and stakeholder-approved
- Constitution ratified
- Risk assessment documented

### Characterization Spec Format
```markdown
# Legacy Module: [Name]

## Current Behavior

### Capability: [Name]
The system currently [behavior description].

#### Scenario: Normal operation
- **GIVEN** [legacy precondition]
- **WHEN** [action]
- **THEN** [observed result]

#### Scenario: Error handling
- **GIVEN** [error condition]
- **WHEN** [action]
- **THEN** [observed error behavior]

## Hidden Logic
- [Undocumented behavior discovered during analysis]

## Integration Points
- [Upstream]: [description]
- [Downstream]: [description]
```

---

## Phase 2: Architecture Design (Week 1-2)

*BMAD Agents: Architect + PM*

### Objectives
- Target architecture designed
- Migration strategy defined
- Module migration order established

### Checklist
- [ ] Design target architecture with ADRs
- [ ] Choose migration strategy:
  - **Strangler Fig** (recommended): incremental replacement
  - **Parallel Run**: compare outputs side by side
  - **Big Bang**: full switch (highest risk — constitution must explicitly approve)
- [ ] Define module migration order (least coupled → most coupled)
- [ ] Design data migration strategy (all migrations must be reversible)
- [ ] Plan API compatibility layer (if external consumers exist)
- [ ] Create `.spec/specs/architecture.md` with new patterns
- [ ] Implementation readiness gate (BMAD: PASS / CONCERNS / FAIL)

### Migration Order Strategy
1. Least coupled, most well-understood modules first
2. Modules with best existing test coverage next
3. Core/critical modules after gaining confidence
4. Modules with most integrations last

---

## Phase 3: Infrastructure (Week 2-3)

*BMAD Agent: Developer*

### Checklist
- [ ] Set up new project skeleton with CI/CD
- [ ] Implement shared utilities
- [ ] Set up feature flag system
- [ ] Create compatibility/adapter layer
- [ ] Set up integration tests for both old and new paths
- [ ] Complete reference module migration (one full cycle):
  1. Characterization specs (already done in Phase 1)
  2. Characterization tests
  3. New implementation
  4. Verification
  5. Feature flag deployment
  6. Archive

---

## Phase 4: Incremental Migration (Week 3-N)

*BMAD Agents: Analyst (legacy) + Developer (new) + QA (review)*

### Per-Module Migration (Repeat for Each Module)

#### 4a. Characterize (Analyst Agent)
- [ ] Verify characterization specs from Phase 1 are complete
- [ ] Write characterization tests that pass against legacy

#### 4b. Specify (PM Agent)
- [ ] Create change proposal: `.spec/changes/migrate-[module]/proposal.md`
- [ ] Write delta specs (OpenSpec format):
  ```markdown
  ## ADDED Requirements
  [New behaviors in new architecture]

  ## MODIFIED Requirements
  [Behavioral changes with rationale]

  ## REMOVED Requirements
  [Deprecated behaviors with rationale]
  ```
- [ ] Update feature parity checklist

#### 4c. Implement (Developer Agent — TDD)
- [ ] Implement new version following new architecture patterns
- [ ] TDD cycle: RED → GREEN → REFACTOR
- [ ] New implementation must pass ALL characterization tests
- [ ] Write additional unit tests for new patterns
- [ ] Deploy behind feature flag

#### 4d. Verify (QA Agent)
- [ ] Characterization tests pass against new implementation
- [ ] Performance benchmark: new meets or exceeds old
- [ ] Feature parity checklist items verified (evidence required)
- [ ] Integration tests pass
- [ ] Parallel comparison (if applicable): old and new produce same outputs

#### 4e. Rollout
- [ ] Gradual rollout: 10% → 50% → 100%
- [ ] Monitor errors, performance, correctness at each stage
- [ ] Bake period (minimum 1 week at 100%)

#### 4f. Archive (OpenSpec)
- [ ] Remove feature flag
- [ ] Remove legacy code for this module
- [ ] Archive change: merge delta specs into main `.spec/specs/`
- [ ] Move change folder to `.spec/changes/archive/`
- [ ] Update migration tracker in `.spec/project-context.md`
- [ ] Update feature parity checklist (mark as verified)

---

## Phase 5: Completion (Final Week)

### Checklist
- [ ] All modules migrated and verified
- [ ] Feature parity checklist 100% complete (with evidence)
- [ ] All feature flags removed
- [ ] Legacy code removed from codebase
- [ ] Database cleanup completed
- [ ] All `.spec/` files updated for final architecture
- [ ] Performance benchmark report: old vs new
- [ ] Constitution updated (remove migration-specific articles)
- [ ] Stakeholder sign-off

---

## Rollback Strategy

| Level | When | How |
|-------|------|-----|
| Feature flag | Single module regression | Toggle to "legacy" |
| Deploy rollback | Multiple module issues | Revert deployment |
| Data rollback | Migration data issues | Restore from backup |
| Full rollback | Systemic failure | All traffic to legacy |

**Readiness checklist:**
- [ ] Feature flags tested bidirectionally
- [ ] Database backups automated and verified
- [ ] Rollback procedure documented and practiced
- [ ] Monitoring alerts for regression indicators

---

## Strict Rules

1. **Characterize first** — Never migrate without capturing current behavior as specs and tests
2. **Feature parity required** — New must match or exceed old in every documented behavior
3. **No features during migration** — Migration branches contain ONLY migration work
4. **Always have rollback** — Never remove legacy code until new is proven in production
5. **Evidence required** — Show test output, performance comparison, parity verification
6. **Delta specs for everything** — Every behavioral change tracked as ADDED/MODIFIED/REMOVED

---

## Anti-Patterns to Avoid

1. **Big Bang rewrite** — "Let's just rewrite everything at once" (highest failure rate)
2. **Skipping characterization** — "I understand the legacy code" (you don't, fully)
3. **New features in migration** — "While we're at it, let's also add..." (scope creep)
4. **Removing legacy too early** — "It's working, let's delete the old code" (premature)
5. **Ignoring hidden logic** — "The spec covers everything" (legacy has undocumented behaviors)
6. **Declaring parity without evidence** — "It looks the same" (prove it with test output)
