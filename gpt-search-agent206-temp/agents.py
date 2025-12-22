"""
CrewAI Agents for GPT Search Application

This module defines specialized agents for semantic search and query answering.
Each agent has a specific role in processing user queries and generating accurate responses.
"""

from crewai import Agent
from crewai_tools import FileReadTool, SeleniumScrapingTool
from langchain_openai import ChatOpenAI


class GPTSearchAgents:
    """Factory class for creating specialized search agents."""

    def __init__(self, api_key: str = None):
        """
        Initialize the agents factory.

        Args:
            api_key: OpenAI API key for LLM initialization
        """
        self.llm = ChatOpenAI(
            model="gpt-4",
            temperature=0.2,
            api_key=api_key
        ) if api_key else None

    def semantic_search_agent(self) -> Agent:
        """
        Agent responsible for semantic search and information retrieval.

        This agent specializes in:
        - Finding semantically similar content to user queries
        - Ranking and filtering search results
        - Extracting the most relevant passages

        Returns:
            Agent: Configured semantic search agent
        """
        return Agent(
            role='Semantic Search Specialist',
            goal='Find the most relevant information from text corpus that matches user queries semantically',
            backstory="""You are an expert in information retrieval and semantic search.
            You have years of experience in understanding user intent and finding the most
            relevant information from large text corpora. You excel at identifying key passages
            that contain answers to user questions, even when the wording differs from the query.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[FileReadTool()]
        )

    def answer_synthesizer_agent(self) -> Agent:
        """
        Agent responsible for synthesizing answers from retrieved information.

        This agent specializes in:
        - Analyzing retrieved text passages
        - Extracting key information relevant to queries
        - Generating clear, accurate, and concise answers
        - Maintaining context and accuracy

        Returns:
            Agent: Configured answer synthesis agent
        """
        return Agent(
            role='Answer Synthesis Expert',
            goal='Generate accurate, well-structured answers based on retrieved information',
            backstory="""You are a skilled information analyst and writer. You excel at
            reading through multiple text passages, identifying the key information, and
            synthesizing it into clear, accurate answers. You always ensure your responses
            are grounded in the provided context and never make up information. If the
            context doesn't contain enough information to answer a query, you clearly
            state this limitation.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )

    def quality_validator_agent(self) -> Agent:
        """
        Agent responsible for validating answer quality and accuracy.

        This agent specializes in:
        - Verifying answers against source material
        - Checking for hallucinations or unsupported claims
        - Ensuring answers directly address the user's query
        - Improving answer clarity and completeness

        Returns:
            Agent: Configured quality validation agent
        """
        return Agent(
            role='Quality Assurance Specialist',
            goal='Ensure all answers are accurate, relevant, and grounded in the source material',
            backstory="""You are a meticulous quality assurance expert with a keen eye
            for detail. You verify that every answer is supported by the source material,
            directly addresses the user's question, and maintains high standards of clarity
            and accuracy. You catch any inconsistencies, hallucinations, or unsupported
            claims before they reach the user.""",
            verbose=True,
            allow_delegation=False,
            llm=self.llm
        )
