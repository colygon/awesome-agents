from crewai import Agent
from tools import DocumentParsingTools, AnalysisTools, ComplianceTools

class LegalDocumentAnalyzerAgents:
    def document_parser(self):
        return Agent(
            role='Legal Document Parser',
            goal='Extract and structure information from legal documents',
            backstory="""You are an expert in parsing legal documents and extracting
            structured information. You understand legal document formats, clauses,
            and can identify key sections like parties, terms, obligations, and
            dates. You excel at converting unstructured legal text into organized,
            analyzable data.""",
            tools=[
                DocumentParsingTools.extract_parties,
                DocumentParsingTools.extract_dates,
                DocumentParsingTools.identify_clauses
            ],
            verbose=True,
            allow_delegation=False
        )

    def contract_analyzer(self):
        return Agent(
            role='Contract Analyzer',
            goal='Analyze contract terms, obligations, and potential risks',
            backstory="""You are a seasoned contract analyst who reviews agreements
            to identify key terms, obligations, rights, and potential risks. You
            understand different contract types, standard clauses, and can spot
            unusual or unfavorable terms. You provide clear summaries of complex
            legal language.""",
            tools=[
                AnalysisTools.analyze_terms,
                AnalysisTools.identify_obligations,
                AnalysisTools.assess_risks
            ],
            verbose=True,
            allow_delegation=False
        )

    def compliance_checker(self):
        return Agent(
            role='Compliance Checker',
            goal='Verify legal documents meet regulatory and compliance requirements',
            backstory="""You are a compliance specialist who ensures legal documents
            meet regulatory requirements and industry standards. You understand
            GDPR, data privacy laws, employment regulations, and contract law. You
            identify potential compliance issues and recommend necessary updates.""",
            tools=[
                ComplianceTools.check_regulatory_compliance,
                ComplianceTools.verify_standard_clauses,
                ComplianceTools.identify_missing_provisions
            ],
            verbose=True,
            allow_delegation=False
        )

    def legal_summarizer(self):
        return Agent(
            role='Legal Summarizer',
            goal='Create clear, concise summaries of legal documents for non-legal audiences',
            backstory="""You are an expert at translating complex legal language
            into plain English summaries. You understand what information is most
            important for different stakeholders and can create executive summaries,
            risk assessments, and action item lists from legal documents.""",
            tools=[
                AnalysisTools.create_executive_summary,
                AnalysisTools.highlight_key_points,
                DocumentParsingTools.generate_comparison
            ],
            verbose=True,
            allow_delegation=False
        )
