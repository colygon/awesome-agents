# Setup Instructions - Gita GPT Agent 36

## Quick Start

1. **Initialize Git Repository**
   ```bash
   cd /Users/colinlowenberg/crew/gitagpt-agent36
   chmod +x init_repo.sh
   ./init_repo.sh
   ```

2. **Set Up Remote Repository** (if you want to push to GitHub)
   ```bash
   # Create a new repository on GitHub first, then:
   git remote add origin https://github.com/YOUR_USERNAME/gitagpt-agent36.git
   git push -u origin crewai-upgrade
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure API Key**
   ```bash
   cp .env.example .env
   # Edit .env and add your OpenAI API key
   ```

5. **Run the Application**
   ```bash
   python main.py
   ```

## Manual Git Setup (Alternative)

If you prefer to set up git manually:

```bash
cd /Users/colinlowenberg/crew/gitagpt-agent36
git init
git add .
git commit -m "Initial commit: Gita GPT Agent 36 CrewAI upgrade"
git checkout -b crewai-upgrade
```

## File Structure

```
gitagpt-agent36/
├── agents.py              # Three specialized agents
├── tasks.py               # Tasks for each agent
├── main.py                # Main application
├── requirements.txt       # Python dependencies
├── .env.example          # Environment template
├── .gitignore            # Git ignore rules
├── README.md             # Project overview
├── CREWAI_UPGRADE.md     # Detailed upgrade documentation
├── SETUP_INSTRUCTIONS.md # This file
├── init_repo.sh          # Git initialization script
└── data/
    ├── __init__.py
    └── sample_verses.py  # Bhagavad Gita verses
```

## Testing the Application

Try these sample queries:
- "How should I deal with failure in my career?"
- "What does the Gita say about fear and anxiety?"
- "How can I find peace in difficult times?"
- "What is the meaning of dharma?"

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists with `OPENAI_API_KEY=your_key`
- Check that python-dotenv is installed
- Verify the key is valid on OpenAI's platform

### Import Errors
- Run `pip install -r requirements.txt`
- Ensure you're using Python 3.8 or higher
- Create a virtual environment if needed

### Git Issues
- Make sure git is installed: `git --version`
- Check file permissions: `chmod +x init_repo.sh`
- Verify you're in the correct directory

## Next Steps

1. Test the application with various queries
2. Review the agent outputs in CREWAI_UPGRADE.md
3. Customize agents or add new ones as needed
4. Share your repository with others
5. Consider contributing enhancements

---

**Agent 36** - Ancient wisdom through modern AI collaboration
