from crewai_tools import tool
import json
from typing import Dict, List, Any
from datetime import datetime, timedelta
import re

class DocumentParsingTools:
    @tool("Extract Parties")
    def extract_parties(document_text: str) -> str:
        """
        Extracts parties involved in the legal document.
        Useful for identifying all stakeholders.
        """
        # Simulated party extraction
        parties = {
            "total_parties": 2,
            "parties": [
                {
                    "role": "First Party / Client",
                    "name": "ABC Corporation",
                    "legal_name": "ABC Corporation, Inc.",
                    "address": "123 Business St, New York, NY 10001",
                    "contact": "John Smith, CEO",
                    "email": "john.smith@abccorp.com",
                    "type": "Corporation"
                },
                {
                    "role": "Second Party / Vendor",
                    "name": "XYZ Services LLC",
                    "legal_name": "XYZ Services, Limited Liability Company",
                    "address": "456 Service Ave, Boston, MA 02101",
                    "contact": "Jane Doe, Director",
                    "email": "jane.doe@xyzservices.com",
                    "type": "LLC"
                }
            ],
            "other_mentioned_parties": [
                "Third-party auditors (as referenced in Section 5.2)",
                "Legal counsel (notification rights)"
            ]
        }

        return json.dumps(parties, indent=2)

    @tool("Extract Dates")
    def extract_dates(document_text: str) -> str:
        """
        Extracts important dates from legal documents.
        Useful for tracking deadlines and milestones.
        """
        dates = {
            "key_dates": [
                {
                    "type": "Effective Date",
                    "date": "2024-01-15",
                    "description": "Date when agreement becomes effective"
                },
                {
                    "type": "Expiration Date",
                    "date": "2026-01-14",
                    "description": "Initial term ends, subject to renewal"
                },
                {
                    "type": "Payment Due Date",
                    "date": "2024-02-01",
                    "description": "First payment of $50,000 due",
                    "recurring": "Monthly"
                },
                {
                    "type": "Notice Period",
                    "date": "N/A",
                    "description": "90 days notice required for termination"
                },
                {
                    "type": "Renewal Deadline",
                    "date": "2025-10-15",
                    "description": "Deadline to provide notice for non-renewal"
                }
            ],
            "milestones": [
                {
                    "milestone": "Deliverable Phase 1",
                    "date": "2024-03-31",
                    "status": "pending"
                },
                {
                    "milestone": "Mid-term Review",
                    "date": "2025-01-15",
                    "status": "pending"
                }
            ],
            "upcoming_deadlines": ["2024-02-01", "2024-03-31"]
        }

        return json.dumps(dates, indent=2)

    @tool("Identify Clauses")
    def identify_clauses(document_text: str) -> str:
        """
        Identifies and categorizes legal clauses in document.
        Useful for understanding document structure.
        """
        clauses = {
            "total_clauses": 24,
            "clause_categories": {
                "Payment Terms": {
                    "sections": ["3.1", "3.2", "3.3"],
                    "summary": "Monthly payments of $50,000, payment terms net 30"
                },
                "Confidentiality": {
                    "sections": ["7.1", "7.2"],
                    "summary": "Mutual NDA, 5-year confidentiality period"
                },
                "Intellectual Property": {
                    "sections": ["8.1", "8.2", "8.3"],
                    "summary": "Work product ownership, license grants, pre-existing IP"
                },
                "Termination": {
                    "sections": ["10.1", "10.2", "10.3"],
                    "summary": "Termination for convenience (90 days), breach (30 days cure)"
                },
                "Liability & Indemnification": {
                    "sections": ["11.1", "11.2", "11.3"],
                    "summary": "Liability cap at 12 months fees, mutual indemnification"
                },
                "Warranties": {
                    "sections": ["6.1", "6.2"],
                    "summary": "Limited warranties, disclaimer of implied warranties"
                },
                "Dispute Resolution": {
                    "sections": ["12.1", "12.2"],
                    "summary": "Binding arbitration, New York venue"
                }
            },
            "special_provisions": [
                "Non-compete clause (Section 9.1)",
                "Automatic renewal provision (Section 2.2)",
                "Force majeure (Section 13.5)"
            ]
        }

        return json.dumps(clauses, indent=2)

    @tool("Generate Comparison")
    def generate_comparison(documents: str) -> str:
        """
        Compares multiple versions or similar documents.
        Useful for reviewing revisions or alternatives.
        """
        comparison = {
            "documents_compared": ["Version 1.0", "Version 2.0"],
            "comparison_date": datetime.now().strftime("%Y-%m-%d"),
            "key_differences": [
                {
                    "section": "Payment Terms (3.1)",
                    "version_1": "$45,000 per month",
                    "version_2": "$50,000 per month",
                    "impact": "high",
                    "recommendation": "Negotiate or accept based on value"
                },
                {
                    "section": "Liability Cap (11.1)",
                    "version_1": "6 months of fees",
                    "version_2": "12 months of fees",
                    "impact": "medium",
                    "recommendation": "Version 2 more favorable to vendor"
                },
                {
                    "section": "Termination Notice (10.1)",
                    "version_1": "60 days notice",
                    "version_2": "90 days notice",
                    "impact": "medium",
                    "recommendation": "Longer notice period in Version 2"
                },
                {
                    "section": "IP Ownership (8.1)",
                    "version_1": "Shared ownership",
                    "version_2": "Client full ownership",
                    "impact": "high",
                    "recommendation": "Version 2 more favorable to client"
                }
            ],
            "clauses_added_in_v2": [
                "Data privacy compliance (Section 14)",
                "Service level agreements (Section 5)"
            ],
            "clauses_removed_from_v1": [
                "Non-solicitation provision"
            ],
            "overall_assessment": "Version 2 has higher costs but better IP protection and added SLA provisions"
        }

        return json.dumps(comparison, indent=2)


class AnalysisTools:
    @tool("Analyze Terms")
    def analyze_terms(contract_text: str) -> str:
        """
        Analyzes contract terms and conditions.
        Useful for understanding agreement details.
        """
        terms_analysis = {
            "contract_type": "Service Agreement",
            "main_terms": {
                "scope_of_work": "Software development and maintenance services",
                "contract_value": "$1,200,000 (24 months)",
                "payment_structure": "Monthly fixed fee",
                "contract_duration": "2 years initial term",
                "renewal_terms": "Automatic renewal unless 90 days notice",
                "price_adjustments": "3% annual increase allowed"
            },
            "performance_obligations": {
                "service_levels": "99.5% uptime guarantee",
                "response_times": "4 hours for critical issues",
                "deliverables": "Monthly progress reports, quarterly reviews",
                "key_personnel": "Named developers must be assigned"
            },
            "financial_terms": {
                "payment_schedule": "Net 30 from invoice date",
                "late_fees": "1.5% per month on overdue amounts",
                "expense_reimbursement": "Pre-approved expenses only",
                "price_protection": "No price increases in first year"
            },
            "unusual_terms": [
                "Automatic renewal with price increase",
                "Limited liability cap below industry standard",
                "Broad definition of confidential information"
            ]
        }

        return json.dumps(terms_analysis, indent=2)

    @tool("Identify Obligations")
    def identify_obligations(contract_text: str) -> str:
        """
        Identifies obligations for each party in the contract.
        Useful for understanding what each party must do.
        """
        obligations = {
            "client_obligations": [
                {
                    "obligation": "Provide timely access to systems and data",
                    "section": "4.1",
                    "frequency": "As needed",
                    "criticality": "high"
                },
                {
                    "obligation": "Designate project manager and stakeholders",
                    "section": "4.2",
                    "frequency": "Initial and as changed",
                    "criticality": "high"
                },
                {
                    "obligation": "Make monthly payments within 30 days",
                    "section": "3.1",
                    "frequency": "Monthly",
                    "criticality": "high"
                },
                {
                    "obligation": "Provide feedback on deliverables within 10 business days",
                    "section": "4.3",
                    "frequency": "Per deliverable",
                    "criticality": "medium"
                },
                {
                    "obligation": "Maintain confidentiality of vendor's proprietary information",
                    "section": "7.1",
                    "frequency": "Ongoing",
                    "criticality": "high"
                }
            ],
            "vendor_obligations": [
                {
                    "obligation": "Deliver services per statement of work",
                    "section": "2.1",
                    "frequency": "Ongoing",
                    "criticality": "high"
                },
                {
                    "obligation": "Maintain service level of 99.5% uptime",
                    "section": "5.1",
                    "frequency": "Ongoing",
                    "criticality": "high"
                },
                {
                    "obligation": "Provide monthly status reports",
                    "section": "2.3",
                    "frequency": "Monthly",
                    "criticality": "medium"
                },
                {
                    "obligation": "Maintain insurance coverage",
                    "section": "11.4",
                    "frequency": "Ongoing",
                    "criticality": "high"
                },
                {
                    "obligation": "Comply with data protection requirements",
                    "section": "14.1",
                    "frequency": "Ongoing",
                    "criticality": "high"
                }
            ],
            "mutual_obligations": [
                "Maintain confidentiality (Section 7)",
                "Provide notice of material changes (Section 15.2)",
                "Cooperate in good faith (Section 16.1)"
            ]
        }

        return json.dumps(obligations, indent=2)

    @tool("Assess Risks")
    def assess_risks(contract_text: str) -> str:
        """
        Assesses potential risks in the contract.
        Useful for risk management and decision making.
        """
        risk_assessment = {
            "overall_risk_level": "medium",
            "identified_risks": [
                {
                    "risk_type": "Financial",
                    "description": "Automatic renewal with 3% price increase",
                    "severity": "medium",
                    "likelihood": "high",
                    "mitigation": "Calendar reminder for 90-day notice period"
                },
                {
                    "risk_type": "Liability",
                    "description": "Liability cap limited to 12 months of fees",
                    "severity": "high",
                    "likelihood": "low",
                    "mitigation": "Consider additional insurance coverage"
                },
                {
                    "risk_type": "Performance",
                    "description": "Limited remedies for SLA breaches",
                    "severity": "medium",
                    "likelihood": "medium",
                    "mitigation": "Negotiate stronger service credits"
                },
                {
                    "risk_type": "Termination",
                    "description": "90-day notice period limits flexibility",
                    "severity": "low",
                    "likelihood": "low",
                    "mitigation": "Plan exit strategy well in advance"
                },
                {
                    "risk_type": "IP Rights",
                    "description": "Vendor retains some IP rights to improvements",
                    "severity": "medium",
                    "likelihood": "high",
                    "mitigation": "Clarify ownership of custom developments"
                },
                {
                    "risk_type": "Data Privacy",
                    "description": "Data processing agreement may need updates for new regulations",
                    "severity": "medium",
                    "likelihood": "medium",
                    "mitigation": "Annual compliance review"
                }
            ],
            "red_flags": [
                "Unilateral right to modify terms with 30 days notice",
                "Broad indemnification obligations",
                "No explicit data breach notification timeline"
            ],
            "recommended_actions": [
                "Negotiate liability cap increase",
                "Add termination for convenience clause",
                "Strengthen data breach provisions",
                "Clarify IP ownership of deliverables"
            ]
        }

        return json.dumps(risk_assessment, indent=2)

    @tool("Create Executive Summary")
    def create_executive_summary(analysis_data: str) -> str:
        """
        Creates executive summary of legal document analysis.
        Useful for quick stakeholder briefing.
        """
        summary = {
            "document_title": "Software Development Services Agreement",
            "parties": "ABC Corporation and XYZ Services LLC",
            "effective_date": "2024-01-15",

            "executive_summary": """
This is a 2-year software development services agreement between ABC Corporation (Client)
and XYZ Services LLC (Vendor) for $1.2M total value. The agreement provides for monthly
payments of $50,000 with automatic renewal and 3% annual price increases. Overall risk
level is medium, with some concerns around liability caps and IP rights that should be
addressed before signing.
            """.strip(),

            "key_highlights": [
                "24-month initial term with automatic renewal",
                "$50,000 monthly fixed fee ($1.2M total)",
                "99.5% uptime SLA with limited remedies",
                "Client owns deliverables, vendor retains improvements",
                "90-day termination notice required"
            ],

            "financial_summary": {
                "total_value": "$1,200,000",
                "payment_terms": "Monthly, net 30",
                "price_increases": "3% annually after year 1",
                "expenses": "Pre-approved only"
            },

            "critical_dates": [
                "2024-01-15: Effective date",
                "2024-02-01: First payment due",
                "2025-10-15: Renewal notice deadline",
                "2026-01-14: Initial term ends"
            ],

            "recommendation": "PROCEED WITH MODIFICATIONS - Negotiate liability cap increase and clarify IP ownership before signing"
        }

        return json.dumps(summary, indent=2)

    @tool("Highlight Key Points")
    def highlight_key_points(document_text: str) -> str:
        """
        Highlights most important points from document.
        Useful for quick review.
        """
        key_points = {
            "must_know": [
                "Contract automatically renews unless 90 days notice given before expiration",
                "Liability limited to 12 months of fees paid (potential risk for major issues)",
                "All custom code developed becomes client property",
                "99.5% uptime guarantee with service credits for breaches",
                "90-day termination notice required even for convenience termination"
            ],
            "financial_commitments": [
                "$50,000 monthly payment (total $1.2M over 2 years)",
                "3% annual price increase allowed after first year",
                "Late payment fees of 1.5% per month",
                "Client responsible for all approved expenses"
            ],
            "important_restrictions": [
                "90-day notice required for termination",
                "Confidentiality obligations extend 5 years post-termination",
                "Non-compete with vendor's other clients in same industry",
                "Cannot assign contract without vendor consent"
            ],
            "your_key_rights": [
                "Terminate for material breach with 30-day cure period",
                "Service credits for SLA failures",
                "Ownership of all deliverables and custom work",
                "Annual audit rights for compliance verification"
            ],
            "watch_out_for": [
                "Automatic renewal with price increase",
                "Limited liability protection",
                "Broad definition of confidential information",
                "Vendor can modify terms with 30 days notice"
            ]
        }

        return json.dumps(key_points, indent=2)


class ComplianceTools:
    @tool("Check Regulatory Compliance")
    def check_regulatory_compliance(document_text: str) -> str:
        """
        Checks document for regulatory compliance requirements.
        Useful for ensuring legal compliance.
        """
        compliance_check = {
            "applicable_regulations": [
                "GDPR (EU data protection)",
                "CCPA (California privacy)",
                "SOC 2 (Security compliance)",
                "Contract law (New York)"
            ],
            "compliance_status": {
                "GDPR": {
                    "status": "compliant",
                    "requirements_met": [
                        "Data processing agreement included",
                        "Data subject rights addressed",
                        "Cross-border transfer mechanisms",
                        "Breach notification procedures"
                    ],
                    "gaps": [
                        "Could strengthen data retention policies"
                    ]
                },
                "CCPA": {
                    "status": "mostly_compliant",
                    "requirements_met": [
                        "Consumer rights disclosure",
                        "Do not sell provision"
                    ],
                    "gaps": [
                        "Need explicit opt-out mechanism",
                        "Add consumer request procedures"
                    ]
                },
                "SOC2": {
                    "status": "compliant",
                    "requirements_met": [
                        "Security controls referenced",
                        "Audit rights granted",
                        "Incident response procedures"
                    ],
                    "gaps": []
                },
                "Contract_Law": {
                    "status": "compliant",
                    "requirements_met": [
                        "Mutual consideration present",
                        "Legal capacity assumed",
                        "Lawful purpose",
                        "Proper execution provisions"
                    ],
                    "gaps": []
                }
            },
            "overall_compliance_score": "85%",
            "priority_fixes": [
                "Add CCPA opt-out mechanism (High priority)",
                "Strengthen data retention language (Medium priority)"
            ]
        }

        return json.dumps(compliance_check, indent=2)

    @tool("Verify Standard Clauses")
    def verify_standard_clauses(document_text: str) -> str:
        """
        Verifies presence of standard legal clauses.
        Useful for ensuring complete contracts.
        """
        clause_verification = {
            "standard_clauses_present": [
                {
                    "clause": "Entire Agreement",
                    "present": True,
                    "section": "15.1",
                    "adequacy": "standard"
                },
                {
                    "clause": "Severability",
                    "present": True,
                    "section": "15.3",
                    "adequacy": "standard"
                },
                {
                    "clause": "Force Majeure",
                    "present": True,
                    "section": "13.5",
                    "adequacy": "comprehensive"
                },
                {
                    "clause": "Governing Law",
                    "present": True,
                    "section": "12.3",
                    "adequacy": "standard"
                },
                {
                    "clause": "Assignment",
                    "present": True,
                    "section": "15.4",
                    "adequacy": "standard"
                },
                {
                    "clause": "Notices",
                    "present": True,
                    "section": "15.5",
                    "adequacy": "comprehensive"
                },
                {
                    "clause": "Waiver",
                    "present": True,
                    "section": "15.2",
                    "adequacy": "standard"
                },
                {
                    "clause": "Amendment",
                    "present": True,
                    "section": "15.6",
                    "adequacy": "weak - allows unilateral changes"
                }
            ],
            "missing_clauses": [
                "Survival clause (should specify which terms survive termination)",
                "Counterparts clause (for electronic execution)"
            ],
            "inadequate_clauses": [
                {
                    "clause": "Amendment",
                    "issue": "Allows vendor to unilaterally modify terms",
                    "recommendation": "Require mutual written consent for amendments"
                }
            ]
        }

        return json.dumps(clause_verification, indent=2)

    @tool("Identify Missing Provisions")
    def identify_missing_provisions(document_text: str) -> str:
        """
        Identifies provisions that should be added to the document.
        Useful for completing contracts.
        """
        missing_provisions = {
            "critical_missing": [
                {
                    "provision": "Data Breach Notification",
                    "importance": "critical",
                    "description": "Should specify timeframe for breach notification (e.g., 72 hours)",
                    "recommended_language": "Vendor must notify Client within 72 hours of discovering any data breach"
                },
                {
                    "provision": "Audit Rights",
                    "importance": "critical",
                    "description": "Client should have right to audit vendor's security practices",
                    "recommended_language": "Client may audit vendor's facilities and practices annually with 30 days notice"
                }
            ],
            "recommended_additions": [
                {
                    "provision": "Background Checks",
                    "importance": "high",
                    "description": "Require background checks for personnel with data access"
                },
                {
                    "provision": "Subcontractor Restrictions",
                    "importance": "high",
                    "description": "Clarify vendor's right to use subcontractors and client approval rights"
                },
                {
                    "provision": "Service Credits",
                    "importance": "medium",
                    "description": "Define specific credits or refunds for SLA breaches"
                },
                {
                    "provision": "Transition Assistance",
                    "importance": "medium",
                    "description": "Require vendor to assist with transition upon termination"
                }
            ],
            "nice_to_have": [
                {
                    "provision": "Key Personnel",
                    "description": "Name key personnel and require approval for replacements"
                },
                {
                    "provision": "Continuous Improvement",
                    "description": "Regular reviews and improvement initiatives"
                },
                {
                    "provision": "Disaster Recovery",
                    "description": "Detailed disaster recovery and business continuity plans"
                }
            ]
        }

        return json.dumps(missing_provisions, indent=2)
