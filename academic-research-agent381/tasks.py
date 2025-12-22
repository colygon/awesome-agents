"""
Academic Research CrewAI Tasks
Defines the workflow for analyzing seminal papers and proposing research directions
"""

from crewai import Task
from agents import document_analyzer, citation_researcher, future_research_synthesizer

def create_tasks(seminal_paper_path: str):
    """
    Create tasks for academic research workflow

    Args:
        seminal_paper_path: Path to the seminal paper PDF

    Returns:
        List of Task objects
    """

    # Task 1: Analyze the seminal paper
    analyze_paper_task = Task(
        description=f"""Analyze the seminal paper provided at {seminal_paper_path}.

        Extract and present the following information:
        1. Seminal Paper: Title, Primary Author(s), Publication Year
        2. Authors: List all authors with affiliations if available
        3. Abstract: Full abstract text
        4. Summary: Concise narrative summary (5-10 sentences) covering core arguments,
           methodology, and findings
        5. Key Topics/Keywords: Main topics or keywords from the paper
        6. Key Innovations: Up to 5 key innovations or novel contributions (bulleted list)
        7. References Cited Within Seminal Paper: Extract bibliography/references section

        Provide a comprehensive analysis that will serve as the foundation for finding
        recent citing papers and identifying future research directions.""",
        agent=document_analyzer,
        expected_output="""A structured analysis containing:
        - Paper metadata (title, authors, year)
        - Complete author list with affiliations
        - Full abstract
        - Narrative summary (5-10 sentences)
        - List of key topics/keywords
        - Bulleted list of 5 key innovations
        - Complete reference list from the paper"""
    )

    # Task 2: Find recent citing papers
    find_citations_task = Task(
        description="""Based on the seminal paper analysis, find recent academic papers
        that cite this work.

        Requirements:
        1. Search for papers published in the current year (2025) and previous year (2024)
        2. Aim to find at least 10 distinct citing papers for each year (20 total minimum)
        3. Use varied search strategies:
           - Different phrasings: "cited by", "references", "based on the work of"
           - Use paper title, DOI, and author names
           - Search academic databases: scholar.google.com, arxiv.org, ieee.org, acm.org
        4. Verify that papers genuinely cite the seminal work
        5. Discard duplicates and low-confidence results

        For each paper found, provide:
        - Title
        - Author(s)
        - Publication Year (2024 or 2025)
        - Source (Journal/Conference/Repository)
        - Link (DOI or URL)

        Group results by year (2025 first, then 2024).""",
        agent=citation_researcher,
        expected_output="""A comprehensive list of recent citing papers grouped by year,
        with each paper including: title, authors, year, source, and link. Include count
        of papers found for each year.""",
        context=[analyze_paper_task]
    )

    # Task 3: Propose future research directions
    propose_research_task = Task(
        description="""Based on the seminal paper analysis and recent citing papers,
        identify and propose future research directions.

        Requirements:
        1. Generate at least 10 distinct future research areas
        2. Each area must demonstrate:
           - Novelty: Addresses gaps not yet adequately explored
           - Future Potential: High impact, influential, or disruptive potential
        3. Ensure diversity across:
           - High Potential Utility (practical applications, real-world benefits)
           - Unexpectedness/Paradigm Shift (challenges assumptions, unconventional)
           - Emerging Popularity (aligns with trends, timely questions)

        For each research area, provide:
        - Clear, concise Title or Theme
        - Brief Rationale (2-4 sentences) explaining:
          * What the research involves
          * Why it's novel or underexplored
          * Why it holds significant future potential

        (Optional) Include a "Potentially Relevant Authors" section listing authors
        from the seminal or recent papers whose expertise aligns with proposed areas.""",
        agent=future_research_synthesizer,
        expected_output="""A numbered list of at least 10 future research areas, each with:
        - Title/Theme
        - Rationale (2-4 sentences covering what, why novel, why impactful)
        Optionally include relevant authors section.""",
        context=[analyze_paper_task, find_citations_task]
    )

    return [analyze_paper_task, find_citations_task, propose_research_task]
