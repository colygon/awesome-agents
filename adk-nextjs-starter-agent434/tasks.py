"""ADK Next.js Starter - CrewAI Task Definitions"""

from crewai import Task
from textwrap import dedent


def create_architecture_planning_task(agent, app_requirements: dict) -> Task:
    requirements = app_requirements.get('description', '')
    return Task(
        description=dedent(f"""
            Design Next.js application architecture for: {requirements}

            Provide comprehensive architecture plan including:
            1. Project structure and folder organization
            2. Data model and database schema
            3. Authentication and authorization strategy
            4. API design and data fetching patterns
            5. State management approach
            6. Deployment and CI/CD recommendations
        """),
        expected_output="Detailed architecture document with diagrams, schemas, and implementation guidelines.",
        agent=agent
    )


def create_development_task(agent, architecture_output, app_requirements: dict) -> Task:
    return Task(
        description=dedent(f"""
            Implement Next.js application based on architecture:
            {architecture_output}

            Provide complete implementation including:
            1. Project setup with Next.js, TypeScript, Tailwind CSS
            2. Component structure and page routes
            3. API routes and Server Actions
            4. Database integration with Prisma
            5. Authentication setup (NextAuth.js)
            6. Form handling and validation
            7. Testing setup (Jest, React Testing Library)
        """),
        expected_output="Complete Next.js application code with all necessary files and configurations.",
        agent=agent,
        context=[architecture_output] if isinstance(architecture_output, Task) else []
    )


def create_optimization_task(agent, architecture_output, development_output) -> Task:
    return Task(
        description=dedent(f"""
            Optimize Next.js application for performance and SEO:

            Architecture: {architecture_output}
            Implementation: {development_output}

            Provide optimization recommendations:
            1. Performance optimization (Core Web Vitals)
            2. SEO improvements and metadata
            3. Image optimization strategies
            4. Code splitting and lazy loading
            5. Caching strategies
            6. Accessibility enhancements
        """),
        expected_output="Performance optimization report with specific recommendations and implementation code.",
        agent=agent,
        context=[architecture_output, development_output] if isinstance(architecture_output, Task) else []
    )
