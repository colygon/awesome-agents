"""Performance Monitor - CrewAI Implementation"""

import os
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import PerformanceMonitorAgents
from tasks import PerformanceMonitorTasks

load_dotenv()


def setup_performance_monitoring(system_config: dict, alert_config: dict) -> str:
    """Setup comprehensive performance monitoring"""

    agents = PerformanceMonitorAgents()
    tasks_factory = PerformanceMonitorTasks()

    metrics_collector = agents.metrics_collector()
    bottleneck_analyzer = agents.bottleneck_analyzer()
    trend_forecaster = agents.trend_forecaster()
    alert_manager = agents.alert_manager()

    collect_task = tasks_factory.collect_metrics(metrics_collector, system_config)
    analyze_task = tasks_factory.analyze_bottlenecks(bottleneck_analyzer)
    analyze_task.context = [collect_task]

    forecast_task = tasks_factory.forecast_trends(trend_forecaster)
    forecast_task.context = [collect_task]

    alert_task = tasks_factory.configure_alerts(alert_manager, alert_config)
    alert_task.context = [analyze_task]

    report_task = tasks_factory.generate_report(metrics_collector, system_config.get('name', 'System'))
    report_task.context = [collect_task, analyze_task, forecast_task, alert_task]

    crew = Crew(
        agents=[metrics_collector, bottleneck_analyzer, trend_forecaster, alert_manager],
        tasks=[collect_task, analyze_task, forecast_task, alert_task, report_task],
        process=Process.sequential,
        verbose=True
    )

    return crew.kickoff()


def main():
    system_config = {'name': 'WebApp', 'type': 'web_service', 'instances': 5}
    alert_config = {'cpu_threshold': 80, 'memory_threshold': 85, 'response_time': 500}
    result = setup_performance_monitoring(system_config, alert_config)
    print(result)


if __name__ == "__main__":
    main()
