from crewai_tools import tool
import json
from datetime import datetime

class NewsGatheringTools:
    @tool("Fetch News")
    def fetch_news(sources: str) -> str:
        """Fetches news from specified sources."""
        articles = {
            "articles": [
                {
                    "title": "Breaking: Major Tech Announcement",
                    "source": "TechNews",
                    "url": "https://example.com/article1",
                    "published": datetime.now().isoformat(),
                    "category": "Technology"
                }
            ],
            "total": 25
        }
        return json.dumps(articles, indent=2)

    @tool("Search By Topic")
    def search_by_topic(topic: str) -> str:
        """Searches news by specific topic or keyword."""
        return json.dumps({
            "topic": topic,
            "results": 42,
            "articles": [{"title": f"Article about {topic}", "relevance": 0.95}]
        }, indent=2)

    @tool("Monitor Sources")
    def monitor_sources(source_list: str) -> str:
        """Monitors news sources for updates."""
        return json.dumps({
            "monitoring": True,
            "sources": ["BBC", "CNN", "Reuters"],
            "updates": 15,
            "last_check": datetime.now().isoformat()
        }, indent=2)


class ContentAnalysisTools:
    @tool("Filter Content")
    def filter_content(criteria: str) -> str:
        """Filters news content by criteria."""
        return json.dumps({
            "filtered": True,
            "original_count": 100,
            "filtered_count": 35,
            "removed": ["duplicates", "low_quality", "irrelevant"]
        }, indent=2)

    @tool("Categorize Articles")
    def categorize_articles(articles: str) -> str:
        """Categorizes news articles by topic."""
        return json.dumps({
            "categories": {
                "Technology": 12,
                "Business": 8,
                "Politics": 10,
                "Science": 5
            }
        }, indent=2)

    @tool("Rank By Relevance")
    def rank_by_relevance(articles: str) -> str:
        """Ranks articles by relevance and importance."""
        return json.dumps({
            "ranking_algorithm": "ML-based",
            "top_articles": [
                {"title": "Most Relevant Story", "score": 0.98},
                {"title": "Second Most Relevant", "score": 0.95}
            ]
        }, indent=2)

    @tool("Verify Sources")
    def verify_sources(article: str) -> str:
        """Verifies credibility of news sources."""
        return json.dumps({
            "source_credibility": "High",
            "fact_check_rating": "Verified",
            "bias_rating": "Center",
            "reliability_score": 8.5
        }, indent=2)

    @tool("Check Bias")
    def check_bias(content: str) -> str:
        """Analyzes content for bias."""
        return json.dumps({
            "bias_detected": "Slight left-leaning",
            "objectivity_score": 7.5,
            "recommendations": "Cross-reference with other sources"
        }, indent=2)

    @tool("Detect Misinformation")
    def detect_misinformation(article: str) -> str:
        """Detects potential misinformation."""
        return json.dumps({
            "misinformation_risk": "Low",
            "verified_claims": 4,
            "unverified_claims": 0,
            "red_flags": []
        }, indent=2)


class SummarizationTools:
    @tool("Summarize Article")
    def summarize_article(article: str) -> str:
        """Summarizes news article."""
        return json.dumps({
            "summary": "Concise 2-3 sentence summary of the article",
            "key_points": ["Point 1", "Point 2", "Point 3"],
            "sentiment": "Neutral",
            "reading_time": "2 minutes"
        }, indent=2)

    @tool("Create Briefing")
    def create_briefing(articles: str) -> str:
        """Creates news briefing from multiple articles."""
        return json.dumps({
            "briefing_date": datetime.now().strftime("%Y-%m-%d"),
            "top_stories": [
                {
                    "category": "Technology",
                    "headline": "Major Tech Development",
                    "summary": "Brief summary...",
                    "importance": "High"
                }
            ],
            "total_articles": 35
        }, indent=2)

    @tool("Extract Key Points")
    def extract_key_points(text: str) -> str:
        """Extracts key points from news content."""
        return json.dumps({
            "key_points": [
                "Main event or development",
                "Key stakeholders involved",
                "Impact and implications",
                "Next steps or outcomes"
            ],
            "entities": ["Person A", "Company B", "Location C"]
        }, indent=2)
