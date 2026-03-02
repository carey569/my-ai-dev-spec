---
name: migrate
description: Use this skill when the user asks to "migrate module", "refactor component", "rewrite module", "迁移模块", "重构组件" in {{PROJECT_NAME}}. Follows characterization → proposal → TDD → verification workflow.
version: 1.0.0
---

# Module Migration Skill

Migrate modules in {{PROJECT_NAME}} following characterization-driven refactoring workflow.

## When to Use

This skill activates when:
- User requests to migrate or refactor a module
- User mentions "migrate", "refactor", "rewrite", "modernize"
- User needs to move code to new architecture
- User wants to replace legacy implementation

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for migration context (legacy + new architecture).

## Instructions

The user's request will specify the module to migrate.

## Migration Checklist

### 1. Characterization (verify done)
- [ ] Characterization spec exists at `.spec/specs/legacy/[module]/spec.md`
- [ ] Characterization tests exist and pass against legacy

### 2. Propose
- [ ] Create `.spec/changes/migrate-[module]/proposal.md`
- [ ] Write delta specs:
  - ADDED: new behaviors in new architecture
  - MODIFIED: changed behaviors with rationale
  - REMOVED: deprecated behaviors with rationale

### 3. TDD Implement
- [ ] Create new implementation following NEW architecture patterns
- [ ] TDD: write test from spec scenario (RED) → implement (GREEN) → refactor
- [ ] Pass ALL characterization tests
- [ ] Do NOT replicate legacy anti-patterns

### 4. Verify
- [ ] All characterization tests pass against new implementation
- [ ] All new unit tests pass
- [ ] Performance benchmark: new >= old (show actual numbers)

### 5. Deploy
- [ ] Deploy behind feature flag
- [ ] Verify in staging environment

## Rules

- NEVER migrate without characterization tests
- NEVER replicate legacy anti-patterns
- NEVER mix new features with migration work
- ALWAYS have rollback via feature flag

## Evidence Required

- Characterization test results (pass against new)
- Performance comparison (old vs new, actual numbers)
- Integration test results
