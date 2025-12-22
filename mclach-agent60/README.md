# McLachApp - Sports Analytics with CrewAI

Intelligent sports analytics platform powered by multi-agent AI systems using CrewAI.

## Quick Start

### Installation

```bash
# Clone the repository
cd /Users/colinlowenberg/crew
git clone <repository-url> mclach-agent60
cd mclach-agent60

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

### Run the Application

```bash
python main.py
```

## Features

### Three Specialized AI Agents

1. **Data Analyst Agent** - Statistical analysis and data processing
2. **Performance Evaluator Agent** - Player and team assessment
3. **Strategy Advisor Agent** - Tactical recommendations

### Analysis Capabilities

- Player performance analysis
- Team performance evaluation
- Player comparisons
- Match analysis
- Strategic recommendations

## Quick Example

```python
from crew import run_player_analysis

player_data = {
    "name": "John Doe",
    "position": "Forward",
    "games_played": 38,
    "goals": 25,
    "assists": 12
}

result = run_player_analysis(player_data)
print(result)
```

## Documentation

See [CREWAI_UPGRADE.md](CREWAI_UPGRADE.md) for comprehensive documentation including:
- Architecture overview
- Detailed agent descriptions
- Advanced usage examples
- Configuration options
- Troubleshooting guide

## Dependencies

Core requirements:
- crewai>=0.86.0
- langchain-openai>=0.3.0
- Python 3.8+
- OpenAI API key

## Project Structure

```
mclach-agent60/
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
├── crew.py                # Crew orchestration
├── main.py                # Application entry point
├── config.py              # Configuration
├── utils.py               # Utilities
├── requirements.txt       # Dependencies
├── CREWAI_UPGRADE.md     # Full documentation
└── README.md              # This file
```

## Contributing

Contributions are welcome! Please see [CREWAI_UPGRADE.md](CREWAI_UPGRADE.md) for development setup and guidelines.

## License

[Add your license here]

## Credits

- **Version:** 2.0.0-crewai
- **Upgraded by:** Agent 60
- **Framework:** CrewAI
- **Date:** December 2025
