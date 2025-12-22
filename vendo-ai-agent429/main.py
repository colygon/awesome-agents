#!/usr/bin/env python
from crewai import Crew, Process
from agents import VendoAIAgents
from tasks import VendoAITasks
from dotenv import load_dotenv

load_dotenv()

def run_vendo_ai():
    print("## Welcome to Vendo AI")
    print('-------------------------------')

    customer_query = input("Enter customer query or 'default': ")
    if customer_query.lower() == 'default':
        customer_query = "Looking for wireless headphones for daily commute"

    customer_data = input("Enter customer data or 'default': ")
    if customer_data.lower() == 'default':
        customer_data = "Returning customer, tech enthusiast, high value"

    agents = VendoAIAgents()
    tasks = VendoAITasks()

    product_spec = agents.product_specialist()
    insights = agents.customer_insights_analyst()
    optimizer = agents.sales_optimizer()
    coordinator = agents.vendo_coordinator()

    assist_task = tasks.assist_customer(product_spec, customer_query)
    analyze_task = tasks.analyze_customers(insights, customer_data)
    optimize_task = tasks.optimize_sales(optimizer, "Current metrics")
    solution_task = tasks.generate_solution(coordinator)

    crew = Crew(
        agents=[product_spec, insights, optimizer, coordinator],
        tasks=[assist_task, analyze_task, optimize_task, solution_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Vendo AI Solution Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_vendo_ai()
