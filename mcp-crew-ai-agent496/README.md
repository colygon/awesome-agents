# MCP Crew AI Server

**Gallery ID:** 496
**Category:** CrewAI MCP Server
**Language:** Python

## Overview

MCP Crew AI Server is a lightweight Python-based server designed to run, manage, and create CrewAI workflows. It leverages the Model Context Protocol (MCP) to communicate with LLMs and tools such as Claude Desktop or Cursor IDE, enabling easy orchestration of multi-agent workflows through YAML configuration.

## External Repository

**Repository:** https://github.com/adam-paterson/mcp-crew-ai
**Author:** Adam Paterson
**License:** MIT
**PyPI:** https://pypi.org/project/mcp-crew-ai/

## Key Features

- **Automatic Configuration**: Loads agent and task configurations from YAML files
- **Command Line Flexibility**: Custom paths via `--agents` and `--tasks` arguments
- **Seamless Workflow Execution**: Run workflows through MCP `run_workflow` tool
- **Local Development**: STDIO mode for development and testing
- **PyPI Package**: Available via `pip install mcp-crew-ai`
- **Multi-IDE Support**: Works with Claude Desktop, Cursor IDE, and more

## Installation

### Option 1: Install from PyPI (Recommended)

```bash
pip install mcp-crew-ai
```

### Option 2: Install from GitHub

```bash
pip install git+https://github.com/adam-paterson/mcp-crew-ai.git
```

### Option 3: Clone and Install

```bash
git clone https://github.com/adam-paterson/mcp-crew-ai.git
cd mcp-crew-ai
pip install -e .
```

## Configuration

### agents.yml

Define agents with roles, goals, and backstories:

```yaml
zookeeper:
  role: Zookeeper
  goal: Manage zoo operations
  backstory: >
    You are a seasoned zookeeper with a passion for wildlife conservation...
```

### tasks.yml

Define tasks with descriptions and assignments:

```yaml
write_stories:
  description: >
    Write an engaging zoo update capturing the day's highlights.
  expected_output: 5 engaging stories
  agent: zookeeper
  output_file: zoo_report.md
```

## Usage

### Standard Python Command

```bash
mcp-crew-ai --agents path/to/agents.yml --tasks path/to/tasks.yml
```

### Using UV Execution (uvx)

```bash
uvx mcp-crew-ai --agents path/to/agents.yml --tasks path/to/tasks.yml
```

### Command Line Options

- `--agents`: Path to agents YAML file (required)
- `--tasks`: Path to tasks YAML file (required)
- `--topic`: Main topic for the crew (default: "Artificial Intelligence")
- `--process`: Process type ("sequential" or "hierarchical")
- `--verbose`: Enable verbose output
- `--variables`: JSON string or file with template variables
- `--version`: Show version information

### Advanced Usage

With template variables:

```bash
mcp-crew-ai --agents examples/agents.yml --tasks examples/tasks.yml --topic "Machine Learning" --variables '{"year": 2025, "focus": "deep learning"}'
```

## Requirements

- Python 3.11+
- MCP SDK
- CrewAI
- PyYAML

## Related Gallery Entries

- [Claude Agent Basic (agent488)](../claude-agent-basic-agent488/) - CrewAI patterns
- [CrewAI-MCP (agent494)](../crewai-mcp-agent494/) - MCP research assistant
- [Claude-CrewAI-MCP (agent495)](../claude-crewai-mcp-agent495/) - Claude Desktop MCP

## Credits

**Author:** Adam Paterson
**Repository:** https://github.com/adam-paterson/mcp-crew-ai
**License:** MIT
**Framework:** Model Context Protocol + CrewAI
