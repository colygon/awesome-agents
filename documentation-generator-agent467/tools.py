"""Custom Tools for Documentation Generator"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class DocstringGeneratorInput(BaseModel):
    function_signature: str = Field(..., description="Function signature")
    code_body: str = Field(..., description="Function code body")


class DocstringGeneratorTool(BaseTool):
    name: str = "Docstring Generator"
    description: str = "Generates docstrings for functions and methods"
    args_schema: Type[BaseModel] = DocstringGeneratorInput

    def _run(self, function_signature: str, code_body: str) -> str:
        return f'''\"\"\"
        Brief description of {function_signature}

        Args:
            param1: Description
            param2: Description

        Returns:
            Return value description

        Raises:
            Exception: When error occurs
        \"\"\"'''


class APISpecParserInput(BaseModel):
    api_endpoint: str = Field(..., description="API endpoint path")


class APISpecParserTool(BaseTool):
    name: str = "API Spec Parser"
    description: str = "Parses API specifications and generates documentation"
    args_schema: Type[BaseModel] = APISpecParserInput

    def _run(self, api_endpoint: str) -> str:
        return f"API Documentation for {api_endpoint}:\\nMethod: GET/POST\\nParameters: ...\\nResponse: ..."
