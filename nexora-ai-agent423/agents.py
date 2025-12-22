from crewai import Agent
from tools import NexoraAITools

class NexoraAIAgents:
    def __init__(self):
        self.tools = NexoraAITools()

    def ai_model_architect(self):
        return Agent(
            role='AI Model Architect',
            goal='Design and architect advanced AI model architectures for various use cases',
            backstory="""You are an expert in AI/ML model architecture design.
            You specialize in creating efficient, scalable model architectures optimized
            for specific tasks, from computer vision to NLP to multimodal systems.""",
            tools=[
                self.tools.design_model_architecture,
                self.tools.optimize_model_structure,
                self.tools.select_model_components
            ],
            verbose=True,
            allow_delegation=False
        )

    def training_specialist(self):
        return Agent(
            role='Model Training Specialist',
            goal='Optimize training processes and hyperparameters for best model performance',
            backstory="""You are a machine learning training expert who excels at optimizing
            training pipelines, selecting hyperparameters, and ensuring models converge
            efficiently while avoiding overfitting.""",
            tools=[
                self.tools.configure_training_pipeline,
                self.tools.tune_hyperparameters,
                self.tools.monitor_training_metrics
            ],
            verbose=True,
            allow_delegation=False
        )

    def deployment_engineer(self):
        return Agent(
            role='AI Deployment Engineer',
            goal='Deploy AI models efficiently and ensure optimal inference performance',
            backstory="""You specialize in deploying AI models to production environments.
            You optimize for latency, throughput, and cost while ensuring reliability
            and scalability of AI inference systems.""",
            tools=[
                self.tools.optimize_for_inference,
                self.tools.deploy_model_endpoint,
                self.tools.configure_autoscaling
            ],
            verbose=True,
            allow_delegation=False
        )

    def ai_project_coordinator(self):
        return Agent(
            role='AI Project Coordinator',
            goal='Coordinate AI development lifecycle and ensure project success',
            backstory="""You are an experienced AI project manager who oversees the entire
            AI development lifecycle. You ensure alignment between model design, training,
            deployment, and business objectives.""",
            tools=[
                self.tools.evaluate_model_performance,
                self.tools.generate_model_documentation,
                self.tools.plan_ai_roadmap
            ],
            verbose=True,
            allow_delegation=True
        )
