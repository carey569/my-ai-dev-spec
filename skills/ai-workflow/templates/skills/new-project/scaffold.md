---
name: scaffold
description: Use this skill when the user asks to "scaffold project", "set up infrastructure", "create project structure", "initialize project", "项目脚手架", "基础设施配置" for {{PROJECT_NAME}}. Sets up project infrastructure following the constitution and architecture.
version: 1.0.0
---

# Project Scaffold Skill

Set up project infrastructure for {{PROJECT_NAME}} following architecture and governance principles.

## When to Use

This skill activates when:
- User requests to scaffold or initialize the project
- User mentions "setup", "infrastructure", "project structure"
- User needs to create the initial project skeleton
- User wants to configure build tools and CI/CD

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack and conventions.

## Instructions

The user's request will describe what to scaffold.

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
