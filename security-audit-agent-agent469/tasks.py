"""CrewAI Tasks for Security Audit"""

from crewai import Task
from textwrap import dedent


class SecurityAuditTasks:
    """Factory class for security audit tasks"""

    def scan_vulnerabilities(self, agent, target_system: dict) -> Task:
        return Task(
            description=dedent(f"""
                Scan for security vulnerabilities:
                System: {target_system}

                Scan for:
                1. Injection vulnerabilities (SQL, XSS, Command)
                2. Authentication/authorization flaws
                3. Sensitive data exposure
                4. Security misconfigurations
                5. Broken access control
                6. Known CVEs
                7. Insecure cryptography
            """),
            agent=agent,
            expected_output='Vulnerability assessment report with severity ratings'
        )

    def audit_dependencies(self, agent, dependency_file: str) -> Task:
        return Task(
            description=dedent(f"""
                Audit project dependencies:
                Dependency File: {dependency_file}

                Check for:
                1. Known vulnerabilities (CVEs)
                2. Outdated packages
                3. Deprecated dependencies
                4. License compliance issues
                5. Malicious packages
                6. Transitive dependencies
            """),
            agent=agent,
            expected_output='Dependency audit report with vulnerable packages',
            context=[]
        )

    def review_configurations(self, agent, config_files: list) -> Task:
        return Task(
            description=dedent(f"""
                Review security configurations:
                Config Files: {config_files}

                Review:
                1. Authentication mechanisms
                2. Access control policies
                3. Encryption settings
                4. API key management
                5. CORS and security headers
                6. Database security
                7. Secrets management
            """),
            agent=agent,
            expected_output='Configuration security review with recommendations',
            context=[]
        )

    def check_compliance(self, agent, standards: list) -> Task:
        return Task(
            description=dedent(f"""
                Check compliance with security standards:
                Standards: {standards}

                Verify:
                1. Data protection requirements
                2. Access control policies
                3. Encryption requirements
                4. Logging and monitoring
                5. Incident response procedures
                6. Data retention policies
            """),
            agent=agent,
            expected_output='Compliance assessment with gap analysis',
            context=[]
        )

    def synthesize_audit(self, agent, system_name: str) -> Task:
        return Task(
            description=dedent(f"""
                Synthesize comprehensive security audit:
                System: {system_name}

                Compile:
                1. Executive summary
                2. Critical vulnerabilities
                3. Risk assessment
                4. Remediation priorities
                5. Compliance status
                6. Actionable recommendations
            """),
            agent=agent,
            expected_output='Comprehensive security audit report with action plan',
            context=[]
        )
