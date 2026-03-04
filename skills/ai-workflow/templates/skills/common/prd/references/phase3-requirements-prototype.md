# Phase 3: Requirements & Prototype

Generate a structured requirements list and high-fidelity interactive HTML prototype for {{PROJECT_NAME}} based on Phase 1-2 analysis.

## Input
- Phase 1: Scenario analysis document (`.spec/prd/{slug}/phase1-scenarios.md`)
- Phase 2: Business process documentation (`.spec/prd/{slug}/phase2-business-doc.md`)
- Raw requirements (for context)

## Task

Create TWO deliverables:
1. **Requirements List** (Markdown) - Structured, prioritized product requirements
2. **High-Fidelity Prototype** (HTML) - Interactive prototype demonstrating the product

---

## Part 1: Requirements List

Save as `.spec/prd/{slug}/phase3-requirements.md`, following this structure:

```markdown
# Product Requirements Document

## Document Information
- **Project**: {{PROJECT_NAME}}
- **Version**: 1.0
- **Date**: [Current Date]
- **Author**: Product Team
- **Status**: Draft for Review

## Executive Summary
[2-3 paragraphs covering:
- Product vision and goals
- Target users and market
- Key features and differentiators
- Success metrics]

## Product Overview

### Vision Statement
[One sentence describing the product's ultimate goal]

### Target Users
1. **[User Persona 1]**
   - Demographics: [Age, role, context]
   - Goals: [What they want to achieve]
   - Pain Points: [Current problems they face]

2. **[User Persona 2]**
   [Repeat structure...]

### Success Metrics
- **[Metric 1]**: [Target value and measurement method]
- **[Metric 2]**: [Target value and measurement method]
- **[Metric 3]**: [Target value and measurement method]

---

## Functional Requirements

### FR-001: [Feature Name]
- **Priority**: P0 (Must Have) / P1 (Should Have) / P2 (Nice to Have)
- **Related Scenario**: [Link to scenario from Phase 1]
- **User Story**: As a [user type], I want to [action] so that [benefit]
- **Description**: [Detailed description of the feature]
- **Acceptance Criteria**:
  - [ ] Given [context], when [action], then [expected result]
  - [ ] Given [context], when [action], then [expected result]
  - [ ] [Additional criteria...]
- **Dependencies**: [Other requirements this depends on]
- **Estimated Effort**: [Small/Medium/Large]
- **Notes**: [Any additional context or considerations]

### FR-002: [Feature Name]
[Repeat structure for each functional requirement...]

---

## Non-Functional Requirements

### NFR-001: [Requirement Name]
- **Category**: Performance / Security / Usability / Compatibility / Reliability
- **Priority**: P0 / P1 / P2
- **Description**: [Detailed description]
- **Acceptance Criteria**:
  - [ ] [Measurable criterion 1]
  - [ ] [Measurable criterion 2]
- **Rationale**: [Why this is important]

### NFR-002: [Requirement Name]
[Repeat structure...]

---

## User Interface Requirements

### UI-001: [Interface Element/Screen]
- **Description**: [What this interface does]
- **Key Elements**:
  - [Element 1]: [Purpose and behavior]
  - [Element 2]: [Purpose and behavior]
- **Interactions**:
  - [Interaction 1]: [Description]
  - [Interaction 2]: [Description]
- **Responsive Behavior**: [How it adapts to different screen sizes]
- **Accessibility**: [Accessibility considerations]

[Repeat for key interfaces...]

---

## Interaction Design Principles

1. **[Principle 1]**: [Description and application]
2. **[Principle 2]**: [Description and application]
3. **[Principle 3]**: [Description and application]

---

## Data Requirements

### Data Entity 1: [Entity Name]
- **Description**: [What this data represents]
- **Key Attributes**:
  - [Attribute 1]: [Type, constraints, description]
  - [Attribute 2]: [Type, constraints, description]
- **Relationships**: [How it relates to other entities]
- **Validation Rules**: [Data validation requirements]

[Repeat for key data entities...]

---

## Integration Requirements

### INT-001: [Integration Name]
- **Type**: API / Service / Third-party
- **Purpose**: [Why this integration is needed]
- **Requirements**: [What needs to be integrated]
- **Priority**: P0 / P1 / P2

---

## Security & Privacy Requirements

- **Authentication**: [Requirements]
- **Authorization**: [Requirements]
- **Data Protection**: [Requirements]
- **Privacy Compliance**: [GDPR, CCPA, etc.]

---

## Constraints & Assumptions

### Constraints
- [Constraint 1]: [Description and impact]
- [Constraint 2]: [Description and impact]

### Assumptions
- [Assumption 1]: [Description]
- [Assumption 2]: [Description]

---

## Out of Scope

Items explicitly NOT included in this version:
- [Item 1]
- [Item 2]
- [Item 3]

---

## Appendix

### Glossary
- **[Term 1]**: [Definition]
- **[Term 2]**: [Definition]

### References
- [Reference 1]
- [Reference 2]
```

---

## Part 2: High-Fidelity Prototype

Save as `.spec/prd/{slug}/phase3-prototype.html`.

### Technical Requirements
- **Single HTML file** (self-contained with inline CSS and JavaScript)
- **Modern CSS** (Flexbox/Grid, animations, transitions)
- **Responsive design** (mobile-first, works on all screen sizes)
- **Interactive elements** (buttons, forms, navigation, modals)
- **Smooth animations** (hover effects, transitions, micro-interactions)
- **Professional appearance** (polished, production-ready look)

### Content Requirements
- **All key screens/pages** from the requirements
- **Realistic mock data** (names, numbers, text that looks real)
- **Complete user flows** (can navigate through main scenarios)
- **Visual hierarchy** (clear information architecture)
- **Consistent design system** (colors, typography, spacing)

### Prototype Template Structure

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{PROJECT_NAME}} - Interactive Prototype</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            /* Design System Variables */
            --primary-color: #007bff;
            --secondary-color: #6c757d;
            --success-color: #28a745;
            --danger-color: #dc3545;
            --warning-color: #ffc107;
            --info-color: #17a2b8;

            --text-primary: #212529;
            --text-secondary: #6c757d;
            --text-light: #ffffff;

            --bg-primary: #ffffff;
            --bg-secondary: #f8f9fa;
            --bg-dark: #343a40;

            --border-color: #dee2e6;
            --border-radius: 8px;

            --spacing-xs: 4px;
            --spacing-sm: 8px;
            --spacing-md: 16px;
            --spacing-lg: 24px;
            --spacing-xl: 32px;

            --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            --font-size-sm: 14px;
            --font-size-base: 16px;
            --font-size-lg: 18px;
            --font-size-xl: 24px;
            --font-size-xxl: 32px;

            --shadow-sm: 0 1px 3px rgba(0,0,0,0.12);
            --shadow-md: 0 4px 6px rgba(0,0,0,0.1);
            --shadow-lg: 0 10px 20px rgba(0,0,0,0.15);

            --transition-fast: 150ms ease;
            --transition-base: 300ms ease;
            --transition-slow: 500ms ease;
        }

        body {
            font-family: var(--font-family);
            font-size: var(--font-size-base);
            line-height: 1.6;
            color: var(--text-primary);
            background: var(--bg-secondary);
        }

        /* Layout Components */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 var(--spacing-md);
        }

        .header {
            background: var(--bg-primary);
            box-shadow: var(--shadow-sm);
            padding: var(--spacing-md) 0;
            position: sticky;
            top: 0;
            z-index: 1000;
        }

        .nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-brand {
            font-size: var(--font-size-xl);
            font-weight: 700;
            color: var(--primary-color);
            text-decoration: none;
        }

        .nav-menu {
            display: flex;
            gap: var(--spacing-lg);
            list-style: none;
        }

        .nav-link {
            color: var(--text-primary);
            text-decoration: none;
            padding: var(--spacing-sm) var(--spacing-md);
            border-radius: var(--border-radius);
            transition: all var(--transition-fast);
        }

        .nav-link:hover {
            background: var(--bg-secondary);
            color: var(--primary-color);
        }

        .main {
            padding: var(--spacing-xl) 0;
        }

        /* UI Components */
        .btn {
            display: inline-block;
            padding: var(--spacing-sm) var(--spacing-lg);
            font-size: var(--font-size-base);
            font-weight: 500;
            text-align: center;
            text-decoration: none;
            border: none;
            border-radius: var(--border-radius);
            cursor: pointer;
            transition: all var(--transition-fast);
        }

        .btn-primary {
            background: var(--primary-color);
            color: var(--text-light);
        }

        .btn-primary:hover {
            background: #0056b3;
            transform: translateY(-2px);
            box-shadow: var(--shadow-md);
        }

        .card {
            background: var(--bg-primary);
            border-radius: var(--border-radius);
            padding: var(--spacing-lg);
            box-shadow: var(--shadow-sm);
            transition: all var(--transition-base);
        }

        .card:hover {
            box-shadow: var(--shadow-md);
            transform: translateY(-4px);
        }

        .form-group {
            margin-bottom: var(--spacing-md);
        }

        .form-label {
            display: block;
            margin-bottom: var(--spacing-xs);
            font-weight: 500;
            color: var(--text-primary);
        }

        .form-control {
            width: 100%;
            padding: var(--spacing-sm) var(--spacing-md);
            font-size: var(--font-size-base);
            border: 1px solid var(--border-color);
            border-radius: var(--border-radius);
            transition: all var(--transition-fast);
        }

        .form-control:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(0,123,255,0.1);
        }

        /* Modal */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0,0,0,0.5);
            z-index: 2000;
            align-items: center;
            justify-content: center;
        }

        .modal.active {
            display: flex;
        }

        .modal-content {
            background: var(--bg-primary);
            border-radius: var(--border-radius);
            padding: var(--spacing-xl);
            max-width: 500px;
            width: 90%;
            animation: modalSlideIn var(--transition-base);
        }

        @keyframes modalSlideIn {
            from {
                opacity: 0;
                transform: translateY(-50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-menu {
                flex-direction: column;
                gap: var(--spacing-sm);
            }

            .container {
                padding: 0 var(--spacing-sm);
            }
        }

        /* Utility Classes */
        .text-center { text-align: center; }
        .text-right { text-align: right; }
        .mt-1 { margin-top: var(--spacing-sm); }
        .mt-2 { margin-top: var(--spacing-md); }
        .mt-3 { margin-top: var(--spacing-lg); }
        .mb-1 { margin-bottom: var(--spacing-sm); }
        .mb-2 { margin-bottom: var(--spacing-md); }
        .mb-3 { margin-bottom: var(--spacing-lg); }
        .grid { display: grid; gap: var(--spacing-md); }
        .grid-2 { grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); }
        .flex { display: flex; }
        .flex-between { justify-content: space-between; }
        .flex-center { justify-content: center; align-items: center; }
        .gap-1 { gap: var(--spacing-sm); }
        .gap-2 { gap: var(--spacing-md); }
        .gap-3 { gap: var(--spacing-lg); }
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <nav class="nav">
                <a href="#" class="nav-brand">{{PROJECT_NAME}}</a>
                <ul class="nav-menu">
                    <li><a href="#home" class="nav-link">Home</a></li>
                    <li><a href="#features" class="nav-link">Features</a></li>
                    <li><a href="#about" class="nav-link">About</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main class="main">
        <div class="container">
            <!-- Add prototype screens here based on requirements -->
            <section id="home">
                <h1 class="text-center mb-3">Welcome to {{PROJECT_NAME}}</h1>
                <p class="text-center mb-3">[Product tagline or description]</p>
                <div class="text-center">
                    <button class="btn btn-primary" onclick="openModal()">Get Started</button>
                </div>
            </section>

            <!-- Add more sections for different screens -->
        </div>
    </main>

    <!-- Modal Example -->
    <div id="exampleModal" class="modal">
        <div class="modal-content">
            <h2 class="mb-2">Example Modal</h2>
            <p class="mb-3">This is an interactive prototype example.</p>
            <button class="btn btn-primary" onclick="closeModal()">Close</button>
        </div>
    </div>

    <script>
        // Interactive functionality
        function openModal() {
            document.getElementById('exampleModal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('exampleModal').classList.remove('active');
        }

        // Add more interactive functions as needed
    </script>
</body>
</html>
```

### Design Guidelines

1. **Visual Hierarchy**
   - Clear heading structure (h1, h2, h3)
   - Consistent spacing and alignment
   - Proper use of white space

2. **Color System**
   - Primary color for main actions
   - Secondary colors for supporting elements
   - Semantic colors (success, warning, error)
   - Sufficient contrast for accessibility

3. **Typography**
   - Readable font sizes (minimum 14px)
   - Appropriate line height (1.5-1.6)
   - Font weight for emphasis

4. **Interactions**
   - Hover states for clickable elements
   - Focus states for form inputs
   - Loading states for async actions
   - Smooth transitions (200-300ms)

5. **Responsive Behavior**
   - Mobile-first approach
   - Breakpoints at 768px, 1024px
   - Touch-friendly tap targets (minimum 44x44px)
   - Readable text on all devices

### Content Guidelines

- Use realistic mock data (not "Lorem ipsum")
- Include representative images or placeholders
- Show different states (empty, loading, error, success)
- Demonstrate key user flows
- Include helpful microcopy and labels

## Output

Save both files to `.spec/prd/{slug}/`:
1. `phase3-requirements.md` - Complete requirements document
2. `phase3-prototype.html` - Fully functional interactive prototype

The prototype should be impressive enough to show to stakeholders and get buy-in for the project.

## Next Steps

After generating the requirements list, suggest using the `pm` skill to create detailed Given/When/Then specifications for each FR item. This bridges the gap from business requirements to implementable technical specifications.
