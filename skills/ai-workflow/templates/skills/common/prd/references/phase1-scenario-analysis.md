# Phase 1: Scenario Analysis

Analyze raw product requirements to extract structured business scenarios for {{PROJECT_NAME}}.

Consult @.spec/constitution.md for governance constraints and @.spec/project-context.md for domain context.

## Input

Raw requirements from the user describing a product or feature idea.

## Task

1. **Identify Core Business Scenarios**
   - Read the raw requirements carefully
   - Identify distinct business scenarios (typically 2-5 scenarios)
   - Each scenario should represent a meaningful user interaction or business process

2. **For Each Scenario, Define**:
   - **Scenario Name**: Clear, concise name (e.g., "User Books Service", "Merchant Manages Appointments")
   - **Target Users**: Who are the primary users in this scenario? (e.g., "End Users", "Merchants", "Administrators")
   - **Description**: 2-3 sentences describing what happens in this scenario
   - **User Journey**: Step-by-step breakdown of what the user does (5-10 steps)
   - **User Flow**: Describe the logical flow and decision points
   - **Functional Support**: List the key features/capabilities needed to support this scenario

3. **Output Format**
   Generate a markdown document following this structure:

```markdown
# Scenario Analysis

## Raw Requirements
[Paste the original requirements here]

## Executive Summary
[2-3 sentences summarizing the overall product vision and key scenarios identified]

## Scenario List

### Scenario 1: [Scenario Name]

**Target Users**: [User role(s)]

**Description**:
[2-3 sentences describing this scenario]

**User Journey**:
1. [First step - what triggers this scenario]
2. [Second step - what the user does]
3. [Third step - system response or next action]
4. [Continue with key steps...]
5. [Final step - outcome or completion]

**User Flow**:
[Describe the logical flow, including:
- Entry points (how users enter this scenario)
- Decision points (where users make choices)
- Alternative paths (what happens in different cases)
- Exit points (how the scenario concludes)]

**Functional Support**:
- [Feature 1 needed for this scenario]
- [Feature 2 needed for this scenario]
- [Feature 3 needed for this scenario]
- [Additional features...]

**Success Criteria**:
- [How do we know this scenario is successful?]
- [What metrics or outcomes indicate success?]

---

### Scenario 2: [Scenario Name]
[Repeat the same structure for each scenario]

---

## Cross-Scenario Considerations

**Shared Features**:
- [Features that appear in multiple scenarios]

**Integration Points**:
- [How scenarios connect or depend on each other]

**Priority Recommendations**:
1. [Highest priority scenario and why]
2. [Second priority scenario and why]
3. [Additional scenarios in order of priority]
```

## Guidelines

- **Be User-Centric**: Focus on what users want to accomplish, not technical implementation
- **Be Specific**: Avoid vague descriptions; use concrete examples
- **Be Comprehensive**: Cover all major use cases mentioned or implied in the requirements
- **Be Realistic**: Consider real-world constraints and user behaviors
- **Think Business Value**: Each scenario should deliver clear business value
- **Avoid Technical Jargon**: This is for business stakeholders, not developers

## Quality Indicators

**Good Scenario**:
- Clear user role and motivation
- Specific, actionable steps
- Realistic flow with decision points
- Measurable success criteria

**Poor Scenario**:
- Vague or technical language
- Missing key steps or context
- No clear outcome or value
- Overly complex or unrealistic

## Output

Save the complete scenario analysis document to `.spec/prd/{slug}/phase1-scenarios.md`. Be thorough but concise. Focus on clarity and actionability.
