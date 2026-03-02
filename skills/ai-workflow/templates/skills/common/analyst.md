---
name: analyst
description: Use this skill when the user asks to "brainstorm", "explore options", "analyze problem", "discover requirements", "结构化头脑风暴", "问题探索", "需求发现" for {{PROJECT_NAME}}, or needs structured discovery before specification. Facilitates structured brainstorming sessions following spec-driven principles.
version: 1.0.0
---

# Analyst Skill

Facilitate structured brainstorming and problem exploration for {{PROJECT_NAME}} following spec-driven development.

## When to Use

This skill activates when:
- User requests brainstorming or exploration
- User mentions "analyst", "discovery", "options", "approaches"
- User needs to understand a problem before specifying
- User asks to explore trade-offs or alternatives

## Context

Read @.spec/constitution.md for governance principles and constraints.
Read @.spec/project-context.md for tech stack, conventions, and patterns.

## Instructions

The user's request will provide the specific topic or problem to explore.

1. Ask ONE question at a time to deeply understand the problem
2. After understanding, propose 2-3 approaches with trade-offs for each:
   - Pros and cons
   - Complexity assessment
   - Constitution compliance
3. Present a design document for approval BEFORE any implementation
4. Save approved design to `.spec/specs/[feature]/design.md`

## Rules

- Do NOT write any code during brainstorming
- Do NOT propose solutions before understanding the problem
- Challenge assumptions respectfully
- Mark unknowns with `[NEEDS CLARIFICATION]`
