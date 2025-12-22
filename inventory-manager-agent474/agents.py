from crewai import Agent
from tools import InventoryTrackingTools, ForecastingTools, OptimizationTools

class InventoryManagerAgents:
    def inventory_analyst(self):
        return Agent(
            role='Inventory Analyst',
            goal='Track and analyze inventory levels, movements, and trends',
            backstory="""You are an experienced inventory analyst who monitors
            stock levels, tracks product movements, and identifies trends in
            inventory data. You understand SKU management, turnover rates, and
            can spot potential stockouts or overstock situations before they
            become problems.""",
            tools=[
                InventoryTrackingTools.check_stock_levels,
                InventoryTrackingTools.track_product_movement,
                InventoryTrackingTools.calculate_turnover_rate
            ],
            verbose=True,
            allow_delegation=False
        )

    def demand_forecaster(self):
        return Agent(
            role='Demand Forecaster',
            goal='Predict future inventory needs based on historical data and trends',
            backstory="""You are a demand planning specialist who uses historical
            data, seasonal patterns, and market trends to forecast future inventory
            requirements. You help prevent stockouts while minimizing excess
            inventory and carrying costs.""",
            tools=[
                ForecastingTools.analyze_demand_patterns,
                ForecastingTools.predict_future_demand,
                ForecastingTools.identify_seasonal_trends
            ],
            verbose=True,
            allow_delegation=False
        )

    def reorder_manager(self):
        return Agent(
            role='Reorder Manager',
            goal='Optimize reorder points and quantities to maintain optimal stock levels',
            backstory="""You are a procurement specialist who manages reorder
            points, safety stock levels, and purchase orders. You balance the
            costs of holding inventory against the risk of stockouts, ensuring
            products are reordered at the right time and in the right quantities.""",
            tools=[
                OptimizationTools.calculate_reorder_point,
                OptimizationTools.optimize_order_quantity,
                OptimizationTools.set_safety_stock
            ],
            verbose=True,
            allow_delegation=False
        )

    def warehouse_optimizer(self):
        return Agent(
            role='Warehouse Optimizer',
            goal='Optimize warehouse operations, layout, and inventory placement',
            backstory="""You are a warehouse operations expert who optimizes
            storage layouts, picking routes, and inventory placement. You understand
            ABC analysis, FIFO/LIFO methods, and how to maximize warehouse
            efficiency while minimizing handling costs.""",
            tools=[
                OptimizationTools.perform_abc_analysis,
                InventoryTrackingTools.audit_inventory,
                OptimizationTools.optimize_storage_layout
            ],
            verbose=True,
            allow_delegation=False
        )
