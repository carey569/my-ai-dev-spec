# {{PROJECT_NAME}} Constitution

> Ratified: {{DATE}}
> Version: 1.0.0
> Migration: {{LEGACY_TECH_STACK}} → {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}

This document governs the refactoring of {{PROJECT_NAME}}. It establishes
principles for the NEW architecture while defining rules for safely
migrating from the legacy system.

---

## Article I: Feature Parity is Non-Negotiable

The new system must replicate every documented behavior of the legacy system.

- Feature parity checklist must be maintained in `.spec/specs/feature-parity.md`
- Every legacy behavior must have a characterization test before migration
- No migration is complete until parity is verified with evidence
- Rationale: Users don't care about the architecture; they care about their workflows

## Article II: Characterization Tests Before Migration

Never migrate a module without capturing its current behavior in tests.

- Write characterization tests that pass against the LEGACY implementation
- These tests become the verification suite for the new implementation
- Cover normal paths, error paths, and edge cases
- Rationale: You cannot verify parity without a baseline

## Article III: Specification Before Implementation

All migration work begins as specifications.

- Each module migration requires a spec in `.spec/specs/`
- Delta specs (ADDED/MODIFIED/REMOVED) track every behavioral change
- Intentional behavioral changes must be documented with rationale
- Rationale: Undocumented changes are the leading cause of migration failures

## Article IV: Incremental Migration (Strangler Fig)

Migrate one module at a time. Never attempt a Big Bang rewrite.

- Follow the module migration order in `.spec/workflow.md`
- Each module deploys behind a feature flag
- Old and new run in parallel until the new is proven
- Remove legacy code only after bake period with no issues
- Rationale: Incremental migration reduces risk and allows course correction

## Article V: Always Have Rollback

Every migration step must be reversible.

- Feature flags enable instant rollback per module
- Database migrations must have down/rollback scripts
- Deployment rollback procedure must be documented and tested
- Rationale: The cost of rollback capability is always less than the cost of being stuck

## Article VI: No New Features During Migration

Migration branches contain ONLY migration work.

- New features go in separate branches against the new architecture
- Do not mix new functionality with migration work
- If a feature requires an unmigrated module, migrate the module first
- Rationale: Scope creep is the primary risk in refactoring projects

## Article VII: New Architecture Patterns Only

All new code follows the NEW architecture. Never replicate legacy anti-patterns.

- Follow {{ARCHITECTURE}} pattern for all new modules
- Use {{FRAMEWORK}} idioms, not legacy conventions
- Document new patterns in `.spec/project-context.md`
- Rationale: The purpose of refactoring is to improve; replicating old patterns defeats that purpose

## Article VIII: Evidence-Based Completion

Every migration milestone requires verification evidence.

- Characterization tests pass against new implementation
- Performance benchmarks compared: new meets or exceeds old
- Feature parity checklist items verified with actual test output
- Rationale: "It looks right" is not evidence of parity

## Article IX: Refactor Intent Alignment

All migration decisions must align with the documented refactor intent.

- Motivation and target state documented in `.spec/intent.md`
- Priority modules migrated in defined order, adjustments require documented rationale
- Pain points drive priority — do not optimize for theoretical benefits
- Rationale: Refactors fail when they lose sight of the original motivation

---

## Governance

### Amendment Process
1. Propose with rationale
2. Review migration impact
3. Update version (MAJOR.MINOR.PATCH)

### Compliance
- Migration PRs reviewed against constitution
- Parity violations are blocking
- Constitution exceptions documented with rationale and timeline to resolve
