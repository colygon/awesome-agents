"""
Code Review Scenario - Multi-Agent Code Review Workflow
Demonstrates a complete code review process with multiple specialized reviewers.
"""

from crewai import Crew, Process, Task
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import (
    create_code_reviewer,
    create_research_analyst,
    create_code_architect,
    create_qa_engineer
)


def run_code_review_workflow(files_to_review: list = None):
    """
    Run a comprehensive code review workflow.

    This demonstrates:
    - Multiple specialized reviewers
    - Parallel review execution
    - Synthesis of findings
    - Actionable recommendations

    Args:
        files_to_review: List of file paths to review (defaults to current project files)

    Returns:
        Comprehensive code review report
    """
    if files_to_review is None:
        files_to_review = ["tools.py", "agents.py", "tasks.py", "main.py"]

    print("\n" + "="*80)
    print("Multi-Agent Code Review Workflow")
    print("="*80)
    print(f"\nReviewing {len(files_to_review)} files with 4 specialized agents:\n")

    # Create specialized review team
    security_reviewer = create_code_reviewer()
    performance_analyst = create_research_analyst()
    qa_reviewer = create_qa_engineer()
    architect = create_code_architect()

    files_list = "\n".join(f"- {f}" for f in files_to_review)

    # Task 1: Security Review (parallel)
    security_task = Task(
        description=f"""Perform a comprehensive security review of these files:

{files_list}

Focus on:
1. OWASP Top 10 vulnerabilities
2. Input validation and sanitization
3. Authentication and authorization issues
4. Sensitive data exposure
5. SQL injection, XSS, CSRF risks
6. Dependency vulnerabilities

Provide specific findings with file:line references.""",
        agent=security_reviewer,
        expected_output="Security review report with vulnerability findings and remediation recommendations",
        async_execution=True  # Runs in parallel
    )

    # Task 2: Performance Review (parallel)
    performance_task = Task(
        description=f"""Analyze performance and efficiency of these files:

{files_list}

Focus on:
1. Algorithm complexity (Big O analysis)
2. Memory usage patterns
3. Database query optimization
4. Network call efficiency
5. Caching opportunities
6. Resource cleanup and management

Provide specific recommendations with file:line references.""",
        agent=performance_analyst,
        expected_output="Performance analysis report with optimization recommendations",
        async_execution=True  # Runs in parallel
    )

    # Task 3: Quality Review (parallel)
    quality_task = Task(
        description=f"""Review code quality and testing of these files:

{files_list}

Focus on:
1. Code readability and maintainability
2. Design patterns and SOLID principles
3. Code duplication (DRY violations)
4. Test coverage and quality
5. Error handling completeness
6. Documentation quality

Provide specific improvements with file:line references.""",
        agent=qa_reviewer,
        expected_output="Code quality report with improvement suggestions",
        async_execution=True  # Runs in parallel
    )

    # Task 4: Architecture Review (parallel)
    architecture_task = Task(
        description=f"""Review system architecture and design of these files:

{files_list}

Focus on:
1. Module organization and dependencies
2. Separation of concerns
3. Scalability considerations
4. Design pattern usage
5. API design quality
6. Future maintainability

Provide architectural recommendations.""",
        agent=architect,
        expected_output="Architecture review with design recommendations",
        async_execution=True  # Runs in parallel
    )

    # Task 5: Synthesis (sequential, after all parallel tasks)
    synthesis_task = Task(
        description="""Synthesize all review findings into a prioritized action plan.

Organize findings by:
1. CRITICAL: Security vulnerabilities and major bugs
2. HIGH: Performance issues and architectural problems
3. MEDIUM: Code quality and maintainability improvements
4. LOW: Minor optimizations and style improvements

For each item:
- Provide file:line references
- Explain the issue
- Suggest specific remediation
- Estimate effort (Small/Medium/Large)

Create an actionable roadmap for addressing these findings.""",
        agent=architect,
        expected_output="""Comprehensive action plan with:
- Prioritized findings
- Specific remediation steps
- File:line references
- Effort estimates
- Implementation order""",
        context=[security_task, performance_task, quality_task, architecture_task],  # Waits for parallel tasks
        async_execution=False  # Sequential
    )

    # Create crew
    crew = Crew(
        agents=[security_reviewer, performance_analyst, qa_reviewer, architect],
        tasks=[security_task, performance_task, quality_task, architecture_task, synthesis_task],
        process=Process.sequential,  # Tasks marked async will run in parallel
        verbose=True
    )

    print("\nStarting parallel code review...")
    print("Four agents are reviewing different aspects simultaneously.\n")

    # Execute
    result = crew.kickoff()

    print("\n" + "="*80)
    print("Code Review Complete")
    print("="*80 + "\n")

    return result


def quick_security_scan(file_path: str):
    """
    Quick security-focused review of a single file.

    Args:
        file_path: Path to file to review

    Returns:
        Security review results
    """
    print(f"\nRunning quick security scan on {file_path}...\n")

    reviewer = create_code_reviewer()

    task = Task(
        description=f"""Perform a quick security scan of {file_path}.

Check for:
- Common vulnerabilities (SQL injection, XSS, etc.)
- Hardcoded secrets or credentials
- Unsafe file operations
- Command injection risks
- Insecure dependencies

Provide a brief report with any findings.""",
        agent=reviewer,
        expected_output="Quick security scan report"
    )

    crew = Crew(
        agents=[reviewer],
        tasks=[task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


if __name__ == "__main__":
    # Can be run standalone
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                    Multi-Agent Code Review Workflow                          ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    import sys
    if len(sys.argv) > 1:
        # Review specific files
        files = sys.argv[1:]
        result = run_code_review_workflow(files)
    else:
        # Review default project files
        result = run_code_review_workflow()

    print("\nFinal Report:")
    print("="*80)
    print(result)
