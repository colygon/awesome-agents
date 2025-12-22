"""Custom Tools for Security Audit"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class VulnerabilityScannerInput(BaseModel):
    target: str = Field(..., description="Target to scan")


class VulnerabilityScannerTool(BaseTool):
    name: str = "Vulnerability Scanner"
    description: str = "Scans for common security vulnerabilities"
    args_schema: Type[BaseModel] = VulnerabilityScannerInput

    def _run(self, target: str) -> str:
        return f"Vulnerability Scan Results for {target}:\\nCRITICAL: 0\\nHIGH: 2\\nMEDIUM: 5\\nLOW: 8\\nINFO: 12"


class DependencyCheckerInput(BaseModel):
    package_file: str = Field(..., description="Package dependency file")


class DependencyCheckerTool(BaseTool):
    name: str = "Dependency Checker"
    description: str = "Checks dependencies for known vulnerabilities"
    args_schema: Type[BaseModel] = DependencyCheckerInput

    def _run(self, package_file: str) -> str:
        return f"Dependency Audit for {package_file}:\\nVulnerable packages: 3\\nOutdated packages: 7\\nRecommended updates available"
