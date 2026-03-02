# {{PROJECT_NAME}} — Spec-Driven Development Workflow

> Generated: {{DATE}} | Type: **Maintenance** | Stack: {{PRIMARY_LANGUAGE}} / {{FRAMEWORK}}
> Repository: {{TOTAL_COMMITS}} commits, {{CONTRIBUTORS}} contributors, {{REPO_AGE}} days
> Methodology: OpenSpec change lifecycle + BMAD scale tracks + Superpowers TDD

---

## Quick Flow (Small Changes)

**Use for**: bug fixes, config changes, minor tweaks, dependency patches

```
1. Write failing test (if applicable)
2. Implement minimum change
3. Verify: test + full suite + evidence
4. Commit with descriptive message
```

---

## Full Method (Features & Significant Changes)

### Step 1: Propose
Create `.spec/changes/[name]/proposal.md`:
- Why: business reason
- What: scope (what changes, what doesn't)
- Impact: affected modules and specs
- Rollback: how to undo

### Step 2: Delta Specs
Create `.spec/changes/[name]/specs/[capability]/spec.md`:
- ADDED: new requirements with Given/When/Then
- MODIFIED: revised requirements (full text, not diff)
- REMOVED: deprecated requirements with reason

### Step 3: Tasks
Create `.spec/changes/[name]/tasks.md`:
- Ordered task list with TDD steps
- Each task: write test → implement → verify

### Step 4: TDD Implement
For each task: RED → GREEN → REFACTOR → evidence

### Step 5: Review
- Spec compliance check
- Regression check
- Constitution compliance
- Evidence verification

### Step 6: Archive
- Merge delta specs into `.spec/specs/`
- Move to `.spec/changes/archive/`

---

## Scale Decision Table

| Signal | → Quick Flow | → Full Method |
|--------|--------------|---------------|
| Bug with known cause | ✓ | |
| Single file change | ✓ | |
| Config/typo fix | ✓ | |
| Dependency minor update | ✓ | |
| New feature | | ✓ |
| New API endpoint | | ✓ |
| Cross-module change | | ✓ |
| Database change | | ✓ |
| Security fix | | ✓ |

---

## Bug Fix Flow

1. Reproduce (write failing test)
2. Root cause analysis (git blame for context)
3. Minimum fix
4. Verify: regression test + full suite
5. Document root cause in commit

**Prompt**: Use `.spec/prompts/dev-bugfix.md`

---

## Dependency Updates

| Type | Track | Process |
|------|-------|---------|
| Security patch | Quick Flow | Apply → test → deploy |
| Minor/patch | Quick Flow | Batch monthly → test |
| Major | Full Method | Proposal → breaking changes → test |

**Prompt**: Use `.spec/prompts/dev-dependency-update.md`

---

## Incident Response

```
DETECT → ASSESS → MITIGATE → FIX → PREVENT
```

**Prompt**: Use `.spec/prompts/ops-incident.md`

---

## High-Churn Files

{{HIGH_CHURN_FILES}}

---

## AI Prompt Usage Guide

| Situation | Prompt |
|-----------|--------|
| Discovery/analysis | `.spec/prompts/analyst-brainstorm.md` |
| New feature spec | `.spec/prompts/pm-requirements.md` |
| Architecture change | `.spec/prompts/architect-design.md` |
| Implementation | `.spec/prompts/dev-implement.md` |
| TDD cycle | `.spec/prompts/dev-tdd.md` |
| Bug fix | `.spec/prompts/dev-bugfix.md` |
| Dependency update | `.spec/prompts/dev-dependency-update.md` |
| Code review | `.spec/prompts/qa-review.md` |
| Incident | `.spec/prompts/ops-incident.md` |
