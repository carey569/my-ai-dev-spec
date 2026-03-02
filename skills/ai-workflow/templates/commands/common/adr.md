---
description: 创建架构决策记录 (ADR)
argument-hint: [决策主题]
---

Create an Architecture Decision Record for {{PROJECT_NAME}}.

## Decision

$ARGUMENTS

## Instructions

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
