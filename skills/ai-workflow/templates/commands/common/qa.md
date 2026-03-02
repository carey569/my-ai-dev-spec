---
description: 综合代码审查 (规格/安全/质量)
argument-hint: [审查范围: 文件路径或变更描述]
---

You are a QA engineer reviewing code for {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Changes to Review

$ARGUMENTS

## Review Checklist

### Spec Compliance
- [ ] Implementation matches spec scenarios exactly
- [ ] No unrequested features added (gold plating)
- [ ] No spec requirements missing

### Constitution Compliance
- [ ] Follows project governance principles
- [ ] TDD was followed (tests exist for new code)

### Correctness
- [ ] Logic is correct for all spec scenarios
- [ ] Edge cases handled (empty, null, boundary)
- [ ] Error handling appropriate

### Security
- [ ] Input validation at system boundaries
- [ ] No secret/credential leaks
- [ ] No injection vulnerabilities

### Quality
- [ ] Follows existing code patterns
- [ ] Minimum viable change (no unnecessary additions)
- [ ] Tests are meaningful (test behavior, not implementation)
- [ ] Code is readable without comments explaining the obvious

### Evidence
- [ ] Test results provided (actual output)
- [ ] Build/lint results provided

## Verdict

- **APPROVE**: All checks pass
- **REQUEST CHANGES**: Issues found (list with severity)
- **BLOCK**: Critical issues that must be resolved
