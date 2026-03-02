---
name: bugfix
description: Use this skill when the user asks to "fix bug", "debug issue", "diagnose problem", "resolve error", "Bug诊断", "修复bug" in {{PROJECT_NAME}}. Follows Quick Flow methodology for rapid bug resolution with test-first approach.
version: 1.0.0
---

# Bug Fix Skill

Fix bugs in {{PROJECT_NAME}} using test-driven diagnosis and minimal change approach.

## When to Use

This skill activates when:
- User reports a bug with expected vs actual behavior
- User asks to debug or diagnose an issue
- User mentions "bug", "error", "broken", "not working"

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Instructions

The user's request will describe the bug (expected behavior vs actual behavior).

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

Run: `{{TEST_CMD}}`
