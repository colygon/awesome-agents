# Safety Plugins Agent - CrewAI Edition

## Migration from Google ADK to CrewAI

This application has been migrated from Google's Agent Development Kit (ADK) to CrewAI, implementing a comprehensive content safety analysis system with multiple specialized agents.

## Overview

The Safety Plugins Agent provides multi-dimensional safety analysis for user-generated content, helping platforms maintain safe and inclusive communities. It analyzes:

1. **Toxicity Detection** - Identifies toxic, offensive, or harmful language
2. **Content Moderation** - Checks for policy violations (violence, adult content, hate speech, etc.)
3. **Privacy Protection** - Detects personally identifiable information (PII) and sensitive data
4. **Bias Analysis** - Identifies bias, stereotypes, and fairness issues

## Architecture

### CrewAI Agents

1. **Content Moderator Agent** - Reviews content against moderation policies
2. **Toxicity Analyzer Agent** - Detects toxic and offensive language
3. **Sensitive Info Guardian Agent** - Identifies PII and privacy risks
4. **Bias Detector Agent** - Analyzes bias and fairness issues
5. **Safety Coordinator Agent** - Synthesizes findings into unified recommendations

### Custom Tools

1. **ContentModerationTool** - Policy violation detection
2. **ToxicityDetectionTool** - Multi-dimensional toxicity scoring
3. **ProfanityFilterTool** - Profanity detection
4. **SensitiveInfoDetectorTool** - PII and sensitive data detection
5. **BiasDetectionTool** - Bias and stereotype identification

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

```bash
cd safety-plugins-agent403
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

## Usage

### Interactive Mode

```bash
python main.py
```

### File Analysis

```bash
python main.py path/to/content.txt
```

### With Context

```bash
python main.py content.txt '{"source": "user_comment", "platform": "forum"}'
```

## Example Output

```
SAFETY ANALYSIS COMPLETE
================================================================================

Overall Safety Score: 65/100

Critical Issues:
- Privacy Risk: 2 email addresses detected
- Toxicity: Moderate level of aggressive language

Moderate Issues:
- Gender Bias: Use of non-inclusive terms detected

Final Recommendation: FLAG_FOR_REVIEW
- Redact email addresses
- Review toxic language in context
- Consider rephrasing for inclusivity

Priority Level: HIGH
```

## Benefits of CrewAI Migration

1. **Specialized Analysis** - Dedicated agents for each safety dimension
2. **Comprehensive Coverage** - Multi-faceted safety assessment
3. **Transparent Decisions** - Clear reasoning for safety determinations
4. **Customizable Policies** - Easy to adjust moderation criteria
5. **Platform Independence** - No Google Cloud dependency

## Production Recommendations

For production deployment, integrate with specialized APIs:

- **Toxicity**: Perspective API, Detoxify
- **Moderation**: OpenAI Moderation API, Azure Content Safety
- **PII Detection**: Microsoft Presidio, AWS Comprehend, Google DLP API
- **Bias**: IBM AI Fairness 360, Google What-If Tool

## License

Apache 2.0

---

**Migration Date:** December 2025
**CrewAI Version:** 0.86.0+
