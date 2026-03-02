---
name: legacy-analyze
description: Use this skill when the user asks to "analyze legacy code", "characterize module", "understand existing code", "遗留代码分析", "表征测试" in {{PROJECT_NAME}}. Creates characterization specs for legacy modules before refactoring.
version: 1.0.0
---

# Legacy Code Analysis Skill

Document legacy code behavior for {{PROJECT_NAME}} through characterization specifications.

## When to Use

This skill activates when:
- User requests to analyze or understand legacy code
- User mentions "characterize", "legacy analysis", "document existing behavior"
- User needs to understand a module before refactoring
- User wants to create characterization tests

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for legacy tech stack details.

## Instructions

The user's request will specify the target module (name or file path).

1. Read the legacy module thoroughly
2. Create a characterization spec in `.spec/specs/legacy/[module]/spec.md`:

```
# Legacy Module: [Name]

## Current Behavior

### Capability: [Name]
The system currently [behavior description].

#### Scenario: Normal operation
- **GIVEN** [precondition]
- **WHEN** [action]
- **THEN** [observed result]

#### Scenario: Error handling
- **GIVEN** [error condition]
- **WHEN** [action]
- **THEN** [observed error behavior]

## Hidden Logic
- [Undocumented behaviors]

## Side Effects
- [Database writes, API calls, file I/O, events]

## Integration Points
- [Upstream]: [what calls this module]
- [Downstream]: [what this module calls]

## Performance Characteristics
- [Caching, batching, rate limiting]
```

3. Document EVERYTHING — even behavior that seems wrong
4. Flag concerns: security issues, performance problems, unclear logic
5. Mark unknowns with `[NEEDS INVESTIGATION]`

## Rules

- Document WHAT the code does, not what it SHOULD do
- Capture edge cases and error handling exactly as implemented
- Include hardcoded values and magic numbers
- Note any undocumented dependencies
