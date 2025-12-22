from crewai import Agent
from tools import LucillaGameStudioTools

class LucillaGameStudioAgents:
    def __init__(self):
        self.tools = LucillaGameStudioTools()

    def game_designer(self):
        return Agent(
            role='AI Game Designer',
            goal='Design engaging game mechanics, narratives, and player experiences',
            backstory="""You are an expert game designer who creates compelling game concepts.
            You specialize in game mechanics, progression systems, player engagement,
            and balancing fun with challenge.""",
            tools=[
                self.tools.design_game_mechanics,
                self.tools.create_narrative_structure,
                self.tools.design_progression_system
            ],
            verbose=True,
            allow_delegation=False
        )

    def procedural_content_generator(self):
        return Agent(
            role='Procedural Content Generator',
            goal='Generate game content procedurally using AI including levels, quests, and assets',
            backstory="""You are an expert in procedural generation and AI-driven content creation.
            You excel at creating diverse, balanced, and engaging game content automatically
            while maintaining quality and coherence.""",
            tools=[
                self.tools.generate_level_layouts,
                self.tools.create_quests,
                self.tools.generate_dialogue
            ],
            verbose=True,
            allow_delegation=False
        )

    def npc_ai_specialist(self):
        return Agent(
            role='NPC AI Behavior Specialist',
            goal='Design intelligent NPC behaviors and create believable AI characters',
            backstory="""You specialize in NPC AI and behavioral systems. You create NPCs
            that feel alive, responsive, and engaging through advanced AI techniques
            and personality systems.""",
            tools=[
                self.tools.design_npc_behaviors,
                self.tools.create_npc_personalities,
                self.tools.implement_dynamic_dialogue
            ],
            verbose=True,
            allow_delegation=False
        )

    def game_director(self):
        return Agent(
            role='AI Game Director',
            goal='Coordinate game development and ensure cohesive player experience',
            backstory="""You are an experienced game director who oversees the complete
            game development process. You ensure all elements work together to create
            an engaging, polished game experience.""",
            tools=[
                self.tools.analyze_player_engagement,
                self.tools.balance_game_difficulty,
                self.tools.generate_game_documentation
            ],
            verbose=True,
            allow_delegation=True
        )
