"""ADK No-Code Builder - CrewAI Tools"""

from crewai_tools import tool


@tool("Component Schema Generator")
def generate_component_schema(component_type: str) -> dict:
    """Generates schema for no-code components."""
    return {"schema": {}, "properties": []}
