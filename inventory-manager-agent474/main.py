#!/usr/bin/env python
from crewai import Crew, Process
from agents import InventoryManagerAgents
from tasks import InventoryManagerTasks
from dotenv import load_dotenv

load_dotenv()

def run_inventory_manager():
    """
    Run the Inventory Manager crew to optimize inventory operations
    """
    print("## Welcome to the Inventory Manager Crew")
    print("-----------------------------------------")

    # Get user input for inventory analysis
    business_type = input("What type of business? (e.g., retail, manufacturing, e-commerce): ")
    num_skus = input("Approximate number of SKUs: ")
    main_challenge = input("Main inventory challenge? (e.g., stockouts, overstock, forecasting): ")

    inventory_data = f"""
    Business Type: {business_type}
    Number of SKUs: {num_skus}
    Main Challenge: {main_challenge}
    Analysis Date: {input("Analysis date (YYYY-MM-DD): ")}
    """

    historical_data = f"""
    Historical sales data for {business_type}
    Period: Last 12 months
    """

    product_catalog = f"""
    Product catalog with {num_skus} SKUs
    Including cost, lead time, and demand data
    """

    warehouse_data = f"""
    Warehouse configuration and current layout
    Total storage capacity and utilization
    """

    # Initialize agents
    agents = InventoryManagerAgents()
    tasks_manager = InventoryManagerTasks()

    # Create agents
    inventory_analyst = agents.inventory_analyst()
    demand_forecaster = agents.demand_forecaster()
    reorder_manager = agents.reorder_manager()
    warehouse_optimizer = agents.warehouse_optimizer()

    # Create tasks
    analysis_task = tasks_manager.analyze_current_inventory(
        inventory_analyst,
        inventory_data
    )

    forecast_task = tasks_manager.forecast_demand(
        demand_forecaster,
        historical_data
    )

    reorder_task = tasks_manager.optimize_reorder_strategy(
        reorder_manager,
        product_catalog
    )

    warehouse_task = tasks_manager.optimize_warehouse_operations(
        warehouse_optimizer,
        warehouse_data
    )

    report_task = tasks_manager.generate_inventory_report(
        inventory_analyst,
        "Current Quarter"
    )

    # Create and run crew
    crew = Crew(
        agents=[
            inventory_analyst,
            demand_forecaster,
            reorder_manager,
            warehouse_optimizer
        ],
        tasks=[
            analysis_task,
            forecast_task,
            reorder_task,
            warehouse_task,
            report_task
        ],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Inventory Manager Results")
    print("########################\n")
    print(result)

    return result


if __name__ == "__main__":
    run_inventory_manager()
