---
name: tdd
description: Use this skill when the user asks to "implement with TDD", "test-driven development", "write tests first", "red-green-refactor", "TDD实现", "测试驱动开发", or needs to implement code following strict test-first discipline. Enforces the TDD red-green-refactor cycle.
version: 1.0.0
---

# TDD Skill

Implement code using strict Test-Driven Development with the red-green-refactor cycle.

## When to Use

This skill activates when:
- User explicitly requests TDD or test-driven development
- User asks to "write tests first" or "implement with tests"
- User mentions "red-green-refactor" cycle
- User wants to ensure test coverage before implementation

## Context Loading

Before starting, dynamically load project context:

1. Check if `.spec/constitution.md` exists in the project root
   - If exists: Read for governance principles and testing requirements
   - If not: Proceed with standard TDD principles
2. Check if `.spec/project-context.md` exists in the project root
   - If exists: Read for tech stack, testing framework, and conventions
   - If not: Detect testing setup from project files

## Test Command Detection

Detect the test command from project context:
- If `package.json` exists: check `scripts.test` field
- If `Makefile` exists: check for `test` target
- If `pyproject.toml` exists: check `tool.poetry.scripts` or use `pytest`
- If `go.mod` exists: use `go test ./...`
- If `Cargo.toml` exists: use `cargo test`
- If none found: ask user for the test command

## The Iron Law

NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
If code was written before its test, DELETE IT and restart. No exceptions.

## Cycle

The user's request will provide the specific feature or module to implement.

### RED — Write Failing Test
1. Write a test based on the spec scenario
2. Run the test command
3. Verify it FAILS (show the failure output)
4. If it passes: the test is wrong or the behavior already exists — investigate

### GREEN — Implement Minimum Code
1. Write the minimum code to make the failing test pass
2. Run the test command
3. Verify it PASSES (show the pass output)
4. Do NOT add code "just in case" — minimum means minimum

### REFACTOR — Clean Up
1. Improve code quality while all tests pass
2. Run the test command
3. Verify tests still PASS after refactoring

## Common Rationalizations to Reject

- "I'll write tests after" → No. Delete the code and start with the test.
- "This is too simple to test" → Simple behavior has simple tests. Write them.
- "I already tested manually" → Manual testing is not a test. Write the test.
- "TDD slows me down" → TDD prevents debugging time. Write the test.

## Evidence Required

Show actual test command output at each stage (RED failure, GREEN pass).
