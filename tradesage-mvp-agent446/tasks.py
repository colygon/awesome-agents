from crewai import Task
from textwrap import dedent

class TradeSageTasks:
    def analyze_market_task(self, agent, symbol, timeframe):
        return Task(
            description=dedent(f"""
                Analyze market conditions for the specified symbol and timeframe.

                Symbol: {symbol}
                Timeframe: {timeframe}

                Steps:
                1. Fetch current market data
                2. Identify trend direction
                3. Find support and resistance levels
                4. Analyze volume patterns
                5. Summarize market conditions
            """),
            agent=agent,
            expected_output="Comprehensive market analysis with trend, levels, and conditions"
        )

    def generate_signals_task(self, agent, symbol, indicators):
        return Task(
            description=dedent(f"""
                Generate trading signals using technical indicators.

                Symbol: {symbol}
                Indicators: {indicators}

                Steps:
                1. Calculate specified technical indicators
                2. Identify crossovers and divergences
                3. Check for chart patterns
                4. Generate buy/sell signals
                5. Provide signal strength and confidence
            """),
            agent=agent,
            expected_output="Trading signals with entry/exit points and confidence levels"
        )

    def analyze_sentiment_task(self, agent, symbol):
        return Task(
            description=dedent(f"""
                Analyze market sentiment for the specified symbol.

                Symbol: {symbol}

                Steps:
                1. Gather news articles about the symbol
                2. Analyze social media sentiment
                3. Check options flow and positioning
                4. Assess institutional activity
                5. Provide overall sentiment score
            """),
            agent=agent,
            expected_output="Market sentiment analysis with bullish/bearish score"
        )

    def design_strategy_task(self, agent, requirements):
        return Task(
            description=dedent(f"""
                Design a trading strategy based on requirements.

                Requirements: {requirements}

                Steps:
                1. Define entry and exit rules
                2. Set risk management parameters
                3. Specify position sizing rules
                4. Add filters and conditions
                5. Document strategy logic
            """),
            agent=agent,
            expected_output="Complete trading strategy with rules and parameters"
        )

    def backtest_strategy_task(self, agent, strategy, symbol, period):
        return Task(
            description=dedent(f"""
                Backtest the trading strategy on historical data.

                Strategy: {strategy}
                Symbol: {symbol}
                Period: {period}

                Steps:
                1. Load historical data for the period
                2. Apply strategy rules to historical data
                3. Calculate performance metrics
                4. Analyze drawdowns and risk metrics
                5. Generate backtest report
            """),
            agent=agent,
            expected_output="Backtest results with performance metrics and analysis"
        )
