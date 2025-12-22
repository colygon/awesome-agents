# 21st.dev Magic AI Agent

**Gallery ID:** 497
**Category:** AI-Powered UI Component Generator
**Language:** TypeScript/Node.js

## Overview

21st.dev Magic AI Agent is a powerful AI-driven tool that helps developers create beautiful, modern UI components instantly through natural language descriptions. Built on the Model Context Protocol (MCP), it integrates seamlessly with popular IDEs and provides a streamlined workflow for UI development.

## External Repository

**Repository:** https://github.com/21st-dev/magic-mcp
**Website:** https://21st.dev/magic
**License:** MIT

## Key Features

- **AI-Powered UI Generation**: Create components via natural language descriptions
- **Multi-IDE Support**:
  - Cursor IDE integration
  - Windsurf support
  - VSCode support
  - VSCode + Cline integration (Beta)
- **Modern Component Library**: Vast collection of pre-built, customizable components
- **Real-time Preview**: Instantly see components as you create them
- **TypeScript Support**: Full TypeScript support for type-safe development
- **SVGL Integration**: Access to professional brand assets and logos
- **Component Enhancement**: Improve existing components (Coming Soon)

## How It Works

1. **Describe What You Need**
   - Type `/ui` in your IDE chat
   - Describe the component: "create a modern navigation bar with responsive design"

2. **Let Magic Create It**
   - IDE prompts you to use Magic
   - Component is instantly built
   - Inspired by 21st.dev's library

3. **Seamless Integration**
   - Components automatically added to your project
   - Fully customizable
   - Ready to use immediately

## Installation

### Prerequisites

- Node.js (Latest LTS version)
- Supported IDE: Cursor, Windsurf, or VSCode (with Cline)

### Method 1: CLI Installation (Recommended)

```bash
npx @21st-dev/cli@latest install <client> --api-key <key>
```

Supported clients: cursor, windsurf, cline, claude

### Method 2: Manual Configuration

Add to your IDE's MCP config file:

```json
{
  "mcpServers": {
    "@21st-dev/magic": {
      "command": "npx",
      "args": ["-y", "@21st-dev/magic@latest", "API_KEY=\"your-api-key\""]
    }
  }
}
```

**Config file locations:**
- Cursor: `~/.cursor/mcp.json`
- Windsurf: `~/.codeium/windsurf/mcp_config.json`
- Cline: `~/.cline/mcp_config.json`
- Claude: `~/.claude/mcp_config.json`

### Method 3: VS Code One-Click Install

Click install buttons at: https://github.com/21st-dev/magic-mcp

## Getting Started

1. **Generate API Key**: Visit https://21st.dev/magic/console
2. **Install**: Use CLI or manual configuration
3. **Start Creating**: Type `/ui` followed by your component description

## Use Cases

- **Rapid Prototyping**: Quickly build UI mockups
- **Component Libraries**: Generate consistent design systems
- **Learning**: See best practices in generated code
- **Productivity**: Save hours on boilerplate UI code
- **Design Systems**: Build cohesive component sets

## FAQ

**How does Magic handle my codebase?**
Only writes/modifies files for generated components. Follows your project's style and structure.

**Can I customize components?**
Yes! All components are fully editable with well-structured code.

**What happens if I run out of generations?**
Upgrade your plan to continue. Existing components remain functional.

**Component complexity limits?**
Handles varying complexity. Best results with smaller, manageable components.

## Project Structure

```
mcp/
├── app/
│   └── components/     # Core UI components
├── types/              # TypeScript definitions
├── lib/                # Utility functions
└── public/             # Static assets
```

## Community & Support

- **Discord**: https://discord.gg/Qx4rFunHfm
- **Twitter**: https://x.com/serafimcloud
- **Website**: https://21st.dev/magic

## Beta Notice

Magic Agent is currently in beta. All features are free during this period.

## Related Gallery Entries

- [CrewAI-MCP (agent494)](../crewai-mcp-agent494/) - MCP with CrewAI
- [Claude-CrewAI-MCP (agent495)](../claude-crewai-mcp-agent495/) - Claude Desktop MCP
- [MCP Crew AI Server (agent496)](../mcp-crew-ai-agent496/) - CrewAI MCP server

## Credits

**Organization:** 21st.dev / Serafim Cloud
**Repository:** https://github.com/21st-dev/magic-mcp
**License:** MIT
**Framework:** Model Context Protocol
**Integration:** SVGL, 21st.dev component library

## Acknowledgments

- Cursor, Windsurf, and Cline teams for collaboration
- 21st.dev for component inspiration
- SVGL for logo and brand assets
- Beta testers and community members
