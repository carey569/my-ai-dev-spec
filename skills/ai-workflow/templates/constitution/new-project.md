# {{PROJECT_NAME}} Constitution

> Ratified: {{DATE}}
> Version: 1.0.0

This document establishes the non-negotiable principles governing all
development decisions for {{PROJECT_NAME}}. All specifications, plans,
and implementations must comply with these articles.

---

## Article I: Specification First

All features begin as written specifications before any implementation code.

- Every feature MUST have a spec document in `.spec/specs/` before coding starts
- Specs define WHAT and WHY; plans define HOW
- No PR may be merged without a corresponding spec
- Rationale: Specifications prevent scope creep, ensure shared understanding, and enable AI to produce consistent results

## Article II: Test-Driven Development

No production code without a failing test first.

- Write the test → verify it fails → implement → verify it passes → refactor
- If code was written before its test, delete the code and restart
- Test coverage for core business logic must exceed {{COVERAGE_TARGET}}%
- Rationale: TDD produces code that is correct by construction and safe to refactor

## Article III: {{ARCHITECTURE_ARTICLE_NAME}}

{{ARCHITECTURE_PRINCIPLE}}

- {{ARCHITECTURE_RULES}}
- Rationale: {{ARCHITECTURE_RATIONALE}}

## Article IV: Minimum Viable Change

Every change should be the smallest possible unit that delivers value.

- One concern per commit; one feature per branch
- Avoid premature abstraction — wait for 3+ concrete use cases
- Do not refactor unrelated code in feature branches
- Rationale: Small changes are easier to review, test, and roll back

## Article V: Explicit Over Implicit

All decisions, conventions, and constraints must be documented.

- Architecture decisions recorded as ADRs in `.spec/specs/`
- Mark ambiguous requirements with `[NEEDS CLARIFICATION]`
- Update `.spec/project-context.md` when new conventions emerge
- Rationale: Implicit knowledge is the enemy of AI-assisted development

## Article VI: Security by Default

Security is not a feature; it is a constraint on all features.

- Validate all external input at system boundaries
- Never commit secrets, credentials, or API keys
- Apply principle of least privilege
- Rationale: Security vulnerabilities are the most expensive bugs to fix

## Article VII: Domain Alignment

All development decisions must align with the project's stated intent and domain context.

- Domain terminology used consistently as defined in `.spec/intent.md`
- Business goals take precedence over technical convenience
- {{DOMAIN_CONTEXT}}
- Rationale: Correct domain modeling prevents the most expensive class of bugs

---

## Governance

### Amendment Process

1. Propose amendment with rationale in a change proposal
2. Review impact on existing specifications
3. Update version number (MAJOR for principle changes, MINOR for additions, PATCH for clarifications)
4. Update this document with the amendment date

### Compliance

- All AI-generated code must be reviewed against this constitution
- Constitutional violations in code review are blocking issues
- When a principle conflicts with practical needs, document the exception and rationale
