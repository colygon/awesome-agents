# GOAT SDK CrewAI Solana Agent

**Gallery ID:** 498
**Category:** CrewAI
**Language:** Python
**Framework:** GOAT SDK + CrewAI

## Overview

This example demonstrates how to integrate GOAT SDK with CrewAI to build autonomous AI agents that interact with blockchain networks. The agent queries Solana SPL token balances and provides intelligent analysis through natural language interaction.

**GOAT (The Greatest of All Time)** is the largest agentic finance toolkit designed specifically for AI agents, enabling them to become economic actors by participating in real financial activities on blockchain networks.

## External Repository

**Repository:** https://github.com/goat-sdk/goat/tree/main/python/examples/by-framework/crewai
**Main Project:** https://github.com/goat-sdk/goat
**License:** MIT
**Documentation:** https://ohmygoat.dev

## Key Features

- **Autonomous Blockchain Querying**: Natural language interface for on-chain data
- **Solana SPL Token Intelligence**: Query token balances and analyze token data
- **CrewAI Integration**: Full adapter support to bridge GOAT tools into CrewAI agents
- **Wallet Abstraction**: Keypair-based authentication and Solana RPC connectivity
- **Interactive CLI**: User-friendly conversational interface for blockchain queries
- **Secure Key Management**: Delegated signer patterns for key separation
- **OpenAI LLM Integration**: Advanced reasoning and natural language processing

## What is GOAT SDK?

GOAT is an open-source, MIT-licensed framework that empowers AI agents to:

- **Transmit Value**: Send/receive payments across multiple blockchains
- **Make Purchases**: Buy physical and digital goods and services
- **Invest**: Earn yields, participate in prediction markets, acquire crypto assets
- **Create Assets**: Tokenize and create new digital assets
- **Gather Insights**: Access financial analytics and on-chain data

### Supported Blockchains

- Ethereum and all EVM-compatible chains
- Solana (featured in this example)
- Aptos, Sui, Starknet
- Chromia, Cosmos, Fuel, Radix, Zetrix, Zilliqa, MultiversX

### 70+ Plugin Integrations

**DEX & Swapping:** Uniswap, Jupiter, 0x, Balancer, Avnu, Enso, KIM, Balmy

**Yield & Lending:** Aave, Ionic, Superfluid, Renzo, Orca, Meteora

**Trading & Markets:** Polymarket, BetSwirl

**Token Creation:** Pump.fun, Solana token creation

**Data & Analytics:** CoinGecko, DexScreener, Nansen, BirdEye, OpenSea

**Cross-Chain:** DeBridge, Mayan

## This Example Demonstrates

The example creates an interactive CLI application that:

1. Initializes a Solana wallet using GOAT's wallet abstraction
2. Activates GOAT's SPL token plugin for Solana compatibility
3. Generates CrewAI-compatible tools through GOAT's adapter
4. Deploys a "Solana SPL Token Analyst" agent with blockchain querying capabilities
5. Provides an interactive loop for natural language queries like:
   - "What is the balance of USDC for my wallet?"
   - "Show me my SPL token holdings"
   - "What tokens do I own?"

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/goat-sdk/goat.git
cd python/examples/by-framework/crewai
```

### 2. Configure Environment

```bash
cp .env.template .env
```

Edit `.env` and add:
- `OPENAI_API_KEY` - Required by CrewAI's default configuration
- `SOLANA_WALLET_SEED` - Your Solana wallet's private key (base58 format)
- `SOLANA_RPC_ENDPOINT` - Your Solana RPC provider URL

### 3. Install Dependencies

```bash
poetry install
```

### 4. Run the Agent

```bash
poetry run python example.py
```

## Usage

The script runs an interactive loop where you can ask questions like:

```
> What is the balance of USDC for my wallet?
> Show me all my SPL token holdings
> What is the current balance of SOL?
```

Type 'quit' to exit the script.

## Technical Stack

**Dependencies:**
- Python 3.11-3.12
- CrewAI 0.108.0+
- GOAT SDK 0.1.0 (core)
- GOAT SDK Wallet Solana 0.1.0
- GOAT SDK Adapter CrewAI 0.1.0+
- python-dotenv 1.0.1+
- OpenAI API

**Architecture:**
- Solana wallet with base58-formatted private key
- SPL token plugin for token balance queries
- CrewAI agent: "Solana SPL Token Analyst"
- Sequential task execution
- Real-time blockchain data retrieval

## Agent Architecture

**Agent Role:** Solana SPL Token Analyst

**Goal:** Answer user questions about SPL token data

**Tools:**
- GOAT-provided tools for SPL token queries
- Blockchain data retrieval utilities
- On-chain data synthesis tools

**Execution:** Sequential task execution through CrewAI's task runner

## Advanced Features

### Agent Wallets with Crossmint

[Crossmint](https://docs.crossmint.com/wallets/quickstarts/agent-wallets) offers advanced solutions for agent developers:

- **Agent Wallets**: One of the most advanced wallet solutions for AI agents
- **Agent Launchpad**: Starter kit for building agent platforms
- **EVM and Solana Support**: Multi-chain wallet integration

See the GOAT SDK examples for:
- [Crossmint EVM Integration](https://github.com/goat-sdk/goat/tree/main/python/examples/by-wallet/crossmint)
- [Crossmint Solana Integration](https://github.com/goat-sdk/goat/tree/main/python/examples/by-wallet/crossmint)
- [Agent Launchpad Starter Kit](https://github.com/Crossmint/agent-launchpad-starter-kit/)

### Delegated Signer Pattern

For enhanced security, GOAT supports delegated signer patterns that separate:
- Hot wallet (for signing transactions)
- Cold wallet (for holding assets)
- Agent decision-making layer

## Framework Support

Beyond CrewAI, GOAT SDK integrates with:
- Langchain
- Vercel AI
- LlamaIndex
- Mastra
- OpenAI Agents SDK
- Eliza
- GAME Agent

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - CrewAI patterns
- [CrewAI-MCP (agent494)](../crewai-mcp-agent494/) - MCP research assistant
- [MCP Crew AI Server (agent496)](../mcp-crew-ai-agent496/) - MCP + CrewAI orchestration

## Use Cases

- **Portfolio Management**: Query and analyze token holdings
- **Trading Bots**: Autonomous trading decisions based on on-chain data
- **DeFi Assistants**: Interact with lending, yield, and swap protocols
- **Token Analytics**: Real-time token balance and metadata queries
- **Wallet Management**: Multi-wallet portfolio tracking
- **Prediction Markets**: Participate in Polymarket and other platforms
- **NFT Operations**: Query and manage NFT holdings

## Why GOAT SDK?

**Lightweight & Extendable**: Install only the components you need

**Language Agnostic**: Python and TypeScript support with more coming

**200+ Integrations**: Comprehensive blockchain ecosystem coverage

**Production Ready**: Battle-tested with error handling and security best practices

**Open Source**: MIT licensed, community-driven development

## Credits

**Project:** GOAT SDK
**Repository:** https://github.com/goat-sdk/goat
**License:** MIT
**Framework:** CrewAI + GOAT SDK
**Documentation:** https://ohmygoat.dev

## Learn More

- [GOAT SDK Documentation](https://ohmygoat.dev)
- [CrewAI Documentation](https://docs.crewai.com)
- [Solana Documentation](https://docs.solana.com)
- [GOAT Python Examples](https://github.com/goat-sdk/goat/tree/main/python/examples)
