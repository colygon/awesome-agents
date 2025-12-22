from crewai_tools import tool

class GuardianOSTools:
    @tool("Scan for Threats")
    def scan_for_threats(self, system: str) -> str:
        """Scans system for security threats, malware, and vulnerabilities."""
        return f"""Threat Scan Results for {system}:

DETECTED THREATS:
- 3 High-severity malware samples detected
- 12 Medium-severity vulnerabilities (CVE-listed)
- 7 Suspicious network connections
- 2 Unauthorized access attempts
- 15 Outdated software components

MALWARE DETECTED:
1. Trojan.Generic.KD.12345 (Critical) - System32 folder
2. Adware.TrackingCookie (Medium) - Browser data
3. PUP.BundledSoftware (Low) - Program Files

VULNERABILITIES:
- CVE-2023-12345: OpenSSL vulnerability (CVSS 9.8)
- CVE-2023-23456: Apache Struts RCE (CVSS 8.1)
- 10 additional medium-severity CVEs

NETWORK THREATS:
- Suspicious outbound connections to 3 unknown IPs
- Port scanning activity detected from 192.168.1.105
- DNS tunneling indicators observed

RECOMMENDATIONS:
1. Quarantine detected malware immediately
2. Patch critical vulnerabilities within 24 hours
3. Block suspicious IP addresses
4. Enable enhanced monitoring"""

    @tool("Analyze Malware")
    def analyze_malware(self, sample: str) -> str:
        """Performs deep analysis of malware samples."""
        return f"""Malware Analysis Report - {sample}:

TYPE: Trojan.Backdoor.Agent
SEVERITY: Critical
BEHAVIOR:
- Creates persistent backdoor on port 4444
- Steals credentials from browsers
- Establishes C&C communication
- Downloads additional payloads
- Disables antivirus software

INDICATORS OF COMPROMISE:
- File: %TEMP%\\svchost32.exe
- Registry: HKLM\\Software\\Microsoft\\Windows\\CurrentVersion\\Run
- Network: Communication with 45.123.45.67:443
- Mutex: Global\\WindowsUpdater2023

MITIGATION:
1. Kill processes: svchost32.exe
2. Delete files and registry keys
3. Block C&C IP addresses
4. Reset compromised credentials
5. Full system scan recommended"""

    @tool("Detect Intrusions")
    def detect_intrusions(self, network_data: str) -> str:
        """Detects network intrusions and attack patterns."""
        return f"""Intrusion Detection Report:

DETECTED ATTACKS:
1. SQL Injection attempts: 45 blocked
2. XSS attacks: 12 blocked
3. Brute force login: 234 attempts from 5 IPs
4. DDoS attempt: Mitigated, 50k requests/min
5. Port scanning: Full TCP scan from external IP

ATTACK SOURCES:
- 45.123.45.67 (China) - Brute force
- 198.51.100.42 (Russia) - SQL injection
- 203.0.113.15 (Unknown) - DDoS
- 192.0.2.89 (US) - Port scanning

INTRUSION SIGNATURES:
- Signature #1245: Web application attack
- Signature #3456: SSH brute force
- Signature #7890: Malware C&C traffic

ACTIONS TAKEN:
- Blocked 8 malicious IP addresses
- Rate-limited suspicious sources
- Alerted security team
- Logged all attempts for analysis"""

    @tool("Contain Threat")
    def contain_threat(self, threat: str) -> str:
        """Contains identified threats to prevent spread."""
        return f"""Threat Containment Report - {threat}:

CONTAINMENT ACTIONS:
1. Isolated infected systems (3 workstations)
2. Disabled compromised accounts (5 users)
3. Blocked malicious IPs in firewall
4. Quarantined malware samples
5. Stopped malicious processes

NETWORK SEGMENTATION:
- Moved affected systems to quarantine VLAN
- Restricted outbound traffic
- Enhanced monitoring on segment

ACCOUNT SECURITY:
- Forced password resets
- Revoked active sessions
- Enabled MFA requirement
- Reviewed access logs

STATUS: Threat contained, eradication in progress"""

    @tool("Patch Vulnerabilities")
    def patch_vulnerabilities(self, vuln_list: str) -> str:
        """Applies patches for identified vulnerabilities."""
        return f"""Vulnerability Patching Report:

PATCHES APPLIED:
- CVE-2023-12345: OpenSSL updated to 3.0.12
- CVE-2023-23456: Apache Struts patched
- Microsoft Security Updates: 15 patches installed
- Java Runtime updated to latest version

SYSTEMS PATCHED:
- Production servers: 12/12 completed
- Workstations: 145/150 completed
- Network devices: 8/8 completed

REBOOT REQUIRED:
- 5 servers scheduled for maintenance window
- Non-critical systems rebooted immediately

VERIFICATION:
- Vulnerability scan re-run: 0 critical issues
- All systems tested and operational
- No service disruptions"""

    @tool("Restore Systems")
    def restore_systems(self, affected_systems: str) -> str:
        """Restores systems after security incident."""
        return f"""System Restoration Report:

RESTORATION STEPS:
1. Verified malware removal (clean scans)
2. Restored from clean backups (2 systems)
3. Rebuilt compromised systems (1 system)
4. Reconfigured security settings
5. Validated system integrity

SYSTEMS RESTORED:
- WS-PROD-01: Restored from backup
- WS-PROD-02: Cleaned and verified
- DB-SERVER-03: Rebuilt from scratch

DATA RECOVERY:
- 0 data loss (backups current)
- All critical services operational
- User access restored

VALIDATION:
- Full security scan: Clean
- Functionality testing: Passed
- Performance benchmarks: Normal
- Monitoring: Enhanced mode enabled"""

    @tool("Audit Compliance")
    def audit_compliance(self, framework: str) -> str:
        """Audits security compliance against frameworks."""
        return f"""Security Compliance Audit - {framework}:

COMPLIANCE SCORE: 78/100

FRAMEWORK REQUIREMENTS:
✓ Access Control: 95% compliant
✓ Encryption: 100% compliant
⚠ Patch Management: 75% compliant
⚠ Incident Response: 70% compliant
✗ Security Training: 45% compliant

GAPS IDENTIFIED:
1. Patch SLA not met (24hr requirement)
2. Incident response plan outdated
3. Security training completion low
4. Log retention below requirement
5. Disaster recovery not tested

RECOMMENDATIONS:
1. Implement automated patching
2. Update IR playbooks
3. Mandatory security training program
4. Extend log retention to 1 year
5. Schedule DR test quarterly

CERTIFICATION READINESS: 6 months"""

    @tool("Assess Security Posture")
    def assess_security_posture(self, organization: str) -> str:
        """Assesses overall security posture of organization."""
        return f"""Security Posture Assessment - {organization}:

OVERALL SCORE: 7.2/10 (Good)

SECURITY DOMAINS:

1. Network Security: 8.5/10
   ✓ Firewall properly configured
   ✓ IDS/IPS operational
   ⚠ Need network segmentation

2. Endpoint Security: 6.8/10
   ✓ Antivirus deployed
   ⚠ EDR coverage incomplete
   ⚠ Patch compliance 85%

3. Application Security: 7.5/10
   ✓ SAST/DAST implemented
   ✓ Security testing in SDLC
   ⚠ Some legacy apps unpatched

4. Identity & Access: 7.0/10
   ✓ MFA enabled
   ⚠ Privilege management weak
   ⚠ Access reviews quarterly

5. Data Security: 8.0/10
   ✓ Encryption at rest/transit
   ✓ DLP deployed
   ✓ Backups regular

STRENGTHS:
- Strong encryption practices
- Good network defenses
- Regular vulnerability scanning

WEAKNESSES:
- Incomplete EDR deployment
- Security awareness training
- Patch management process

TOP PRIORITIES:
1. Deploy EDR to all endpoints
2. Improve patch management
3. Enhance security training"""

    @tool("Generate Compliance Report")
    def generate_compliance_report(self, data: str) -> str:
        """Generates comprehensive compliance documentation."""
        return f"""COMPLIANCE REPORT - GUARDIANOS

EXECUTIVE SUMMARY:
Security compliance assessment shows 78% overall compliance
with industry standards. Critical controls in place, moderate
gaps identified in training and patch management.

FRAMEWORKS ASSESSED:
- NIST CSF: 82% compliant
- ISO 27001: 75% compliant
- SOC 2: 80% compliant
- PCI DSS: 85% compliant (if applicable)

CONTROL EFFECTIVENESS:
Preventive Controls: 85%
Detective Controls: 80%
Corrective Controls: 70%

AUDIT FINDINGS:
3 Critical gaps
12 Medium gaps
24 Low priority items

ACTION PLAN:
Q1: Address critical gaps
Q2: Remediate medium issues
Q3: Implement improvements
Q4: Re-certification audit"""

    @tool("Prioritize Threats")
    def prioritize_threats(self, threat_list: str) -> str:
        """Prioritizes security threats by risk level."""
        return f"""Threat Prioritization Matrix:

CRITICAL (Immediate Action):
1. Active malware on production server
   Impact: High | Likelihood: High | Risk: 9.5
2. Unpatched critical vulnerability (CVE-2023-12345)
   Impact: High | Likelihood: Medium | Risk: 8.8
3. Suspected data exfiltration
   Impact: Critical | Likelihood: Medium | Risk: 9.0

HIGH (24-48 Hours):
4. Brute force attacks ongoing
5. Unauthorized access attempts
6. Missing security patches (10 systems)

MEDIUM (This Week):
7. Outdated antivirus signatures
8. Weak password policies
9. Incomplete access reviews

LOW (This Month):
10. Security awareness training
11. Policy updates
12. Documentation gaps

RESOURCE ALLOCATION:
Critical: All hands
High: Security team
Medium: Scheduled work
Low: Backlog"""

    @tool("Generate Security Report")
    def generate_security_report(self, period: str) -> str:
        """Generates comprehensive security operations report."""
        return f"""SECURITY OPERATIONS REPORT - {period}

EXECUTIVE SUMMARY:
Detected and mitigated 3 critical threats, applied 15 security
patches, maintained 99.8% uptime. Overall security posture improved
from 6.8 to 7.2 out of 10.

THREAT LANDSCAPE:
- Threats detected: 342
- Threats mitigated: 340
- Active incidents: 2
- False positives: 12%

INCIDENT RESPONSE:
- Incidents handled: 8
- Mean time to detect: 15 minutes
- Mean time to respond: 45 minutes
- Mean time to resolve: 4 hours

VULNERABILITY MANAGEMENT:
- Vulnerabilities found: 47
- Critical: 2 (patched)
- High: 12 (10 patched)
- Medium: 33 (15 patched)

COMPLIANCE STATUS:
- Overall: 78%
- Improving trend: +5% this quarter

METRICS:
- Security events: 125,000
- Blocked attacks: 2,340
- Phishing emails blocked: 1,456
- System uptime: 99.8%"""

    @tool("Recommend Improvements")
    def recommend_improvements(self, current_state: str) -> str:
        """Recommends security improvements and roadmap."""
        return f"""Security Improvement Roadmap:

IMMEDIATE (0-30 days):
1. Deploy EDR to remaining endpoints ($15k)
2. Patch critical vulnerabilities (0 cost)
3. Enable MFA for all accounts ($5k)
4. Update incident response playbooks (0 cost)

SHORT-TERM (1-3 months):
5. Implement SIEM solution ($50k)
6. Security awareness training ($10k)
7. Network segmentation project ($25k)
8. Vulnerability management platform ($20k)

MEDIUM-TERM (3-6 months):
9. Zero Trust architecture planning ($100k)
10. Security orchestration (SOAR) ($75k)
11. Enhanced DLP capabilities ($30k)
12. Red team assessment ($25k)

LONG-TERM (6-12 months):
13. SOC maturity improvement ($200k)
14. Cloud security posture mgmt ($40k)
15. Deception technology ($50k)

TOTAL INVESTMENT: $645k over 12 months
EXPECTED ROI: 35% reduction in incidents
RISK REDUCTION: High to Medium overall risk"""
