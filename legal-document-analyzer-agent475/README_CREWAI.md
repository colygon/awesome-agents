# Legal Document Analyzer - CrewAI Implementation

A multi-agent system for analyzing legal documents, contracts, and agreements using CrewAI with specialized agents for parsing, analysis, compliance checking, and summarization.

## Overview

This CrewAI implementation automates legal document analysis by coordinating specialized agents that extract information, analyze terms, check compliance, and create plain-language summaries of complex legal documents.

## Agents

1. **Document Parser**: Extracts structured information from legal documents
2. **Contract Analyzer**: Analyzes terms, obligations, and risks
3. **Compliance Checker**: Verifies regulatory compliance
4. **Legal Summarizer**: Creates executive summaries in plain language

## Features

- Automated document parsing and information extraction
- Party, date, and clause identification
- Term and obligation analysis
- Risk assessment and red flag detection
- Regulatory compliance checking (GDPR, CCPA, etc.)
- Missing provision identification
- Document comparison capabilities
- Executive summaries in plain language
- Action item generation

## Installation

1. Clone this repository or navigate to the project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Usage

Run the legal document analyzer:

```bash
python main.py
```

You'll be prompted to provide:
- Document type (contract, NDA, employment agreement, etc.)
- Document name/title
- Analysis purpose
- Optional: comparison document

The crew will then:
1. Parse and extract structured information
2. Analyze contract terms and obligations
3. Check regulatory compliance
4. Create executive summary
5. Optionally compare documents

## Project Structure

```
legal-document-analyzer-agent475/
├── agents.py           # Agent definitions
├── tasks.py           # Task definitions
├── tools.py           # Custom tools
├── main.py            # Main execution script
├── requirements.txt   # Dependencies
├── .env.example       # Environment template
└── README_CREWAI.md   # This file
```

## Tools

### Document Parsing Tools
- **Extract Parties**: Identifies all parties and stakeholders
- **Extract Dates**: Finds deadlines and important dates
- **Identify Clauses**: Categorizes legal clauses
- **Generate Comparison**: Compares multiple documents

### Analysis Tools
- **Analyze Terms**: Reviews contract terms and conditions
- **Identify Obligations**: Maps party obligations
- **Assess Risks**: Evaluates potential risks
- **Create Executive Summary**: Plain language overview
- **Highlight Key Points**: Most important information

### Compliance Tools
- **Check Regulatory Compliance**: Verifies legal compliance
- **Verify Standard Clauses**: Ensures complete contracts
- **Identify Missing Provisions**: Finds gaps

## Supported Document Types

### Contracts
- Service agreements
- Sales contracts
- Partnership agreements
- Licensing agreements
- Vendor contracts

### Employment Documents
- Employment agreements
- Offer letters
- Consulting agreements
- Non-compete agreements

### Confidentiality
- Non-disclosure agreements (NDAs)
- Confidentiality agreements
- Data processing agreements

### Real Estate
- Lease agreements
- Purchase agreements
- Property management contracts

### Corporate
- Shareholder agreements
- Operating agreements
- Bylaws and articles

## Analysis Components

### Document Parsing
- Party identification and roles
- Key date extraction
- Clause categorization
- Financial term extraction
- Milestone identification

### Risk Assessment
- Financial risks
- Liability exposure
- Performance risks
- Termination conditions
- IP rights concerns
- Data privacy issues

### Compliance Checking
- GDPR compliance
- CCPA compliance
- Industry regulations
- Standard clause verification
- Missing provision identification

### Executive Summary
- Plain language overview
- Key highlights
- Financial summary
- Critical dates
- Recommendations

## Use Cases

- **Pre-signature Review**: Analyze contracts before signing
- **Due Diligence**: Review documents for M&A
- **Contract Management**: Ongoing contract monitoring
- **Compliance Audits**: Verify regulatory compliance
- **Vendor Management**: Evaluate vendor agreements
- **Employment**: Review employment documents
- **Real Estate**: Analyze lease and purchase agreements

## Key Features Detected

### Financial Terms
- Payment amounts and schedules
- Price adjustments and escalations
- Expense handling
- Late fees and penalties
- Security deposits or retainers

### Performance Terms
- Service levels and SLAs
- Deliverables and milestones
- Quality standards
- Acceptance criteria
- Reporting requirements

### Legal Protections
- Liability caps and limitations
- Indemnification provisions
- Insurance requirements
- Warranty disclaimers
- Force majeure

### Exit Terms
- Termination conditions
- Notice periods
- Termination fees
- Transition assistance
- Post-termination obligations

## Risk Levels

### High Risk
- Unlimited liability exposure
- Unfavorable IP terms
- Onerous penalties
- One-sided obligations
- Missing critical protections

### Medium Risk
- Limited remedies
- Automatic renewals
- Broad confidentiality
- Restrictive covenants
- Moderate liability caps

### Low Risk
- Standard terms
- Balanced obligations
- Fair termination rights
- Adequate protections
- Clear definitions

## Output

The crew generates:
- Structured document data (JSON)
- Term and obligation analysis
- Risk assessment report
- Compliance checklist
- Executive summary
- Action item list
- Comparison tables (if requested)

## Compliance Regulations

### Data Privacy
- GDPR (EU)
- CCPA (California)
- PIPEDA (Canada)
- Privacy Shield
- Data localization laws

### Industry Specific
- HIPAA (Healthcare)
- SOC 2 (Security)
- PCI DSS (Payments)
- FDA (Pharmaceuticals)
- FINRA (Financial services)

### Employment
- FLSA (Fair Labor Standards)
- EEOC regulations
- State employment laws
- Benefits compliance

## Best Practices

1. **Review Original**: Always review the original document
2. **Verify Accuracy**: Confirm extracted information is correct
3. **Seek Legal Counsel**: Use for preliminary review, not legal advice
4. **Track Changes**: Compare versions before signing
5. **Document Questions**: Note items needing clarification
6. **Set Reminders**: Calendar critical dates and deadlines
7. **Regular Reviews**: Periodic contract reviews

## Limitations

- Not a substitute for legal counsel
- May not catch all nuances
- OCR errors possible with scanned documents
- Jurisdiction-specific laws require expert review
- Complex legal language may need clarification

## Integration Options

### Document Management
- SharePoint
- DocuSign
- PandaDoc
- ContractWorks

### Legal Research
- LexisNexis
- Westlaw
- Bloomberg Law

### Contract Lifecycle Management
- Icertis
- Agiloft
- Concord
- Ironclad

## Requirements

- Python 3.10+
- OpenAI API key (or other LLM provider)
- PDF/text documents
- Optional: OCR service for scanned documents

## Disclaimer

This tool provides automated analysis to assist in document review. It is not a substitute for professional legal advice. Always consult with qualified legal counsel for important legal matters.

## License

MIT License
