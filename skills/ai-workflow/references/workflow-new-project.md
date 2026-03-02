# New Project (0→1) Spec-Driven Development Workflow

Synthesizes: Spec-Kit's constitution-first pipeline, Superpowers' mandatory
design→plan→TDD, BMAD's role-based agents, OpenSpec's spec structure.

## Philosophy

> "Specifications are the source of truth. Code serves the specification." — Spec-Kit

Build foundations right: establish governance, define specifications, then
implement with TDD. Resist the urge to "just start coding."

---

## Phase 1: Constitution and Context (Day 1)

*Agents: Analyst + Architect*

### Objectives
- Establish project governance (constitution)
- Define tech stack and architectural direction
- Initialize spec-driven development workspace

### Checklist
- [ ] Initialize git repository
- [ ] Create `.spec/` directory structure
- [ ] Draft `constitution.md` — non-negotiable principles (test-first, spec-first, security, etc.)
- [ ] Draft `project-context.md` — tech stack, conventions, initial architecture
- [ ] Create `CLAUDE.md` with initial AI behavioral guidelines
- [ ] Set up package manager and install core dependencies
- [ ] Configure linting, formatting, and type checking
- [ ] Set up initial CI pipeline (lint + type check)

### Quality Gate (Spec-Kit style)
- Constitution ratified (all articles have rationale)
- Project context documents exact versions and commands
- CI pipeline passes
- `[NEEDS CLARIFICATION]` items documented (not hidden)

### Scale Track (BMAD)
This phase is always "Full Method" — never skip governance for new projects.

---

## Phase 2: Specification (Days 2-4)

*Agents: PM + Architect*

### Objectives
- Define WHAT the system does (not HOW) as specifications
- Capture user stories with acceptance criteria
- Identify ambiguities explicitly

### Checklist
- [ ] Write specs for core features in `.spec/specs/[feature-name]/spec.md`
- [ ] Use Gherkin-style scenarios (Given/When/Then) for acceptance criteria (OpenSpec)
- [ ] Mark ambiguities with `[NEEDS CLARIFICATION]` (Spec-Kit)
- [ ] Define data models and API contracts
- [ ] Review specs against constitution for compliance
- [ ] Get user/stakeholder approval on specs

### Spec Format (OpenSpec style)
```markdown
## Feature: [Name]

### Requirement: [Requirement Name]
The system SHALL [behavior description].

#### Scenario: [Scenario Name]
- **GIVEN** [precondition]
- **WHEN** [action]
- **THEN** [expected result]
- **AND** [additional expectation]
```

### Quality Gate
- All features have specs with at least one scenario each
- No `[NEEDS CLARIFICATION]` items remain unresolved
- Constitution compliance verified

---

## Phase 3: Architecture and Planning (Days 3-5)

*Agents: Architect + PM*

### Objectives
- Define HOW the system will be built (technical architecture)
- Create ADRs for key decisions
- Break specs into implementable tasks

### Checklist
- [ ] Create architecture document with:
  - Directory structure
  - Component diagram
  - Data flow diagram
  - API contracts
  - Technology justifications as ADRs
- [ ] Verify architecture against constitution principles
- [ ] Break each spec into ordered tasks (Spec-Kit format):
  - `[T001] [P] [Feature] Task description` (P = parallelizable)
  - Phase tasks: setup → models → services → endpoints → integration
  - Within each phase: test first, then implement (Superpowers TDD)
- [ ] Update `project-context.md` with architecture decisions
- [ ] Implementation readiness check (BMAD gate: PASS / CONCERNS / FAIL)

### Quality Gate
- Architecture documented and reviewed
- Task breakdown complete with dependency ordering
- Implementation readiness: PASS
- At least one vertical slice defined as reference implementation

---

## Phase 4: Foundation Implementation (Days 5-7)

*Agents: Developer (TDD mode)*

### Objectives
- Implement project skeleton with working build/test/lint
- Complete reference implementation (one vertical slice)
- Verify development workflow end-to-end

### Checklist
- [ ] Create directory structure per architecture document
- [ ] Set up build pipeline: `install` → `dev` → `build` → `test` → `lint`
- [ ] Write first test (verify test infrastructure works)
- [ ] Implement reference vertical slice following TDD:
  1. Write failing test (RED)
  2. Implement minimum code to pass (GREEN)
  3. Refactor while tests pass (REFACTOR)
- [ ] Set up pre-commit hooks (lint + format + type check)
- [ ] Document all commands in CLAUDE.md
- [ ] Update `project-context.md` with implementation patterns

### Quality Gate (Superpowers verification)
- All commands documented and working (evidence: actual output)
- Reference implementation passes all tests
- CI pipeline passes
- New developer can clone and run in < 5 minutes

### Scale Track
- Small tasks (< 30 min): Quick Flow — spec → implement → verify
- Larger tasks: Full Method — spec → plan → TDD implement → review

---

## Phase 5: Core Implementation (Days 7-21)

*Agents: Developer + QA*

### Objectives
- Implement remaining features per spec and task breakdown
- Maintain TDD discipline throughout
- Continuous verification against specs

### Task Execution (Superpowers pattern)
For each task batch (3-5 tasks):
1. Read the spec for the feature being implemented
2. Write failing tests based on spec scenarios
3. Implement minimum code to pass tests
4. Verify against spec acceptance criteria (evidence required)
5. Code review checkpoint (QA agent)
6. Commit and continue

### Checklist
- [ ] Implement features in task order (respect dependencies)
- [ ] TDD for all business logic — no exceptions
- [ ] Integration tests for all API endpoints / user flows
- [ ] Input validation at system boundaries
- [ ] Error handling per architecture document
- [ ] Logging per project context conventions
- [ ] Security review (OWASP top 10)
- [ ] Update specs if implementation reveals new requirements

### Quality Gate
- All spec scenarios pass as tests
- Core business logic coverage > 70%
- No critical security issues
- All `[NEEDS CLARIFICATION]` items resolved

---

## Phase 6: Documentation and Deployment (Days 14-21)

*Agents: Developer + PM*

### Checklist
- [ ] Complete README with setup, usage, and contribution guide
- [ ] API documentation (if applicable)
- [ ] Deployment configuration
- [ ] Final CLAUDE.md review and update
- [ ] Final `project-context.md` review
- [ ] Archive completed specs (all are now baseline specifications)

### Quality Gate
- Documentation enables new contributor onboarding without assistance
- Deployment is automated and repeatable
- All `.spec/` files are current and accurate

---

## Anti-Patterns to Avoid

1. **Skipping specs** — "I'll just start coding" leads to rework
2. **Skipping TDD** — "Tests slow me down" leads to bugs and fragile code
3. **Gold plating** — Building beyond spec leads to scope creep
4. **Vague specs** — If you can't write a Given/When/Then, the requirement isn't clear
5. **Ignoring constitution** — Principles exist for reasons; violating them has consequences
6. **Declaring done without evidence** — Show the test output, not "it should work"
