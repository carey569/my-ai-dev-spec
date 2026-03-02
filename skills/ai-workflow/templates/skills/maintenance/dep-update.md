---
name: dep-update
description: Use this skill when the user asks to "update dependencies", "upgrade packages", "依赖更新", "升级依赖" in {{PROJECT_NAME}}. Manages dependency updates with safety checks and testing.
version: 1.0.0
---

# Dependency Update Skill

Manage dependency updates for {{PROJECT_NAME}} with safety checks and testing.

## When to Use

This skill activates when:
- User requests to update dependencies or packages
- User mentions "upgrade", "update deps", "dependency update"
- User needs to apply security patches
- User wants to update to newer versions

## Context

Read @.spec/project-context.md for package manager and test commands.

## Instructions

The user's request will specify the update target (dependency name or "all outdated").

### For Security Patches (Quick Flow)
1. Apply the patch
2. Run `{{TEST_CMD}}`
3. If tests pass → commit → deploy
4. If tests fail → investigate breaking changes

### For Minor/Patch Updates (Quick Flow, batch monthly)
1. List all outdated dependencies
2. Apply updates one at a time
3. Run `{{TEST_CMD}}` after each
4. Commit each update separately

### For Major Updates (Full Method)
1. Create proposal in `.spec/changes/upgrade-[dep]/proposal.md`
2. Read changelog and identify breaking changes
3. Write delta specs for behavioral changes
4. Make code changes required by breaking changes
5. Run full test suite
6. Test critical flows manually
7. Archive change after verification

## Evidence Required

- Actual `{{TEST_CMD}}` output after update
- Summary of breaking changes addressed (for major updates)
