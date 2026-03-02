---
description: 项目脚手架搭建与基础设施配置
argument-hint: [搭建内容描述]
---

You are a Developer setting up project infrastructure for {{PROJECT_NAME}}.

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Task

$ARGUMENTS

## Instructions

1. Follow the architecture document for directory structure
2. Follow the constitution for tooling choices
3. Create:
   - Directory structure per architecture
   - Configuration files (linting, formatting, type checking)
   - CI pipeline configuration
   - "Hello world" entry point that verifies the setup
   - Trivial test that verifies test infrastructure
4. Document all commands in CLAUDE.md
5. Verify everything works:
   - `{{INSTALL_CMD}}`
   - `{{BUILD_CMD}}`
   - `{{TEST_CMD}}`
   - `{{LINT_CMD}}`
6. Show actual command output as evidence
