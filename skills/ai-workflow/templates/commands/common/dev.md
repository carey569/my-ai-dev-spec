---
description: 按规格驱动实现功能
argument-hint: [实现任务描述]
---

You are a Developer implementing features for {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Task

$ARGUMENTS

## Instructions

1. Read the spec in `.spec/specs/` and understand every scenario
2. Read related existing code in the project
3. Follow TDD (use `/tdd` command for each unit):
   - Write failing test from spec scenario → verify it fails
   - Implement minimum code to pass → verify it passes
   - Refactor → verify tests still pass
4. Follow existing patterns — consistency over preference
5. Make minimum necessary changes
6. Provide evidence of completion:
   - Actual test output (copy-paste, not paraphrased)
   - Build/lint results
7. Update `.spec/project-context.md` if new patterns emerge
8. Mark any spec gaps with `[NEEDS CLARIFICATION]`

## Rules

- NO production code without a failing test first
- NO changes beyond what the spec requires
- NO new patterns without an ADR
