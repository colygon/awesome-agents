"""Security Audit Agent - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import SecurityAuditAgents
from tasks import SecurityAuditTasks

load_dotenv()


def perform_security_audit(target_system: dict, dependency_file: str, config_files: list, standards: list) -> str:
    """Perform comprehensive security audit"""

    agents = SecurityAuditAgents()
    tasks_factory = SecurityAuditTasks()

    vuln_scanner = agents.vulnerability_scanner()
    dep_auditor = agents.dependency_auditor()
    config_reviewer = agents.configuration_reviewer()
    compliance_checker = agents.compliance_checker()

    vuln_task = tasks_factory.scan_vulnerabilities(vuln_scanner, target_system)
    dep_task = tasks_factory.audit_dependencies(dep_auditor, dependency_file)
    config_task = tasks_factory.review_configurations(config_reviewer, config_files)
    compliance_task = tasks_factory.check_compliance(compliance_checker, standards)

    synthesis_task = tasks_factory.synthesize_audit(vuln_scanner, target_system.get('name', 'System'))
    synthesis_task.context = [vuln_task, dep_task, config_task, compliance_task]

    crew = Crew(
        agents=[vuln_scanner, dep_auditor, config_reviewer, compliance_checker],
        tasks=[vuln_task, dep_task, config_task, compliance_task, synthesis_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    target_system = {'name': 'WebApp', 'type': 'web_application', 'stack': 'Python/Flask'}
    result = perform_security_audit(target_system, 'requirements.txt', ['config.py', '.env'], ['OWASP', 'GDPR'])
    print(result)


if __name__ == "__main__":
    main()
