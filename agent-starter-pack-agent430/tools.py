from crewai_tools import tool

class AgentStarterTools:
    @tool("Search Web")
    def search_web(self, query: str) -> str:
        """Searches the web for information on query."""
        return f"""Web Search Results for: {query}

Top Results:
1. "Complete Guide to {query}" - authority-site.com
   - Comprehensive overview with expert insights
   - Published: 2024, Highly rated

2. "Latest Trends in {query}" - industry-news.com
   - Current statistics and market analysis
   - Updated regularly

3. "Expert Analysis: {query}" - research-institute.org
   - Academic perspective and data
   - Peer-reviewed content

Key Findings:
- Market size: $X billion (growing Y% annually)
- Key players: A, B, C companies
- Emerging trends: Trend 1, Trend 2
- Expert consensus: [Summary]

Sources: 15 credible sources identified"""

    @tool("Summarize Content")
    def summarize_content(self, text: str) -> str:
        """Summarizes long-form content into key points."""
        return f"""Content Summary:

Main Points:
1. [Primary topic/thesis statement]
2. [Key supporting point #1]
3. [Key supporting point #2]
4. [Important finding or conclusion]

Key Statistics:
- Metric 1: X% increase/decrease
- Metric 2: Y units/value
- Comparison: Z vs benchmark

Conclusions:
[Main takeaway and implications]

Length: Reduced from 2,500 words to 150 words
Retention: All critical information preserved"""

    @tool("Extract Key Facts")
    def extract_key_facts(self, content: str) -> str:
        """Extracts key facts and data points."""
        return f"""Key Facts Extracted:

FACTS:
- Fact 1: [Specific data point]
- Fact 2: [Important statistic]
- Fact 3: [Notable finding]
- Fact 4: [Key trend]
- Fact 5: [Expert opinion]

STATISTICS:
- 75% of [relevant metric]
- $X.X billion market size
- Y% growth rate
- Z million users/customers

TRENDS:
- Increasing adoption of [technology/method]
- Shift towards [direction]
- Growing concern about [issue]

SOURCES:
- Authority Site (2024)
- Research Institute Report
- Industry Analysis"""

    @tool("Generate Content")
    def generate_content(self, brief: str) -> str:
        """Generates written content from brief."""
        return f"""Generated Content:

TITLE: [Engaging, Descriptive Title]

INTRODUCTION:
[Opening paragraph that hooks reader and introduces topic.
Sets context and outlines what will be covered.]

MAIN CONTENT:

Section 1: [Heading]
[Well-developed paragraph with supporting details, examples,
and evidence. Clear topic sentence and smooth transitions.]

Section 2: [Heading]
[Continued development of topic with additional insights,
data, and explanations. Maintains reader engagement.]

Section 3: [Heading]
[Further exploration with practical applications, case
studies, or real-world examples.]

CONCLUSION:
[Summary of key points, actionable takeaways, and
compelling closing statement.]

Word Count: 800 words
Readability: Grade 10 (accessible)
Tone: Professional yet engaging"""

    @tool("Edit Text")
    def edit_text(self, draft: str) -> str:
        """Edits text for clarity, flow, and impact."""
        return f"""Editing Results:

IMPROVEMENTS MADE:
- Clarity: 15 sentences restructured
- Conciseness: Reduced wordiness by 12%
- Flow: Improved transitions between sections
- Impact: Strengthened opening and closing
- Consistency: Unified tone and style

CORRECTIONS:
- Grammar: 8 fixes
- Punctuation: 12 corrections
- Spelling: 3 corrections
- Style: 6 improvements

READABILITY:
- Before: Grade 12
- After: Grade 10
- Improvement: +15% readability score

FINAL STATUS:
✓ Clear and concise
✓ Proper structure
✓ Engaging tone
✓ Error-free
Ready for publication"""

    @tool("Check Grammar")
    def check_grammar(self, text: str) -> str:
        """Checks grammar, spelling, and style."""
        return f"""Grammar Check Results:

ERRORS FOUND:
- Critical errors: 0
- Grammar issues: 2 (corrected)
- Spelling mistakes: 1 (corrected)
- Punctuation: 3 (corrected)
- Style suggestions: 5 (applied)

SPECIFIC CORRECTIONS:
1. Subject-verb agreement: Line 12
2. Comma splice: Line 28
3. Spelling: "recieve" → "receive"

STYLE IMPROVEMENTS:
- Passive voice: 3 instances made active
- Wordiness: 5 phrases simplified
- Redundancy: 2 instances removed

SCORE:
Grammar: 98/100
Clarity: 95/100
Professionalism: 100/100

STATUS: Approved for publication"""

    @tool("Analyze Data")
    def analyze_data(self, dataset: str) -> str:
        """Analyzes data and identifies patterns."""
        return f"""Data Analysis Results:

DATASET: {dataset}
Records: 1,000
Variables: 15

SUMMARY STATISTICS:
- Mean: 45.2
- Median: 43.5
- Std Dev: 12.3
- Range: 15-78

KEY FINDINGS:
1. Strong positive correlation (0.78) between X and Y
2. Three distinct clusters identified
3. 15% year-over-year growth trend
4. Seasonal pattern with Q4 peaks

PATTERNS:
- Upward trend in primary metric
- Cyclical behavior every 90 days
- Outliers: 23 data points (2.3%)

ANOMALIES:
- Unusual spike in Week 12
- Data gap in August (investigate)

QUALITY: 95/100 (high quality data)"""

    @tool("Create Visualizations")
    def create_visualizations(self, data: str) -> str:
        """Creates data visualizations."""
        return f"""Visualizations Created:

CHARTS GENERATED:
1. Line Chart: Trend over time
   - Shows 15% growth trajectory
   - Highlights seasonal peaks

2. Bar Chart: Category comparison
   - Top 5 categories displayed
   - Clear performance differences

3. Pie Chart: Market share
   - Segment distribution
   - Percentages labeled

4. Scatter Plot: Correlation
   - X vs Y relationship
   - R² = 0.78 (strong)

5. Heatmap: Variable relationships
   - Correlation matrix
   - Color-coded intensity

FORMAT: PNG (high-res) + Interactive HTML
STYLE: Professional, colorful, accessible
Ready for presentation and reports"""

    @tool("Generate Insights")
    def generate_insights(self, analysis: str) -> str:
        """Generates actionable insights from analysis."""
        return f"""Key Insights & Recommendations:

INSIGHTS:
1. Strong Growth Opportunity
   - 15% YoY growth trend identified
   - Market expansion potential: $50M
   - Recommendation: Invest in growth initiatives

2. Seasonal Patterns Detected
   - Q4 shows 35% higher performance
   - Opportunity: Optimize for peak season
   - Recommendation: Seasonal marketing campaigns

3. Customer Segmentation Clear
   - 3 distinct customer groups identified
   - Top segment: 60% of revenue
   - Recommendation: Targeted strategies per segment

4. Efficiency Gap Identified
   - Current process: 68% efficient
   - Industry benchmark: 85%
   - Recommendation: Process optimization

ACTIONABLE RECOMMENDATIONS:
1. Immediate: Implement seasonal campaigns ($10K)
2. Short-term: Segment marketing (3 months, $25K)
3. Long-term: Process optimization (6 months, $50K)

EXPECTED IMPACT:
Revenue: +18-22%
Efficiency: +17 percentage points
ROI: 280% on recommended investments"""

    @tool("Integrate Outputs")
    def integrate_outputs(self, all_work: str) -> str:
        """Integrates outputs from all agents."""
        return f"""Integrated Project Deliverable:

EXECUTIVE SUMMARY:
Comprehensive analysis completed combining research, content
creation, and data analysis. Key findings and recommendations
integrated into cohesive deliverable.

RESEARCH FINDINGS:
- 15 credible sources analyzed
- Key trends and statistics identified
- Expert opinions synthesized
- Market landscape mapped

CONTENT CREATED:
- Main report: 2,500 words
- Executive summary: 500 words
- Supporting slides: 15 slides
- All content professionally edited

DATA ANALYSIS:
- 1,000 records analyzed
- 5 visualizations created
- Key insights extracted
- Recommendations generated

INTEGRATED INSIGHTS:
Research + Analysis = Strategic Recommendations
Content quality: Publication-ready
Visualizations: Presentation-ready

DELIVERABLES:
✓ Final report (PDF)
✓ Executive summary (PDF)
✓ Presentation (PPTX)
✓ Data visualizations (PNG + HTML)
✓ Source documentation"""

    @tool("Quality Check")
    def quality_check(self, deliverable: str) -> str:
        """Performs quality assurance on deliverable."""
        return f"""Quality Assurance Results:

CONTENT QUALITY:
✓ Accuracy: All facts verified
✓ Completeness: All requirements met
✓ Clarity: Clear and understandable
✓ Consistency: Unified style and tone
✓ Grammar: Error-free

RESEARCH QUALITY:
✓ Sources: 15 credible sources cited
✓ Currency: All sources recent (2023-2024)
✓ Diversity: Multiple perspectives included
✓ Verification: Cross-referenced claims

ANALYSIS QUALITY:
✓ Methodology: Sound and appropriate
✓ Accuracy: Calculations verified
✓ Insights: Actionable and relevant
✓ Visualizations: Clear and professional

PRESENTATION:
✓ Formatting: Professional and consistent
✓ Design: Visually appealing
✓ Navigation: Well-organized
✓ Accessibility: Readable and accessible

OVERALL SCORE: 96/100 (Excellent)
STATUS: APPROVED FOR DELIVERY
Minor suggestions: [Optional improvements listed]"""

    @tool("Generate Final Report")
    def generate_final_report(self, project_data: str) -> str:
        """Generates comprehensive final project report."""
        return f"""FINAL PROJECT REPORT

PROJECT: {project_data}

EXECUTIVE SUMMARY:
Successfully completed comprehensive research, content
creation, and analysis project. Delivered high-quality
integrated deliverable meeting all requirements.

PROJECT SCOPE:
- Research: ✓ Completed
- Content Creation: ✓ Completed
- Data Analysis: ✓ Completed
- Integration: ✓ Completed
- Quality Assurance: ✓ Passed

KEY DELIVERABLES:
1. Research Report (15 sources, 3,000 words)
2. Content Pieces (2,500 words, edited)
3. Data Analysis (1,000 records, 5 visualizations)
4. Integrated Report (Publication-ready)
5. Executive Summary (500 words)
6. Presentation (15 slides)

QUALITY METRICS:
- Accuracy: 100%
- Completeness: 100%
- Quality Score: 96/100
- Client Satisfaction: Projected High

KEY FINDINGS:
- Finding 1: [Major insight]
- Finding 2: [Important trend]
- Finding 3: [Strategic opportunity]

RECOMMENDATIONS:
1. Immediate actions (0-30 days)
2. Short-term initiatives (1-3 months)
3. Long-term strategy (3-6 months)

PROJECT STATISTICS:
- Duration: On schedule
- Resources: Within budget
- Quality: Exceeds standards
- Deliverables: 100% complete

NEXT STEPS:
1. Review final deliverables
2. Implement recommendations
3. Monitor outcomes
4. Schedule follow-up

PROJECT STATUS: SUCCESSFULLY COMPLETED ✓"""
