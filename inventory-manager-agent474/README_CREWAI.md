# Inventory Manager - CrewAI Implementation

A multi-agent system for comprehensive inventory management, demand forecasting, and warehouse optimization using CrewAI.

## Overview

This CrewAI implementation provides an intelligent inventory management solution with specialized agents for inventory analysis, demand forecasting, reorder optimization, and warehouse operations.

## Agents

1. **Inventory Analyst**: Tracks stock levels, movements, and turnover rates
2. **Demand Forecaster**: Predicts future inventory needs and trends
3. **Reorder Manager**: Optimizes reorder points and quantities
4. **Warehouse Optimizer**: Improves warehouse layout and operations

## Features

- Real-time inventory tracking and monitoring
- Demand forecasting with confidence intervals
- Optimal reorder point calculations
- Economic Order Quantity (EOQ) optimization
- Safety stock recommendations
- ABC inventory analysis
- Warehouse layout optimization
- Inventory turnover analysis
- Automated alerts for low stock and overstock
- Comprehensive reporting and KPIs

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

Run the inventory manager:

```bash
python main.py
```

You'll be prompted to provide:
- Business type (retail, manufacturing, e-commerce)
- Number of SKUs
- Main inventory challenges
- Analysis date

The crew will then:
1. Analyze current inventory status
2. Forecast future demand
3. Optimize reorder strategies
4. Improve warehouse operations
5. Generate comprehensive reports

## Project Structure

```
inventory-manager-agent474/
├── agents.py           # Agent definitions
├── tasks.py           # Task definitions
├── tools.py           # Custom tools
├── main.py            # Main execution script
├── requirements.txt   # Dependencies
├── .env.example       # Environment template
└── README_CREWAI.md   # This file
```

## Tools

### Inventory Tracking Tools
- **Check Stock Levels**: Monitor current inventory
- **Track Product Movement**: Analyze inventory flow
- **Calculate Turnover Rate**: Measure inventory efficiency
- **Audit Inventory**: Maintain accuracy

### Forecasting Tools
- **Analyze Demand Patterns**: Identify trends
- **Predict Future Demand**: Forecast requirements
- **Identify Seasonal Trends**: Plan for seasonality

### Optimization Tools
- **Calculate Reorder Point**: Prevent stockouts
- **Optimize Order Quantity**: Minimize costs (EOQ)
- **Set Safety Stock**: Buffer against variability
- **Perform ABC Analysis**: Prioritize items
- **Optimize Storage Layout**: Improve efficiency

## Key Concepts

### Reorder Point (ROP)
```
ROP = (Average Daily Demand × Lead Time) + Safety Stock
```
The inventory level that triggers a new order.

### Economic Order Quantity (EOQ)
```
EOQ = √(2 × Annual Demand × Order Cost / Holding Cost)
```
The optimal order quantity that minimizes total costs.

### Safety Stock
```
Safety Stock = Z-score × Demand Std Dev × √Lead Time
```
Buffer inventory to protect against stockouts.

### Inventory Turnover
```
Turnover = Cost of Goods Sold / Average Inventory Value
```
Measures how quickly inventory sells.

## ABC Analysis

### A Items (High Value)
- 10% of SKUs, 70% of value
- Daily monitoring and tight control
- Accurate forecasting required
- Frequent cycle counts

### B Items (Medium Value)
- 30% of SKUs, 25% of value
- Weekly monitoring
- Regular review cycles
- Standard procedures

### C Items (Low Value)
- 60% of SKUs, 5% of value
- Monthly monitoring
- Simple reorder systems
- Bulk ordering acceptable

## Use Cases

- **Retail**: Multi-location inventory management
- **E-commerce**: Fast-moving consumer goods
- **Manufacturing**: Raw materials and components
- **Wholesale**: Distribution center operations
- **Healthcare**: Medical supplies and pharmaceuticals
- **Automotive**: Parts and accessories

## Key Metrics

### Inventory Metrics
- Stock levels by SKU
- Inventory turnover rate
- Days of inventory on hand
- Stockout frequency
- Fill rate percentage

### Financial Metrics
- Total inventory value
- Carrying costs
- Obsolescence costs
- Order costs
- Total cost of ownership

### Operational Metrics
- Order cycle time
- Lead time variability
- Forecast accuracy
- Warehouse utilization
- Pick accuracy

## Alerts and Notifications

The system can alert you for:
- Stock below reorder point
- Potential stockouts
- Overstock situations
- Slow-moving inventory
- Inventory discrepancies
- Supplier delays

## Integration Options

### ERP Systems
- SAP
- Oracle NetSuite
- Microsoft Dynamics
- Odoo

### Warehouse Management Systems (WMS)
- Manhattan Associates
- Blue Yonder
- Infor WMS

### E-commerce Platforms
- Shopify
- WooCommerce
- Magento
- Amazon Seller Central

### Suppliers
- EDI integration
- API connections
- Automated ordering

## Best Practices

1. **Regular Audits**: Conduct cycle counts regularly
2. **Data Accuracy**: Maintain clean, accurate data
3. **ABC Focus**: Prioritize A items for management
4. **Demand Planning**: Review forecasts regularly
5. **Safety Stock**: Balance service level and costs
6. **Lead Times**: Track supplier performance
7. **Seasonality**: Plan ahead for seasonal variations
8. **Technology**: Leverage automation where possible

## Optimization Strategies

### Reduce Carrying Costs
- Optimize order quantities
- Reduce safety stock where appropriate
- Implement just-in-time (JIT) for suitable items
- Negotiate better payment terms

### Prevent Stockouts
- Set appropriate reorder points
- Maintain safety stock for critical items
- Monitor lead times closely
- Develop backup suppliers

### Improve Turnover
- Identify and clear slow-moving stock
- Adjust pricing strategies
- Improve demand forecasting
- Optimize product mix

### Warehouse Efficiency
- Implement ABC slotting
- Optimize picking routes
- Use technology (RFID, barcode)
- Cross-train staff

## Output

The crew generates:
- Current inventory status reports
- Demand forecasts with confidence intervals
- Optimized reorder points and quantities
- Purchase order recommendations
- Warehouse optimization plans
- Executive KPI dashboards

## Requirements

- Python 3.10+
- OpenAI API key (or other LLM provider)
- Optional: ERP/WMS system access
- Historical sales data

## License

MIT License
