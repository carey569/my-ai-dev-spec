---
description: 生成产品需求文档 (PRD)，含业务场景、流程图和交互原型
argument-hint: [需求描述]
---

Product Manager creating a Product Requirements Document for {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.
Read @.spec/intent.md for project goals (if available).

## Requirements

$ARGUMENTS

## Instructions

1. Analyze the requirements to extract 2-5 business scenarios
2. For each scenario, define user roles, journeys, flows, and functional support
3. Generate business process documentation with Mermaid flow diagrams (MD + HTML)
4. Produce structured requirements list (FR/NFR/UI)
5. Create high-fidelity HTML interactive prototype
6. Save all outputs to `.spec/prd/[project-slug]/`

## Execution Modes

- Default: Phase 1-2 auto, pause before Phase 3
- `--auto`: All phases without pausing
- `--interactive`: Pause after each phase
- `--stage=N`: Only run phase N

## Deliverables

- `phase1-scenarios.md` — Scenario analysis
- `phase2-business-doc.md` + `.html` — Business process documentation
- `phase3-requirements.md` — Structured requirements
- `phase3-prototype.html` — Interactive prototype

After PRD approval, use the `pm` skill to create detailed Given/When/Then specifications.
