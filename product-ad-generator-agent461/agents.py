"""
CrewAI Agents for Product Ad Generator
Specialized agents for creating compelling product advertisements
"""

from crewai import Agent
from crewai_tools import FileReadTool, WebSearchTool
import os


class ProductAdAgents:
    """Factory class for creating product advertisement agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def market_researcher(self) -> Agent:
        """
        Market Research Agent
        Analyzes target audience and market trends
        """
        return Agent(
            role='Market Research Specialist',
            goal='Conduct comprehensive market research to understand target audience demographics, '
                 'preferences, pain points, and competitive landscape for effective ad positioning',
            backstory='You are a seasoned market researcher with 12+ years of experience in '
                     'consumer behavior analysis and competitive intelligence. You excel at '
                     'identifying market trends, audience segmentation, and uncovering unique '
                     'selling propositions. Your insights have helped countless brands position '
                     'their products effectively in crowded markets.',
            verbose=True,
            allow_delegation=False,
            tools=[WebSearchTool()],
            llm='gpt-4o'
        )

    def copywriter(self) -> Agent:
        """
        Copywriter Agent
        Creates compelling ad copy and headlines
        """
        return Agent(
            role='Creative Copywriter',
            goal='Craft persuasive, engaging, and conversion-focused ad copy that resonates with '
                 'the target audience and highlights product benefits',
            backstory='You are an award-winning copywriter with expertise in direct response '
                     'advertising, storytelling, and persuasive writing. You understand the '
                     'psychology of consumer decision-making and know how to craft messages '
                     'that drive action. Your work has generated millions in revenue for '
                     'major brands across various industries.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def visual_designer(self) -> Agent:
        """
        Visual Design Agent
        Recommends visual elements and design strategies
        """
        return Agent(
            role='Visual Design Strategist',
            goal='Recommend visual design elements, color schemes, imagery, and layout strategies '
                 'that maximize ad impact and brand consistency',
            backstory='You are a creative director with extensive experience in advertising design '
                     'and visual communication. You understand how colors, typography, imagery, '
                     'and composition influence consumer perception and behavior. Your designs '
                     'have won multiple industry awards and consistently outperform benchmarks '
                     'in A/B testing.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def performance_analyst(self) -> Agent:
        """
        Performance Analyst Agent
        Evaluates ad effectiveness and suggests optimizations
        """
        return Agent(
            role='Ad Performance Analyst',
            goal='Evaluate ad creative against best practices and industry benchmarks, providing '
                 'data-driven recommendations for optimization',
            backstory='You are a digital marketing analyst specializing in ad performance optimization. '
                     'You have deep knowledge of conversion rate optimization, A/B testing, and '
                     'advertising metrics. You analyze ad creative through the lens of proven '
                     'performance principles and consumer psychology.',
            verbose=True,
            allow_delegation=False,
            tools=[WebSearchTool()],
            llm='gpt-4o'
        )

    def brand_strategist(self) -> Agent:
        """
        Brand Strategy Agent
        Ensures brand alignment and consistency
        """
        return Agent(
            role='Brand Strategy Specialist',
            goal='Ensure all ad elements align with brand identity, voice, and values while '
                 'maintaining consistency across campaigns',
            backstory='You are a brand strategist with expertise in brand positioning, messaging '
                     'architecture, and brand identity systems. You ensure that every piece of '
                     'creative work strengthens brand equity and maintains consistency with '
                     'brand guidelines. You balance creativity with strategic brand objectives.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )
