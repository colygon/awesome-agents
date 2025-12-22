"""
Custom Tools for Learning Content Creation
"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class CurriculumInput(BaseModel):
    subject: str = Field(..., description="Subject or topic")
    level: str = Field(..., description="Difficulty level")


class CurriculumDesignTool(BaseTool):
    name: str = "Curriculum Design Tool"
    description: str = "Designs learning curricula with objectives and modules"
    args_schema: Type[BaseModel] = CurriculumInput

    def _run(self, subject: str, level: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)
            prompt = f"""Design a curriculum for {subject} at {level} level.

            Include:
            1. Course title and description
            2. Learning objectives (SMART format)
            3. 6-10 modules with topics
            4. Prerequisite knowledge
            5. Assessment strategy
            6. Learning progression rationale"""

            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class ContentInput(BaseModel):
    module_topic: str = Field(..., description="Module topic")
    learning_objectives: str = Field(..., description="Learning objectives")


class ContentGeneratorTool(BaseTool):
    name: str = "Content Generator Tool"
    description: str = "Generates educational content for modules"
    args_schema: Type[BaseModel] = ContentInput

    def _run(self, module_topic: str, learning_objectives: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
            prompt = f"""Create educational content for: {module_topic}

            Objectives: {learning_objectives}

            Include:
            1. Introduction and context
            2. Core concepts (3-5)
            3. Examples and analogies
            4. Practice activities
            5. Summary and key points"""

            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"


class AssessmentInput(BaseModel):
    topic: str = Field(..., description="Topic to assess")
    objectives: str = Field(..., description="Learning objectives")


class AssessmentCreatorTool(BaseTool):
    name: str = "Assessment Creator Tool"
    description: str = "Creates assessments and quizzes"
    args_schema: Type[BaseModel] = AssessmentInput

    def _run(self, topic: str, objectives: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Create assessment for: {topic}

            Objectives: {objectives}

            Include:
            1. 10 multiple choice questions
            2. 5 short answer questions
            3. 2 essay/application questions
            4. Rubric for grading
            5. Answer key"""

            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Error: {str(e)}"
