from crewai import Task
from textwrap import dedent

class ParticlePhysicsTasks:
    def analyze_collision_events(self, agent, collision_data):
        return Task(
            description=dedent(f"""
                Analyze the particle collision data to identify interesting events
                and extract physics signals.

                Collision Data: {collision_data}

                Your analysis should include:
                1. Event selection and filtering
                2. Particle identification and reconstruction
                3. Background estimation
                4. Signal extraction
                5. Systematic uncertainty assessment
            """),
            expected_output="""A detailed analysis report containing:
                - Number of candidate events identified
                - Particle types and momenta reconstructed
                - Background levels and composition
                - Signal significance estimates
                - Key systematic uncertainties""",
            agent=agent
        )

    def theoretical_interpretation(self, agent, analysis_results):
        return Task(
            description=dedent(f"""
                Interpret the experimental results within theoretical frameworks
                and assess compatibility with physics models.

                Analysis Results: {analysis_results}

                Your interpretation should cover:
                1. Comparison with Standard Model predictions
                2. Assessment of agreement/disagreement
                3. Calculation of relevant theoretical quantities
                4. Suggestions for beyond Standard Model scenarios if applicable
                5. Predictions for related observables
            """),
            expected_output="""A theoretical interpretation including:
                - Standard Model predictions for the observed process
                - Chi-square or pull values for comparison
                - Theoretical uncertainties
                - Implications for new physics if relevant
                - Recommendations for follow-up studies""",
            agent=agent
        )

    def detector_optimization(self, agent, detector_config):
        return Task(
            description=dedent(f"""
                Optimize detector performance for the physics process of interest.

                Detector Configuration: {detector_config}

                Your optimization should address:
                1. Detector efficiency for target particles
                2. Background rejection capabilities
                3. Energy and momentum resolution
                4. Trigger strategy optimization
                5. Calibration requirements
            """),
            expected_output="""A detector optimization report with:
                - Efficiency curves for signal particles
                - Background rejection factors
                - Resolution estimates
                - Optimized trigger thresholds
                - Calibration strategy recommendations""",
            agent=agent
        )

    def synthesize_research_findings(self, agent):
        return Task(
            description=dedent("""
                Synthesize all analysis results, theoretical interpretations,
                and detector studies into a comprehensive research summary.

                Your synthesis should include:
                1. Executive summary of key findings
                2. Integration of experimental and theoretical results
                3. Statistical significance assessment
                4. Comparison with previous measurements
                5. Implications for particle physics
                6. Recommendations for future research
            """),
            expected_output="""A comprehensive research report containing:
                - Executive summary (1-2 paragraphs)
                - Main results with statistical significance
                - Theoretical context and interpretation
                - Comparison with literature
                - Physics implications
                - Future research directions
                - Key figures and tables
                - References to relevant papers""",
            agent=agent
        )
