"""
Custom Tools for Academic Research
Provides PDF analysis, web search, and citation finding capabilities
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI


class PDFAnalysisInput(BaseModel):
    """Input schema for PDFAnalysisTool"""
    pdf_path: str = Field(..., description="Path to the PDF file to analyze")


class PDFAnalysisTool(BaseTool):
    name: str = "PDF Analysis Tool"
    description: str = """Analyzes academic papers in PDF format. Extracts title, authors,
    abstract, key contributions, methodology, and references. Returns structured information
    about the paper."""
    args_schema: Type[BaseModel] = PDFAnalysisInput

    def _run(self, pdf_path: str) -> str:
        """
        Analyze a PDF file and extract academic paper information

        Args:
            pdf_path: Path to the PDF file

        Returns:
            Structured analysis of the paper
        """
        try:
            # Load PDF
            loader = PyPDFLoader(pdf_path)
            pages = loader.load()

            # Combine all pages
            full_text = "\n\n".join([page.page_content for page in pages])

            # Use LLM to extract structured information
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

            prompt = f"""Analyze this academic paper and extract the following information:

1. Title
2. All authors with affiliations (if available)
3. Publication year
4. Full abstract
5. 5-10 sentence summary of core arguments, methodology, and findings
6. Key topics and keywords
7. Top 5 key innovations or contributions
8. Complete reference list

Paper content:
{full_text[:15000]}  # Limit to avoid token limits

Provide a well-structured response with clear sections."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing PDF: {str(e)}"


class WebSearchInput(BaseModel):
    """Input schema for WebSearchTool"""
    query: str = Field(..., description="Search query to execute")


class WebSearchTool(BaseTool):
    name: str = "Web Search Tool"
    description: str = """Performs web searches to find academic papers and citations.
    Useful for finding papers on Google Scholar, arXiv, IEEE, ACM, and other academic sources."""
    args_schema: Type[BaseModel] = WebSearchInput

    def _run(self, query: str) -> str:
        """
        Perform a web search using a search API or service

        Args:
            query: Search query string

        Returns:
            Search results as formatted string
        """
        try:
            # Note: In production, integrate with actual search APIs like:
            # - Google Custom Search API
            # - Serper API
            # - SerpAPI
            # For this example, we'll return a placeholder

            # Check if SERPER_API_KEY is available
            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                # Use Serper API for actual searches
                url = "https://google.serper.dev/search"
                payload = {"q": query, "num": 10}
                headers = {
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json"
                }

                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    results = response.json()
                    # Format results
                    formatted = []
                    for item in results.get("organic", [])[:10]:
                        formatted.append(f"Title: {item.get('title')}\nLink: {item.get('link')}\nSnippet: {item.get('snippet')}\n")
                    return "\n".join(formatted)

            # Fallback: Return guidance for manual search
            return f"""To find papers for query: {query}

Suggested search strategies:
1. Google Scholar: scholar.google.com - "{query}"
2. arXiv: arxiv.org - search for "{query}"
3. IEEE Xplore: ieeexplore.ieee.org - "{query}"
4. ACM Digital Library: dl.acm.org - "{query}"

Note: For production use, integrate with Google Custom Search API, Serper API, or SerpAPI by setting SERPER_API_KEY environment variable."""

        except Exception as e:
            return f"Error performing search: {str(e)}"


class CitationFinderInput(BaseModel):
    """Input schema for CitationFinderTool"""
    paper_title: str = Field(..., description="Title of the paper to find citations for")
    year: int = Field(..., description="Year to search for citations (e.g., 2024 or 2025)")


class CitationFinderTool(BaseTool):
    name: str = "Citation Finder Tool"
    description: str = """Finds academic papers that cite a specific paper. Searches for
    recent citations published in a specific year. Returns paper title, authors, year, source, and link."""
    args_schema: Type[BaseModel] = CitationFinderInput

    def _run(self, paper_title: str, year: int) -> str:
        """
        Find papers that cite a specific work

        Args:
            paper_title: Title of the paper to find citations for
            year: Year to filter citations

        Returns:
            List of citing papers
        """
        try:
            # Construct search queries
            queries = [
                f'"{paper_title}" cited by year:{year}',
                f'papers citing "{paper_title}" published {year}',
                f'"{paper_title}" references {year}'
            ]

            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                all_results = []
                url = "https://google.serper.dev/search"
                headers = {
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json"
                }

                for query in queries[:2]:  # Try first 2 queries
                    payload = {"q": query, "num": 10}
                    response = requests.post(url, json=payload, headers=headers)

                    if response.status_code == 200:
                        results = response.json()
                        for item in results.get("organic", []):
                            all_results.append(
                                f"Title: {item.get('title')}\n"
                                f"Link: {item.get('link')}\n"
                                f"Snippet: {item.get('snippet')}\n"
                            )

                return "\n".join(all_results) if all_results else f"No citations found for {year}"

            # Fallback guidance
            return f"""Search for citations of "{paper_title}" published in {year}:

Try these searches:
1. Google Scholar: scholar.google.com - 'cited by "{paper_title}" year:{year}'
2. Semantic Scholar: semanticscholar.org - search for paper and view citations filtered by {year}
3. Web of Science / Scopus - if you have access

Note: Set SERPER_API_KEY environment variable for automated searches."""

        except Exception as e:
            return f"Error finding citations: {str(e)}"
