"""
Research Scenario - Collaborative Research Team Workflow
Demonstrates how multiple agents collaborate on research and analysis tasks.
"""

from crewai import Crew, Process, Task
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import (
    create_research_analyst,
    create_code_architect,
    create_technical_writer
)


def run_codebase_research(target_directory: str = "."):
    """
    Run a comprehensive codebase research workflow.

    This demonstrates:
    - Multiple analysts working on different aspects
    - Pattern detection and dependency mapping
    - Collaborative synthesis
    - Documentation of findings

    Args:
        target_directory: Directory to analyze (defaults to current directory)

    Returns:
        Comprehensive research report
    """
    print("\n" + "="*80)
    print("Collaborative Codebase Research Workflow")
    print("="*80)
    print(f"\nAnalyzing codebase in: {target_directory}\n")

    # Create research team
    analyst1 = create_research_analyst()
    analyst2 = create_research_analyst()
    architect = create_code_architect()
    writer = create_technical_writer()

    # Task 1: Architecture Analysis (parallel)
    architecture_analysis = Task(
        description=f"""Analyze the architectural patterns in {target_directory}.

Research objectives:
1. Identify main modules and their responsibilities
2. Map dependencies between components
3. Detect architectural patterns (MVC, layered, etc.)
4. Find potential architectural issues
5. Assess scalability and maintainability

Use glob_files to discover the structure and read_file to examine key files.

Provide a detailed architectural analysis.""",
        agent=analyst1,
        expected_output="""Architectural analysis including:
- Module structure diagram
- Dependency map
- Pattern identification
- Scalability assessment""",
        async_execution=True
    )

    # Task 2: Code Pattern Analysis (parallel)
    pattern_analysis = Task(
        description=f"""Analyze code patterns and practices in {target_directory}.

Research objectives:
1. Identify common design patterns in use
2. Find code duplication opportunities
3. Detect anti-patterns and code smells
4. Analyze error handling patterns
5. Review testing patterns and coverage

Use grep_search to find patterns across the codebase.

Provide a code pattern analysis report.""",
        agent=analyst2,
        expected_output="""Code pattern analysis including:
- Design patterns in use
- Code duplication findings
- Anti-pattern detection
- Testing pattern analysis""",
        async_execution=True
    )

    # Task 3: Synthesis and Recommendations (sequential)
    synthesis_task = Task(
        description="""Synthesize the research findings and provide architectural recommendations.

Based on the analyses:
1. Identify key strengths of the current architecture
2. Highlight main areas for improvement
3. Provide specific, actionable recommendations
4. Prioritize recommendations by impact
5. Suggest a roadmap for improvements

Create a comprehensive improvement plan.""",
        agent=architect,
        expected_output="""Improvement plan with:
- Current state summary
- Strengths and weaknesses
- Prioritized recommendations
- Implementation roadmap""",
        context=[architecture_analysis, pattern_analysis],
        async_execution=False
    )

    # Task 4: Documentation (sequential)
    documentation_task = Task(
        description="""Document all research findings in a clear, readable report.

Create a comprehensive research report including:
1. Executive summary
2. Methodology
3. Architectural findings
4. Code pattern findings
5. Recommendations with priorities
6. Implementation roadmap

Make it accessible to both technical and non-technical stakeholders.""",
        agent=writer,
        expected_output="""Complete research report with:
- Executive summary
- Detailed findings
- Visual diagrams (text-based)
- Actionable recommendations
- Glossary of terms""",
        context=[architecture_analysis, pattern_analysis, synthesis_task],
        async_execution=False
    )

    # Create crew
    crew = Crew(
        agents=[analyst1, analyst2, architect, writer],
        tasks=[architecture_analysis, pattern_analysis, synthesis_task, documentation_task],
        process=Process.sequential,
        verbose=True
    )

    print("\nStarting collaborative research...")
    print("Two analysts will research in parallel, then architect will synthesize,")
    print("and technical writer will document findings.\n")

    # Execute
    result = crew.kickoff()

    print("\n" + "="*80)
    print("Research Complete")
    print("="*80 + "\n")

    return result


def run_technology_research(technology: str, use_case: str):
    """
    Research a specific technology for a use case.

    Args:
        technology: Technology to research (e.g., "GraphQL", "Redis")
        use_case: Intended use case

    Returns:
        Technology research report
    """
    print(f"\nResearching {technology} for {use_case}...\n")

    analyst = create_research_analyst()
    architect = create_code_architect()
    writer = create_technical_writer()

    # Research task
    research_task = Task(
        description=f"""Research {technology} for use in {use_case}.

Investigation areas:
1. Core features and capabilities
2. Performance characteristics
3. Integration complexity
4. Learning curve
5. Community and ecosystem
6. Alternatives comparison

Provide a comprehensive analysis.""",
        agent=analyst,
        expected_output=f"Detailed analysis of {technology} for {use_case}"
    )

    # Recommendation task
    recommendation_task = Task(
        description=f"""Based on the research, provide architectural recommendations for using {technology}.

Include:
1. Recommended architecture pattern
2. Integration approach
3. Potential challenges and solutions
4. Migration strategy (if applicable)
5. Best practices

Provide actionable guidance.""",
        agent=architect,
        expected_output="Architectural recommendations and implementation guidance",
        context=[research_task]
    )

    # Documentation task
    doc_task = Task(
        description=f"""Create a decision document for adopting {technology}.

Include:
1. Executive summary with recommendation
2. Technology overview
3. Pros and cons analysis
4. Implementation plan
5. Risk assessment
6. Resource requirements

Make it suitable for stakeholder review.""",
        agent=writer,
        expected_output="Complete decision document",
        context=[research_task, recommendation_task]
    )

    crew = Crew(
        agents=[analyst, architect, writer],
        tasks=[research_task, recommendation_task, doc_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def run_dependency_analysis(project_path: str = "."):
    """
    Analyze project dependencies and suggest updates.

    Args:
        project_path: Path to project

    Returns:
        Dependency analysis report
    """
    print(f"\nAnalyzing dependencies in {project_path}...\n")

    analyst = create_research_analyst()
    architect = create_code_architect()

    analysis_task = Task(
        description=f"""Analyze project dependencies in {project_path}.

Check:
1. Dependencies listed in requirements.txt or package.json
2. Direct vs transitive dependencies
3. Version currency (are they up-to-date?)
4. Security vulnerabilities
5. Unused dependencies
6. Missing dependencies

Use glob_files to find dependency files and read_file to analyze them.""",
        agent=analyst,
        expected_output="Comprehensive dependency analysis"
    )

    recommendation_task = Task(
        description="""Provide recommendations for dependency management.

Include:
1. Dependencies to update
2. Dependencies to remove
3. Missing dependencies to add
4. Security concerns to address
5. Update strategy (all at once vs incremental)

Prioritize by risk and impact.""",
        agent=architect,
        expected_output="Dependency update recommendations with priorities",
        context=[analysis_task]
    )

    crew = Crew(
        agents=[analyst, architect],
        tasks=[analysis_task, recommendation_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


if __name__ == "__main__":
    print("""
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║                   Collaborative Research Team Workflow                       ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
    """)

    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "codebase":
            target = sys.argv[2] if len(sys.argv) > 2 else "."
            result = run_codebase_research(target)
        elif command == "technology":
            if len(sys.argv) < 4:
                print("Usage: python research.py technology <tech> <use-case>")
                print("Example: python research.py technology GraphQL 'API development'")
                sys.exit(1)
            tech = sys.argv[2]
            use_case = sys.argv[3]
            result = run_technology_research(tech, use_case)
        elif command == "dependencies":
            path = sys.argv[2] if len(sys.argv) > 2 else "."
            result = run_dependency_analysis(path)
        else:
            print("Unknown command. Use: codebase, technology, or dependencies")
            sys.exit(1)
    else:
        # Default: run codebase research
        result = run_codebase_research()

    print("\nFinal Report:")
    print("="*80)
    print(result)
