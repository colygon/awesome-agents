"""Smart Home Automation - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import SmartHomeAgents
from tasks import SmartHomeTasks

load_dotenv()


def setup_smart_home(devices: list, user_preferences: dict, security_config: dict) -> str:
    """Setup smart home automation system"""

    agents = SmartHomeAgents()
    tasks_factory = SmartHomeTasks()

    device_coordinator = agents.device_coordinator()
    automation_designer = agents.automation_designer()
    energy_optimizer = agents.energy_optimizer()
    security_monitor = agents.security_monitor()

    coordinate_task = tasks_factory.coordinate_devices(device_coordinator, devices)
    automation_task = tasks_factory.design_automation(automation_designer, user_preferences)
    automation_task.context = [coordinate_task]

    energy_task = tasks_factory.optimize_energy(energy_optimizer)
    energy_task.context = [coordinate_task]

    security_task = tasks_factory.monitor_security(security_monitor, security_config)
    security_task.context = [coordinate_task]

    crew = Crew(
        agents=[device_coordinator, automation_designer, energy_optimizer, security_monitor],
        tasks=[coordinate_task, automation_task, energy_task, security_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    devices = ['Philips Hue Lights', 'Nest Thermostat', 'Ring Doorbell', 'August Smart Lock']
    user_preferences = {'wake_time': '7:00', 'sleep_time': '23:00', 'comfort_temp': 72}
    security_config = {'armed_schedule': 'nights_and_away', 'notifications': 'all'}
    result = setup_smart_home(devices, user_preferences, security_config)
    print(result)


if __name__ == "__main__":
    main()
