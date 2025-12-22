from crewai import Task
from textwrap import dedent

class LegalDocumentAnalyzerTasks:
    def parse_document(self, agent, document_info):
        return Task(
            description=dedent(f"""
                Parse and extract structured information from the legal document:

                Document Information:
                {document_info}

                Your tasks:
                1. Identify document type and purpose
                2. Extract all parties involved (names, roles, addresses)
                3. Identify all important dates (effective date, expiration, deadlines)
                4. Extract financial terms (amounts, payment schedules)
                5. Identify key clauses and sections
                6. Create structured data representation of the document
                7. Note any incomplete or missing information

                Provide a structured document analysis.
            """),
            agent=agent,
            expected_output="Structured document data with parties, dates, financial terms, and key clauses extracted"
        )

    def analyze_contract(self, agent, contract_data):
        return Task(
            description=dedent(f"""
                Analyze the contract terms and identify key obligations and risks:

                Contract Data:
                {contract_data}

                Your tasks:
                1. Summarize main terms and conditions
                2. Identify obligations for each party
                3. Analyze payment terms and conditions
                4. Review termination and renewal clauses
                5. Identify liability and indemnification provisions
                6. Assess intellectual property rights
                7. Flag potentially unfavorable or unusual terms
                8. Identify areas requiring negotiation or clarification

                Provide comprehensive contract analysis.
            """),
            agent=agent,
            expected_output="Detailed contract analysis with terms, obligations, risks, and negotiation points"
        )

    def check_compliance(self, agent, document_data):
        return Task(
            description=dedent(f"""
                Verify compliance with relevant regulations and standards:

                Document Data:
                {document_data}

                Your tasks:
                1. Identify applicable regulations and laws
                2. Check for required legal clauses
                3. Verify data privacy and GDPR compliance (if applicable)
                4. Review employment law compliance (for HR documents)
                5. Check for industry-specific requirements
                6. Identify missing or inadequate provisions
                7. Flag potential compliance risks
                8. Recommend necessary updates or additions

                Provide compliance assessment report.
            """),
            agent=agent,
            expected_output="Compliance report with regulatory requirements, gaps, and recommendations"
        )

    def create_summary(self, agent, full_analysis):
        return Task(
            description=dedent(f"""
                Create executive summary and plain-language explanation:

                Full Analysis:
                {full_analysis}

                Your tasks:
                1. Write 2-3 paragraph executive summary
                2. Highlight top 5 most important points
                3. List key obligations and deadlines
                4. Summarize financial commitments
                5. Present risk assessment in plain language
                6. Create action items checklist
                7. Prepare stakeholder-specific summaries
                8. Include FAQ section for common questions

                Provide comprehensive summary package.
            """),
            agent=agent,
            expected_output="Executive summary with key points, obligations, risks, and action items in plain language"
        )

    def generate_comparison(self, agent, documents_to_compare):
        return Task(
            description=dedent(f"""
                Compare multiple legal documents and identify differences:

                Documents to Compare:
                {documents_to_compare}

                Your tasks:
                1. Identify structural differences between documents
                2. Compare key terms and conditions
                3. Highlight variations in obligations
                4. Compare financial terms
                5. Identify missing clauses in any version
                6. Flag inconsistencies or contradictions
                7. Recommend which version or terms are more favorable
                8. Create side-by-side comparison table

                Provide detailed comparison analysis.
            """),
            agent=agent,
            expected_output="Document comparison with differences, inconsistencies, and recommendations"
        )
