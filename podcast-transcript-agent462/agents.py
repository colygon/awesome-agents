"""
CrewAI Agents for Podcast Transcript Analysis
Specialized agents for processing, analyzing, and summarizing podcast transcripts
"""

from crewai import Agent
from crewai_tools import FileReadTool, WebSearchTool
import os


class PodcastTranscriptAgents:
    """Factory class for creating podcast transcript processing agents"""

    def __init__(self):
        self.openai_api_key = os.getenv('OPENAI_API_KEY')

    def transcript_processor(self) -> Agent:
        """
        Transcript Processor Agent
        Cleans and formats raw podcast transcripts
        """
        return Agent(
            role='Transcript Processing Specialist',
            goal='Clean, format, and structure raw podcast transcripts for optimal readability '
                 'and analysis, removing filler words and formatting speaker segments',
            backstory='You are an expert in audio transcription post-processing with years of '
                     'experience refining automated transcripts. You excel at identifying and '
                     'removing filler words, fixing punctuation, segmenting speaker turns, and '
                     'creating well-structured, readable transcripts from raw audio-to-text output.',
            verbose=True,
            allow_delegation=False,
            tools=[FileReadTool()],
            llm='gpt-4o'
        )

    def content_analyzer(self) -> Agent:
        """
        Content Analyzer Agent
        Analyzes transcript content for themes, topics, and insights
        """
        return Agent(
            role='Podcast Content Analyst',
            goal='Analyze podcast transcript content to identify key themes, topics, insights, '
                 'and discussion points, providing comprehensive content breakdown',
            backstory='You are a skilled content analyst specializing in long-form audio content. '
                     'You have a talent for identifying main themes, extracting key insights, '
                     'recognizing topic transitions, and understanding the narrative arc of '
                     'conversations. Your analysis helps audiences quickly understand the value '
                     'and content of podcast episodes.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def summarizer(self) -> Agent:
        """
        Summarizer Agent
        Creates concise summaries at multiple levels
        """
        return Agent(
            role='Podcast Summary Writer',
            goal='Create engaging, accurate summaries of podcast episodes at multiple levels '
                 '(brief, standard, detailed) that capture essential information and insights',
            backstory='You are an expert summarization specialist with a background in journalism '
                     'and content curation. You excel at distilling lengthy conversations into '
                     'concise, engaging summaries that preserve key insights while being '
                     'accessible to busy audiences. Your summaries help people decide if an '
                     'episode is worth their time.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def timestamp_generator(self) -> Agent:
        """
        Timestamp Generator Agent
        Creates chapter markers and timestamps for key moments
        """
        return Agent(
            role='Timestamp and Chapter Specialist',
            goal='Generate accurate timestamps and chapter markers for podcast episodes, '
                 'identifying topic transitions and key moments for easy navigation',
            backstory='You are a podcast production specialist with expertise in creating '
                     'listener-friendly chapter markers. You understand how to identify natural '
                     'topic breaks, significant moments, and content transitions. Your timestamps '
                     'help listeners navigate to specific content and improve the overall '
                     'listening experience.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def quote_extractor(self) -> Agent:
        """
        Quote Extractor Agent
        Identifies memorable quotes and soundbites
        """
        return Agent(
            role='Quote and Soundbite Curator',
            goal='Identify and extract the most memorable, impactful, and shareable quotes '
                 'from podcast transcripts for social media and promotional use',
            backstory='You are a content curator with a keen eye for compelling soundbites and '
                     'quotable moments. You understand what makes a quote shareable, memorable, '
                     'and valuable for audiences. Your selections help promote episodes and '
                     'capture the essence of conversations in bite-sized formats.',
            verbose=True,
            allow_delegation=False,
            tools=[],
            llm='gpt-4o'
        )

    def seo_optimizer(self) -> Agent:
        """
        SEO Optimizer Agent
        Creates SEO-friendly metadata and show notes
        """
        return Agent(
            role='Podcast SEO Specialist',
            goal='Optimize podcast metadata, show notes, and descriptions for search engines '
                 'and discovery platforms to maximize visibility and reach',
            backstory='You are an SEO expert specializing in podcast optimization. You understand '
                     'how podcast platforms, search engines, and recommendation algorithms work. '
                     'You know how to craft compelling titles, descriptions, and show notes that '
                     'both appeal to listeners and rank well in searches.',
            verbose=True,
            allow_delegation=False,
            tools=[WebSearchTool()],
            llm='gpt-4o'
        )
