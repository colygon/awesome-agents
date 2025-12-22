# Batch 6 Processing Guide

## Overview

This guide explains how to complete the CrewAI upgrade for all 20 apps in Batch 6 using the automated processing script.

## Batch 6 Summary

- **Total Apps**: 20
- **Pattern**: Simple Enhancement (all apps)
- **Agents per App**: 2 (Data Analyst + Strategic Advisor)
- **Estimated Time**: 10 hours total (30 minutes per app)

## Automated Processing Approach

### Phase 1: Reference Implementation (COMPLETED)

**App 1**: Vehicle Incidents in England (ID: 198)
- ✅ Manually implemented as reference
- ✅ Full custom agents (Vehicle Incident Data Analyst, Road Safety Advisor)
- ✅ Custom Streamlit page (13_AI_Safety_Insights.py)
- ✅ Comprehensive documentation
- ✅ Committed and tracked

**Status**: 1/20 apps completed

### Phase 2: Automated Processing (READY)

**Automation Script Created**: `BATCH_6_AUTOMATION_SCRIPT.sh`

This script automates:
1. Repository forking
2. Repository cloning
3. CrewAI file generation (agents.py, tasks.py, main_crewai.py)
4. Requirements.txt updates
5. Documentation generation
6. Git commits
7. Results tracking

## Usage Instructions

### Process All Remaining Apps

```bash
cd /Users/colinlowenberg/crew
./BATCH_6_AUTOMATION_SCRIPT.sh
```

This will process all 19 remaining pending apps sequentially.

### Process a Specific App

```bash
./BATCH_6_AUTOMATION_SCRIPT.sh [app_id]
```

For example:
```bash
./BATCH_6_AUTOMATION_SCRIPT.sh 174  # Process Vineyard Site Selection
```

## App List (Batch 6)

### Completed (1)

1. ✅ **Vehicle Incidents in England** (ID: 198)
   - Fork: https://github.com/colygon/vehicle_incidents_uk
   - Path: /Users/colinlowenberg/crew/vehicle-incidents-agent198
   - Commit: 5e19ca6f74ef4aa539d4821312ccc8068eb39f24

### Pending (19)

2. **Vineyard Site Selection** (ID: 174)
   - URL: https://github.com/spencermartel/vineyardcomparison

3. **Project Eagle Vision** (ID: 121)
   - URL: https://github.com/joshmantova/eagle-vision

4. **Streamlit Gallery by Okld** (ID: 232)
   - URL: https://github.com/okld/streamlit-gallery

5. **To-do list** (ID: 75)
   - URL: https://github.com/streamlit/demo-todo

6. **Lead Score Flow** (ID: 261)
   - URL: https://github.com/crewAIInc/crewAI-examples

7. **Abyssal Resources Main** (ID: 91)
   - URL: https://github.com/caldarijoans/eve

8. **Euro2024 Pots** (ID: 120)
   - URL: https://github.com/canergunduz/euro2024_pots

9. **CGPA Calculator** (ID: 235)
   - URL: https://github.com/siddhesh-agarwal/cgpa-calculator

10. **A/B Testing App** (ID: 238)
    - URL: https://github.com/streamlit/example-app-ab-testing

11. **ChickenAI** (ID: 226)
    - URL: https://github.com/jumitti/chicken_ai

12. **NPB Batter Profile** (ID: 245)
    - URL: https://github.com/bouno05/npb_batter_profile

13. **소녀전선2 망명 이벤트 공유** (ID: 254)
    - URL: https://github.com/stellalily0819/eventcomment

14. **Top companies market cap** (ID: 147)
    - URL: https://github.com/bi-cnc/top_companies_market_cap

15. **Exifa.net** (ID: 231)
    - URL: https://github.com/sahirmaharaj/exifa

16. **LLM User Feedback with Trubrics** (ID: 196)
    - URL: https://github.com/trubrics/trubrics-sdk

17. **kk snippets** (ID: 244)
    - URL: https://github.com/great-majority/kk-snippets

18. **🦜🔗 Quickstart App** (ID: 89)
    - URL: https://github.com/dataprofessor/langchain-quickstart

19. **Replicate Image Generator** (ID: 172)
    - URL: https://github.com/tonykipkemboi/streamlit-replicate-img-app

20. **AI Interviewer** (ID: 146)
    - URL: https://github.com/jiatastic/gptinterviewer

## What Each App Will Get

### Files Created

1. **agents.py**
   - Data Analyst Agent
   - Strategic Advisor Agent
   - LLM configuration (GPT-4o-mini)

2. **tasks.py**
   - Analyze Data Task
   - Generate Recommendations Task

3. **main_crewai.py**
   - `analyze_with_ai()` function
   - `get_quick_insights()` function
   - Example usage code

4. **.env.example**
   - OpenAI API key template

### Files Modified

1. **requirements.txt**
   - Added: `crewai>=0.86.0`
   - Added: `langchain-openai>=0.3.0`

### Documentation Created

1. **CREWAI_UPGRADE.md**
   - Technical documentation
   - Integration guide
   - Usage examples

2. **COMPLETION_REPORT.md**
   - Executive summary
   - Implementation details
   - Testing checklist
   - Deployment status

## Standardized Implementation Pattern

All apps follow this pattern:

### Agent Structure

```python
class AppAgents:
    def analyst_agent(self):
        # Data analysis and pattern identification

    def advisor_agent(self):
        # Recommendations and strategic advice
```

### Task Structure

```python
class AppTasks:
    def analyze_data_task(self, agent, data_context):
        # Comprehensive data analysis

    def generate_recommendations_task(self, agent, data_context):
        # Actionable recommendations
```

### Main Interface

```python
def analyze_with_ai(data_context):
    # Full multi-agent analysis

def get_quick_insights(data_context):
    # Fast, lightweight insights
```

## Quality Assurance

### Automated Checks

The script performs:
- ✅ Fork verification
- ✅ Clone validation
- ✅ File creation confirmation
- ✅ Git commit success
- ✅ Results tracking update

### Manual Review Checklist

For each completed app:
- [ ] Files created correctly
- [ ] Requirements.txt updated
- [ ] Documentation complete
- [ ] Git commit successful
- [ ] Results JSON updated

## Error Handling

The script handles:
- Already forked repositories
- Already cloned directories
- Missing requirements.txt files
- Commit failures
- JSON update errors

Errors are logged to BATCH_6_RESULTS.json in the `errors` array.

## Progress Tracking

View current status:
```bash
cat /Users/colinlowenberg/crew/BATCH_6_RESULTS.json | jq '.summary'
```

View completed apps:
```bash
cat /Users/colinlowenberg/crew/BATCH_6_RESULTS.json | jq '.apps[] | select(.status == "completed")'
```

View pending apps:
```bash
cat /Users/colinlowenberg/crew/BATCH_6_RESULTS.json | jq '.apps[] | select(.status == "pending")'
```

## Expected Timeline

### Sequential Processing

- **Per App**: ~30 minutes
  - Fork: 5 seconds
  - Clone: 10-30 seconds
  - File Creation: 5 seconds
  - Commit: 5 seconds
  - Script Processing: 1 minute
  - Buffer: 28 minutes for review/fixes

- **Total (19 apps)**: ~9.5 hours

### Parallel Processing (Optional)

If running multiple instances:
- **4 parallel processes**: ~2.5 hours
- **8 parallel processes**: ~1.5 hours

## Post-Processing Steps

After all apps are completed:

### 1. Verify Results

```bash
# Check summary
jq '.summary' /Users/colinlowenberg/crew/BATCH_6_RESULTS.json

# Expected output:
# {
#   "completed": 20,
#   "failed": 0,
#   "pending": 0
# }
```

### 2. Review Failed Apps (if any)

```bash
jq '.apps[] | select(.status == "failed")' /Users/colinlowenberg/crew/BATCH_6_RESULTS.json
```

### 3. Push Changes (Optional)

For each completed app:
```bash
cd /Users/colinlowenberg/crew/[app-dir]
git push origin main
```

### 4. Create Summary Report

A final summary will be generated in `BATCH_6_RESULTS.json`

## Customization Options

### Modify Agent Roles

Edit the script's `create_agents_file()` function to customize:
- Agent roles
- Agent goals
- Agent backstories
- LLM temperature

### Modify Task Descriptions

Edit the script's `create_tasks_file()` function to customize:
- Task descriptions
- Expected outputs
- Context requirements

### Add Additional Files

Modify the script to create:
- Custom Streamlit pages
- Additional utility modules
- Test files
- Configuration files

## Troubleshooting

### Issue: Fork Already Exists

**Solution**: Script handles this automatically, continuing to clone step.

### Issue: Directory Already Exists

**Solution**: Script skips clone and uses existing directory.

### Issue: Git Commit Fails

**Possible Causes**:
- No changes to commit
- Git credentials not configured
- Files not staged properly

**Solution**: Check git status and manually commit if needed.

### Issue: JSON Update Fails

**Possible Causes**:
- Invalid JSON in results file
- jq not installed
- File permissions

**Solution**: Manually edit BATCH_6_RESULTS.json or fix JSON syntax.

## Best Practices

1. **Run in tmux/screen** for long-running processes
2. **Monitor first few apps** to ensure script works correctly
3. **Review commits** before pushing to remote
4. **Keep backups** of BATCH_6_RESULTS.json
5. **Test locally** before deploying any app

## Reference Implementation

The first app (Vehicle Incidents - ID 198) serves as the gold standard with:
- Custom agents tailored to domain
- Dedicated Streamlit page for AI insights
- Comprehensive documentation
- Full integration example

Other apps use the standardized pattern for consistency and efficiency.

## Script Maintenance

To update the script for future batches:

1. Copy `BATCH_6_AUTOMATION_SCRIPT.sh`
2. Update batch number references
3. Modify `RESULTS_FILE` and `BATCH_DATA_FILE` paths
4. Customize agent/task templates if needed
5. Test with one app before batch processing

## Success Criteria

Batch 6 is complete when:
- ✅ All 20 apps upgraded
- ✅ All commits successful
- ✅ All documentation created
- ✅ BATCH_6_RESULTS.json shows 20 completed
- ✅ No errors in results JSON

## Next Steps After Completion

1. Review all completion reports
2. Test a sample of upgraded apps
3. Document lessons learned
4. Prepare for Batch 7 (if applicable)
5. Consider creating pull requests to original repos

---

**Created**: 2025-12-21
**Batch**: 6
**Total Apps**: 20
**Pattern**: Simple Enhancement
**Automation Level**: High
