# Batch 27: Quick Start Guide

## 🚀 Quick Implementation Steps

### Prerequisites
```bash
# Required
- Python 3.11+
- Git
- Anthropic API key

# Installation
pip install crewai crewai-tools langchain langchain-anthropic python-dotenv pydantic
```

---

## 📁 Step 1: Setup Repository

```bash
cd /Users/colinlowenberg/crew
mkdir -p adk-batch27
cd adk-batch27
git clone https://github.com/colygon/adk-samples.git .
```

---

## 🔧 Step 2: Create Each App

### App 1: Antom Payment (382)

```bash
mkdir -p antom-payment-agent382
cd antom-payment-agent382
```

**Copy these 8 files from BATCH_27_UPGRADE_PLAN.md:**
1. tools.py (PaymentGatewayTool, TransactionValidatorTool, ReceiptGeneratorTool)
2. agents.py (transaction_validator, payment_processor)
3. tasks.py (validate_transaction_task, process_payment_task)
4. main.py
5. requirements.txt
6. config.py
7. .env.example
8. .gitignore

**Setup and test:**
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
pip install -r requirements.txt
python main.py
```

**Git commit:**
```bash
git init
git add .
git commit -m "Convert Antom Payment from Google ADK to CrewAI

- Implement transaction validator and payment processor agents
- Create payment gateway, transaction validator, and receipt generator tools
- Add multi-currency payment processing with fraud detection
- Include automated receipt generation

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### App 2: Brand Search Optimization (384)

```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p brand-search-agent384
cd brand-search-agent384
```

**Copy these 8 files from BATCH_27_UPGRADE_PLAN.md:**
1. tools.py (SEOAnalyzerTool, KeywordResearchTool, RankingTrackerTool)
2. agents.py (keyword_researcher, content_optimizer)
3. tasks.py (research_keywords_task, optimize_content_task)
4. main.py
5. requirements.txt
6. config.py
7. .env.example
8. .gitignore

**Setup and test:**
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
pip install -r requirements.txt
python main.py
```

**Git commit:**
```bash
git init
git add .
git commit -m "Convert Brand Search Optimization from Google ADK to CrewAI

- Implement keyword researcher and content optimizer agents
- Create SEO analyzer, keyword research, and ranking tracker tools
- Add comprehensive keyword research with trend analysis
- Include content optimization recommendations

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### App 3: Image Scoring (394)

```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p image-scoring-agent394
cd image-scoring-agent394
```

**Copy these 8 files from BATCH_27_UPGRADE_PLAN.md:**
1. tools.py (VisionAnalysisTool, QualityScorerTool, ContentDetectionTool)
2. agents.py (image_analyzer, score_calculator)
3. tasks.py (analyze_image_task, calculate_score_task)
4. main.py
5. requirements.txt
6. config.py
7. .env.example
8. .gitignore

**Setup and test:**
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
pip install -r requirements.txt
python main.py
```

**Git commit:**
```bash
git init
git add .
git commit -m "Convert Image Scoring from Google ADK to CrewAI

- Implement image analyzer and score calculator agents
- Create vision analysis, quality scorer, and content detection tools
- Add computer vision analysis with object detection
- Include multi-dimensional quality scoring

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### App 4: LLM Auditor (395)

```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p llm-auditor-agent395
cd llm-auditor-agent395
```

**Copy these 8 files from BATCH_27_UPGRADE_PLAN.md:**
1. tools.py (ModelEvaluationTool, BenchmarkTool, MetricsAggregatorTool)
2. agents.py (performance_tester, report_generator)
3. tasks.py (test_performance_task, generate_report_task)
4. main.py
5. requirements.txt
6. config.py
7. .env.example
8. .gitignore

**Setup and test:**
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
pip install -r requirements.txt
python main.py
```

**Git commit:**
```bash
git init
git add .
git commit -m "Convert LLM Auditor from Google ADK to CrewAI

- Implement performance tester and report generator agents
- Create model evaluation, benchmark, and metrics aggregator tools
- Add comprehensive LLM performance testing
- Include automated audit report generation

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### App 5: Safety Plugins (403)

```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p safety-plugins-agent403
cd safety-plugins-agent403
```

**Copy these 8 files from BATCH_27_UPGRADE_PLAN.md:**
1. tools.py (ContentFilterTool, ToxicityDetectorTool, RiskScorerTool)
2. agents.py (content_moderator, risk_assessor)
3. tasks.py (moderate_content_task, assess_risk_task)
4. main.py
5. requirements.txt
6. config.py
7. .env.example
8. .gitignore

**Setup and test:**
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
pip install -r requirements.txt
python main.py
```

**Git commit:**
```bash
git init
git add .
git commit -m "Convert Safety Plugins from Google ADK to CrewAI

- Implement content moderator and risk assessor agents
- Create content filter, toxicity detector, and risk scorer tools
- Add multi-layer content safety checking
- Include comprehensive risk assessment

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

### App 6: Travel Concierge (406)

```bash
cd /Users/colinlowenberg/crew/adk-batch27
mkdir -p travel-concierge-agent406
cd travel-concierge-agent406
```

**Copy these 8 files from BATCH_27_UPGRADE_PLAN.md:**
1. tools.py (TravelAPITool, BookingTool, ItineraryBuilderTool)
2. agents.py (itinerary_planner, booking_agent)
3. tasks.py (plan_itinerary_task, make_bookings_task)
4. main.py
5. requirements.txt
6. config.py
7. .env.example
8. .gitignore

**Setup and test:**
```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
pip install -r requirements.txt
python main.py
```

**Git commit:**
```bash
git init
git add .
git commit -m "Convert Travel Concierge from Google ADK to CrewAI

- Implement itinerary planner and booking agent agents
- Create travel API, booking, and itinerary builder tools
- Add comprehensive travel search and planning
- Include automated booking confirmations

🤖 Generated with Claude Code
Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
```

---

## 📊 Step 3: Verify All Apps

```bash
cd /Users/colinlowenberg/crew/adk-batch27

# Check all directories exist
ls -la

# Expected output:
# antom-payment-agent382/
# brand-search-agent384/
# image-scoring-agent394/
# llm-auditor-agent395/
# safety-plugins-agent403/
# travel-concierge-agent406/
```

---

## ✅ Completion Checklist

- [ ] Clone adk-samples repository
- [ ] Create antom-payment-agent382
  - [ ] Copy all 8 files
  - [ ] Test with `python main.py`
  - [ ] Git commit
- [ ] Create brand-search-agent384
  - [ ] Copy all 8 files
  - [ ] Test with `python main.py`
  - [ ] Git commit
- [ ] Create image-scoring-agent394
  - [ ] Copy all 8 files
  - [ ] Test with `python main.py`
  - [ ] Git commit
- [ ] Create llm-auditor-agent395
  - [ ] Copy all 8 files
  - [ ] Test with `python main.py`
  - [ ] Git commit
- [ ] Create safety-plugins-agent403
  - [ ] Copy all 8 files
  - [ ] Test with `python main.py`
  - [ ] Git commit
- [ ] Create travel-concierge-agent406
  - [ ] Copy all 8 files
  - [ ] Test with `python main.py`
  - [ ] Git commit
- [ ] Verify BATCH_27_RESULTS.json exists
- [ ] Review BATCH_27_EXECUTIVE_SUMMARY.md

---

## 🔍 Testing Each App

### Basic Test
```bash
cd {app-directory}
python main.py
```

### Expected Output Pattern
```
=== Starting {App Name} Crew ===

Agent: {Agent 1 Name}
Task: {Task 1 Description}
[Tool usage and reasoning...]

Agent: {Agent 2 Name}
Task: {Task 2 Description}
[Tool usage and reasoning...]

=== {App Name} Result ===
[Final output]
```

---

## 🐛 Troubleshooting

### Issue: Module not found
```bash
pip install -r requirements.txt
```

### Issue: API key error
```bash
# Check .env file exists
cat .env

# Should contain:
ANTHROPIC_API_KEY=sk-ant-...
```

### Issue: Import errors
```bash
# Ensure you're in the app directory
pwd
# Should show: .../adk-batch27/{app-directory}

# Run from app directory
python main.py
```

### Issue: Tool validation errors
- Check that input data matches Pydantic schema
- Review tool implementation in tools.py
- Verify all required fields are provided

---

## 📈 Performance Tips

### Optimize Response Time
- Use simpler test prompts during development
- Cache API responses where possible
- Consider parallel processing for independent tools

### Monitor Costs
- Track token usage per run
- Use shorter prompts during testing
- Implement rate limiting for production

### Improve Accuracy
- Refine agent backstories
- Adjust task descriptions
- Provide more context in inputs

---

## 🔐 Security Best Practices

1. **Never commit .env files**
   - Always in .gitignore
   - Use .env.example for templates

2. **Protect API keys**
   - Store in environment variables
   - Rotate keys regularly
   - Use separate keys for dev/prod

3. **Validate inputs**
   - Pydantic handles this automatically
   - Add custom validation as needed
   - Sanitize user inputs

4. **Error handling**
   - Don't expose sensitive data in errors
   - Log errors securely
   - Provide helpful but safe error messages

---

## 📚 Additional Resources

### Documentation
- **BATCH_27_UPGRADE_PLAN.md** - Complete implementation details
- **BATCH_27_RESULTS.json** - Technical specifications
- **BATCH_27_EXECUTIVE_SUMMARY.md** - Overview and business value

### Code References
- All tool implementations in BATCH_27_UPGRADE_PLAN.md
- Agent and task definitions included
- Complete main.py examples provided

### External Resources
- CrewAI Documentation: https://docs.crewai.com
- Pydantic Documentation: https://docs.pydantic.dev
- Anthropic API Documentation: https://docs.anthropic.com

---

## 🎯 Quick Command Reference

```bash
# Setup
cd /Users/colinlowenberg/crew/adk-batch27
git clone https://github.com/colygon/adk-samples.git .

# Create app
mkdir -p {app-directory}
cd {app-directory}

# Install dependencies
pip install -r requirements.txt

# Configure
cp .env.example .env
# Edit .env with your API key

# Run
python main.py

# Commit
git init
git add .
git commit -m "Your message"
```

---

## ⏱️ Time Estimates

| Task | Estimated Time |
|------|---------------|
| Clone repository | 2 minutes |
| Create single app | 15 minutes |
| Test single app | 5 minutes |
| Git commit | 2 minutes |
| **Total per app** | **~25 minutes** |
| **All 6 apps** | **~2.5 hours** |

---

## 🎉 Success Criteria

You'll know you're done when:
- ✅ All 6 app directories exist
- ✅ Each app runs without errors
- ✅ All git commits are created
- ✅ BATCH_27_RESULTS.json is complete
- ✅ All tools validate inputs correctly
- ✅ Agents collaborate successfully

---

## 💡 Pro Tips

1. **Work on one app at a time** - Complete, test, commit, then move to next
2. **Use the same .env** - Copy ANTHROPIC_API_KEY to each app's .env
3. **Test frequently** - Run `python main.py` after each file creation
4. **Check output** - Verify agent reasoning and tool usage makes sense
5. **Keep it simple** - Use the provided examples as-is first, customize later

---

## 🚦 Next Steps After Completion

1. **Review outputs** - Ensure each app produces expected results
2. **Customize prompts** - Adjust agent backstories and task descriptions
3. **Add features** - Extend tools with additional capabilities
4. **Deploy** - Move to production environment
5. **Monitor** - Track usage and performance
6. **Iterate** - Improve based on feedback

---

**Document Version:** 1.0
**Last Updated:** December 21, 2025
**Estimated Implementation Time:** 2.5-3 hours
