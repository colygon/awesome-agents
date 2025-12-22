#!/usr/bin/env python
from crewai import Crew, Process
from agents import LegalDocumentAnalyzerAgents
from tasks import LegalDocumentAnalyzerTasks
from dotenv import load_dotenv

load_dotenv()

def run_legal_document_analyzer():
    """
    Run the Legal Document Analyzer crew to analyze contracts and legal documents
    """
    print("## Welcome to the Legal Document Analyzer Crew")
    print("-----------------------------------------------")

    # Get user input for document analysis
    document_type = input("What type of document? (e.g., contract, NDA, employment agreement): ")
    document_name = input("Document name or title: ")
    analysis_purpose = input("Purpose of analysis? (e.g., review before signing, compliance check): ")

    document_info = f"""
    Document Type: {document_type}
    Document Name: {document_name}
    Analysis Purpose: {analysis_purpose}
    Analysis Date: {input("Analysis date (YYYY-MM-DD): ")}
    """

    # Sample document data (in production, this would be loaded from actual document)
    contract_data = """
    Software Development Services Agreement between parties
    with various terms, obligations, and conditions
    """

    document_data = f"""
    Document: {document_name}
    Type: {document_type}
    """

    full_analysis = """
    Comprehensive analysis including parsing, contract analysis, and compliance check
    """

    # Initialize agents
    agents = LegalDocumentAnalyzerAgents()
    tasks_manager = LegalDocumentAnalyzerTasks()

    # Create agents
    document_parser = agents.document_parser()
    contract_analyzer = agents.contract_analyzer()
    compliance_checker = agents.compliance_checker()
    legal_summarizer = agents.legal_summarizer()

    # Create tasks
    parsing_task = tasks_manager.parse_document(
        document_parser,
        document_info
    )

    analysis_task = tasks_manager.analyze_contract(
        contract_analyzer,
        contract_data
    )

    compliance_task = tasks_manager.check_compliance(
        compliance_checker,
        document_data
    )

    summary_task = tasks_manager.create_summary(
        legal_summarizer,
        full_analysis
    )

    # Optional comparison task
    compare_documents = input("Do you want to compare with another document? (yes/no): ").lower()
    tasks = [parsing_task, analysis_task, compliance_task, summary_task]

    if compare_documents == 'yes':
        other_document = input("Enter the other document name: ")
        comparison_task = tasks_manager.generate_comparison(
            legal_summarizer,
            f"{document_name} vs {other_document}"
        )
        tasks.append(comparison_task)

    # Create and run crew
    crew = Crew(
        agents=[
            document_parser,
            contract_analyzer,
            compliance_checker,
            legal_summarizer
        ],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Legal Document Analysis Results")
    print("########################\n")
    print(result)

    return result


if __name__ == "__main__":
    run_legal_document_analyzer()
