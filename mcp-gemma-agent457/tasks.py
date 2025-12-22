"""
MCP-Gemma CrewAI Tasks
"""

from crewai import Task
from agents import mcp_coordinator, gemma_specialist, integration_expert

def create_tasks(user_query: str, mcp_servers: list = None):
    coordinate_task = Task(
        description=f"""Coordinate MCP servers for query: {user_query}

Available servers: {mcp_servers or ['filesystem', 'database', 'web']}

Tasks:
- Connect to relevant MCP servers
- Discover available tools
- Gather context and resources
- Prepare execution environment""",
        agent=mcp_coordinator,
        expected_output="MCP setup with available tools and resources"
    )

    execute_task = Task(
        description=f"""Execute using Gemma with MCP context:

Query: {user_query}

Steps:
- Use Gemma models with MCP context
- Leverage discovered tools
- Access resources through MCP
- Generate comprehensive response""",
        agent=gemma_specialist,
        expected_output="Query response using Gemma with MCP tools",
        context=[coordinate_task]
    )

    optimize_task = Task(
        description="""Optimize MCP-Gemma integration:
        - Evaluate tool usage efficiency
        - Identify improvement opportunities
        - Suggest caching strategies
        - Recommend server configurations""",
        agent=integration_expert,
        expected_output="Integration optimization report",
        context=[coordinate_task, execute_task]
    )

    return [coordinate_task, execute_task, optimize_task]
