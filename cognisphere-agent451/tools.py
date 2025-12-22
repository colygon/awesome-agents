"""
Custom Tools for Cognisphere
Provides knowledge graph construction, semantic search, and concept analysis
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import os
import requests
from langchain_openai import ChatOpenAI


class KnowledgeGraphInput(BaseModel):
    """Input schema for KnowledgeGraphTool"""
    topic: str = Field(..., description="Topic or domain to build knowledge graph for")
    concepts: list[str] = Field(default_factory=list, description="Optional list of concepts to include")


class KnowledgeGraphTool(BaseTool):
    name: str = "Knowledge Graph Builder"
    description: str = """Constructs knowledge graphs for topics and domains. Identifies
    concepts, relationships, and structures within knowledge areas. Returns graph
    representation showing nodes (concepts) and edges (relationships)."""
    args_schema: Type[BaseModel] = KnowledgeGraphInput

    def _run(self, topic: str, concepts: list[str] = None) -> str:
        """
        Build a knowledge graph for a given topic

        Args:
            topic: Topic or domain to map
            concepts: Optional predefined concepts to include

        Returns:
            Knowledge graph structure as text
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Create a comprehensive knowledge graph for the topic: {topic}

Your task:
1. Identify 15-25 key concepts within this domain
2. Define relationships between concepts (e.g., "is-a", "part-of", "enables", "requires", "contradicts")
3. Organize concepts into clusters or categories
4. Identify hierarchical structures if applicable
5. Note interdisciplinary connections

{f"Include these concepts: {', '.join(concepts)}" if concepts else ""}

Format your response as:

CONCEPTS:
- [Concept Name]: [Brief definition]

RELATIONSHIPS:
- [Concept A] --[relationship]--> [Concept B]: [Explanation]

CLUSTERS:
- [Cluster Name]: [Concepts in this cluster]

HIERARCHY:
- [Top-level concepts and their subconcepts]

Provide a detailed, well-structured knowledge graph."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error building knowledge graph: {str(e)}"


class SemanticSearchInput(BaseModel):
    """Input schema for SemanticSearchTool"""
    query: str = Field(..., description="Search query for semantic information retrieval")
    domain: str = Field(default="general", description="Knowledge domain to search within")


class SemanticSearchTool(BaseTool):
    name: str = "Semantic Knowledge Search"
    description: str = """Performs semantic search for knowledge, concepts, and information.
    Retrieves relevant information based on meaning and context, not just keywords.
    Useful for finding related concepts, definitions, and connections."""
    args_schema: Type[BaseModel] = SemanticSearchInput

    def _run(self, query: str, domain: str = "general") -> str:
        """
        Perform semantic search for knowledge

        Args:
            query: Search query
            domain: Knowledge domain to focus on

        Returns:
            Search results with semantic matches
        """
        try:
            # Check for SERPER_API_KEY for web search
            serper_api_key = os.getenv("SERPER_API_KEY")

            if serper_api_key:
                url = "https://google.serper.dev/search"
                payload = {
                    "q": f"{query} {domain if domain != 'general' else ''}",
                    "num": 10
                }
                headers = {
                    "X-API-KEY": serper_api_key,
                    "Content-Type": "application/json"
                }

                response = requests.post(url, json=payload, headers=headers)
                if response.status_code == 200:
                    results = response.json()
                    formatted = []

                    # Include knowledge graph if available
                    if "knowledgeGraph" in results:
                        kg = results["knowledgeGraph"]
                        formatted.append(f"KNOWLEDGE GRAPH:\nTitle: {kg.get('title')}\nDescription: {kg.get('description')}\n")

                    # Format organic results
                    for item in results.get("organic", [])[:10]:
                        formatted.append(
                            f"Title: {item.get('title')}\n"
                            f"Link: {item.get('link')}\n"
                            f"Snippet: {item.get('snippet')}\n"
                        )
                    return "\n".join(formatted)

            # Fallback: Use LLM for semantic knowledge retrieval
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Provide comprehensive information about: {query}

{f"Focus on the domain: {domain}" if domain != "general" else ""}

Include:
1. Definition and core concepts
2. Key characteristics and attributes
3. Related concepts and connections
4. Historical context or development
5. Current applications or relevance
6. Notable sources or references

Provide detailed, accurate information."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error performing semantic search: {str(e)}"


class ConceptAnalysisInput(BaseModel):
    """Input schema for ConceptAnalysisTool"""
    concept: str = Field(..., description="Concept to analyze")
    context: str = Field(default="", description="Optional context or domain for analysis")


class ConceptAnalysisTool(BaseTool):
    name: str = "Concept Deep Analysis"
    description: str = """Performs deep analysis of individual concepts. Examines definition,
    characteristics, relationships, evolution, and implications. Returns comprehensive
    conceptual breakdown."""
    args_schema: Type[BaseModel] = ConceptAnalysisInput

    def _run(self, concept: str, context: str = "") -> str:
        """
        Perform deep analysis of a concept

        Args:
            concept: Concept to analyze
            context: Optional domain or context

        Returns:
            Detailed concept analysis
        """
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)

            prompt = f"""Perform a comprehensive deep analysis of the concept: {concept}

{f"Within the context of: {context}" if context else ""}

Your analysis should include:

1. DEFINITION
   - Precise definition
   - Essential characteristics
   - Scope and boundaries

2. COMPONENTS & DIMENSIONS
   - Key components or aspects
   - Dimensions of variation
   - Subtypes or categories

3. RELATIONSHIPS
   - Related concepts (similar, opposite, complementary)
   - Hierarchical position (broader/narrower concepts)
   - Causal or functional relationships

4. EVOLUTION
   - Historical development
   - How the concept has changed over time
   - Different interpretations or schools of thought

5. APPLICATIONS
   - Practical uses or manifestations
   - Examples in different domains
   - Real-world implications

6. DEBATES & OPEN QUESTIONS
   - Current controversies or debates
   - Unresolved questions
   - Areas of active research or discussion

7. SIGNIFICANCE
   - Why this concept matters
   - Its impact or influence
   - Future relevance

Provide a thorough, nuanced analysis."""

            response = llm.invoke(prompt)
            return response.content

        except Exception as e:
            return f"Error analyzing concept: {str(e)}"
