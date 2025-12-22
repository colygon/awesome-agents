"""
Academic Research Assistant CrewAI Tasks
Defines the workflow for research assistance
"""

from crewai import Task
from agents import (
    literature_searcher,
    paper_summarizer,
    citation_manager,
    literature_synthesizer,
    research_question_developer
)


def create_tasks(research_topic: str, num_papers: int = 15):
    """
    Create tasks for academic research workflow

    Args:
        research_topic: The research topic or question
        num_papers: Number of papers to find and analyze

    Returns:
        List of Task objects
    """

    # Task 1: Search for Relevant Literature
    search_literature_task = Task(
        description=f"""Search for relevant academic literature on: {research_topic}

        Search Strategy:
        1. Identify key search terms and synonyms
        2. Search across multiple databases:
           - Google Scholar
           - PubMed (if health/life sciences related)
           - arXiv (if computer science/physics/math)
           - IEEE Xplore (if engineering/technology)
           - ACM Digital Library (if computer science)
        3. Use advanced search techniques (Boolean operators, phrase search, field search)
        4. Find at least {num_papers} highly relevant papers
        5. Prioritize recent papers (last 5 years) but include seminal older works
        6. Consider paper quality indicators:
           - Citation count
           - Journal/conference reputation
           - Author credentials
           - Peer-review status

        For each paper found, provide:
        - Title
        - Author(s)
        - Publication year
        - Source (journal/conference)
        - DOI or URL
        - Citation count
        - Brief relevance note (one sentence)

        Organize papers by relevance and recency.""",
        agent=literature_searcher,
        expected_output=f"""List of {num_papers}+ relevant papers including:
        - Complete bibliographic information
        - Citation metrics
        - Relevance notes
        - Access links (DOI/URL)
        Organized by relevance to research topic"""
    )

    # Task 2: Summarize Key Papers
    summarize_papers_task = Task(
        description=f"""Analyze and summarize the most relevant papers found on {research_topic}.

        For the top 10 most relevant papers, create detailed summaries including:

        For EACH paper:
        1. OVERVIEW:
           - Full citation
           - Research question/objective
           - Significance/motivation

        2. METHODOLOGY:
           - Research design (experimental, survey, case study, meta-analysis, etc.)
           - Data collection methods
           - Sample size and characteristics
           - Analysis techniques

        3. KEY FINDINGS:
           - Main results (with data/statistics if available)
           - Important discoveries or contributions
           - Supporting evidence

        4. CONCLUSIONS:
           - Authors' interpretations
           - Theoretical contributions
           - Practical implications

        5. LIMITATIONS:
           - Acknowledged limitations
           - Potential weaknesses in methodology
           - Gaps left unaddressed

        6. RELEVANCE:
           - How it relates to {research_topic}
           - How it connects to other papers
           - Unique contribution to the field

        Create summaries that are:
        - Comprehensive yet concise (300-500 words each)
        - Technically accurate
        - Easy to understand
        - Focused on insights relevant to {research_topic}""",
        agent=paper_summarizer,
        expected_output="""Detailed summaries of top 10 papers, each including:
        - Overview and research question
        - Methodology description
        - Key findings with data
        - Conclusions and implications
        - Limitations and gaps
        - Relevance to research topic""",
        context=[search_literature_task]
    )

    # Task 3: Generate Citations and Bibliography
    citations_task = Task(
        description=f"""Create properly formatted citations for all papers found on {research_topic}.

        Requirements:
        1. Generate citations in multiple formats:
           - APA 7th edition
           - MLA 9th edition
           - Chicago 17th edition
           - IEEE style

        2. Organize bibliography:
           - Alphabetically by first author
           - Properly formatted with hanging indents
           - Include DOI links where available

        3. Create in-text citation examples:
           - Show how to cite each paper in-text
           - Include page numbers for quotes
           - Demonstrate multiple authors format

        4. Export-ready formats:
           - Plain text
           - BibTeX format for LaTeX users
           - EndNote/Zotero compatible format

        5. Citation quality check:
           - Verify all required fields present
           - Check for formatting consistency
           - Ensure DOI/URL accuracy

        Provide organized reference list ready for use in academic writing.""",
        agent=citation_manager,
        expected_output="""Complete citation package including:
        - Full bibliography in APA, MLA, Chicago, and IEEE formats
        - In-text citation examples
        - BibTeX entries
        - EndNote/Zotero compatible references
        - Citation quick reference guide""",
        context=[search_literature_task, summarize_papers_task]
    )

    # Task 4: Synthesize Literature Review
    literature_review_task = Task(
        description=f"""Create a comprehensive literature review on {research_topic}.

        Synthesize the analyzed papers into a coherent narrative:

        1. INTRODUCTION:
           - Define the research topic
           - Explain its significance and relevance
           - Preview the structure of the review

        2. THEMATIC ORGANIZATION:
           - Identify 3-5 major themes or categories
           - Group papers by theme
           - For each theme:
             * Summarize key findings across papers
             * Note points of agreement
             * Highlight contradictions or debates
             * Show how research has evolved

        3. METHODOLOGICAL REVIEW:
           - Common methodological approaches
           - Strengths and limitations of different methods
           - Methodological gaps

        4. THEORETICAL FRAMEWORKS:
           - Dominant theories or models
           - How different studies build on each other
           - Theoretical debates or competing perspectives

        5. KEY FINDINGS SYNTHESIS:
           - What we know: consensus findings
           - What remains unclear: contradictions
           - What's missing: research gaps

        6. CRITICAL ANALYSIS:
           - Strengths of current research
           - Limitations across the literature
           - Biases or blind spots

        7. FUTURE DIRECTIONS:
           - Identified research gaps
           - Emerging trends
           - Recommended future studies

        Create a literature review that:
        - Is well-organized and flows logically
        - Demonstrates critical thinking
        - Integrates sources rather than just listing them
        - Identifies clear patterns and gaps
        - Provides foundation for future research
        - Is approximately 2000-3000 words""",
        agent=literature_synthesizer,
        expected_output="""Comprehensive literature review (2000-3000 words) including:
        - Introduction to the topic
        - Thematic organization of existing research
        - Methodological and theoretical analysis
        - Synthesis of key findings
        - Critical analysis of the literature
        - Identified gaps and future directions""",
        context=[search_literature_task, summarize_papers_task, citations_task]
    )

    # Task 5: Develop Research Questions
    research_questions_task = Task(
        description=f"""Based on the literature review, develop focused research questions for {research_topic}.

        Requirements:

        1. IDENTIFY GAPS:
           - What hasn't been studied?
           - What contradictions need resolution?
           - What populations/contexts are underrepresented?
           - What methodologies haven't been applied?
           - What theoretical perspectives are missing?

        2. GENERATE RESEARCH QUESTIONS:
           - Create 5-7 potential research questions
           - Each should address a specific gap
           - Questions should be:
             * Specific and focused
             * Researchable with available methods
             * Significant and contributing to the field
             * Original and novel
             * Clearly stated

        3. FOR EACH QUESTION PROVIDE:
           - The research question statement
           - Rationale (why this is important)
           - Related gap in literature
           - Potential methodology (how to study it)
           - Expected contribution (theoretical/practical)
           - Feasibility assessment (resources, time, access)

        4. PRIORITIZE QUESTIONS:
           - Rank questions by:
             * Significance/impact
             * Feasibility
             * Novelty
             * Your interest/passion
           - Recommend top 2-3 questions to pursue

        5. DEVELOP HYPOTHESES:
           - For quantitative-leaning questions, suggest testable hypotheses
           - Include null and alternative hypotheses
           - Base on theoretical frameworks from literature

        6. RESEARCH DESIGN SKETCH:
           - For top 2 questions, outline potential research design
           - Suggested methods (qualitative/quantitative/mixed)
           - Data collection approaches
           - Analysis techniques
           - Timeline estimate

        Help the researcher move from literature review to actionable research plan.""",
        agent=research_question_developer,
        expected_output="""Research question development package including:
        - 5-7 potential research questions with full details
        - Gap analysis for each question
        - Methodology suggestions
        - Feasibility assessments
        - Prioritized recommendations
        - Hypotheses for top questions
        - Research design sketches for top 2 questions""",
        context=[search_literature_task, summarize_papers_task, literature_review_task]
    )

    return [
        search_literature_task,
        summarize_papers_task,
        citations_task,
        literature_review_task,
        research_questions_task
    ]
