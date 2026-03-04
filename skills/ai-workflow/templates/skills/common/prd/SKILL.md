---
name: prd
description: Use this skill when the user asks to "create PRD", "product requirements", "business scenarios", "需求分析", "产品需求", "业务场景", "PRD" for {{PROJECT_NAME}}, or needs to transform raw ideas into structured Product Requirements Documents with business scenarios, process flows, and interactive prototypes.
version: 1.0.0
---

# PRD Generation Skill

Transform raw product requirements into comprehensive Product Requirements Documents (PRD) through a structured 3-phase workflow: scenario abstraction, business process documentation, and requirements specification with high-fidelity prototypes. Produce business-focused documentation suitable for stakeholder review and approval.

## Quick Reference

| Input | Output |
|-------|--------|
| Raw product requirements | `.spec/prd/{slug}/phase1-scenarios.md` — Business scenario analysis |
| | `.spec/prd/{slug}/phase2-business-doc.md` — Business process documentation |
| | `.spec/prd/{slug}/phase2-business-doc.html` — Process docs with rendered diagrams |
| | `.spec/prd/{slug}/phase3-requirements.md` — Structured requirements list (FR/NFR/UI) |
| | `.spec/prd/{slug}/phase3-prototype.html` — High-fidelity interactive prototype |

## When to Use

- User wants to create a PRD from raw requirements
- User says "prd", "产品需求", "需求分析", "业务需求", "business scenarios", "product requirements"
- User needs to document business scenarios and processes
- User wants to create high-fidelity prototypes for stakeholder review
- Task requires structured requirements analysis for business stakeholders

## When NOT to Use

- User wants technical implementation documentation — use the `dev` skill instead
- User wants to write detailed Given/When/Then specifications — use the `pm` skill
- User just wants to explore options — respond conversationally
- User wants API documentation or technical specs — use appropriate technical tools

## Context

Read @.spec/constitution.md for governance principles.
Read @.spec/project-context.md for tech stack, conventions, and domain terminology.
Read @.spec/intent.md for project goals (if available).

## Execution Modes

- **Default (Semi-Auto)**: Phase 1-2 run automatically, pause before Phase 3 for review
- **Full Auto (`--auto`)**: All phases run without pausing
- **Interactive (`--interactive`)**: Pause after each phase for review
- **Specific Stage (`--stage=N`)**: Only run phase N (requires previous phase outputs)

Parse `$ARGUMENTS` for mode flags. Default to semi-auto if no flags specified.

## Instructions

### Phase 1: Scenario Abstraction

**Goal**: Extract business scenarios and map user journeys from raw requirements.

1. Read `references/phase1-scenario-analysis.md` for detailed instructions
2. Analyze raw requirements to identify 2-5 core business scenarios
3. For each scenario, define: name, target users, description, user journey, user flow, functional support, success criteria
4. Include cross-scenario considerations (shared features, integration points, priorities)
5. Save output to `.spec/prd/{slug}/phase1-scenarios.md`

**Pause point (interactive mode)**: Show Phase 1 output, wait for confirmation.

---

### Phase 2: Business Process Documentation

**Goal**: Transform scenarios into business process documentation with flow diagrams.

1. Read `references/phase2-business-process.md` for detailed instructions
2. Based on Phase 1 scenario analysis, map business processes for each scenario
3. Generate Mermaid flow diagrams for each process
4. Create both Markdown and HTML outputs:
   - `phase2-business-doc.md` — Markdown with Mermaid code blocks
   - `phase2-business-doc.html` — HTML with rendered diagrams, professional styling, print-friendly
5. Save outputs to `.spec/prd/{slug}/`

**Pause point (semi-auto and interactive modes)**: Show Phase 1-2 outputs, wait for confirmation before proceeding to Phase 3.

---

### Phase 3: Requirements & Prototype

**Goal**: Produce structured requirements list and high-fidelity HTML interactive prototype.

1. Read `references/phase3-requirements-prototype.md` for detailed instructions
2. Based on Phase 1-2 analysis, generate:
   - **Requirements list** (`phase3-requirements.md`): FR (functional), NFR (non-functional), UI requirements, interaction design, data requirements, integration, security
   - **Interactive prototype** (`phase3-prototype.html`): Single self-contained HTML file with inline CSS/JS, responsive design, interactive elements, realistic mock data
3. Save outputs to `.spec/prd/{slug}/`

---

## State Management

Track progress in `.spec/prd/.state.json`:

```json
{
  "active": true,
  "currentPhase": 1,
  "projectSlug": "project-slug",
  "outputDir": ".spec/prd/project-slug",
  "phases": {
    "phase1": { "status": "pending" },
    "phase2": { "status": "pending" },
    "phase3": { "status": "pending" }
  },
  "executionMode": "semi-auto",
  "rawRequirements": "...",
  "updatedAt": "2026-01-01T00:00:00Z"
}
```

Update state after each phase completes. If resuming, check state file to continue from the last completed phase.

## Examples

**Good input**:
- "开发一个在线预约系统,用户可以预约服务,商家可以管理预约" — Clear domain, multiple roles, core features
- "PRD for a customer feedback platform with survey creation and analytics" — Specific domain, clear features

**Bad input**:
- "implement user authentication" — Technical implementation task, use `dev` skill
- "what should I build?" — Too vague, gather requirements conversationally first

## Verification

After completing all phases, verify:
- [ ] All requested phases completed
- [ ] Phase 1: scenario analysis document created
- [ ] Phase 2: business documentation (MD + HTML) created
- [ ] Phase 3: requirements list and prototype created
- [ ] All files saved to `.spec/prd/{slug}/`
- [ ] State file updated with completion status
- [ ] Summary of deliverables provided to user

## Next Steps

After PRD approval, suggest:
- Use the `pm` skill to create detailed Given/When/Then specifications from the requirements list
- Use the `architect` skill to design technical architecture based on requirements
- Use the `dev` skill for spec-driven implementation

## Advanced Usage

### Output Structure

```
.spec/prd/
└── {project-slug}/
    ├── phase1-scenarios.md
    ├── phase2-business-doc.md
    ├── phase2-business-doc.html
    ├── phase3-requirements.md
    └── phase3-prototype.html
```

### Resume

If interrupted, run the skill again. It checks `.spec/prd/.state.json` and resumes from the last completed phase.

### Re-run a Specific Phase

Use `--stage=N` to re-run a specific phase. Previous phase outputs must exist.

### Best Practices for Input

1. Be specific about the domain — "online booking system" not just "system"
2. Mention key user roles — "users and merchants" helps identify scenarios
3. Include core features — "booking, management, analytics" provides context
4. Describe the business value — helps with scenario abstraction
5. Avoid technical jargon — focus on business needs, not implementation details
