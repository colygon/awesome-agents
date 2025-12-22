# Quick Start Guide - ADK Batch 381-390

## Overview
This batch contains 10 CrewAI implementations of ADK applications (IDs 381-390).

## Applications

| ID | Name | Status | Agents | Use Case |
|----|------|--------|--------|----------|
| 381 | Academic Research | NEW | 4 | Research paper writing with citations |
| 382 | Antom Payment | NEW | 4 | Payment processing and fraud detection |
| 383 | Blog Writer | EXISTS | 3 | Technical blog post creation |
| 384 | Brand Search Optimization | NEW | 5 | SEO analysis and optimization |
| 385 | CAMEL Multi-Agent | NEW | 3 | Role-playing agent collaboration |
| 386 | Customer Service | NEW | 5 | Customer support automation |
| 387 | Data Engineering | ROOT | - | Data pipeline management |
| 388 | Data Science | NEW | 5 | End-to-end ML workflow |
| 389 | Financial Advisor | EXISTS | - | Financial planning and advice |
| 390 | FOMC Research | NEW | 5 | Federal Reserve analysis |

## Quick Setup

### 1. Install Dependencies
```bash
cd /Users/colinlowenberg/crew/adk-batch23/{app-directory}
pip install -r requirements.txt
```

### 2. Configure Environment
```bash
cp .env.example .env
# Edit .env and add:
# OPENAI_API_KEY=your_key_here
# SERPER_API_KEY=your_key_here (if needed)
```

### 3. Run Application
```bash
python main.py
# Follow interactive prompts
```

## Recommended First Tests

### Easiest to Test
1. **Customer Service Agent (386)**
   - Pre-loaded example scenarios
   - Instant feedback
   - No data requirements

2. **CAMEL Framework (385)**
   - Simple role-playing demo
   - Quick iteration
   - Clear outputs

3. **Blog Writer Agent (383)**
   - Straightforward topic input
   - Good for seeing multi-agent collaboration

### Most Impressive Demos
1. **Data Science Agent (388)**
   - Complete ML workflow
   - Comprehensive outputs
   - Professional quality

2. **FOMC Research Agent (390)**
   - Real-world financial analysis
   - Multiple focus modes
   - Publication-ready reports

3. **Brand Search Optimization (384)**
   - Comprehensive SEO analysis
   - Actionable recommendations
   - Multi-agent expertise

## Common Commands

### Run with defaults
```bash
python main.py
# Press Enter for default values
```

### API Usage (Python)
```python
from main import {main_function}

result = {main_function}(
    # your parameters
)

print(result)
```

## Tips

### For Development
- Start with simpler agents first
- Review README.md for each agent
- Check example usage in main.py
- Monitor API costs

### For Testing
- Use short/simple inputs initially
- Check verbose output for debugging
- Save outputs for comparison
- Test error handling

### For Production
- Add proper error handling
- Implement rate limiting
- Add logging and monitoring
- Consider caching responses

## File Structure
Each agent directory contains:
```
{agent-name}/
├── main.py           # Main implementation
├── requirements.txt  # Python dependencies
├── .env.example     # Environment template
└── README.md        # Full documentation
```

## Support & Documentation

### For Each Agent
- See individual README.md for detailed docs
- Check main.py for usage examples
- Review agent backstories for capabilities

### General Resources
- CrewAI docs: https://docs.crewai.com
- OpenAI docs: https://platform.openai.com/docs
- Batch completion report: BATCH_381-390_COMPLETION_REPORT.md

## Troubleshooting

### Missing API Keys
```bash
# Make sure .env file exists and contains:
OPENAI_API_KEY=sk-...
SERPER_API_KEY=... # if needed
```

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

### Rate Limits
- Reduce temperature
- Add delays between calls
- Use cheaper model (gpt-3.5-turbo)

### Slow Response
- Normal for complex multi-agent workflows
- Check verbose output for progress
- Consider reducing max_iter

## Next Steps

1. **Pick an agent** based on your use case
2. **Read its README.md** for detailed info
3. **Set up environment** with API keys
4. **Run the demo** with test inputs
5. **Customize** for your needs

## Quick Examples

### Academic Research (381)
```bash
cd academic-research-agent381
python main.py
# Topic: "Machine Learning in Healthcare"
# Citation: APA
```

### Customer Service (386)
```bash
cd customer-service-agent386
python main.py
# Select scenario 1 (password reset)
```

### Data Science (388)
```bash
cd data-science-agent388
python main.py
# Problem: "Customer churn prediction"
# Type: classification
```

---

**Ready to start?** Pick an agent and follow the setup steps above!

For detailed information, see: `BATCH_381-390_COMPLETION_REPORT.md`
