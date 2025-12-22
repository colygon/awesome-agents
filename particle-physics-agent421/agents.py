from crewai import Agent
from tools import ParticlePhysicsTools

class ParticlePhysicsAgents:
    def __init__(self):
        self.tools = ParticlePhysicsTools()

    def particle_data_analyst(self):
        return Agent(
            role='Particle Physics Data Analyst',
            goal='Analyze particle collision data and identify significant patterns and anomalies',
            backstory="""You are an expert in analyzing high-energy physics experimental data.
            You specialize in processing data from particle accelerators and detectors,
            identifying rare events, and extracting meaningful physics signals from noise.""",
            tools=[
                self.tools.analyze_collision_data,
                self.tools.detect_particle_signatures,
                self.tools.calculate_cross_sections
            ],
            verbose=True,
            allow_delegation=False
        )

    def theoretical_physicist(self):
        return Agent(
            role='Theoretical Particle Physicist',
            goal='Interpret experimental results within the framework of particle physics theories',
            backstory="""You are a theoretical physicist with deep knowledge of the Standard Model
            and beyond. You excel at comparing experimental observations with theoretical predictions,
            suggesting new physics scenarios, and calculating theoretical quantities.""",
            tools=[
                self.tools.calculate_feynman_diagrams,
                self.tools.predict_decay_channels,
                self.tools.compare_with_standard_model
            ],
            verbose=True,
            allow_delegation=False
        )

    def detector_specialist(self):
        return Agent(
            role='Particle Detector Specialist',
            goal='Optimize detector performance and interpret detector signals',
            backstory="""You are an expert in particle detector technology and signal processing.
            You understand how different particles interact with detector materials and can
            optimize detection strategies for various particle types and energy ranges.""",
            tools=[
                self.tools.simulate_detector_response,
                self.tools.calibrate_detector_systems,
                self.tools.optimize_trigger_conditions
            ],
            verbose=True,
            allow_delegation=False
        )

    def research_coordinator(self):
        return Agent(
            role='Physics Research Coordinator',
            goal='Synthesize findings from different analyses and prepare research outputs',
            backstory="""You are a senior physicist who coordinates complex particle physics
            research projects. You excel at integrating results from multiple analysis streams,
            assessing statistical significance, and presenting findings clearly.""",
            tools=[
                self.tools.calculate_statistical_significance,
                self.tools.search_physics_literature,
                self.tools.generate_research_summary
            ],
            verbose=True,
            allow_delegation=True
        )
