from crewai import Task
from textwrap import dedent

class FinancialGraphTasks:
    def extract_entities_task(self, agent, financial_data):
        return Task(
            description=dedent(f"""
                Extract financial entities from the provided data.

                Financial Data: {financial_data}

                Steps:
                1. Parse financial documents/data
                2. Identify entity types (companies, accounts, persons)
                3. Extract entity attributes and properties
                4. Standardize entity identifiers
                5. Return structured entity data
            """),
            agent=agent,
            expected_output="Structured list of financial entities with attributes"
        )

    def analyze_relationships_task(self, agent, entities):
        return Task(
            description=dedent(f"""
                Analyze and identify relationships between financial entities.

                Entities: {entities}

                Steps:
                1. Review entity data
                2. Identify relationship types (owns, transacts, controls)
                3. Extract relationship attributes
                4. Determine relationship strength and direction
                5. Create relationship mapping
            """),
            agent=agent,
            expected_output="Comprehensive relationship mapping between entities"
        )

    def build_graph_task(self, agent, entities, relationships):
        return Task(
            description=dedent(f"""
                Build a financial knowledge graph from entities and relationships.

                Entities: {entities}
                Relationships: {relationships}

                Steps:
                1. Design graph schema
                2. Create nodes for entities
                3. Create edges for relationships
                4. Add properties and attributes
                5. Validate graph structure
            """),
            agent=agent,
            expected_output="Financial knowledge graph with nodes and edges"
        )

    def query_graph_task(self, agent, query_requirements):
        return Task(
            description=dedent(f"""
                Query the financial graph to extract insights.

                Query Requirements: {query_requirements}

                Steps:
                1. Understand query requirements
                2. Design optimal graph query
                3. Execute query on graph database
                4. Process and format results
                5. Provide insights and findings
            """),
            agent=agent,
            expected_output="Query results with financial insights"
        )

    def visualize_graph_task(self, agent, graph_data, focus_area):
        return Task(
            description=dedent(f"""
                Create visualization of the financial graph.

                Graph Data: {graph_data}
                Focus Area: {focus_area}

                Steps:
                1. Analyze graph structure
                2. Design visualization layout
                3. Apply visual styling for clarity
                4. Highlight important relationships
                5. Generate interactive visualization
            """),
            agent=agent,
            expected_output="Visual representation of financial graph with insights"
        )
