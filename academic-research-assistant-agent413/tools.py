"""
Custom Tools for Academic Research
Provides literature search, paper summarization, and citation management
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests
from langchain_openai import ChatOpenAI


class LiteratureSearchInput(BaseModel):
    """Input schema for LiteratureSearchTool"""
    query: str = Field(..., description="Search query for academic literature")
    num_results: int = Field(default=15, description="Number of results to return")


class LiteratureSearchTool(BaseTool):
    name: str = "Literature Search Tool"
    description: str = """Searches academic databases for relevant papers. Finds papers
    on Google Scholar, PubMed, arXiv, and other sources. Returns paper titles, authors,
    citations, and links."""
    args_schema: Type[BaseModel] = LiteratureSearchInput

    def _run(self, query: str, num_results: int = 15) -> str:
        """
        Search for academic literature

        Args:
            query: Search query
            num_results: Number of results

        Returns:
            List of relevant papers
        """
        try:
            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                # Search Google Scholar via Serper
                url = "https://google.serper.dev/scholar"
                headers = {
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json"
                }
                payload = {"q": query, "num": num_results}

                response = requests.post(url, json=payload, headers=headers)

                if response.status_code == 200:
                    results = response.json()
                    papers = []

                    for item in results.get("organic", []):
                        paper = f"""Title: {item.get('title')}
Authors: {item.get('publication_info', {}).get('authors', 'N/A')}
Year: {item.get('publication_info', {}).get('summary', 'N/A')}
Cited by: {item.get('inline_links', {}).get('cited_by', {}).get('total', 0)}
Link: {item.get('link')}
Snippet: {item.get('snippet', '')}
---"""
                        papers.append(paper)

                    return "\n".join(papers) if papers else "No papers found"

            # Fallback: Provide search guidance
            return f"""To search for papers on: {query}

Recommended search strategies:

1. GOOGLE SCHOLAR (scholar.google.com):
   Search: "{query}"
   - Use quotes for exact phrases
   - Use AND, OR, NOT for Boolean logic
   - Sort by relevance or date
   - Check "Cited by" for related papers

2. PUBMED (pubmed.ncbi.nlm.nih.gov) - if health/life sciences:
   Search: "{query}"
   - Use MeSH terms for precision
   - Use filters: publication date, article type
   - Export citations

3. ARXIV (arxiv.org) - if CS/Physics/Math:
   Search: "{query}"
   - Browse by category
   - Check recent submissions
   - Download PDFs directly

4. IEEE XPLORE (ieeexplore.ieee.org) - if engineering/tech:
   Search: "{query}"
   - Use advanced search
   - Filter by conferences/journals

5. ACM DIGITAL LIBRARY (dl.acm.org) - if computer science:
   Search: "{query}"
   - Browse by topic
   - Check proceedings

Search Tips:
- Start broad, then refine
- Check citation chains (forward and backward)
- Look for review papers first
- Note highly cited papers
- Verify peer-review status

Note: Set SERPER_API_KEY for automated searches."""

        except Exception as e:
            return f"Error searching literature: {str(e)}"


class PaperSummarizerInput(BaseModel):
    """Input schema for PaperSummarizerTool"""
    paper_text: str = Field(..., description="Text content of the paper to summarize")


class PaperSummarizerTool(BaseTool):
    name: str = "Paper Summarizer Tool"
    description: str = """Analyzes and summarizes academic papers. Extracts research
    questions, methodology, findings, and conclusions. Returns structured summary."""
    args_schema: Type[BaseModel] = PaperSummarizerInput

    def _run(self, paper_text: str) -> str:
        """
        Summarize an academic paper

        Args:
            paper_text: Full or partial text of paper

        Returns:
            Structured summary
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

            prompt = f"""Analyze this academic paper and create a comprehensive summary:

Paper content:
{paper_text[:12000]}

Create a structured summary with these sections:

1. OVERVIEW
   - Full citation (if extractable)
   - Research question/objective
   - Significance

2. METHODOLOGY
   - Research design
   - Data collection
   - Sample/participants
   - Analysis methods

3. KEY FINDINGS
   - Main results (with statistics if available)
   - Important discoveries
   - Supporting evidence

4. CONCLUSIONS
   - Authors' interpretations
   - Theoretical contributions
   - Practical implications

5. LIMITATIONS
   - Acknowledged limitations
   - Methodological weaknesses
   - Unaddressed gaps

6. CONTRIBUTION
   - Novel contribution to field
   - How it advances knowledge
   - Relevance to current research

Make the summary:
- Comprehensive yet concise (300-500 words)
- Technically accurate
- Well-structured
- Focused on key insights"""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error summarizing paper: {str(e)}"


class CitationInput(BaseModel):
    """Input schema for CitationManagerTool"""
    paper_info: str = Field(..., description="Paper information to format as citation")
    style: str = Field(default="APA", description="Citation style: APA, MLA, Chicago, or IEEE")


class CitationManagerTool(BaseTool):
    name: str = "Citation Manager Tool"
    description: str = """Formats citations in various academic styles (APA, MLA, Chicago, IEEE).
    Creates bibliographies and in-text citations. Returns properly formatted citations."""
    args_schema: Type[BaseModel] = CitationInput

    def _run(self, paper_info: str, style: str = "APA") -> str:
        """
        Format citations for papers

        Args:
            paper_info: Paper details
            style: Citation style

        Returns:
            Formatted citations
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

            prompt = f"""Format this paper information as a citation in {style} style.

Paper information:
{paper_info}

Provide:

1. FULL REFERENCE (bibliography entry):
   - Properly formatted for {style} style
   - All required elements (author, year, title, source, etc.)
   - Correct punctuation and formatting
   - DOI or URL if available

2. IN-TEXT CITATION examples:
   - Parenthetical citation
   - Narrative citation
   - Multiple authors format
   - Quote citation (with page number placeholder)

3. BIBTEX entry (for LaTeX users):
   - Complete BibTeX format
   - Appropriate entry type (@article, @inproceedings, etc.)

4. NOTES:
   - Any missing information
   - Formatting notes

Follow {style} style guidelines precisely.
Common styles:
- APA: Author, A. A. (Year). Title. Journal, Volume(Issue), pages. DOI
- MLA: Author. "Title." Journal, vol. Volume, no. Issue, Year, pages.
- Chicago: Author. "Title." Journal Volume, no. Issue (Year): pages.
- IEEE: [1] A. Author, "Title," Journal, vol. Volume, no. Issue, pp. pages, Year."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error formatting citation: {str(e)}"
