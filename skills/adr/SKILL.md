---
name: adr
description: Use this skill when the user asks to "create ADR", "document decision", "architecture decision record", "创建ADR", "架构决策记录", "记录决策", or needs to document significant architectural or technical decisions. Creates structured Architecture Decision Records.
version: 1.0.0
---

# ADR Skill

Create Architecture Decision Records to document significant technical and architectural decisions.

## When to Use

This skill activates when:
- User requests to create an ADR
- User mentions "architecture decision", "technical decision", "ADR"
- User needs to document a significant design choice
- User wants to record rationale for a technical approach

## Instructions

The user's request will provide the decision topic.

Write the ADR in this format and save to `.spec/specs/adr/ADR-[NUMBER]-[title].md`:

```
# ADR-[NUMBER]: [Title]

## Status
[Proposed | Accepted | Deprecated | Superseded]

## Context
[What is the situation? What forces are at play?]

## Decision
[What is the decision and why?]

## Consequences
### Positive
- [benefit]

### Negative
- [trade-off]

### Neutral
- [side effect]
```

Check existing ADRs in `.spec/specs/adr/` to determine the next number.
