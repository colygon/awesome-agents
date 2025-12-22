from crewai import Task
from textwrap import dedent

class GuardianOSTasks:
    def detect_threats(self, agent, system_data):
        return Task(
            description=dedent(f"""
                Scan and analyze the system for security threats and vulnerabilities.

                System Data: {system_data}

                Your analysis should include:
                1. Malware and virus detection
                2. Network intrusion detection
                3. Vulnerability scanning
                4. Suspicious activity monitoring
                5. Threat severity assessment
            """),
            expected_output="""A comprehensive threat detection report with:
                - Identified threats and malware
                - Detected intrusions and attacks
                - Discovered vulnerabilities (CVEs)
                - Suspicious activities and anomalies
                - Severity ratings and risk scores
                - Recommended immediate actions""",
            agent=agent
        )

    def respond_to_incidents(self, agent, threat_report):
        return Task(
            description=dedent(f"""
                Respond to identified security threats and incidents.

                Threat Report: {threat_report}

                Your response should include:
                1. Threat containment actions
                2. Vulnerability patching
                3. System hardening
                4. Affected system recovery
                5. Prevention measures
            """),
            expected_output="""A detailed incident response plan with:
                - Containment procedures executed
                - Patches applied and systems updated
                - Hardening measures implemented
                - Recovery steps completed
                - Future prevention strategies
                - Timeline of response actions""",
            agent=agent
        )

    def audit_compliance(self, agent, standards):
        return Task(
            description=dedent(f"""
                Audit system security compliance with standards and regulations.

                Standards: {standards}

                Your audit should cover:
                1. Compliance with security frameworks
                2. Security posture assessment
                3. Gap analysis
                4. Best practices evaluation
                5. Certification readiness
            """),
            expected_output="""A comprehensive compliance audit report with:
                - Compliance status by framework
                - Security posture score
                - Identified gaps and deficiencies
                - Best practice recommendations
                - Remediation priorities
                - Certification readiness assessment""",
            agent=agent
        )

    def coordinate_security(self, agent):
        return Task(
            description=dedent("""
                Coordinate all security operations and generate comprehensive report.

                Your coordination should include:
                1. Integration of threat detection and response
                2. Overall security posture evaluation
                3. Risk prioritization
                4. Strategic security recommendations
                5. Executive security summary
            """),
            expected_output="""A comprehensive security operations report with:
                - Executive summary of security status
                - Integrated threat and response overview
                - Overall risk assessment
                - Prioritized action items
                - Strategic security roadmap
                - Metrics and KPIs
                - Budget and resource recommendations""",
            agent=agent
        )
