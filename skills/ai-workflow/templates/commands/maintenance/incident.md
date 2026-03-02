---
description: 事故响应 (检测→评估→缓解→修复→预防)
argument-hint: [事故描述: 严重程度、影响范围、错误日志]
---

You are handling an incident for {{PROJECT_NAME}}.

## Incident Details

$ARGUMENTS

## Response Protocol

### 1. DETECT
- Identify the error from logs/monitoring
- Classify severity and blast radius

### 2. ASSESS
- Is this affecting users right now?
- What is the scope (one endpoint, one service, entire system)?
- When did it start? What changed recently?

### 3. MITIGATE (Quick Flow)
Choose the fastest path to stop user impact:
- [ ] Rollback last deployment?
- [ ] Toggle feature flag?
- [ ] Scale resources?
- [ ] Apply hotfix?

### 4. FIX (may escalate to Full Method)
If hotfix needed:
1. Write regression test
2. Minimum fix
3. Fast-track CI
4. Deploy with monitoring

### 5. PREVENT (Full Method)
After resolution:
1. Create proposal: `.spec/changes/incident-[id]/proposal.md`
2. Document root cause
3. Add monitoring/alerting for this failure mode
4. Add test coverage for this scenario
5. Update `.spec/project-context.md` with new gotcha

## Post-Mortem Template

```
## Incident: [Title]
- Duration: [start - end]
- Severity: [level]
- Root Cause: [why it happened]
- Resolution: [what fixed it]
- Prevention: [what will prevent recurrence]
- Action Items: [specific tasks with owners]
```
