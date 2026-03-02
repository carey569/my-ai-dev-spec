---
name: dev
description: Use this skill when the user asks to "implement feature", "code this", "build functionality", "实现功能", "编写代码", "开发功能", or needs to implement code following specifications. Follows spec-driven implementation with TDD and minimum necessary changes.
version: 1.0.0
---

# Developer Skill

Implement features following specifications with test-driven development and minimum necessary changes.

## When to Use

This skill activates when:
- User requests to implement a feature or functionality
- User mentions "implement", "code", "build", "develop"
- User has a specification and needs it implemented
- User wants spec-driven implementation

## Context Loading

Before starting, dynamically load project context:

1. Check if `.spec/constitution.md` exists in the project root
   - If exists: Read for governance principles and implementation rules
   - If not: Proceed with standard development practices
2. Check if `.spec/project-context.md` exists in the project root
   - If exists: Read for tech stack, patterns, and conventions
   - If not: Infer patterns from existing codebase

## Instructions

The user's request will provide the implementation task.

1. Read the spec in `.spec/specs/` and understand every scenario
2. Read related existing code in the project
3. Follow TDD for each unit:
   - Write failing test from spec scenario → verify it fails
   - Implement minimum code to pass → verify it passes
   - Refactor → verify tests still pass
4. Follow existing patterns — consistency over preference
5. Make minimum necessary changes
6. Provide evidence of completion:
   - Actual test output (copy-paste, not paraphrased)
   - Build/lint results if applicable
7. Update `.spec/project-context.md` if new patterns emerge
8. Mark any spec gaps with `[NEEDS CLARIFICATION]`

## Rules

- NO production code without a failing test first
- NO changes beyond what the spec requires
- NO new patterns without an ADR (Architecture Decision Record)

## Test Command Detection

Detect the test command from project context:
- If `package.json` exists: check `scripts.test` field
- If `Makefile` exists: check for `test` target
- If `pyproject.toml` exists: check `tool.poetry.scripts` or use `pytest`
- If `go.mod` exists: use `go test ./...`
- If `Cargo.toml` exists: use `cargo test`
- If none found: ask user for the test command
