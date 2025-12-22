from crewai import Task
from textwrap import dedent

class InventoryManagerTasks:
    def analyze_current_inventory(self, agent, inventory_data):
        return Task(
            description=dedent(f"""
                Analyze current inventory status and identify issues:

                Inventory Data:
                {inventory_data}

                Your tasks:
                1. Check stock levels for all SKUs
                2. Identify products at or below reorder point
                3. Flag overstock items
                4. Calculate inventory turnover rates
                5. Identify slow-moving or dead stock
                6. Track inventory aging
                7. Highlight items requiring immediate attention

                Provide comprehensive inventory status report.
            """),
            agent=agent,
            expected_output="Detailed inventory analysis with stock levels, turnover rates, and items requiring attention"
        )

    def forecast_demand(self, agent, historical_data):
        return Task(
            description=dedent(f"""
                Forecast future demand for inventory planning:

                Historical Data:
                {historical_data}

                Your tasks:
                1. Analyze historical sales and demand patterns
                2. Identify seasonal trends and cycles
                3. Account for promotional periods and events
                4. Predict demand for next 30, 60, and 90 days
                5. Calculate confidence intervals for forecasts
                6. Identify high-risk items (high variance in demand)
                7. Provide recommendations for safety stock levels

                Provide detailed demand forecast report.
            """),
            agent=agent,
            expected_output="Comprehensive demand forecast with predictions, trends, and safety stock recommendations"
        )

    def optimize_reorder_strategy(self, agent, product_catalog):
        return Task(
            description=dedent(f"""
                Optimize reorder points and quantities:

                Product Catalog:
                {product_catalog}

                Your tasks:
                1. Calculate optimal reorder points for each SKU
                2. Determine economic order quantities (EOQ)
                3. Set appropriate safety stock levels
                4. Consider lead times and supplier reliability
                5. Factor in storage costs and carrying costs
                6. Create reorder schedule and priorities
                7. Generate purchase order recommendations

                Provide optimized reorder strategy document.
            """),
            agent=agent,
            expected_output="Optimized reorder strategy with reorder points, quantities, and purchase recommendations"
        )

    def optimize_warehouse_operations(self, agent, warehouse_data):
        return Task(
            description=dedent(f"""
                Optimize warehouse layout and operations:

                Warehouse Data:
                {warehouse_data}

                Your tasks:
                1. Perform ABC analysis on inventory items
                2. Optimize product placement based on pick frequency
                3. Design efficient picking routes
                4. Recommend storage method improvements
                5. Identify opportunities for space optimization
                6. Suggest automation opportunities
                7. Create warehouse efficiency improvement plan

                Provide warehouse optimization recommendations.
            """),
            agent=agent,
            expected_output="Warehouse optimization plan with layout recommendations, efficiency improvements, and cost savings"
        )

    def generate_inventory_report(self, agent, reporting_period):
        return Task(
            description=dedent(f"""
                Generate comprehensive inventory management report:

                Reporting Period:
                {reporting_period}

                Your tasks:
                1. Summarize inventory performance metrics
                2. Report on stockouts and overstock situations
                3. Analyze inventory turnover and carrying costs
                4. Track accuracy of demand forecasts
                5. Measure warehouse efficiency metrics
                6. Identify cost savings opportunities
                7. Provide strategic recommendations
                8. Create executive summary with KPIs

                Provide complete inventory management report.
            """),
            agent=agent,
            expected_output="Comprehensive inventory report with metrics, analysis, and strategic recommendations"
        )
