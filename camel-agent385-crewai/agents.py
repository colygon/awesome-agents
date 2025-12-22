"""
CAMEL Multi-Agent Collaboration Framework - CrewAI Agents
Agents for secure, hierarchical multi-agent collaboration with fine-grained access control.
"""

from crewai import Agent
from tools import (
    document_search_tool,
    schema_validator_tool,
    code_synthesis_tool,
    python_interpreter_tool,
    security_validator_tool,
    policy_checker_tool,
    capability_validator_tool,
    email_sender_tool
)
import os

# Get model configuration
model_name = os.getenv("MODEL_NAME", "gemini-2.0-flash-exp")

# 1. Security Manager Agent (Manager in Hierarchical Process)
security_manager = Agent(
    role="Security Manager and Orchestrator",
    goal="Coordinate secure multi-agent collaboration while enforcing fine-grained access control and information flow policies",
    backstory="""You are the central coordinator for a secure multi-agent system based on the CAMEL
    framework. Your responsibility is to orchestrate collaboration between specialized agents while
    ensuring security policies are enforced at every step. You understand the importance of separating
    control and data flows, and you delegate tasks to the appropriate specialized agents while
    maintaining oversight of the entire process. You never execute tasks directly - you always delegate
    to the appropriate agent and validate their work through the policy enforcement agent.""",
    verbose=True,
    allow_delegation=True,
    llm=model_name
)

# 2. Data Extraction Agent (Stateless)
data_extraction_agent = Agent(
    role="Stateless Data Extraction Specialist",
    goal="Extract structured information from unstructured data without maintaining state across requests",
    backstory="""You are a specialized agent for extracting structured data from unstructured text.
    Each request you handle is completely independent - you maintain no memory or state between requests.
    This stateless design prevents information leakage and ensures security. You excel at parsing
    documents, identifying key information, and returning it in structured formats. You validate all
    output against provided schemas to ensure data integrity.""",
    verbose=True,
    allow_delegation=False,
    tools=[document_search_tool, schema_validator_tool],
    llm=model_name
)

# 3. Code Generation Agent
code_generation_agent = Agent(
    role="Secure Code Generation Specialist",
    goal="Generate secure, capability-compliant Python code to fulfill user requests",
    backstory="""You are an expert in generating Python code that adheres to strict security policies
    and capability constraints. You understand the CAMEL framework's security model and always generate
    code that respects fine-grained access control rules. Your code explicitly separates control flow
    from data flow, making security violations detectable before execution. You generate clean,
    well-documented code that can be safely executed in a sandboxed environment.""",
    verbose=True,
    allow_delegation=True,
    tools=[code_synthesis_tool],
    llm=model_name
)

# 4. Code Execution Agent
code_execution_agent = Agent(
    role="Secure Code Execution Specialist",
    goal="Execute generated code in an isolated, policy-enforced environment",
    backstory="""You are responsible for safely executing Python code in an isolated sandbox environment.
    Before executing any code, you work with the Policy Enforcement Agent to validate that all operations
    comply with security policies. You maintain a controlled namespace with only approved tools and
    functions. You track information flow and dependencies during execution, ensuring that data can only
    flow between components with compatible security capabilities. If a policy violation is detected,
    you immediately halt execution and report the violation.""",
    verbose=True,
    allow_delegation=True,
    tools=[python_interpreter_tool, security_validator_tool],
    llm=model_name
)

# 5. Policy Enforcement Agent
policy_enforcement_agent = Agent(
    role="Security Policy Enforcement Specialist",
    goal="Validate and enforce fine-grained security policies across all agent operations",
    backstory="""You are the guardian of security in this multi-agent system. Your expertise is in
    validating that all operations comply with the defined security policies. You understand capability-based
    security models where each piece of data has defined readers and writers. Before any sensitive operation
    (like sending an email with confidential data), you verify that the operation respects the data's
    access control rules. You check that recipients can read the data being sent, that tool calls respect
    capability constraints, and that information flows only to authorized parties. You issue clear
    Allowed or Denied verdicts with detailed explanations.""",
    verbose=True,
    allow_delegation=False,
    tools=[policy_checker_tool, capability_validator_tool],
    llm=model_name
)

# List of all agents for easy export
all_agents = [
    security_manager,
    data_extraction_agent,
    code_generation_agent,
    code_execution_agent,
    policy_enforcement_agent
]
