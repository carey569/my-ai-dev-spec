# Spec-Driven Development Principles

Synthesized from four leading frameworks: **Spec-Kit**, **OpenSpec**, **Superpowers**, **BMAD Method**.

## Core Conviction

> Specifications are the source of truth. Code serves the specification, not the other way around.
> AI-assisted development must be structured and spec-driven, not ad-hoc "vibe coding."

---

## Framework Synopsis

| Framework | Creator | Core Idea | Best For |
|-----------|---------|-----------|----------|
| **Spec-Kit** | GitHub | Constitution → Spec → Plan → Tasks → Implement | Greenfield with governance |
| **OpenSpec** | Fission-AI | Brownfield-first; proposal → delta specs → apply → archive | Evolving existing codebases |
| **Superpowers** | Jesse Vincent | Composable skills; mandatory design → plan → TDD implement | Developer-centric TDD workflow |
| **BMAD** | bmad-code-org | Agent team (PM/Architect/Dev/QA); scale-adaptive tracks | Full product lifecycle |

---

## Synthesized Principles

### 1. Specification Before Implementation (All Four)

Never write production code without a specification. The spec defines WHAT and WHY; the plan defines HOW; only then does implementation begin.

- **Spec-Kit**: "Executable specifications precise enough to generate working systems"
- **OpenSpec**: "Structure before code"
- **Superpowers**: "Do NOT write any code until you have a design and the user has approved it"
- **BMAD**: "Documentation as source of truth; code is derivative"

### 2. Constitution / Project Governance (Spec-Kit, BMAD)

Every project needs non-negotiable principles documented upfront. These govern all subsequent technical decisions and prevent drift.

- **Spec-Kit's Constitution**: Versioned articles with rationale (e.g., "Test-First: no implementation code before unit tests")
- **BMAD's Project Context**: Living document capturing implementation rules, patterns, and preferences
- **Application**: Generate a `constitution.md` for new projects; generate `project-context.md` for existing projects

### 3. Progressive Context Building (BMAD, OpenSpec)

Build context incrementally. Each phase's outputs feed into the next. AI agents work best with clear, structured context, not a raw code dump.

- **BMAD**: PRD → Architecture → Epics → Stories → Code (each embeds all necessary context)
- **OpenSpec**: project.md provides worldview; change-scoped specs provide focused context
- **Application**: Generate layered context files that can be loaded on-demand

#### 3a. PRD Before Specs (BMAD)

For complex features or new products, generate a Product Requirements Document (PRD) before writing detailed specifications. The PRD captures business scenarios, process flows, and requirements at a higher level of abstraction.

- **BMAD**: PRD → Architecture → Epics → Stories → Code
- **Application**: Use the `prd` skill for business-level analysis (scenarios, process flows, prototypes), then the `pm` skill for detailed Given/When/Then specifications

### 4. Brownfield-First Design (OpenSpec)

Most real-world development is evolving existing systems, not building greenfield. The workflow must support:

- **Delta specifications**: ADDED / MODIFIED / REMOVED requirement tracking
- **Change isolation**: Each change gets its own workspace with proposal, design, and tasks
- **Archive workflow**: Completed changes merge into living specifications
- **Application**: For maintenance and refactor projects, generate change tracking infrastructure

### 5. Scale-Adaptive Ceremony (BMAD, Superpowers)

The right amount of process depends on scope. Bug fixes don't need the same ceremony as platform builds.

- **BMAD**: Quick Flow (tech spec → implement) vs Full Method (PRD → Architecture → Stories → Sprint)
- **Superpowers**: 2-5 minute task granularity with batch execution
- **Application**: Workflow should define when to use lightweight vs heavyweight processes

### 6. Role-Based AI Agents (BMAD)

Different phases need different AI "personas" with distinct expertise and constraints:

| Role | Phase | Focus |
|------|-------|-------|
| **Analyst** | Discovery | Probing questions, brainstorming facilitation |
| **PM (PRD)** | Discovery→Planning | Business scenarios, process docs, prototypes |
| **PM (Spec)** | Planning | Requirements, user stories, acceptance criteria |
| **Architect** | Design | Technical decisions, ADRs, data models, API contracts |
| **Developer** | Implementation | Code following specs, TDD, minimum necessary changes |
| **QA** | Review | Security, correctness, regression, consistency |

- **Application**: Generate role-based prompt templates instead of generic prompts

### 7. Test-Driven Development Enforcement (Superpowers)

Testing is not optional. The TDD cycle (RED → GREEN → REFACTOR) is mandatory.

- **Superpowers**: "If you wrote code before testing, delete it entirely and restart. No exceptions."
- **Application**: Embed TDD requirements in the developer implementation prompts

### 8. Verification-Before-Completion (Superpowers)

Never declare success without evidence. Provide concrete proof: actual command output, test results, before/after comparison.

- **Superpowers**: "Provide concrete evidence (actual command output) before declaring success"
- **Application**: Every task in the workflow should specify verification criteria

### 9. Explicit Ambiguity Marking (Spec-Kit, OpenSpec)

Unresolved questions must be visible, not silently assumed.

- **Spec-Kit**: `[NEEDS CLARIFICATION]` tags in specs
- **OpenSpec**: Artifact dependency graph ensures nothing is skipped
- **Application**: Templates should include explicit markers for sections that need human input

### 10. Change Lifecycle Management (OpenSpec)

Changes follow a lifecycle: propose → specify → design → implement → verify → archive.

- **OpenSpec**: `changes/` directory with proposal.md, design.md, tasks.md, delta specs
- **Application**: For maintenance/refactor, generate change tracking structure

---

## Generated Output Structure

Based on these principles, the ai-workflow skill generates:

```
target-project/
├── CLAUDE.md                           # AI behavioral guidelines + project context
│                                       # (Inspired by: OpenSpec AGENTS.md + BMAD project-context.md)
│
└── .spec/                              # Spec-driven development workspace
    ├── constitution.md                 # Project principles & governance
    │                                   # (Inspired by: Spec-Kit constitution)
    │
    ├── project-context.md              # Tech stack, conventions, constraints
    │                                   # (Inspired by: OpenSpec project.md + BMAD project-context.md)
    │
    ├── workflow.md                     # Phased development workflow
    │                                   # (Synthesized from all four frameworks)
    │
    ├── prd/                            # Product Requirements Documents
    │   └── [slug]/                     # (Generated by prd skill)
    │
    ├── specs/                          # Living specifications
    │   └── README.md                   # (Inspired by: OpenSpec specs/)
    │
    ├── changes/                        # Change tracking (maintenance/refactor only)
    │   └── README.md                   # (Inspired by: OpenSpec changes/)
    │
    └── prompts/                        # Role-based AI prompts
        ├── README.md                   # Usage guide
        ├── analyst-brainstorm.md       # Analyst: discovery & brainstorming
        ├── pm-requirements.md          # PM: PRD & user stories
        ├── architect-design.md         # Architect: technical design & ADRs
        ├── dev-implement.md            # Developer: spec-driven implementation
        ├── dev-tdd.md                  # Developer: TDD workflow
        ├── qa-review.md               # QA: comprehensive review
        └── [type-specific prompts]     # Additional per project type
```

## Mapping to Project Types

| Concept | New (0→1) | Maintenance | Refactor |
|---------|-----------|-------------|----------|
| **Constitution** | Generate from scratch | Extract from existing codebase | New constitution for target architecture |
| **Project Context** | Minimal (tech stack choices) | Rich (conventions, patterns, gotchas) | Dual context (legacy + new) |
| **Workflow Model** | Spec-Kit's full pipeline | OpenSpec's change lifecycle | BMAD's story-driven migration |
| **Scale Adaptation** | Full Method by default | Quick Flow for bugs/small; Full for features | Full Method always |
| **Spec Format** | Freeform with Gherkin scenarios | Delta specs (ADDED/MODIFIED/REMOVED) | Characterization specs + delta specs |
| **Key Prompts** | Analyst + PM + Architect + Dev | Dev + QA + DevOps | Analyst (legacy) + Architect (new) + Dev + QA |
| **TDD Approach** | Write tests first (Superpowers) | Regression tests for bugs; TDD for features | Characterization tests first (BMAD) |
| **Verification** | Evidence-based completion | Regression + integration proof | Feature parity verification |

## Framework-Specific Concepts Applied

### From Spec-Kit
- Constitution with versioned articles
- `[NEEDS CLARIFICATION]` markers
- Numbered feature specs (e.g., `001-feature-name/`)
- Spec → Plan → Tasks pipeline

### From OpenSpec
- `project.md` as the "worldview" document
- Delta specifications for existing codebases
- Change lifecycle (propose → specify → implement → archive)
- Gherkin-style Given/When/Then scenarios

### From Superpowers
- Mandatory design → plan → implement (no skipping)
- TDD enforcement with no exceptions
- Verification-before-completion (evidence required)
- Git worktree isolation recommendation
- Design docs as committed artifacts

### From BMAD
- Role-based agent prompts (PM, Architect, Dev, QA)
- Scale-adaptive ceremony (Quick Flow vs Full Method)
- Implementation readiness gate (PASS/CONCERNS/FAIL)
- Progressive context building through document chain
- Story files embedding all necessary context
