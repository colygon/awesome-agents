# Claude-CrewAI-MCP Server

**Gallery ID:** 495
**Category:** MCP Server for Claude Desktop
**Language:** Python

## Overview

Claude-CrewAI-MCP is a Model Context Protocol (MCP) server for Claude Desktop that instructs it on how to properly code Python projects using CrewAI. Built with FastMCP, it provides intelligent guidance and code generation capabilities for CrewAI development.

## External Repository

**Repository:** https://github.com/NahumKorda/Claude-CrewAI-MCP
**Author:** Nahum Korda
**License:** Open Source

## Key Features

- **MCP Server for Claude Desktop**: Integrates directly with Claude Desktop app
- **FastMCP Framework**: Built on FastMCP for robust MCP implementation
- **CrewAI Expertise**: Teaches Claude how to properly structure CrewAI projects
- **Code Generation**: Generates proper CrewAI Python code patterns
- **Best Practices**: Enforces CrewAI development best practices

## Installation

Add to your Claude Desktop configuration file (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "CrewaiMcpServer": {
      "command": "path/to/venv/with/installed/fastmcp",
      "args": ["path/to/crewai_mcp_server.py"]
    }
  }
}
```

Detailed instructions: https://modelcontextprotocol.io/quickstart/user

## Usage

1. Configure the MCP server in Claude Desktop
2. Restart Claude Desktop completely
3. Ask Claude to help with CrewAI projects
4. Claude will use the MCP server for proper CrewAI code generation

## Contributing

Contributions welcome! See repository for details:
- Fork the repository
- Create a feature branch
- Submit a pull request

For collaboration inquiries, contact via GitHub Issues.

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - CrewAI examples
- [MCP Crew AI Server (agent496)](../mcp-crew-ai-agent496/) - Alternative MCP server

## Credits

**Author:** Nahum Korda
**Repository:** https://github.com/NahumKorda/Claude-CrewAI-MCP
**Framework:** FastMCP + CrewAI
**IDE:** Claude Desktop
