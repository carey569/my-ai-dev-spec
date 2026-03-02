# Maintenance Project Spec-Driven Workflow

Synthesizes: OpenSpec's brownfield-first change lifecycle, BMAD's scale-adaptive
tracks, Superpowers' evidence-based verification, Spec-Kit's governance.

## Philosophy

> "Real-world development is predominantly brownfield." — OpenSpec

Stability is the priority. Use spec-driven discipline to make changes safely:
propose → specify → implement → verify → archive.

---

## Scale Tracks (BMAD Adaptation)

### Quick Flow (Small Changes)

Use for: bug fixes, config changes, minor UI tweaks, dependency patches.

```
Trigger: Change < 30 min estimated effort
Pipeline: spec-note → TDD implement → verify → commit
Skip: formal proposal, delta specs, architecture review
```

### Full Method (Features & Significant Changes)

Use for: new features, API changes, architectural modifications, cross-module work.

```
Trigger: Change > 30 min OR affects public API OR crosses module boundaries
Pipeline: propose → delta specs → design → tasks → TDD implement → review → archive
```

### Decision Criteria

| Signal | → Quick Flow | → Full Method |
|--------|--------------|---------------|
| Single file change | ✓ | |
| Bug with known root cause | ✓ | |
| Dependency minor update | ✓ | |
| New endpoint/feature | | ✓ |
| Multiple module changes | | ✓ |
| Database schema change | | ✓ |
| Public API modification | | ✓ |
| Security-related change | | ✓ |

---

## Full Method: Change Lifecycle (OpenSpec)

### Step 1: Propose

Create `.spec/changes/[change-name]/proposal.md`:

```markdown
# Proposal: [Change Name]

## Why
[Business reason for this change]

## What
[Scope: what is changing, what is NOT changing]

## Impact
- Affected modules: [list]
- Affected specs: [list]
- Database changes: [yes/no]
- API changes: [yes/no]

## Rollback Plan
[How to undo if something goes wrong]
```

### Step 2: Delta Specs

Create `.spec/changes/[change-name]/specs/[capability]/spec.md`:

```markdown
## ADDED Requirements

### Requirement: [Name]
The system SHALL [new behavior].

#### Scenario: [Name]
- **GIVEN** [precondition]
- **WHEN** [action]
- **THEN** [result]

## MODIFIED Requirements

### Requirement: [Existing Name] (revised)
The system SHALL [updated behavior].
[Full revised text, not just the diff]

## REMOVED Requirements

### Requirement: [Name]
[Reason for removal]
```

### Step 3: Design (if architecture is affected)

Create `.spec/changes/[change-name]/design.md` with technical approach.

### Step 4: Tasks

Create `.spec/changes/[change-name]/tasks.md`:

```markdown
## Tasks

- [ ] Write failing test for [scenario]
- [ ] Implement [component]
- [ ] Update [affected module]
- [ ] Run full test suite
- [ ] Update project-context.md if patterns changed
```

### Step 5: TDD Implementation (Superpowers)

For each task:
1. Write failing test based on spec scenario (RED)
2. Implement minimum code to pass (GREEN)
3. Refactor while tests pass (REFACTOR)
4. Verify with actual output (evidence-based completion)

### Step 6: Review (BMAD QA Agent)

Review checklist:
- Spec compliance: does implementation match delta specs exactly?
- Regression: do all existing tests pass?
- Constitution: does the change comply with project principles?
- Evidence: are test results provided, not just claimed?

### Step 7: Archive (OpenSpec)

After change is verified and deployed:
1. ADDED specs append to main `.spec/specs/`
2. MODIFIED specs replace existing versions
3. REMOVED specs delete from main specs
4. Move change folder to `.spec/changes/archive/`

---

## Bug Fix Flow (Quick Flow)

```
1. Reproduce → write failing test
2. Identify root cause (not symptoms)
3. Check git blame for context
4. Fix minimum code
5. Verify: test passes + full suite passes
6. Document root cause in commit message
```

Evidence required: actual test output showing the fix works.

---

## Dependency Management

| Type | Track | Process |
|------|-------|---------|
| Security patch | Quick Flow | Apply → test → deploy immediately |
| Minor/patch update | Quick Flow | Batch monthly → full test suite |
| Major update | Full Method | Proposal → review breaking changes → test → deploy |
| Framework upgrade | Full Method | Treat as mini-project with own proposal |

---

## Quality Standards

### Testing
- Regression test for EVERY bug fix
- Tests for all new behavior (from spec scenarios)
- Coverage must not decrease
- TDD mandatory for all business logic

### CI/CD Quality Gates
- All tests pass
- Coverage >= existing level
- Lint and format checks pass
- Type checking passes
- Build succeeds in production mode

### Verification (Superpowers)
- Never declare done without evidence
- Provide actual command output for test/build/lint
- Show before/after for bug fixes

---

## Incident Response

```
1. DETECT:  Alert or user report
2. ASSESS:  Severity + blast radius (Quick Flow for triage)
3. MITIGATE: Rollback or hotfix (Quick Flow)
4. FIX:     Root cause fix with regression test (may escalate to Full Method)
5. PREVENT: Spec update + monitoring + test (Full Method proposal)
```

---

## Anti-Patterns to Avoid

1. **Skipping the proposal** — "It's a small change" grows into a large change without spec
2. **Mixing concerns** — One PR should address one change, not three
3. **Refactoring in feature branches** — Refactoring is a separate tracked effort
4. **Ignoring delta specs** — Without ADDED/MODIFIED/REMOVED tracking, specs drift from reality
5. **Declaring done without evidence** — Show the output, not "it works"
6. **Skipping TDD for "simple" changes** — Simple changes have simple tests; write them
