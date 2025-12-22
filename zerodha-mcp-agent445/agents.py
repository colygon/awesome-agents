from crewai import Agent
from tools import (
    kite_api_connector,
    market_data_fetcher,
    order_executor,
    portfolio_analyzer,
    risk_manager
)

class ZerodhaMCPAgents:
    def market_data_agent(self):
        return Agent(
            role='Market Data Specialist',
            goal='Fetch and analyze real-time market data from Zerodha/Kite',
            backstory="""You are an expert in accessing and analyzing market
            data through the Zerodha Kite API. You fetch quotes, historical data,
            and market depth information efficiently.""",
            tools=[kite_api_connector, market_data_fetcher],
            verbose=True,
            allow_delegation=False
        )

    def order_management_agent(self):
        return Agent(
            role='Order Management Specialist',
            goal='Execute and manage trading orders through Kite API',
            backstory="""You are a trading operations expert who manages order
            placement, modification, and cancellation. You ensure orders are
            executed according to specifications and handle error cases.""",
            tools=[order_executor, kite_api_connector],
            verbose=True,
            allow_delegation=False
        )

    def portfolio_agent(self):
        return Agent(
            role='Portfolio Analyst',
            goal='Analyze portfolio holdings and positions',
            backstory="""You are a portfolio analysis expert who tracks holdings,
            positions, and portfolio performance. You provide insights into
            portfolio composition and performance metrics.""",
            tools=[portfolio_analyzer, market_data_fetcher],
            verbose=True,
            allow_delegation=True
        )

    def risk_management_agent(self):
        return Agent(
            role='Risk Manager',
            goal='Monitor and manage trading risks',
            backstory="""You are a risk management specialist who monitors
            exposure, calculates position sizes, and ensures trading stays
            within risk parameters.""",
            tools=[risk_manager, portfolio_analyzer],
            verbose=True,
            allow_delegation=True
        )

    def mcp_integration_agent(self):
        return Agent(
            role='MCP Integration Specialist',
            goal='Integrate Zerodha/Kite with Model Context Protocol',
            backstory="""You are an integration expert who bridges the Zerodha
            Kite API with the Model Context Protocol, enabling seamless
            access to trading functions through MCP.""",
            tools=[kite_api_connector, market_data_fetcher],
            verbose=True,
            allow_delegation=True
        )
