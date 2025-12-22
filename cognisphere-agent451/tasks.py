"""
Cognisphere CrewAI Tasks
Defines the workflow for knowledge exploration and cognitive analysis
"""

from crewai import Task
from agents import knowledge_explorer, concept_analyzer, insight_generator

def create_tasks(topic: str, depth: str = "comprehensive"):
    """
    Create tasks for knowledge exploration workflow

    Args:
        topic: The knowledge domain or topic to explore
        depth: Analysis depth - "overview", "detailed", or "comprehensive"

    Returns:
        List of Task objects
    """

    # Task 1: Explore and map the knowledge domain
    explore_knowledge_task = Task(
        description=f"""Explore and map the knowledge domain: {topic}

        Your objectives:
        1. Identify the core concepts, themes, and components of this domain
        2. Map relationships and connections between concepts
        3. Construct a knowledge graph showing the structure of this domain
        4. Identify key sources, authorities, and foundational works
        5. Discover related domains and interdisciplinary connections
        6. Highlight emerging trends and frontier areas

        Depth level: {depth}

        Provide a comprehensive map of the knowledge domain including:
        - Core concepts and their definitions
        - Hierarchical structure (if applicable)
        - Network of relationships
        - Historical development and evolution
        - Key contributors and seminal works
        - Related and intersecting domains""",
        agent=knowledge_explorer,
        expected_output="""A structured knowledge domain map containing:
        - List of core concepts with definitions
        - Knowledge graph showing concept relationships
        - Hierarchy or taxonomy (if applicable)
        - Timeline of key developments
        - List of seminal works and key contributors
        - Related domains and interdisciplinary connections
        - Emerging trends and frontier areas"""
    )

    # Task 2: Analyze concepts and synthesize insights
    analyze_concepts_task = Task(
        description=f"""Based on the knowledge domain exploration, perform deep conceptual
        analysis of the key themes in {topic}.

        Your objectives:
        1. Select 5-10 most significant concepts from the domain map
        2. Perform deep analysis of each concept:
           - Definition and essential characteristics
           - Historical development and evolution
           - Relationships with other concepts
           - Theoretical foundations
           - Practical manifestations
        3. Identify conceptual tensions, paradoxes, or debates
        4. Synthesize meta-insights about the domain as a whole
        5. Discover novel connections and emergent patterns
        6. Identify gaps or underexplored areas

        For each major concept, provide:
        - Clear definition and scope
        - Key attributes and dimensions
        - Relationships to other concepts
        - Evolution over time
        - Current debates or open questions""",
        agent=concept_analyzer,
        expected_output="""A comprehensive conceptual analysis including:
        - Deep analysis of 5-10 major concepts (definition, characteristics, relationships)
        - Identification of conceptual tensions and debates
        - Meta-insights about the domain structure
        - Novel connections and emergent patterns
        - Gaps and underexplored areas
        - Synthesis of how concepts form a coherent framework""",
        context=[explore_knowledge_task]
    )

    # Task 3: Generate actionable insights and recommendations
    generate_insights_task = Task(
        description=f"""Based on the knowledge exploration and conceptual analysis of {topic},
        generate actionable insights and strategic recommendations.

        Your objectives:
        1. Identify practical applications and use cases
        2. Recognize innovation opportunities
        3. Predict emerging trends and future directions
        4. Formulate recommendations for:
           - Research and investigation priorities
           - Practical implementations
           - Educational or learning pathways
           - Strategic initiatives or projects
        5. Bridge theoretical knowledge with practical action
        6. Identify potential challenges and mitigation strategies

        Generate at least 8-12 insights organized into categories:
        - Immediate applications (ready to implement)
        - Innovation opportunities (novel possibilities)
        - Future trends (emerging directions)
        - Learning pathways (how to engage with this domain)
        - Strategic recommendations (prioritized actions)

        Each insight should include:
        - Clear description
        - Rationale and supporting evidence
        - Potential impact
        - Implementation considerations
        - Resources or prerequisites needed""",
        agent=insight_generator,
        expected_output="""A comprehensive insights report with 8-12 actionable items including:
        - Immediate applications with implementation steps
        - Innovation opportunities with potential impact
        - Future trends with timeline predictions
        - Learning pathways with recommended resources
        - Strategic recommendations with priorities
        - Risk assessment and mitigation strategies
        Each organized by category with clear rationale and implementation guidance""",
        context=[explore_knowledge_task, analyze_concepts_task]
    )

    return [explore_knowledge_task, analyze_concepts_task, generate_insights_task]
