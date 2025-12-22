from crewai import Agent
from tools import NewsGatheringTools, ContentAnalysisTools, SummarizationTools

class NewsAggregatorAgents:
    def news_collector(self):
        return Agent(
            role='News Collector',
            goal='Gather news from multiple sources across various topics',
            backstory="""You are a skilled news gatherer who monitors multiple
            sources, identifies breaking news, and collects relevant articles
            based on user interests and trending topics.""",
            tools=[
                NewsGatheringTools.fetch_news,
                NewsGatheringTools.search_by_topic,
                NewsGatheringTools.monitor_sources
            ],
            verbose=True,
            allow_delegation=False
        )

    def content_curator(self):
        return Agent(
            role='Content Curator',
            goal='Filter, categorize, and rank news content by relevance',
            backstory="""You are a content curation expert who filters out noise,
            categorizes articles by topic, and ranks content by relevance and
            credibility.""",
            tools=[
                ContentAnalysisTools.filter_content,
                ContentAnalysisTools.categorize_articles,
                ContentAnalysisTools.rank_by_relevance
            ],
            verbose=True,
            allow_delegation=False
        )

    def fact_checker(self):
        return Agent(
            role='Fact Checker',
            goal='Verify news accuracy and identify misinformation',
            backstory="""You are a fact-checking specialist who verifies claims,
            cross-references sources, and flags potentially misleading or false
            information.""",
            tools=[
                ContentAnalysisTools.verify_sources,
                ContentAnalysisTools.check_bias,
                ContentAnalysisTools.detect_misinformation
            ],
            verbose=True,
            allow_delegation=False
        )

    def news_summarizer(self):
        return Agent(
            role='News Summarizer',
            goal='Create concise, informative news summaries and briefings',
            backstory="""You are an expert at distilling complex news stories
            into clear, concise summaries that capture key facts and context
            without bias.""",
            tools=[
                SummarizationTools.summarize_article,
                SummarizationTools.create_briefing,
                SummarizationTools.extract_key_points
            ],
            verbose=True,
            allow_delegation=False
        )
