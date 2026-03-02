---
name: tdd
description: Use this skill when the user asks to "implement with TDD", "test-driven development", "write tests first", "red-green-refactor", "TDD实现", "测试驱动开发" for {{PROJECT_NAME}}, or needs to implement code following strict test-first discipline. Enforces the TDD red-green-refactor cycle.
version: 1.0.0
---

# TDD Skill

Implement code for {{PROJECT_NAME}} using strict Test-Driven Development with the red-green-refactor cycle.

## When to Use

This skill activates when:
- User explicitly requests TDD or test-driven development
- User asks to "write tests first" or "implement with tests"
- User mentions "red-green-refactor" cycle
- User wants to ensure test coverage before implementation

## Context

Read @.spec/constitution.md for governance principles and testing requirements.
Read @.spec/project-context.md for tech stack, testing framework, and conventions.

## The Iron Law

NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
If code was written before its test, DELETE IT and restart. No exceptions.

## Cycle

The user's request will provide the specific feature or module to implement.

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
