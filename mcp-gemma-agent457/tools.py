"""
Custom Tools for MCP-Gemma Integration
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class MCPServerInput(BaseModel):
    server_name: str = Field(..., description="MCP server to connect to")


class MCPServerTool(BaseTool):
    name: str = "MCP Server Connector"
    description: str = "Connects to MCP servers and discovers available tools"
    args_schema: Type[BaseModel] = MCPServerInput

    def _run(self, server_name: str) -> str:
        try:
            # Simulated MCP server connection
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Simulate MCP server connection to: {server_name}

Describe:
- Available tools
- Resource types
- Capabilities
- Connection status"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error connecting to MCP server: {str(e)}"


class GemmaInferenceInput(BaseModel):
    prompt: str = Field(..., description="Prompt for Gemma model")
    context: str = Field(default="", description="MCP context")


class GemmaInferenceTool(BaseTool):
    name: str = "Gemma Model Inference"
    description: str = "Runs inference using Gemma models with MCP context"
    args_schema: Type[BaseModel] = GemmaInferenceInput

    def _run(self, prompt: str, context: str = "") -> str:
        try:
            # Simulated Gemma inference
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
            full_prompt = f"""Using Gemma model with MCP context:

Context: {context}
Query: {prompt}

Generate response leveraging MCP tools and resources."""
            return llm.invoke(full_prompt).content
        except Exception as e:
            return f"Error with Gemma inference: {str(e)}"


class ContextManagerTool(BaseTool):
    name: str = "MCP Context Manager"
    description: str = "Manages context across MCP servers and Gemma"
    args_schema: Type[BaseModel] = BaseModel

    def _run(self, context_data: str = "") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
            prompt = f"""Manage MCP context:

{context_data}

Organize:
- Active connections
- Available tools
- Resource cache
- Context state"""
            return llm.invoke(prompt).content
        except Exception as e:
            return f"Error managing context: {str(e)}"
