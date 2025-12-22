from crewai import Task
from textwrap import dedent

class ZerodhaMCPTasks:
    def fetch_market_data_task(self, agent, symbols):
        return Task(
            description=dedent(f"""
                Fetch real-time market data for specified symbols.

                Symbols: {symbols}

                Steps:
                1. Connect to Kite API
                2. Fetch current quotes for symbols
                3. Retrieve market depth information
                4. Get historical data if needed
                5. Format and return market data
            """),
            agent=agent,
            expected_output="Comprehensive market data with quotes, depth, and historical information"
        )

    def execute_order_task(self, agent, order_details):
        return Task(
            description=dedent(f"""
                Execute a trading order through Kite API.

                Order Details: {order_details}

                Steps:
                1. Validate order parameters
                2. Check account margins
                3. Place order through Kite API
                4. Receive and validate order confirmation
                5. Return order status and details
            """),
            agent=agent,
            expected_output="Order execution confirmation with order ID and status"
        )

    def analyze_portfolio_task(self, agent):
        return Task(
            description=dedent("""
                Analyze current portfolio holdings and positions.

                Steps:
                1. Fetch current holdings
                2. Get open positions
                3. Calculate portfolio metrics
                4. Analyze performance and P&L
                5. Generate portfolio report
            """),
            agent=agent,
            expected_output="Detailed portfolio analysis with holdings, positions, and performance"
        )

    def manage_risk_task(self, agent, positions):
        return Task(
            description=dedent(f"""
                Monitor and manage trading risk for current positions.

                Positions: {positions}

                Steps:
                1. Calculate current exposure
                2. Assess position sizes
                3. Check margin utilization
                4. Identify risk concentrations
                5. Recommend risk mitigation actions
            """),
            agent=agent,
            expected_output="Risk assessment report with recommendations"
        )

    def integrate_mcp_task(self, agent, mcp_request):
        return Task(
            description=dedent(f"""
                Process MCP request and integrate with Kite API.

                MCP Request: {mcp_request}

                Steps:
                1. Parse MCP request
                2. Map to Kite API operations
                3. Execute API calls
                4. Format response for MCP
                5. Return MCP-compliant response
            """),
            agent=agent,
            expected_output="MCP-formatted response with Kite API data"
        )
