"""ADK Next.js Starter - CrewAI Tools"""

from crewai_tools import tool


@tool("Next.js Component Generator")
def generate_nextjs_component(component_name: str, component_type: str) -> dict:
    """Generates Next.js component templates."""
    return {"code": "", "path": f"components/{component_name}.tsx"}


@tool("Performance Analyzer")
def analyze_performance(bundle_stats: dict) -> dict:
    """Analyzes Next.js bundle performance."""
    return {"recommendations": [], "metrics": {}}
