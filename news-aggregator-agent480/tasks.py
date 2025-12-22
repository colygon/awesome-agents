from crewai import Task
from textwrap import dedent

class NewsAggregatorTasks:
    def collect_news(self, agent, topics):
        return Task(
            description=dedent(f"""
                Collect news articles: {topics}

                Tasks: Monitor news sources, fetch latest articles, identify
                breaking news, gather content from multiple sources.
            """),
            agent=agent,
            expected_output="Collection of news articles with metadata and source information"
        )

    def curate_content(self, agent, articles):
        return Task(
            description=dedent(f"""
                Curate and organize news content: {articles}

                Tasks: Filter irrelevant content, categorize by topic, rank
                by relevance, identify trending stories.
            """),
            agent=agent,
            expected_output="Curated and categorized news feed with relevance rankings"
        )

    def verify_accuracy(self, agent, content):
        return Task(
            description=dedent(f"""
                Verify news accuracy: {content}

                Tasks: Check source credibility, verify claims, cross-reference
                facts, flag misinformation, assess bias.
            """),
            agent=agent,
            expected_output="Fact-check report with credibility ratings and verification status"
        )

    def create_briefing(self, agent, curated_news):
        return Task(
            description=dedent(f"""
                Create news briefing: {curated_news}

                Tasks: Summarize top stories, extract key points, provide context,
                organize by category, create daily digest.
            """),
            agent=agent,
            expected_output="News briefing with summaries, key points, and organized content"
        )
