"""CrewAI Tasks for Code Review Assistant"""

from crewai import Task
from textwrap import dedent


class CodeReviewTasks:
    """Factory class for code review tasks"""

    def analyze_code_quality(self, agent, code_file: str, language: str) -> Task:
        return Task(
            description=dedent(f"""
                Analyze code quality for: {code_file}
                Language: {language}

                Review Areas:
                1. Code complexity and maintainability
                2. Bug-prone patterns
                3. Code smells and anti-patterns
                4. Error handling
                5. Code duplication
                6. Best practices adherence
            """),
            agent=agent,
            expected_output='Detailed code quality report with issues and recommendations'
        )

    def review_security(self, agent, code_file: str) -> Task:
        return Task(
            description=dedent(f"""
                Security review for: {code_file}

                Check for:
                1. SQL injection vulnerabilities
                2. XSS vulnerabilities
                3. Authentication/authorization issues
                4. Sensitive data exposure
                5. Insecure dependencies
                6. Cryptographic weaknesses
            """),
            agent=agent,
            expected_output='Security assessment with vulnerability severity ratings',
            context=[]
        )

    def review_performance(self, agent, code_file: str) -> Task:
        return Task(
            description=dedent(f"""
                Performance review for: {code_file}

                Analyze:
                1. Algorithm complexity (Big O)
                2. Memory usage patterns
                3. Database query efficiency
                4. Loop optimization opportunities
                5. Caching strategies
                6. Resource management
            """),
            agent=agent,
            expected_output='Performance analysis with optimization suggestions',
            context=[]
        )

    def check_style(self, agent, code_file: str, style_guide: str = "PEP 8") -> Task:
        return Task(
            description=dedent(f"""
                Style and convention check for: {code_file}
                Style Guide: {style_guide}

                Verify:
                1. Naming conventions
                2. Formatting and indentation
                3. Comment quality
                4. Documentation completeness
                5. Import organization
                6. Code organization
            """),
            agent=agent,
            expected_output='Style compliance report with formatting suggestions',
            context=[]
        )

    def synthesize_review(self, agent, code_file: str) -> Task:
        return Task(
            description=dedent(f"""
                Synthesize comprehensive code review for: {code_file}

                Compile:
                1. Summary of all findings
                2. Prioritized issue list
                3. Approval recommendation
                4. Suggested improvements
                5. Learning opportunities
            """),
            agent=agent,
            expected_output='Complete code review summary with recommendations',
            context=[]
        )
