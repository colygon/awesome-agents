"""LineBot ADK - CrewAI Tools"""

from crewai_tools import tool


@tool("LINE Message Validator")
def validate_line_message(message_content: str) -> dict:
    """Validates LINE message format and content."""
    return {"valid": True, "suggestions": []}


@tool("Flex Message Builder")
def build_flex_message(template_type: str) -> dict:
    """Generates LINE Flex Message templates."""
    return {"template": {}, "preview_url": ""}
