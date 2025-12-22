# Zerodha MCP - CrewAI Implementation

## Overview
A multi-agent system integrating Zerodha/Kite API with Model Context Protocol for automated trading operations.

## Agents

### 1. Market Data Specialist
- Fetches real-time market data
- Retrieves quotes and depth
- Accesses historical data

### 2. Order Management Specialist
- Executes trading orders
- Manages order lifecycle
- Handles order modifications

### 3. Portfolio Analyst
- Tracks holdings and positions
- Analyzes performance
- Calculates portfolio metrics

### 4. Risk Manager
- Monitors exposure levels
- Calculates position sizes
- Ensures risk compliance

### 5. MCP Integration Specialist
- Bridges Kite API with MCP
- Formats MCP responses
- Manages protocol integration

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your Kite API credentials
```

3. Get Kite API credentials from: https://kite.trade

4. Run the system:
```bash
python main.py
```

## Features
- Real-time market data access
- Order execution and management
- Portfolio tracking
- Risk management
- MCP protocol integration
- Position monitoring

## Kite API Operations
- Quote fetching
- Order placement
- Holdings retrieval
- Position tracking
- Margin checking
- Historical data access

## Use Cases
- Automated trading systems
- Portfolio management
- Market data analysis
- Risk monitoring
- Trading strategy execution

## Security Notes
- Keep API credentials secure
- Use environment variables
- Enable 2FA on Zerodha account
- Monitor API usage limits
- Implement rate limiting

## Disclaimer
This is for educational purposes. Trading involves risk. Always test with paper trading first.
