from crewai import Agent
from tools import GuardianOSTools

class GuardianOSAgents:
    def __init__(self):
        self.tools = GuardianOSTools()

    def threat_detector(self):
        return Agent(
            role='Cybersecurity Threat Detector',
            goal='Detect and analyze security threats, vulnerabilities, and suspicious activities',
            backstory="""You are an expert in cybersecurity threat detection and analysis.
            You specialize in identifying malware, intrusions, vulnerabilities, and
            security anomalies across systems and networks.""",
            tools=[
                self.tools.scan_for_threats,
                self.tools.analyze_malware,
                self.tools.detect_intrusions
            ],
            verbose=True,
            allow_delegation=False
        )

    def security_responder(self):
        return Agent(
            role='Security Incident Responder',
            goal='Respond to security incidents and implement protective measures',
            backstory="""You are a security incident response specialist who handles
            breaches, attacks, and security events. You excel at containment, eradication,
            and recovery from security incidents.""",
            tools=[
                self.tools.contain_threat,
                self.tools.patch_vulnerabilities,
                self.tools.restore_systems
            ],
            verbose=True,
            allow_delegation=False
        )

    def compliance_auditor(self):
        return Agent(
            role='Security Compliance Auditor',
            goal='Ensure systems meet security standards and regulatory compliance',
            backstory="""You are a security compliance expert who ensures systems meet
            regulatory requirements and industry standards. You perform audits, assessments,
            and ensure best practices are followed.""",
            tools=[
                self.tools.audit_compliance,
                self.tools.assess_security_posture,
                self.tools.generate_compliance_report
            ],
            verbose=True,
            allow_delegation=False
        )

    def security_coordinator(self):
        return Agent(
            role='Security Operations Coordinator',
            goal='Coordinate security operations and maintain overall system protection',
            backstory="""You are a security operations manager who oversees the complete
            security lifecycle. You coordinate threat detection, incident response, and
            compliance to ensure comprehensive protection.""",
            tools=[
                self.tools.prioritize_threats,
                self.tools.generate_security_report,
                self.tools.recommend_improvements
            ],
            verbose=True,
            allow_delegation=True
        )
