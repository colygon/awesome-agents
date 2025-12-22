# Budget Tracker - CrewAI Edition

## Overview

The Budget Tracker is a multi-agent personal finance management system built with CrewAI that helps users track expenses, create budgets, and achieve savings goals through three specialized agents:

1. **Expense Analyzer** - Categorizes and analyzes spending patterns
2. **Budget Planner** - Creates realistic budgets aligned with income and goals
3. **Savings Advisor** - Identifies cost-saving opportunities and financial goals

## Features

- Automatic expense categorization across 10+ categories
- Spending pattern analysis and trend detection
- Personalized budget creation using proven methodologies (50/30/20, zero-based)
- Cost-saving opportunity identification
- Savings goal setting and tracking
- Debt payoff strategy recommendations
- Month-over-month spending comparisons
- Financial health insights and recommendations

## Architecture

### CrewAI Agents

#### 1. Expense Analysis Specialist
- **Role**: Categorize and analyze spending patterns
- **Expertise**: Transaction categorization, trend analysis, anomaly detection
- **Output**: Detailed spending breakdown with insights

#### 2. Budget Planning Expert
- **Role**: Create sustainable budgets
- **Expertise**: Budgeting methodologies, income allocation, financial planning
- **Output**: Personalized budget with category limits

#### 3. Savings Strategy Advisor
- **Role**: Maximize savings and achieve financial goals
- **Expertise**: Cost reduction, goal setting, wealth building
- **Output**: Actionable savings strategies and goal roadmap

### Process Flow

```
Financial Data Input (Income + Expenses)
        ↓
Expense Analyzer → Spending Analysis
        ↓
Budget Planner → Budget Plan
        ↓
Savings Advisor → Savings Strategy
        ↓
Complete Financial Plan
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Navigate to directory**

```bash
cd budget-tracker-agent482
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure environment**

```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Interactive Mode

```bash
python main.py
```

### Programmatic Usage

```python
from main import analyze_budget

financial_data = {
    "monthly_income": 6000,
    "expenses": {
        "rent": 1800,
        "utilities": 250,
        "groceries": 500,
        "dining_out": 400,
        "transportation": 300,
        "insurance": 400,
        "entertainment": 200,
        "subscriptions": 80,
        "miscellaneous": 300
    },
    "debt": {
        "credit_card": 150,
        "student_loan": 400
    },
    "current_savings": 5000,
    "financial_goals": [
        "Emergency fund: $18,000",
        "Down payment: $40,000",
        "Retirement contributions"
    ]
}

result = analyze_budget(financial_data)
print(result)
```

### Example Output

The system produces:

1. **Expense Analysis**
   - Categorized spending breakdown
   - Percentage of income per category
   - Spending trends and patterns
   - Unusual expense alerts

2. **Budget Plan**
   - Recommended spending limits per category
   - Budget methodology (50/30/20, etc.)
   - Variance analysis (actual vs budget)
   - Adjustment recommendations

3. **Savings Strategy**
   - 5-10 cost-saving opportunities
   - Savings goals with timelines
   - Monthly savings targets
   - Debt payoff priorities

## Budgeting Methodologies

### 50/30/20 Rule
- 50% Needs (housing, food, utilities, transportation)
- 30% Wants (entertainment, dining, hobbies)
- 20% Savings/Debt (emergency fund, retirement, debt payoff)

### Zero-Based Budgeting
- Every dollar assigned a purpose
- Income - Expenses = 0
- Maximizes intentional spending

### Envelope Method
- Cash allocated to categories
- When envelope empty, stop spending
- Great for discretionary categories

## Expense Categories

The system tracks expenses across standard categories:

- **Housing**: Rent/mortgage, property tax, HOA, insurance
- **Utilities**: Electric, gas, water, trash, internet, phone
- **Transportation**: Car payment, gas, insurance, maintenance, parking
- **Food**: Groceries, dining out, coffee, snacks
- **Healthcare**: Insurance, doctor visits, prescriptions, dental
- **Entertainment**: Streaming, hobbies, events, travel
- **Personal**: Clothing, grooming, gym, personal care
- **Debt**: Credit cards, student loans, personal loans
- **Savings**: Emergency fund, retirement, investments
- **Miscellaneous**: Gifts, donations, pet care, other

## Customization

### Change Budgeting Methodology

```python
# In main.py, specify preferred methodology
financial_data = {
    "monthly_income": 5000,
    "budget_methodology": "zero-based",  # or "50/30/20", "envelope"
    # ... other data
}
```

### Add Custom Expense Categories

```python
# In tools.py, extend categorization
custom_categories = {
    "pet_care": ["vet", "pet food", "grooming"],
    "education": ["tuition", "books", "courses"],
    "business": ["equipment", "software", "marketing"]
}
```

### Adjust Savings Priorities

```python
# In tasks.py, modify savings strategy task
financial_data = {
    "savings_priorities": [
        "emergency_fund_first",      # Build safety net
        "high_interest_debt",         # Pay off expensive debt
        "employer_match",             # Max 401k match
        "additional_savings"          # Extra savings goals
    ]
}
```

## Integration Options

### Bank Account Integration
- Plaid API (connect bank accounts)
- Teller API (bank transaction data)
- MX Platform (financial data aggregation)

### Budget Tracking Apps
- Mint API integration
- YNAB (You Need A Budget) API
- Personal Capital

### Export Formats
- CSV export for Excel/Google Sheets
- PDF reports
- JSON for custom integrations

## Best Practices

### Accurate Expense Tracking
- Track every expense (even small ones)
- Categorize consistently
- Use descriptive transaction notes
- Review monthly bank/credit statements

### Realistic Budgeting
- Base budget on actual spending history
- Start with current spending, then optimize
- Allow 10-15% buffer for unexpected expenses
- Adjust budget monthly based on reality

### Effective Savings
- Automate savings (pay yourself first)
- Start with small, achievable goals
- Track progress and celebrate milestones
- Increase savings rate gradually

## Troubleshooting

### "Income doesn't cover expenses"

Review and prioritize:
```python
# Focus on needs vs wants
priorities = [
    "Housing (rent/mortgage)",
    "Food (groceries)",
    "Utilities",
    "Transportation",
    "Healthcare",
    # Then reduce wants and discretionary spending
]
```

### Expenses categorized incorrectly

Provide more detailed transaction descriptions:
```python
expenses = {
    "groceries_safeway": 150,      # More specific
    "dining_chipotle": 35,          # Include merchant
    "utilities_electric_pge": 120   # Include utility type
}
```

### Savings goals seem unreachable

Break into smaller milestones:
```python
goals = {
    "emergency_fund": {
        "total": 15000,
        "milestones": [1000, 2500, 5000, 10000, 15000],
        "monthly_target": 500
    }
}
```

## Performance Optimization

### Reduce API Costs

```python
# Use GPT-3.5-turbo for routine analysis
agents = create_all_agents(model="gpt-3.5-turbo", temperature=0.7)

# Use GPT-4 only for complex planning
planner = create_budget_planner_agent(
    ChatOpenAI(model="gpt-4", temperature=0.5)
)
```

### Batch Analysis

Process multiple months at once:
```python
financial_data = {
    "time_period": "quarterly",
    "months": ["January", "February", "March"],
    # ... monthly data for each
}
```

## Advanced Features

### Debt Payoff Strategies

```python
# Snowball method (smallest balance first)
# Avalanche method (highest interest first)
debt_strategy = {
    "method": "avalanche",
    "debts": [
        {"name": "Credit Card A", "balance": 5000, "rate": 18.99, "min_payment": 150},
        {"name": "Credit Card B", "balance": 3000, "rate": 15.99, "min_payment": 90},
        {"name": "Student Loan", "balance": 25000, "rate": 5.5, "min_payment": 300}
    ],
    "extra_payment": 200  # Additional monthly amount
}
```

### Investment Recommendations

```python
# After emergency fund and debt payoff
investment_guidance = {
    "risk_tolerance": "moderate",
    "time_horizon": "20+ years",
    "accounts": ["401k", "IRA", "taxable"],
    "allocation": "age-based target date fund"
}
```

### Seasonal Budget Adjustments

```python
# Account for seasonal expenses
seasonal_factors = {
    "holiday_season": {"months": [11, 12], "extra_budget": 500},
    "summer_vacation": {"months": [6, 7], "extra_budget": 800},
    "tax_season": {"months": [4], "extra_expense": 200}
}
```

## Financial Health Metrics

The system tracks key metrics:

- **Savings Rate**: Percentage of income saved
- **Debt-to-Income Ratio**: Monthly debt payments / monthly income
- **Emergency Fund Coverage**: Months of expenses saved
- **Budget Adherence**: Actual spending vs budget
- **Net Worth Trend**: Assets - liabilities over time

## Example Use Cases

### Recent Graduate
```python
data = {
    "income": 3500,
    "student_loans": 25000,
    "rent": 900,
    "goals": ["Emergency fund", "Pay off debt", "Save for apartment"]
}
```

### Young Family
```python
data = {
    "income": 8000,
    "expenses": {"childcare": 1200, "mortgage": 2000},
    "goals": ["College savings", "Family vacation", "Home improvements"]
}
```

### Pre-Retirement
```python
data = {
    "income": 12000,
    "retirement_savings": 500000,
    "goals": ["Max retirement contributions", "Pay off mortgage", "Travel fund"]
}
```

## Future Enhancements

Potential improvements:
1. **Bank integration** for automatic expense import
2. **Receipt scanning** with OCR
3. **Bill reminders** and payment tracking
4. **Credit score monitoring** integration
5. **Tax optimization** recommendations
6. **Investment portfolio** analysis
7. **Net worth tracking** over time
8. **Budget vs actual** visualizations

## Privacy and Security

- All financial data processed locally
- No data stored by CrewAI agents
- OpenAI API calls encrypted
- Sensitive data never logged
- Use environment variables for API keys

## License

Apache 2.0

## Support

For issues or questions:
- Review example use cases
- Check troubleshooting section
- Adjust agent parameters for better results

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 482** - Budget Tracker
