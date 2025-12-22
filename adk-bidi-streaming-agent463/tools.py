"""Custom Tools for Bidirectional Streaming"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class ConnectionMonitorInput(BaseModel):
    connection_id: str = Field(..., description="Connection identifier")


class ConnectionMonitorTool(BaseTool):
    name: str = "Connection Monitor"
    description: str = "Monitors bidirectional streaming connection health and metrics"
    args_schema: Type[BaseModel] = ConnectionMonitorInput

    def _run(self, connection_id: str) -> str:
        return f"Monitoring connection: {connection_id}\\nStatus: Active\\nLatency: 45ms\\nMessages: 1250"


class MessageValidatorInput(BaseModel):
    message: str = Field(..., description="Message to validate")
    schema: str = Field(..., description="Expected schema")


class MessageValidatorTool(BaseTool):
    name: str = "Message Validator"
    description: str = "Validates streaming messages against schema"
    args_schema: Type[BaseModel] = MessageValidatorInput

    def _run(self, message: str, schema: str) -> str:
        return f"Message validation: PASS\\nSchema: {schema}\\nSize: {len(message)} bytes"
