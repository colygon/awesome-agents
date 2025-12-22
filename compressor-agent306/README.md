# Files Compressor Tool - CrewAI Agent System

A sophisticated multi-agent system powered by CrewAI for intelligent file compression and archive management. This application uses three specialized AI agents working collaboratively to optimize file compression strategies.

## Overview

This project demonstrates the integration of CrewAI's agent framework with file compression operations, providing intelligent strategy formulation, execution management, and optimization analysis.

## Architecture

### Specialized Agents

1. **Compression Strategist Agent**
   - Analyzes file structures and compression needs
   - Recommends optimal compression formats and levels
   - Considers trade-offs between ratio, speed, and compatibility
   - Provides compression estimates

2. **Archive Manager Agent**
   - Executes compression operations
   - Manages file and directory processing
   - Ensures data integrity during compression
   - Handles error recovery and validation

3. **Optimization Analyst Agent**
   - Analyzes compression results
   - Identifies optimization opportunities
   - Provides efficiency metrics
   - Recommends future improvements

## Features

- Multi-agent collaborative workflow using CrewAI
- Intelligent compression strategy formulation
- Sequential task processing with context sharing
- Interactive command-line interface
- Comprehensive error handling
- Environment-based configuration
- Detailed logging and verbose output

## Installation

```bash
# Navigate to the project directory
cd compressor-agent306

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your OpenAI API key
```

## Configuration

Edit the `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the interactive application:

```bash
python main.py
```

### Example Requests

- "Compress log files from /var/logs older than 30 days"
- "Create a backup archive of my project directory"
- "Compress database dumps with maximum compression"
- "Archive photos for long-term storage with good compression"

## Project Structure

```
compressor-agent306/
├── agents.py              # Agent definitions
├── tasks.py               # Task specifications
├── main.py                # Main application
├── requirements.txt       # Python dependencies
├── .env.example           # Environment template
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── COMPLETION_REPORT.md   # Detailed completion report
└── CREWAI_UPGRADE.md      # CrewAI integration documentation
```

## Dependencies

- `crewai>=0.86.0` - Multi-agent framework
- `langchain-openai>=0.3.0` - LLM integration
- `python-dotenv>=1.0.0` - Environment management
- `openai>=1.0.0` - OpenAI API client

## How It Works

1. **Request Input**: User describes compression requirements
2. **Strategy Formulation**: Strategist analyzes and creates plan
3. **Execution**: Archive Manager executes compression
4. **Analysis**: Optimization Analyst reviews results
5. **Output**: User receives comprehensive analysis and recommendations

## Advanced Features

- Context-aware task dependencies
- Sequential process orchestration
- Verbose output for transparency
- Customizable LLM temperature settings
- Multi-format support (ZIP, TAR, GZIP, BZIP2, 7Z)

## License

MIT License - Feel free to use and modify for your projects

## Author

Agent 306 - Files Compressor Tool
Part of the CrewAI Tools demonstration series

## Support

For issues, questions, or contributions, please refer to the project documentation.
