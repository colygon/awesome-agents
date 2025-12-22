from crewai import Task
from textwrap import dedent

class NexoraAITasks:
    def design_ai_architecture(self, agent, use_case):
        return Task(
            description=dedent(f"""
                Design an AI model architecture optimized for the specified use case.

                Use Case: {use_case}

                Your design should include:
                1. Model architecture selection and justification
                2. Component specifications (layers, attention mechanisms, etc.)
                3. Input/output specifications
                4. Model size and complexity analysis
                5. Expected performance characteristics
            """),
            expected_output="""A comprehensive architecture design document containing:
                - Selected architecture type and rationale
                - Detailed layer specifications
                - Parameter count and model size estimates
                - Expected computational requirements
                - Performance projections
                - Architecture diagram description
                - Trade-offs and design decisions""",
            agent=agent
        )

    def optimize_training_process(self, agent, architecture_spec):
        return Task(
            description=dedent(f"""
                Design and optimize the training process for the AI model.

                Architecture Specification: {architecture_spec}

                Your training plan should include:
                1. Training pipeline configuration
                2. Hyperparameter recommendations
                3. Data preprocessing strategy
                4. Training schedule and learning rate policy
                5. Regularization and optimization techniques
            """),
            expected_output="""A complete training optimization plan with:
                - Training pipeline architecture
                - Recommended hyperparameters (learning rate, batch size, etc.)
                - Data augmentation and preprocessing steps
                - Learning rate schedule
                - Optimization algorithm selection
                - Regularization strategies
                - Expected training time and resource requirements
                - Monitoring and checkpointing strategy""",
            agent=agent
        )

    def plan_deployment_strategy(self, agent, model_specs):
        return Task(
            description=dedent(f"""
                Plan the deployment strategy for the trained AI model.

                Model Specifications: {model_specs}

                Your deployment plan should address:
                1. Inference optimization techniques
                2. Deployment infrastructure requirements
                3. Scaling strategy
                4. Latency and throughput targets
                5. Cost optimization
            """),
            expected_output="""A comprehensive deployment strategy including:
                - Inference optimization recommendations (quantization, pruning, etc.)
                - Infrastructure specifications
                - API endpoint design
                - Auto-scaling configuration
                - Performance targets (latency, throughput)
                - Cost estimates and optimization strategies
                - Monitoring and observability setup
                - Rollback and versioning strategy""",
            agent=agent
        )

    def coordinate_ai_project(self, agent):
        return Task(
            description=dedent("""
                Coordinate the complete AI project and ensure successful delivery.

                Your coordination should include:
                1. Integration of architecture, training, and deployment plans
                2. Performance evaluation against objectives
                3. Risk assessment and mitigation
                4. Documentation and knowledge transfer
                5. Future improvement roadmap
            """),
            expected_output="""A comprehensive AI project summary containing:
                - Executive summary of the AI solution
                - Integrated architecture, training, and deployment overview
                - Performance metrics and evaluation results
                - Risk assessment and mitigation strategies
                - Complete technical documentation
                - Model cards and usage guidelines
                - Maintenance and monitoring plan
                - Future enhancement roadmap
                - Success criteria and KPIs""",
            agent=agent
        )
