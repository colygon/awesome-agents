"""CrewAI Tasks for Performance Monitor"""

from crewai import Task
from textwrap import dedent


class PerformanceMonitorTasks:
    """Factory class for performance monitoring tasks"""

    def collect_metrics(self, agent, system_config: dict) -> Task:
        return Task(
            description=dedent(f"""
                Collect performance metrics:
                System: {system_config}

                Collect:
                1. CPU usage and load averages
                2. Memory utilization
                3. Disk I/O and space
                4. Network traffic
                5. Application response times
                6. Database query performance
                7. Error rates and exceptions
            """),
            agent=agent,
            expected_output='Comprehensive metrics collection plan with data sources'
        )

    def analyze_bottlenecks(self, agent, metrics_data: dict = None) -> Task:
        return Task(
            description=dedent(f"""
                Analyze performance bottlenecks:
                Metrics: {metrics_data if metrics_data else 'Current system metrics'}

                Identify:
                1. Slow database queries
                2. Memory leaks
                3. CPU-intensive operations
                4. I/O bottlenecks
                5. Network latency issues
                6. Inefficient algorithms
                7. Resource contention
            """),
            agent=agent,
            expected_output='Bottleneck analysis with root causes and impact assessment',
            context=[]
        )

    def forecast_trends(self, agent, historical_data: dict = None) -> Task:
        return Task(
            description=dedent(f"""
                Forecast performance trends:
                Historical Data: {historical_data if historical_data else 'Last 30 days'}

                Forecast:
                1. Resource usage trends
                2. Capacity planning needs
                3. Scaling requirements
                4. Cost projections
                5. Peak usage patterns
                6. Seasonal variations
            """),
            agent=agent,
            expected_output='Performance trend analysis with capacity recommendations',
            context=[]
        )

    def configure_alerts(self, agent, alert_config: dict) -> Task:
        return Task(
            description=dedent(f"""
                Configure performance alerts:
                Config: {alert_config}

                Setup:
                1. Threshold-based alerts
                2. Anomaly detection rules
                3. Alert severity levels
                4. Escalation policies
                5. Notification channels
                6. Alert aggregation rules
                7. SLA monitoring
            """),
            agent=agent,
            expected_output='Alert configuration with intelligent thresholds',
            context=[]
        )

    def generate_report(self, agent, system_name: str) -> Task:
        return Task(
            description=dedent(f"""
                Generate performance monitoring report:
                System: {system_name}

                Include:
                1. Current performance status
                2. Key metrics summary
                3. Identified bottlenecks
                4. Trend analysis
                5. Alert configuration
                6. Optimization recommendations
                7. Action items
            """),
            agent=agent,
            expected_output='Comprehensive performance monitoring report',
            context=[]
        )
