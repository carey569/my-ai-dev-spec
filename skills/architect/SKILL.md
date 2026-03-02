---
name: architect
description: Use this skill when the user asks to "design architecture", "create technical design", "break down tasks", "架构设计", "技术设计", "任务分解", or needs to design the technical approach for implementing a feature. Creates architecture designs and task breakdowns.
version: 1.0.0
---

# Architect Skill

Design technical approaches and break down features into implementation tasks.

## When to Use

This skill activates when:
- User requests architecture or technical design
- User mentions "design", "architect", "technical approach"
- User needs to break down a feature into tasks
- User wants to understand how to implement a specification

## Context Loading

Before starting, dynamically load project context:

1. Check if `.spec/constitution.md` exists in the project root
   - If exists: Read for governance principles and architectural constraints
   - If not: Proceed without project-specific constraints
2. Check if `.spec/project-context.md` exists in the project root
   - If exists: Read for tech stack, architecture patterns, and conventions
   - If not: Infer architecture from existing codebase

## Instructions

The user's request will provide the design target.

1. Read the relevant spec in `.spec/specs/` thoroughly — design must implement the spec exactly
2. Propose the technical approach:
   - Component architecture
   - Data models and relationships
   - API contracts (if applicable)
   - Error handling strategy
   - Testing approach
3. Create ADR for significant decisions (suggest using the adr skill)
4. Verify against constitution principles (if constitution exists)
5. Break into ordered tasks:
   - Format: `[T001] [P] [Feature] Description` (P = parallelizable)
   - Order: tests before implementation, models before services
6. Implementation readiness assessment: PASS / CONCERNS / FAIL

## Deliverable

Architecture section + task breakdown ready for implementation
