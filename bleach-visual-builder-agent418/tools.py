"""Bleach Visual Builder Tools"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class DesignInput(BaseModel):
    style: str = Field(..., description="Design style")
    colors: str = Field(default="auto", description="Color preferences")


class DesignSystemTool(BaseTool):
    name: str = "Design System Tool"
    description: str = "Creates design systems with colors, typography, and spacing"
    args_schema: Type[BaseModel] = DesignInput

    def _run(self, style: str, colors: str = "auto") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.6)
            prompt = f"""Create design system for {style} style:
            1. Color palette (primary, secondary, neutrals)
            2. Typography scale (headings, body, etc.)
            3. Spacing scale (4px, 8px, 16px, etc.)
            4. Border radius and shadows
            5. Design tokens"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class ComponentInput(BaseModel):
    component_type: str = Field(..., description="Component type")


class ComponentGeneratorTool(BaseTool):
    name: str = "Component Generator Tool"
    description: str = "Generates UI component specifications"
    args_schema: Type[BaseModel] = ComponentInput

    def _run(self, component_type: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
            prompt = f"""Design {component_type} component:
            1. Variants (primary, secondary, etc.)
            2. States (default, hover, active, disabled)
            3. Sizes (small, medium, large)
            4. Props/API
            5. Usage examples"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class CodeGenInput(BaseModel):
    design_spec: str = Field(..., description="Design specification")
    framework: str = Field(default="React", description="Framework")


class CodeGeneratorTool(BaseTool):
    name: str = "Code Generator Tool"
    description: str = "Generates frontend code from designs"
    args_schema: Type[BaseModel] = CodeGenInput

    def _run(self, design_spec: str, framework: str = "React") -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Generate {framework} code for: {design_spec}
            Include:
            1. Component code
            2. Styles (CSS/Tailwind)
            3. Props and types
            4. Accessibility attributes
            5. Responsive utilities"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
