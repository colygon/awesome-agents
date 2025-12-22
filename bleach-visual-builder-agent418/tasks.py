"""Bleach Visual Builder Tasks"""

from crewai import Task
from agents import ui_designer, component_architect, accessibility_specialist, responsive_designer, code_generator


def create_tasks(project_spec: dict):
    """Create visual design tasks"""

    project_name = project_spec.get('name', 'Web Application')
    style = project_spec.get('style', 'Modern')

    design_task = Task(
        description=f"""Create UI design for {project_name}.

        Style: {style}
        Pages: {project_spec.get('pages', 'Home, About, Contact')}

        Design:
        1. Color scheme and typography
        2. Layout structure
        3. Visual hierarchy
        4. Iconography and imagery
        5. Design mockups""",
        agent=ui_designer,
        expected_output="Complete UI design specifications"
    )

    component_task = Task(
        description=f"""Design component system for {project_name}.

        Create:
        1. Design system documentation
        2. Component library (buttons, forms, cards, etc.)
        3. Component variants and states
        4. Spacing and sizing scales
        5. Composition patterns""",
        agent=component_architect,
        expected_output="Component system design",
        context=[design_task]
    )

    accessibility_task = Task(
        description=f"""Ensure accessibility for {project_name}.

        Check:
        1. Color contrast ratios (WCAG AA/AAA)
        2. Keyboard navigation
        3. ARIA labels and semantic HTML
        4. Focus indicators
        5. Alt text for images""",
        agent=accessibility_specialist,
        expected_output="Accessibility compliance report",
        context=[design_task, component_task]
    )

    responsive_task = Task(
        description=f"""Create responsive design for {project_name}.

        Define:
        1. Breakpoints (mobile, tablet, desktop)
        2. Responsive layouts
        3. Touch targets for mobile
        4. Mobile navigation patterns
        5. Image optimization""",
        agent=responsive_designer,
        expected_output="Responsive design specifications",
        context=[design_task, component_task]
    )

    code_task = Task(
        description=f"""Generate frontend code for {project_name}.

        Framework: {project_spec.get('framework', 'React')}

        Generate:
        1. Component code (React/Vue/HTML)
        2. CSS/Tailwind styles
        3. Responsive utilities
        4. Accessibility attributes
        5. Documentation""",
        agent=code_generator,
        expected_output="Production-ready frontend code",
        context=[design_task, component_task, accessibility_task, responsive_task]
    )

    return [design_task, component_task, accessibility_task, responsive_task, code_task]
