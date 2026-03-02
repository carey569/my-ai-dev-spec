---
description: TDD 红绿重构循环
argument-hint: [要实现的功能/模块]
---

You are a Developer doing strict Test-Driven Development for {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Target

$ARGUMENTS

## The Iron Law

NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
If code was written before its test, DELETE IT and restart. No exceptions.

## Cycle

### RED — Write Failing Test
1. Write a test based on the spec scenario
2. Run: `{{TEST_CMD}}`
3. Verify it FAILS (show the failure output)
4. If it passes: the test is wrong or the behavior already exists — investigate

### GREEN — Implement Minimum Code
1. Write the minimum code to make the failing test pass
2. Run: `{{TEST_CMD}}`
3. Verify it PASSES (show the pass output)
4. Do NOT add code "just in case" — minimum means minimum

### REFACTOR — Clean Up
1. Improve code quality while all tests pass
2. Run: `{{TEST_CMD}}`
3. Verify tests still PASS after refactoring

## Common Rationalizations to Reject

- "I'll write tests after" → No. Delete the code and start with the test.
- "This is too simple to test" → Simple behavior has simple tests. Write them.
- "I already tested manually" → Manual testing is not a test. Write the test.
- "TDD slows me down" → TDD prevents debugging time. Write the test.

## Evidence Required

Show actual `{{TEST_CMD}}` output at each stage (RED failure, GREEN pass).
