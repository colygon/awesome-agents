# Emoji Shortcodes with CrewAI

Enhanced version of the Streamlit Emoji Shortcodes app with AI-powered emoji analysis and recommendations using CrewAI.

## Features

### Original Features
- Browse all supported Streamlit emoji shortcodes
- View emoji-to-shortcode mappings
- Search and discover emojis

### New CrewAI Features
- **Smart Emoji Recommendations**: Get AI-powered emoji suggestions for your text based on context and tone
- **Emoji Analysis**: Deep analysis of emoji meanings, contexts, and cultural significance
- **Sentiment Analysis**: Understand the emotional tone of emoji-enhanced messages
- **Alternative Discovery**: Find similar or alternative emojis for any use case

## Multi-Agent System

This app uses 3 specialized CrewAI agents:

1. **Emoji Analyst Agent**: Analyzes emoji meanings, contexts, and cultural significance
2. **Recommendation Agent**: Provides intelligent emoji suggestions based on content and tone
3. **Usage Insights Agent**: Offers analytics and best practices for emoji communication

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements_crewai.txt
   ```

3. Set up your environment:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENAI_API_KEY
   ```

## Usage

Run the enhanced Streamlit app:
```bash
streamlit run streamlit_app_crewai.py
```

Or use the original app:
```bash
streamlit run streamlit_app.py
```

## Python API

You can also use the CrewAI features programmatically:

```python
from crew import recommend_emojis, analyze_emoji, analyze_sentiment

# Get emoji recommendations
result = recommend_emojis("I'm so happy today!", tone="happy")
print(result)

# Analyze an emoji
analysis = analyze_emoji("😊")
print(analysis)

# Analyze sentiment
sentiment = analyze_sentiment("Great work team! 🎉💪")
print(sentiment)
```

## Requirements

- Python 3.8+
- OpenAI API key
- CrewAI >= 0.86.0
- LangChain OpenAI >= 0.3.0

## Configuration

Edit `.env` to configure:
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `OPENAI_MODEL`: Model to use (default: gpt-4)
- `OPENAI_TEMPERATURE`: Creativity level (default: 0.7)

## License

Apache License 2.0

---

**Upgraded with CrewAI by Agent 81**
Generated with Claude Code
