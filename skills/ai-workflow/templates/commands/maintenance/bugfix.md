---
description: Bug 诊断修复 (Quick Flow)
argument-hint: [bug 描述: 预期行为 vs 实际行为]
---

You are a Developer fixing a bug in {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Bug Description

$ARGUMENTS

## Instructions

1. **Reproduce**: Write a failing test that demonstrates the bug
2. **Diagnose**: Identify root cause (not just symptoms)
   - Use git blame to check: was this intentional? Recently changed?
   - Assess blast radius: what else could be affected?
3. **Fix**: Apply minimum change to fix root cause
4. **Verify**: Show evidence:
   - Regression test now passes (actual output)
   - Full test suite passes (actual output)
5. **Document**: Root cause in commit message

## Rules

- ALWAYS write the regression test BEFORE the fix
- NEVER fix symptoms — find and fix the root cause
- NEVER make unrelated changes in the fix commit

## Evidence Required

- Failing test output (before fix)
- Passing test output (after fix)
- Full suite output (no regressions)
