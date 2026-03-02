---
name: pm
description: Use this skill when the user asks to "write spec", "create specification", "define requirements", "编写规格", "创建规范", "定义需求" for {{PROJECT_NAME}}, or needs to document feature requirements using Given/When/Then format. Creates structured specifications following spec-driven development principles.
version: 1.0.0
---

# Product Manager Skill

Create structured specifications for {{PROJECT_NAME}} using Given/When/Then format, following spec-driven development principles.

## When to Use

This skill activates when:
- User requests to write a specification or requirements document
- User mentions "spec", "requirements", "user story", "acceptance criteria"
- User needs to define what a feature should do (WHAT, not HOW)
- User asks to document feature behavior in Given/When/Then format

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack, conventions, and domain terminology.

## Instructions

The user's request will provide the feature to specify.

1. Clarify requirements by asking specific questions
2. Write the specification in `.spec/specs/[feature]/spec.md` using this format:

```
## Feature: [Name]

### Requirement: [Requirement Name]
The system SHALL [behavior description].

#### Scenario: [Scenario Name]
- **GIVEN** [precondition]
- **WHEN** [action]
- **THEN** [expected result]
- **AND** [additional expectation]
```

3. Every requirement MUST have at least one scenario
4. Mark ambiguities with `[NEEDS CLARIFICATION]`
5. Check spec against `.spec/constitution.md` for compliance
6. Do NOT include technical implementation details (WHAT, not HOW)

## Deliverable

A complete spec.md file in `.spec/specs/[feature]/`
