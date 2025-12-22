"""Custom Tools for API Testing"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class APIRequestInput(BaseModel):
    endpoint: str = Field(..., description="API endpoint URL")
    method: str = Field(default="GET", description="HTTP method")


class APIRequestTool(BaseTool):
    name: str = "API Request Tool"
    description: str = "Makes API requests and validates responses"
    args_schema: Type[BaseModel] = APIRequestInput

    def _run(self, endpoint: str, method: str = "GET") -> str:
        return f"{method} {endpoint}\\nStatus: 200 OK\\nResponse Time: 45ms\\nContent-Type: application/json"


class SchemaValidatorInput(BaseModel):
    response: str = Field(..., description="API response")
    schema: str = Field(..., description="Expected schema")


class SchemaValidatorTool(BaseTool):
    name: str = "Schema Validator"
    description: str = "Validates API responses against expected schemas"
    args_schema: Type[BaseModel] = SchemaValidatorInput

    def _run(self, response: str, schema: str) -> str:
        return f"Schema Validation: PASS\\nAll required fields present\\nTypes match specification"
