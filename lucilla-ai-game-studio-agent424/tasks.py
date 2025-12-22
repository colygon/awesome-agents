from crewai import Task
from textwrap import dedent

class LucillaGameStudioTasks:
    def design_game_concept(self, agent, game_idea):
        return Task(
            description=dedent(f"""
                Design a comprehensive game concept based on the initial idea.

                Game Idea: {game_idea}

                Your design should include:
                1. Core game mechanics and gameplay loop
                2. Narrative structure and story framework
                3. Player progression system
                4. Win/loss conditions and objectives
                5. Unique selling points and innovation
            """),
            expected_output="""A complete game design document containing:
                - Game concept overview
                - Core mechanics description
                - Gameplay loop definition
                - Narrative framework and story beats
                - Progression system design
                - Win conditions and objectives
                - Innovation and unique features
                - Target audience and market positioning""",
            agent=agent
        )

    def generate_game_content(self, agent, game_design):
        return Task(
            description=dedent(f"""
                Generate procedural game content based on the game design.

                Game Design: {game_design}

                Your content generation should include:
                1. Procedural level layouts
                2. Quest and mission generation
                3. Dialogue and narrative content
                4. Asset variations and combinations
                5. Content balancing and variety
            """),
            expected_output="""A comprehensive content generation plan with:
                - Level generation algorithms and parameters
                - Quest templates and generation rules
                - Dialogue trees and conversation systems
                - Asset generation guidelines
                - Content variety metrics
                - Sample generated content examples
                - Quality assurance criteria""",
            agent=agent
        )

    def create_npc_ai_system(self, agent, game_world):
        return Task(
            description=dedent(f"""
                Design the NPC AI system to populate the game world with
                believable characters.

                Game World: {game_world}

                Your NPC system should include:
                1. NPC behavior patterns and AI
                2. Personality systems and traits
                3. Dynamic dialogue responses
                4. Relationship and reputation systems
                5. Adaptive behaviors based on player actions
            """),
            expected_output="""A complete NPC AI system design with:
                - Behavior tree architectures
                - Personality trait systems
                - Dynamic dialogue generation
                - Relationship mechanics
                - Reputation and faction systems
                - Adaptive AI algorithms
                - Memory and learning systems
                - Sample NPC profiles""",
            agent=agent
        )

    def finalize_game_design(self, agent):
        return Task(
            description=dedent("""
                Integrate all game elements and finalize the complete game design.

                Your finalization should include:
                1. Integration of mechanics, content, and AI systems
                2. Player engagement analysis
                3. Difficulty balancing
                4. Complete game documentation
                5. Development roadmap
            """),
            expected_output="""A comprehensive game design package containing:
                - Executive summary of the game
                - Integrated design document
                - Player engagement projections
                - Difficulty curves and balancing
                - Technical requirements
                - Development timeline and milestones
                - Marketing and monetization strategy
                - Risk assessment and mitigation
                - Complete technical documentation""",
            agent=agent
        )
