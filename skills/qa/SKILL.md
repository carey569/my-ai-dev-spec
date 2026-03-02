---
name: qa
description: Use this skill when the user asks to "review code", "check quality", "code review", "代码审查", "质量检查", "审核代码", or needs comprehensive code review covering spec compliance, security, and quality. Performs structured code review following governance principles.
version: 1.0.0
---

# QA Skill

Perform comprehensive code review covering spec compliance, security, correctness, and quality.

## When to Use

This skill activates when:
- User requests code review or quality check
- User mentions "review", "QA", "quality", "check code"
- User wants to verify implementation against specifications
- User needs security or correctness validation

## Context Loading

Before starting, dynamically load project context:

1. Check if `.spec/constitution.md` exists in the project root
   - If exists: Read for governance principles and quality standards
   - If not: Use standard quality practices
2. Check if `.spec/project-context.md` exists in the project root
   - If exists: Read for tech stack, patterns, and conventions
   - If not: Infer patterns from codebase

## Instructions

The user's request will provide the changes to review (file paths or change description).

## Review Checklist

### Spec Compliance
- [ ] Implementation matches spec scenarios exactly
- [ ] No unrequested features added (gold plating)
- [ ] No spec requirements missing

### Constitution Compliance
- [ ] Follows project governance principles (if constitution exists)
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
