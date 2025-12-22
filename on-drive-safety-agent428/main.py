#!/usr/bin/env python
from crewai import Crew, Process
from agents import ONDriveSafetyAgents
from tasks import ONDriveSafetyTasks
from dotenv import load_dotenv

load_dotenv()

def run_on_drive_safety():
    print("## Welcome to ON:DRIVE Safety Platform")
    print('-------------------------------')

    vehicle_data = input("Enter vehicle data or 'default': ")
    if vehicle_data.lower() == 'default':
        vehicle_data = "2023 Sedan, 15K miles, all systems equipped"

    driving_data = input("Enter driving data or 'default': ")
    if driving_data.lower() == 'default':
        driving_data = "Last 30 days, 1,200 miles driven"

    route_data = input("Enter route data or 'default': ")
    if route_data.lower() == 'default':
        route_data = "Daily commute, 25 miles, Highway 101"

    agents = ONDriveSafetyAgents()
    tasks = ONDriveSafetyTasks()

    monitor = agents.vehicle_monitor()
    analyst = agents.driver_behavior_analyst()
    assessor = agents.risk_assessor()
    coordinator = agents.safety_coordinator()

    monitor_task = tasks.monitor_vehicle(monitor, vehicle_data)
    analyze_task = tasks.analyze_driver(analyst, driving_data)
    risk_task = tasks.assess_risks(assessor, route_data)
    coord_task = tasks.coordinate_safety(coordinator)

    crew = Crew(
        agents=[monitor, analyst, assessor, coordinator],
        tasks=[monitor_task, analyze_task, risk_task, coord_task],
        process=Process.sequential,
        verbose=True
    )

    result = crew.kickoff()

    print("\n\n########################")
    print("## Safety Analysis Complete!")
    print("########################\n")
    print(result)

    return result

if __name__ == "__main__":
    run_on_drive_safety()
