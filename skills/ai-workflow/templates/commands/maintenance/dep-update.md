---
description: 依赖更新管理 (安全补丁/小版本/大版本)
argument-hint: [依赖名称或 "all outdated"]
---

You are a Developer managing dependencies for {{PROJECT_NAME}}.

## Context

Read @.spec/project-context.md for package manager and test commands.

## Update Target

$ARGUMENTS

## Instructions

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
