"""
Enhanced Task Workflows - Claude Code Agent CrewAI Implementation
Demonstrates advanced task patterns: hierarchical delegation, parallel execution, context sharing.
"""

from crewai import Task, Agent
from typing import List, Optional


def create_architecture_task(agent: Agent, project_description: str) -> Task:
    """
    Create a high-level architecture design task.
    This task typically runs first in a hierarchical workflow.

    Args:
        agent: Code Architect agent
        project_description: Description of the project to architect

    Returns:
        Task for system architecture design
    """
    return Task(
        description=f"""Analyze the following project requirements and design a system architecture:

{project_description}

Your design should include:
1. High-level component breakdown
2. Module structure and dependencies
3. Data flow and API design
4. Technology stack recommendations
5. File organization structure

Provide a clear, actionable architecture document that the development team can follow.""",
        agent=agent,
        expected_output="""Comprehensive architecture document with:
- Component diagram
- Module structure
- API specifications
- File organization
- Technology recommendations"""
    )


def create_implementation_task(agent: Agent, file_path: str, feature_description: str, context: Optional[List[Task]] = None) -> Task:
    """
    Create a code implementation task.
    Depends on architecture/design decisions from previous tasks.

    Args:
        agent: Senior Developer agent
        file_path: Path to file to implement
        feature_description: What feature to implement
        context: Previous tasks to use as context

    Returns:
        Task for feature implementation
    """
    return Task(
        description=f"""Implement the following feature in {file_path}:

{feature_description}

Requirements:
- Follow the architecture design from previous tasks
- Write clean, maintainable code
- Include inline comments for complex logic
- Follow Python best practices and PEP 8
- Handle errors appropriately

If the file doesn't exist, create it with proper structure.""",
        agent=agent,
        expected_output=f"Complete, working implementation in {file_path} with clean code and proper structure",
        context=context or []
    )


def create_code_review_task(agent: Agent, file_paths: List[str], context: Optional[List[Task]] = None) -> Task:
    """
    Create a code review task.
    Reviews code implemented in previous tasks.

    Args:
        agent: Code Reviewer agent
        file_paths: List of files to review
        context: Implementation tasks to review

    Returns:
        Task for code review
    """
    files_list = "\n".join(f"- {fp}" for fp in file_paths)

    return Task(
        description=f"""Review the following files for code quality and security:

{files_list}

Check for:
1. Security vulnerabilities (SQL injection, XSS, etc.)
2. Code smells and anti-patterns
3. Performance issues
4. Error handling
5. Code readability and maintainability
6. Adherence to best practices

Provide specific, actionable feedback with file names and line numbers.""",
        agent=agent,
        expected_output="""Detailed code review report with:
- Security findings (if any)
- Code quality issues
- Performance recommendations
- Specific improvements with file:line references""",
        context=context or []
    )


def create_testing_task(agent: Agent, test_file_path: str, code_to_test: str, context: Optional[List[Task]] = None) -> Task:
    """
    Create a testing task.
    Writes tests for code implemented in previous tasks.

    Args:
        agent: QA Engineer agent
        test_file_path: Path to test file to create
        code_to_test: Description of code to test
        context: Implementation tasks to reference

    Returns:
        Task for test creation
    """
    return Task(
        description=f"""Create comprehensive tests in {test_file_path} for:

{code_to_test}

Requirements:
- Write unit tests covering main functionality
- Include edge cases and error scenarios
- Use pytest framework
- Aim for high code coverage
- Include docstrings explaining what each test validates

Run the tests to ensure they pass.""",
        agent=agent,
        expected_output=f"Complete test suite in {test_file_path} with passing tests and good coverage",
        context=context or []
    )


def create_documentation_task(agent: Agent, project_name: str, context: Optional[List[Task]] = None) -> Task:
    """
    Create a documentation task.
    Documents the project based on all previous tasks.

    Args:
        agent: Technical Writer agent
        project_name: Name of the project
        context: All previous tasks to synthesize

    Returns:
        Task for documentation creation
    """
    return Task(
        description=f"""Create comprehensive documentation for {project_name}.

Based on the architecture, implementation, and testing from the team, create:

1. README.md with:
   - Project overview
   - Installation instructions
   - Usage examples
   - Architecture summary
   - Contributing guidelines

2. API.md (if applicable) with:
   - API endpoints/functions
   - Parameters and return values
   - Example requests/responses

Make the documentation clear, complete, and beginner-friendly.""",
        agent=agent,
        expected_output="""Complete documentation set including README.md and API.md with clear,
comprehensive information for users and contributors""",
        context=context or []
    )


def create_deployment_task(agent: Agent, deployment_target: str, context: Optional[List[Task]] = None) -> Task:
    """
    Create a deployment preparation task.
    Prepares the project for deployment.

    Args:
        agent: DevOps Engineer agent
        deployment_target: Where to deploy (e.g., "Docker", "Cloud", "Production")
        context: Previous tasks to reference

    Returns:
        Task for deployment preparation
    """
    return Task(
        description=f"""Prepare the project for deployment to {deployment_target}.

Tasks:
1. Create Dockerfile (if needed)
2. Set up CI/CD configuration
3. Create deployment scripts
4. Document deployment process
5. Ensure all dependencies are properly specified

Make the deployment process automated and repeatable.""",
        agent=agent,
        expected_output=f"""Complete deployment setup for {deployment_target} including:
- Dockerfile (if applicable)
- CI/CD configuration
- Deployment scripts
- Deployment documentation""",
        context=context or []
    )


def create_analysis_task(agent: Agent, analysis_target: str, analysis_type: str = "codebase") -> Task:
    """
    Create a code analysis/research task.
    Can run in parallel with other analysis tasks.

    Args:
        agent: Research Analyst agent
        analysis_target: What to analyze (file path or pattern)
        analysis_type: Type of analysis (codebase, dependencies, patterns)

    Returns:
        Task for code analysis
    """
    return Task(
        description=f"""Perform a {analysis_type} analysis on: {analysis_target}

Analysis objectives:
1. Identify key patterns and structures
2. Map dependencies and relationships
3. Find potential issues or improvements
4. Document findings with specific examples

Provide actionable insights and recommendations.""",
        agent=agent,
        expected_output=f"""Comprehensive {analysis_type} analysis report with:
- Key findings
- Pattern identification
- Dependency mapping
- Recommendations for improvement""",
        async_execution=True  # Can run in parallel with other async tasks
    )


def create_parallel_review_tasks(
    security_agent: Agent,
    performance_agent: Agent,
    quality_agent: Agent,
    file_paths: List[str]
) -> List[Task]:
    """
    Create parallel code review tasks.
    Multiple agents review different aspects simultaneously.

    Args:
        security_agent: Agent focused on security
        performance_agent: Agent focused on performance
        quality_agent: Agent focused on code quality
        file_paths: Files to review

    Returns:
        List of tasks that can run in parallel
    """
    files_list = "\n".join(f"- {fp}" for fp in file_paths)

    security_task = Task(
        description=f"""Perform security review of:
{files_list}

Focus on:
- OWASP top 10 vulnerabilities
- Input validation
- Authentication/authorization
- Sensitive data handling
- Injection attacks""",
        agent=security_agent,
        expected_output="Security review report with vulnerability findings",
        async_execution=True  # Runs in parallel
    )

    performance_task = Task(
        description=f"""Perform performance analysis of:
{files_list}

Focus on:
- Algorithm complexity
- Database query efficiency
- Memory usage
- Bottlenecks
- Optimization opportunities""",
        agent=performance_agent,
        expected_output="Performance analysis report with optimization recommendations",
        async_execution=True  # Runs in parallel
    )

    quality_task = Task(
        description=f"""Perform code quality review of:
{files_list}

Focus on:
- Code readability
- Design patterns
- Code duplication
- Maintainability
- Test coverage""",
        agent=quality_agent,
        expected_output="Code quality report with improvement suggestions",
        async_execution=True  # Runs in parallel
    )

    return [security_task, performance_task, quality_task]


def create_synthesis_task(agent: Agent, context_tasks: List[Task]) -> Task:
    """
    Create a synthesis task that aggregates results from parallel tasks.
    This task waits for all context tasks to complete.

    Args:
        agent: Code Architect agent
        context_tasks: Parallel tasks to synthesize

    Returns:
        Task that synthesizes parallel task results
    """
    return Task(
        description="""Synthesize the findings from all review tasks into a single action plan.

Create a prioritized list of:
1. Critical issues to fix immediately
2. Important improvements for the next iteration
3. Nice-to-have enhancements for the future

Include specific file references and recommendations.""",
        agent=agent,
        expected_output="""Comprehensive action plan with prioritized improvements,
organized by urgency and impact""",
        context=context_tasks,  # Waits for all parallel tasks to complete
        async_execution=False  # Sequential, after parallel tasks finish
    )


class TaskOrchestrator:
    """
    Orchestrates complex multi-task workflows.
    Demonstrates advanced CrewAI patterns.
    """

    @staticmethod
    def create_full_development_workflow(
        architect: Agent,
        developer: Agent,
        reviewer: Agent,
        qa: Agent,
        writer: Agent,
        devops: Agent,
        project_description: str,
        feature_description: str
    ) -> List[Task]:
        """
        Create a complete development workflow from architecture to deployment.

        Returns:
            List of tasks in sequential order with proper dependencies
        """
        # Phase 1: Architecture
        arch_task = create_architecture_task(architect, project_description)

        # Phase 2: Implementation
        impl_task = create_implementation_task(
            developer,
            "src/main.py",
            feature_description,
            context=[arch_task]
        )

        # Phase 3: Review
        review_task = create_code_review_task(
            reviewer,
            ["src/main.py"],
            context=[impl_task]
        )

        # Phase 4: Testing
        test_task = create_testing_task(
            qa,
            "tests/test_main.py",
            "main.py functionality",
            context=[impl_task, review_task]
        )

        # Phase 5: Documentation
        doc_task = create_documentation_task(
            writer,
            "Project",
            context=[arch_task, impl_task, test_task]
        )

        # Phase 6: Deployment
        deploy_task = create_deployment_task(
            devops,
            "Docker",
            context=[impl_task, test_task, doc_task]
        )

        return [arch_task, impl_task, review_task, test_task, doc_task, deploy_task]

    @staticmethod
    def create_parallel_analysis_workflow(
        analysts: List[Agent],
        codebase_path: str
    ) -> List[Task]:
        """
        Create a parallel analysis workflow where multiple analysts work simultaneously.

        Args:
            analysts: List of research analyst agents
            codebase_path: Path to analyze

        Returns:
            List of tasks that run in parallel
        """
        return [
            create_analysis_task(analysts[0], codebase_path, "architecture"),
            create_analysis_task(analysts[1], codebase_path, "dependencies"),
            create_analysis_task(analysts[2] if len(analysts) > 2 else analysts[0], codebase_path, "patterns")
        ]


# Export all task creators
__all__ = [
    'create_architecture_task',
    'create_implementation_task',
    'create_code_review_task',
    'create_testing_task',
    'create_documentation_task',
    'create_deployment_task',
    'create_analysis_task',
    'create_parallel_review_tasks',
    'create_synthesis_task',
    'TaskOrchestrator'
]
