"""
McLachApp Configuration
Application settings and configuration management
"""

import os
from typing import Optional


class Config:
    """Application configuration class"""

    # API Configuration
    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4")
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))

    # CrewAI Configuration
    CREWAI_VERBOSE: bool = os.getenv("CREWAI_VERBOSE", "True").lower() == "true"
    MAX_ITERATIONS: int = int(os.getenv("MAX_ITERATIONS", "5"))

    # Application Configuration
    APP_NAME: str = "McLachApp"
    APP_VERSION: str = "2.0.0-crewai"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"

    @classmethod
    def validate(cls) -> bool:
        """
        Validate configuration settings

        Returns:
            bool: True if configuration is valid
        """
        if not cls.OPENAI_API_KEY:
            return False
        return True

    @classmethod
    def get_llm_config(cls) -> dict:
        """
        Get LLM configuration as a dictionary

        Returns:
            dict: LLM configuration parameters
        """
        return {
            "model": cls.OPENAI_MODEL,
            "temperature": cls.OPENAI_TEMPERATURE,
            "api_key": cls.OPENAI_API_KEY
        }

    @classmethod
    def print_config(cls):
        """Print current configuration (hiding sensitive data)"""
        print("\n" + "="*80)
        print(f"{cls.APP_NAME} v{cls.APP_VERSION} - Configuration")
        print("="*80)
        print(f"OpenAI Model: {cls.OPENAI_MODEL}")
        print(f"Temperature: {cls.OPENAI_TEMPERATURE}")
        print(f"API Key Set: {'Yes' if cls.OPENAI_API_KEY else 'No'}")
        print(f"Verbose Mode: {cls.CREWAI_VERBOSE}")
        print(f"Max Iterations: {cls.MAX_ITERATIONS}")
        print(f"Debug Mode: {cls.DEBUG}")
        print("="*80 + "\n")
