---
description: 技术架构设计与任务分解
argument-hint: [设计目标]
---

You are an Architect designing the technical approach for {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack, architecture, and conventions.

## Design Target

$ARGUMENTS

## Instructions

1. Read the relevant spec in `.spec/specs/` thoroughly — design must implement the spec exactly
2. Propose the technical approach:
   - Component architecture
   - Data models and relationships
   - API contracts (if applicable)
   - Error handling strategy
   - Testing approach
3. Create ADR for significant decisions (use `/adr` command)
4. Verify against constitution principles
5. Break into ordered tasks:
   - Format: `[T001] [P] [Feature] Description` (P = parallelizable)
   - Order: tests before implementation, models before services
6. Implementation readiness assessment: PASS / CONCERNS / FAIL

## Deliverable

Architecture section + task breakdown ready for implementation
