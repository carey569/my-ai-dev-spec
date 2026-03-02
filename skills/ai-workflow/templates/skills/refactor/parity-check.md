---
name: parity-check
description: Use this skill when the user asks to "verify parity", "check feature parity", "validate migration", "功能对等检查", "迁移验证" in {{PROJECT_NAME}}. Verifies migrated modules maintain feature parity with legacy.
version: 1.0.0
---

# Feature Parity Check Skill

Verify feature parity for migrated modules in {{PROJECT_NAME}}.

## When to Use

This skill activates when:
- User requests to verify feature parity
- User mentions "parity check", "validate migration", "compare implementations"
- User needs to ensure migrated code matches legacy behavior
- User wants to verify migration completeness

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for migration context.

## Instructions

The user's request will specify the module under verification.

## References

- Characterization spec: `.spec/specs/legacy/[module]/spec.md`
- Delta specs: `.spec/changes/migrate-[module]/specs/`

## Verification Process

### For EACH capability in the characterization spec:
1. **Identify**: Read the scenario
2. **Test**: Verify the new implementation handles it correctly
3. **Evidence**: Run the test and capture actual output
4. **Compare**: If behavior differs from legacy:
   - Check delta specs: is this an intentional MODIFIED or REMOVED?
   - If intentional: verify rationale is documented
   - If unintentional: flag as parity failure

### Performance Verification
- Run performance benchmark against legacy and new
- New must meet or exceed old
- Show actual numbers, not estimates

### Integration Verification
- Verify all upstream callers work with new implementation
- Verify all downstream dependencies are satisfied

## Report Template

```
## Feature Parity Report: [Module]

### Status: [PASS / PARTIAL / FAIL]

### Verified Capabilities
| Capability | Scenarios | Result | Evidence |
|------------|-----------|--------|----------|
| [name] | [count] | PASS/FAIL | [test output ref] |

### Intentional Changes (from delta specs)
- [MODIFIED]: [description] — [rationale]
- [REMOVED]: [description] — [rationale]

### Issues Found
- [issue description + severity]

### Performance
| Metric | Legacy | New | Verdict |
|--------|--------|-----|---------|
| [metric] | [value] | [value] | pass/fail |

### Recommendation
[Ready for rollout / Needs more work / Block — with reasons]
```

## Rules

- NEVER approve without running actual tests
- NEVER skip edge cases or error scenarios
- ALWAYS verify performance, not just correctness
- ALWAYS check delta specs before flagging behavioral differences
