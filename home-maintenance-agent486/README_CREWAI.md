# Home Maintenance - CrewAI Edition

## Overview

The Home Maintenance Assistant is a multi-agent system built with CrewAI that provides comprehensive home care guidance through three specialized agents:

1. **Home Repair Specialist** - Diagnoses issues and provides repair guidance
2. **Home Maintenance Coordinator** - Creates preventive maintenance schedules
3. **Home Improvement Consultant** - Guides remodeling and upgrade projects

## Features

- Repair diagnosis and DIY fix instructions
- Professional vs DIY assessments
- Comprehensive maintenance schedules (monthly/seasonal/annual)
- Home improvement project planning and budgeting
- Contractor hiring guidance
- Cost estimating for repairs and improvements
- Safety warnings and code compliance
- Material selection recommendations
- ROI analysis for improvements
- Preventive care to avoid costly repairs

## Architecture

### CrewAI Agents

#### 1. Home Repair Specialist
- **Role**: Diagnose and repair home issues
- **Expertise**: Plumbing, electrical, HVAC, appliances, general repairs
- **Output**: Repair diagnosis, DIY instructions, or professional referral

#### 2. Home Maintenance Coordinator
- **Role**: Create preventive maintenance schedules
- **Expertise**: System lifecycles, seasonal maintenance, tracking
- **Output**: Comprehensive maintenance calendar with checklists

#### 3. Home Improvement Consultant
- **Role**: Plan and budget improvement projects
- **Expertise**: Remodeling, material selection, contractor management
- **Output**: Project plan with budget, timeline, and execution guide

### Process Flow

```
Home Request (Repair + Maintenance + Improvement)
        ↓
Repair Specialist → Diagnosis & Fix Guide
        ↓
Maintenance Coordinator → Maintenance Schedule
        ↓
Improvement Consultant → Project Plan
        ↓
Complete Home Care Package
```

## Setup and Installation

### Prerequisites

- Python 3.10+
- OpenAI API key

### Installation

1. **Navigate to directory**

```bash
cd home-maintenance-agent486
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
from main import get_home_maintenance_help

request = {
    "home_info": {
        "type": "Condo",
        "age": "8 years",
        "size": "1,400 sq ft"
    },
    "repair": "Dishwasher not draining completely, water pooling at bottom",
    "maintenance": "Need seasonal maintenance checklist",
    "improvement": "Want to update kitchen backsplash, budget $1,500"
}

result = get_home_maintenance_help(request)
print(result)
```

### Example Output

The system produces:

1. **Repair Guidance**
   - Problem diagnosis
   - Step-by-step DIY instructions
   - Tools and materials needed
   - Safety warnings
   - When to call professional
   - Cost estimates

2. **Maintenance Schedule**
   - Monthly tasks
   - Seasonal checklists
   - Annual big tasks
   - System-by-system breakdown
   - Tracking calendar
   - Budget estimates

3. **Improvement Project Plan**
   - Project scope and timeline
   - Detailed budget
   - Material recommendations
   - DIY vs professional breakdown
   - Contractor hiring guide
   - ROI analysis

## Common Use Cases

### Emergency Repairs

```python
request = {
    "repair": "Water heater is leaking from the bottom. Is this an emergency?"
}
```

### Preventive Maintenance

```python
request = {
    "maintenance": "15-year-old home in humid climate, need comprehensive year-round maintenance plan"
}
```

### Remodeling Projects

```python
request = {
    "improvement": "Kitchen remodel - new cabinets, countertops, backsplash. Budget $25,000. What can I DIY?"
}
```

### New Homeowner

```python
request = {
    "home_info": "Just bought first home, 20 years old",
    "repair": "What should I inspect/fix first?",
    "maintenance": "What regular maintenance do I need?",
    "improvement": "What upgrades add most value?"
}
```

## Home Systems Covered

### Plumbing
- Leaks, clogs, pressure issues
- Toilets, faucets, drains
- Water heaters
- Sump pumps

### Electrical
- Outlets, switches, fixtures
- Circuit breakers
- GFCI outlets
- Lighting

### HVAC
- Heating and cooling systems
- Filters and maintenance
- Thermostats
- Ductwork

### Appliances
- Dishwashers, washing machines
- Refrigerators, ovens
- Garbage disposals
- Water filtration

### Exterior
- Roof and gutters
- Siding and paint
- Foundation
- Deck and patio
- Landscaping

### Interior
- Walls and flooring
- Doors and windows
- Cabinets and countertops
- Painting and finishing

## Safety First

### Always Call Professional For:

1. **Electrical**
   - Panel work
   - Rewiring
   - Adding circuits
   - Anything beyond outlet/switch replacement

2. **Plumbing**
   - Gas line work
   - Main line issues
   - Re-piping
   - Sewer line problems

3. **Structural**
   - Foundation repairs
   - Load-bearing wall modifications
   - Major settling/cracks

4. **Roofing**
   - Roof replacement
   - Major repairs
   - Anything multi-story

5. **HVAC**
   - System installation
   - Refrigerant work
   - Ductwork modifications

### DIY Safety Rules

- Turn off power/water before work
- Use proper safety equipment (goggles, gloves, respirator)
- Follow manufacturer instructions
- Know building codes
- Get permits when required
- Never work alone on ladders or heavy objects
- Know your skill limits

## Customization

### Adjust for Home Type

```python
# Different homes need different focus
home_types = {
    "single_family": "Full systems, yard, roof",
    "condo": "Interior focus, shared systems limited",
    "townhouse": "Some exterior, shared walls",
    "mobile_home": "Unique considerations"
}
```

### Climate-Specific Maintenance

```python
climate_tasks = {
    "cold": ["Winterize pipes", "Furnace service", "Ice dam prevention"],
    "hot": ["AC maintenance", "Irrigation system", "Heat protection"],
    "humid": ["Mold prevention", "Dehumidification", "Moisture control"],
    "coastal": ["Salt corrosion", "Hurricane prep", "Flood prevention"]
}
```

### Budget Tiers

```python
# Adjust recommendations based on budget
budget_levels = {
    "budget": "Essential repairs, DIY focus, basic materials",
    "moderate": "Quality materials, some professional help",
    "premium": "High-end materials, professional installation"
}
```

## Integration Options

### Home Management Apps
- HomeZada (maintenance tracking)
- BrightNest (task reminders)
- Centriq (manual/warranty storage)

### Service Providers
- Angi (contractor matching)
- HomeAdvisor (quotes)
- TaskRabbit (handyman services)

### Smart Home
- Nest/Ecobee (HVAC monitoring)
- Flo (water leak detection)
- Ring (security/doorbell)

## Maintenance Calendar Templates

### Monthly
- HVAC filter change
- Test smoke/CO detectors
- Clean garbage disposal
- Check GFCI outlets
- Inspect under sinks for leaks

### Quarterly
- Clean gutters
- Dryer vent cleaning
- Water heater flush
- Check weatherstripping
- Reverse ceiling fans

### Seasonal
- **Spring**: AC service, outdoor cleaning, gutter check
- **Summer**: Deck maintenance, exterior painting
- **Fall**: Heating service, winterize, clean chimney
- **Winter**: Check insulation, prevent frozen pipes

### Annual
- Roof inspection
- Septic pumping (if applicable)
- Chimney sweep
- Pressure wash exterior
- Deep clean carpets
- Service well pump (if applicable)

## Troubleshooting Common Issues

### "Not sure if it's emergency"

**Call immediately if:**
- Gas smell
- Electrical fire/sparks
- Major water leak
- No heat in freezing weather
- Complete power loss
- Sewage backup

**Can wait for business hours:**
- Slow drains
- Running toilet
- Minor leak
- Appliance not working
- Cosmetic issues

### "DIY repair failed"

Common reasons:
- Wrong diagnosis
- Missing tools/skills
- Harder than expected
- Code compliance issues

**Solutions:**
- Don't force it
- Call professional before causing damage
- Learn from experience
- Some jobs just need pros

### "Contractor quotes vary widely"

This is normal. Compare:
- Scope of work (same?)
- Materials specified
- Timeline
- Warranty/guarantee
- Reviews and references

Red flags:
- Dramatically low bid (too good to be true)
- All cash, no contract
- Pressure to decide immediately
- No license/insurance

## Cost Planning

### Emergency Fund
Recommended: 1-3% of home value annually for maintenance/repairs

Example for $300,000 home:
- Conservative: $3,000-9,000/year
- Rule of thumb: $500/month reserve

### Budgeting by Category
- **Routine maintenance**: $100-300/month
- **Minor repairs**: $500-2,000/year
- **Major systems**: Save for eventual replacement
  - Roof: $8,000-15,000 (20-25 year life)
  - HVAC: $5,000-10,000 (15-20 year life)
  - Water heater: $1,000-2,000 (10-15 year life)

### Improvement ROI
Best return on investment:
1. Minor kitchen remodel (70-80% ROI)
2. Bathroom update (60-70% ROI)
3. New garage door (60-70% ROI)
4. Deck addition (60-70% ROI)
5. Energy efficiency upgrades (varies)

## Future Enhancements

Potential improvements:
1. **Photo diagnosis** - Upload pictures of issues
2. **Video tutorials** - Visual repair guides
3. **Maintenance tracking** - Log completed tasks
4. **Cost database** - Real-time pricing by region
5. **Contractor matching** - Connect with local pros
6. **Warranty tracking** - Know what's covered
7. **Home value tracker** - Monitor equity impact
8. **Energy audit** - Efficiency recommendations

## Resources

### DIY Learning
- YouTube (This Old House, Home RenoVision DIY)
- Family Handyman magazine
- Fine Homebuilding
- Local hardware store workshops

### Professional Organizations
- NARI (National Association of the Remodeling Industry)
- NAHB (National Association of Home Builders)
- Better Business Bureau
- Angi (formerly Angie's List)

### Tools and Materials
- Home Depot / Lowe's
- Local hardware stores
- Specialized suppliers
- Online retailers

## License

Apache 2.0

## Support

For issues or questions:
- Review example use cases
- Check troubleshooting section
- Remember: Safety first, call professionals when needed

---

**CrewAI Version:** 0.86.0+
**Python Version:** 3.10+
**Agent 486** - Home Maintenance

**Safety Disclaimer**: This tool provides educational guidance only. Always prioritize safety, follow building codes, obtain required permits, and call licensed professionals for work beyond your skill level. Electrical, gas, structural, and other specialized work should be performed by licensed professionals.
