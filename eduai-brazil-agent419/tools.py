"""Edu.AI Brazil Tools"""

from crewai_tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI


class BrazilEdInput(BaseModel):
    level: str = Field(..., description="Nível educacional")
    subject: str = Field(..., description="Disciplina")


class BrazilEducationTool(BaseTool):
    name: str = "Brazil Education System Tool"
    description: str = "Fornece informações sobre sistema educacional brasileiro"
    args_schema: Type[BaseModel] = BrazilEdInput

    def _run(self, level: str, subject: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.3)
            prompt = f"""Informações sobre educação brasileira para {subject} - {level}:
            1. Estrutura do sistema educacional
            2. Requisitos BNCC
            3. Competências e habilidades
            4. Carga horária típica
            5. Métodos avaliativos"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Erro: {str(e)}"


class CurriculumBRInput(BaseModel):
    subject: str = Field(..., description="Disciplina")
    level: str = Field(..., description="Nível")


class CurriculumBrasilTool(BaseTool):
    name: str = "Curriculum Brasil Tool"
    description: str = "Cria currículos alinhados com BNCC"
    args_schema: Type[BaseModel] = CurriculumBRInput

    def _run(self, subject: str, level: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.4)
            prompt = f"""Criar currículo BNCC para {subject} - {level}:
            1. Competências gerais
            2. Competências específicas
            3. Objetos de conhecimento
            4. Habilidades (códigos BNCC)
            5. Unidades temáticas"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Erro: {str(e)}"


class AssessmentBRInput(BaseModel):
    subject: str = Field(..., description="Disciplina")
    topic: str = Field(..., description="Tópico")


class AssessmentBRTool(BaseTool):
    name: str = "Assessment Brasil Tool"
    description: str = "Cria avaliações para educação brasileira"
    args_schema: Type[BaseModel] = AssessmentBRInput

    def _run(self, subject: str, topic: str) -> str:
        try:
            llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.5)
            prompt = f"""Criar avaliação brasileira para {subject} - {topic}:
            1. Questões objetivas (múltipla escolha)
            2. Questões discursivas
            3. Questões contextualizadas
            4. Rubrica de avaliação
            5. Gabarito comentado"""
            response = llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Erro: {str(e)}"
