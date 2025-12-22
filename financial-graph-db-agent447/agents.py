from crewai import Agent
from tools import (
    graph_builder,
    relationship_analyzer,
    entity_extractor,
    query_optimizer,
    graph_visualizer
)

class FinancialGraphAgents:
    def entity_extraction_agent(self):
        return Agent(
            role='Financial Entity Extractor',
            goal='Extract and identify financial entities from data',
            backstory="""You are an expert in financial data processing who
            identifies entities like companies, transactions, accounts, and
            persons from financial documents and databases.""",
            tools=[entity_extractor],
            verbose=True,
            allow_delegation=False
        )

    def relationship_agent(self):
        return Agent(
            role='Relationship Analyst',
            goal='Identify and map relationships between financial entities',
            backstory="""You are a specialist in analyzing relationships between
            financial entities. You understand ownership structures, transactions,
            affiliations, and financial connections.""",
            tools=[relationship_analyzer, entity_extractor],
            verbose=True,
            allow_delegation=True
        )

    def graph_builder_agent(self):
        return Agent(
            role='Graph Database Engineer',
            goal='Build and maintain financial knowledge graphs',
            backstory="""You are a graph database expert who designs and builds
            financial knowledge graphs. You create nodes, edges, and properties
            that represent complex financial relationships.""",
            tools=[graph_builder, relationship_analyzer],
            verbose=True,
            allow_delegation=True
        )

    def query_agent(self):
        return Agent(
            role='Graph Query Specialist',
            goal='Query and analyze financial graph data',
            backstory="""You are an expert in graph query languages like Cypher
            and SPARQL. You write efficient queries to extract insights from
            financial knowledge graphs.""",
            tools=[query_optimizer, graph_builder],
            verbose=True,
            allow_delegation=False
        )

    def visualization_agent(self):
        return Agent(
            role='Graph Visualization Specialist',
            goal='Create visual representations of financial graphs',
            backstory="""You are a data visualization expert who creates clear
            and insightful visualizations of financial relationships and
            network structures.""",
            tools=[graph_visualizer, relationship_analyzer],
            verbose=True,
            allow_delegation=False
        )
