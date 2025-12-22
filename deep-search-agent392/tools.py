from crewai_tools import tool
import os
import requests
from typing import List, Dict
import json

class SearchTools:
    @tool("Search the web")
    def search_web(query: str) -> str:
        """
        Search the web for information on a given query.
        Returns search results with titles, snippets, and URLs.
        """
        # Using Google Custom Search API
        api_key = os.getenv('GOOGLE_API_KEY')
        search_engine_id = os.getenv('GOOGLE_SEARCH_ENGINE_ID')

        if not api_key or not search_engine_id:
            return "Error: Google API credentials not configured. Set GOOGLE_API_KEY and GOOGLE_SEARCH_ENGINE_ID."

        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                'key': api_key,
                'cx': search_engine_id,
                'q': query,
                'num': 10
            }

            response = requests.get(url, params=params)
            response.raise_for_status()

            results = response.json()

            if 'items' not in results:
                return f"No results found for query: {query}"

            formatted_results = []
            for item in results['items']:
                formatted_results.append({
                    'title': item.get('title', 'No title'),
                    'link': item.get('link', ''),
                    'snippet': item.get('snippet', 'No description'),
                })

            return json.dumps(formatted_results, indent=2)

        except Exception as e:
            return f"Search error: {str(e)}"

class AnalysisTools:
    @tool("Analyze content")
    def analyze_content(content: str) -> str:
        """
        Analyze content to extract key themes, patterns, and insights.
        Returns structured analysis of the content.
        """
        # Simple analysis - in production, could use NLP tools
        lines = content.split('\n')
        word_count = len(content.split())

        analysis = {
            'word_count': word_count,
            'line_count': len(lines),
            'summary': 'Content analyzed successfully',
            'insights': []
        }

        # Extract key phrases (simple implementation)
        sentences = content.split('.')
        if sentences:
            analysis['key_sentences'] = sentences[:3]

        return json.dumps(analysis, indent=2)

    @tool("Extract entities")
    def extract_entities(text: str) -> str:
        """
        Extract named entities like people, organizations, locations from text.
        Returns list of identified entities.
        """
        # Simple entity extraction - in production, use spaCy or similar
        entities = {
            'people': [],
            'organizations': [],
            'locations': [],
            'dates': []
        }

        # Basic capitalized word extraction as placeholder
        words = text.split()
        capitalized = [w for w in words if w and w[0].isupper() and len(w) > 1]

        entities['potential_entities'] = list(set(capitalized))[:20]

        return json.dumps(entities, indent=2)

    @tool("Verify facts")
    def verify_facts(claim: str) -> str:
        """
        Verify a factual claim by searching for corroborating evidence.
        Returns verification status and supporting evidence.
        """
        # In production, this would search multiple fact-checking databases
        verification = {
            'claim': claim,
            'status': 'pending_verification',
            'confidence': 'medium',
            'note': 'Manual fact-checking recommended for critical claims'
        }

        return json.dumps(verification, indent=2)

    @tool("Summarize findings")
    def summarize_findings(findings: str) -> str:
        """
        Summarize research findings into a concise overview.
        Returns a structured summary.
        """
        summary = {
            'executive_summary': 'Research findings processed',
            'key_points': [],
            'recommendations': [],
            'source_count': 0
        }

        # Count potential sources (URLs)
        source_count = findings.count('http')
        summary['source_count'] = source_count

        return json.dumps(summary, indent=2)
