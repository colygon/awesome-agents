"""CRM Q&A Agent - CrewAI Tools"""
from crewai_tools import tool

@tool("CRM Query Builder")
def build_crm_query(intent: str, entities: list) -> dict:
    return {"query": "SELECT * FROM contacts", "parameters": []}

@tool("CRM Data Fetcher")
def fetch_crm_data(query: str) -> list:
    return [{"name": "Sample Contact", "email": "contact@example.com"}]
