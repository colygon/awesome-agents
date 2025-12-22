#!/usr/bin/env python
from crewai import Crew, Process
from agents import AgriFlowAgents
from tasks import AgriFlowTasks
from dotenv import load_dotenv

load_dotenv()

def run_agriflow():
    print("## Welcome to AgriFlow Nexus")
    print('-------------------------------')

    farm_data = input("Enter farm data or 'default': ")
    if farm_data.lower() == 'default':
        farm_data = "33 acres corn, 3 zones, IoT sensors deployed"

    sensor_data = input("Enter sensor data or 'default': ")
    if sensor_data.lower() == 'default':
        sensor_data = "Soil sensors, weather station, drone imagery available"

    agents = AgriFlowAgents()
    tasks = AgriFlowTasks()

    crop_analyst = agents.crop_analyst()
    iot_processor = agents.iot_data_processor()
    optimizer = agents.farm_optimizer()
    coordinator = agents.agri_coordinator()

    crop_task = tasks.analyze_crops(crop_analyst, farm_data)
    iot_task = tasks.process_iot_data(iot_processor, sensor_data)
    optimize_task = tasks.optimize_operations(optimizer, "Current practices")
    plan_task = tasks.create_farm_plan(coordinator)

    crew = Crew(
        agents=[crop_analyst, iot_processor, optimizer, coordinator],
        tasks=[crop_task, iot_task, optimize_task, plan_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Farm Plan Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_agriflow()
