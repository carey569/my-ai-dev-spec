# {{PROJECT_NAME}} Constitution

> Ratified: {{DATE}}
> Version: 1.0.0
> Extracted from: codebase analysis of {{TOTAL_COMMITS}} commits over {{REPO_AGE}} days

This document codifies the development principles observed in and required by
{{PROJECT_NAME}}. Extracted from existing patterns and elevated to non-negotiable rules.

---

## Article I: Stability First

Every change must preserve existing functionality.

- No PR may be merged if existing tests fail
- Regression tests are mandatory for every bug fix
- Test coverage must not decrease
- Rationale: In a mature codebase, breaking existing behavior is the highest-cost failure

## Article II: Specification Before Change

All changes begin as specifications, not code.

- New features: write a spec in `.spec/specs/` first
- Bug fixes: document root cause before fixing
- Changes: propose in `.spec/changes/` with delta specs (ADDED/MODIFIED/REMOVED)
- Rationale: Spec-first prevents scope creep and ensures impact is understood

## Article III: Consistency Over Preference

Follow existing patterns, even when you disagree.

- Match naming conventions, file organization, and code style of existing code
- Use the established {{FRAMEWORK}} patterns, not alternatives
- New patterns require a documented ADR with team consensus
- Rationale: Consistency reduces cognitive load and enables reliable AI assistance

## Article IV: Minimum Viable Change

Every change should be the smallest unit that delivers value.

- One concern per commit; one feature per branch
- Boy Scout Rule: improve one small thing when touching a file, no more
- Large refactors are separate tracked efforts, never mixed with features
- Rationale: Small changes are reviewable, testable, and reversible

## Article V: Evidence-Based Completion

Never declare a task complete without verification evidence.

- Provide actual test output, not "tests should pass"
- Show actual command results for build/lint/type checks
- For bug fixes: demonstrate the fix with before/after evidence
- Rationale: "It works on my machine" is not evidence

## Article VI: Backward Compatibility

Changes must not break downstream consumers without explicit migration.

- API changes require versioning or deprecation notices
- Database changes require reversible migrations
- Configuration changes require documentation
- Rationale: Breaking changes have unbounded downstream impact

## Article VII: Security by Default

Security is a constraint on all changes.

- Validate all external input at system boundaries
- Never commit secrets or credentials
- Security patches are highest priority and applied immediately
- Rationale: Security debt compounds faster than technical debt

---

## Observed Conventions (from codebase analysis)

These conventions were detected in the existing codebase and are hereby formalized:

{{OBSERVED_CONVENTIONS}}

## Governance

### Amendment Process
1. Propose with rationale in `.spec/changes/`
2. Review impact on existing work
3. Update version (MAJOR.MINOR.PATCH)

### Compliance
- All code changes reviewed against constitution
- Violations are blocking in code review
- Exceptions must be documented with rationale
