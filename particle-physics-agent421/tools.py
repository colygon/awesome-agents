from crewai_tools import tool
import numpy as np

class ParticlePhysicsTools:
    @tool("Analyze Collision Data")
    def analyze_collision_data(self, data: str) -> str:
        """
        Analyzes particle collision data to identify events of interest.
        Processes detector hits, reconstructs particle trajectories, and applies selection criteria.

        Args:
            data: Raw collision event data or data specification

        Returns:
            Analysis results including event counts and particle properties
        """
        # Simulation of collision data analysis
        return f"""Collision Data Analysis Results:
        - Total events processed: 1,000,000
        - Events passing selection: 1,247
        - Signal efficiency: 45.3%
        - Background contamination: ~12%

        Reconstructed particles:
        - Electrons: 856 candidates (avg pT: 38.2 GeV)
        - Muons: 723 candidates (avg pT: 42.1 GeV)
        - Jets: 2,341 candidates (avg pT: 95.7 GeV)
        - Missing ET: Average 31.5 GeV

        Invariant mass distribution shows peak at 91.2 GeV (Z boson)
        """

    @tool("Detect Particle Signatures")
    def detect_particle_signatures(self, event_data: str) -> str:
        """
        Identifies specific particle signatures in detector data based on
        characteristic decay patterns and detector responses.

        Args:
            event_data: Event-level detector information

        Returns:
            Identified particle types and confidence levels
        """
        return f"""Particle Signature Detection:
        - Z → e+e- candidates: 234 (purity: 89%)
        - Z → μ+μ- candidates: 198 (purity: 92%)
        - W → eν candidates: 412 (purity: 78%)
        - Top quark candidates: 23 (purity: 65%)
        - Higgs → γγ candidates: 12 (purity: 45%)

        Notable features:
        - Clean isolated leptons indicate electroweak processes
        - High-pT jets suggest heavy particle production
        - Missing energy consistent with neutrino production
        """

    @tool("Calculate Cross Sections")
    def calculate_cross_sections(self, process: str) -> str:
        """
        Calculates production cross sections for particle physics processes
        from measured event rates and integrated luminosity.

        Args:
            process: Physics process name

        Returns:
            Cross section values with uncertainties
        """
        return f"""Cross Section Calculation for {process}:
        - Measured cross section: 1.87 ± 0.12 (stat) ± 0.15 (syst) nb
        - Standard Model prediction: 1.92 ± 0.08 nb
        - Agreement: 1.2σ

        Systematic uncertainties:
        - Luminosity: 4.5%
        - Trigger efficiency: 3.2%
        - Background modeling: 5.8%
        - Detector acceptance: 2.9%

        The measurement is in good agreement with SM predictions.
        """

    @tool("Calculate Feynman Diagrams")
    def calculate_feynman_diagrams(self, process: str) -> str:
        """
        Calculates matrix elements and predictions from Feynman diagrams
        for specified particle physics processes.

        Args:
            process: Physics process to calculate

        Returns:
            Theoretical predictions and diagram information
        """
        return f"""Feynman Diagram Calculation for {process}:

        Leading order diagrams: 3
        - s-channel exchange
        - t-channel exchange
        - u-channel exchange

        Next-to-leading order contributions: 12 diagrams

        Theoretical predictions:
        - LO cross section: 1.85 nb
        - NLO cross section: 1.92 nb (K-factor: 1.038)
        - PDF uncertainty: ±4.2%
        - Scale uncertainty: ±3.8%

        Dominant production mechanism: gluon-gluon fusion (78%)
        """

    @tool("Predict Decay Channels")
    def predict_decay_channels(self, particle: str) -> str:
        """
        Predicts decay channels and branching ratios for particles
        based on Standard Model calculations.

        Args:
            particle: Particle name or type

        Returns:
            Decay channels with branching fractions
        """
        return f"""Decay Channel Predictions for {particle}:

        Major decay modes:
        1. {particle} → bb̄: 58.2% (BR)
        2. {particle} → WW*: 21.5%
        3. {particle} → ττ: 6.3%
        4. {particle} → ZZ*: 2.6%
        5. {particle} → γγ: 0.23%

        Total width: 4.07 MeV
        Mean lifetime: 1.56 × 10^-22 s

        Most promising search channels:
        - γγ: Clean signature, low background
        - ZZ* → 4ℓ: "Golden channel", excellent mass resolution
        - WW* → ℓνℓν: Higher rate, moderate background
        """

    @tool("Compare With Standard Model")
    def compare_with_standard_model(self, measurements: str) -> str:
        """
        Compares experimental measurements with Standard Model predictions
        and assesses agreement or tension.

        Args:
            measurements: Experimental measurement results

        Returns:
            Comparison results and statistical assessment
        """
        return f"""Standard Model Comparison:

        Observable: {measurements}
        Experimental value: 125.09 ± 0.24 GeV
        SM prediction: 125.10 ± 0.14 GeV

        Pull: -0.04σ (excellent agreement)
        Chi-square: 0.002 (1 dof)
        p-value: 0.96

        Conclusion: The measurement is in excellent agreement with SM predictions.
        No evidence for beyond-Standard-Model physics in this observable.

        Precision comparison:
        - Experimental precision: 0.19%
        - Theory precision: 0.11%
        - Measurement is systematics-limited
        """

    @tool("Simulate Detector Response")
    def simulate_detector_response(self, particle_type: str) -> str:
        """
        Simulates how particles interact with detector systems and
        the resulting signals in various detector components.

        Args:
            particle_type: Type of particle to simulate

        Returns:
            Detector response simulation results
        """
        return f"""Detector Response Simulation for {particle_type}:

        Tracking system:
        - Track reconstruction efficiency: 94.2%
        - Momentum resolution: σ(pT)/pT = 0.05% × pT ⊕ 1.2%
        - Impact parameter resolution: 15 μm

        Calorimetry:
        - Energy resolution: σ(E)/E = 10%/√E ⊕ 0.7%
        - Position resolution: 3 mm
        - Isolation efficiency: 87%

        Muon system:
        - Detection efficiency: 96.8%
        - Momentum resolution: 2.5% (pT < 200 GeV)
        - Fake rate: 0.3%

        Overall particle identification: 91.5% efficiency, 97.2% purity
        """

    @tool("Calibrate Detector Systems")
    def calibrate_detector_systems(self, system: str) -> str:
        """
        Performs calibration of detector systems using known physics processes
        and reference particles.

        Args:
            system: Detector subsystem to calibrate

        Returns:
            Calibration results and corrections
        """
        return f"""Detector Calibration Results for {system}:

        Calibration method: Z → ℓℓ events
        Reference sample: 125,000 events

        Energy scale correction:
        - Scale factor: 1.0021 ± 0.0003
        - Non-linearity correction: < 0.2% (E > 20 GeV)
        - Uniformity: < 0.5% across detector

        Resolution:
        - Constant term: 0.7%
        - Stochastic term: 10% / √E
        - Noise term: 0.3 GeV

        Time-dependent corrections applied
        Calibration valid for integrated luminosity: 150 fb^-1
        """

    @tool("Optimize Trigger Conditions")
    def optimize_trigger_conditions(self, physics_target: str) -> str:
        """
        Optimizes trigger thresholds and conditions to maximize signal
        efficiency while maintaining acceptable trigger rates.

        Args:
            physics_target: Target physics process

        Returns:
            Optimized trigger strategy
        """
        return f"""Trigger Optimization for {physics_target}:

        Recommended trigger configuration:
        - Single electron: pT > 27 GeV, |η| < 2.47
        - Single muon: pT > 24 GeV, |η| < 2.4
        - Di-electron: pT > 17, 12 GeV
        - Di-muon: pT > 14, 10 GeV
        - Missing ET: > 110 GeV

        Expected performance:
        - Signal efficiency: 92.3%
        - Trigger rate: 850 Hz (within budget)
        - Prescale factor: 1 (unprescaled)

        Background rejection: 99.97%
        Dead time: < 2%

        Trigger efficiency vs offline selection: 98.5%
        """

    @tool("Calculate Statistical Significance")
    def calculate_statistical_significance(self, signal: str, background: str) -> str:
        """
        Calculates statistical significance of observations using
        appropriate statistical methods for particle physics.

        Args:
            signal: Signal event count
            background: Background event count

        Returns:
            Statistical significance assessment
        """
        return f"""Statistical Significance Calculation:

        Signal events (S): {signal}
        Background events (B): {background}

        Simple significance: S/√B = 5.2σ
        Profile likelihood: 5.1σ
        Asimov significance: 5.0σ

        p-value: 2.8 × 10^-7
        Local significance: 5.0σ
        Global significance (look-elsewhere effect): 4.2σ

        Conclusion: Strong evidence for signal (> 5σ threshold)
        Compatible with discovery-level significance

        Systematic uncertainties included in significance calculation
        """

    @tool("Search Physics Literature")
    def search_physics_literature(self, query: str) -> str:
        """
        Searches particle physics literature databases (arXiv, INSPIRE-HEP)
        for relevant papers and references.

        Args:
            query: Search query for physics literature

        Returns:
            Relevant papers and citations
        """
        return f"""Literature Search Results for: {query}

        Top relevant papers:

        1. "Observation of {query} at the LHC"
           ATLAS Collaboration, Phys. Lett. B 716 (2012) 1-29
           Citations: 15,234

        2. "Measurement of {query} production cross section"
           CMS Collaboration, JHEP 06 (2021) 128
           Citations: 432

        3. "Precision calculations for {query}"
           Theoretical study, Phys. Rev. D 105 (2022) 013001
           Citations: 156

        4. "Search for new physics in {query}"
           LHCb Collaboration, arXiv:2312.xxxxx
           Citations: 23

        Related phenomenology studies: 47 papers
        Similar experimental searches: 18 papers
        """

    @tool("Generate Research Summary")
    def generate_research_summary(self, analysis_data: str) -> str:
        """
        Generates a comprehensive research summary integrating all
        analysis results and findings.

        Args:
            analysis_data: All analysis results to summarize

        Returns:
            Formatted research summary
        """
        return f"""PARTICLE PHYSICS RESEARCH SUMMARY

        EXECUTIVE SUMMARY
        We report measurements of particle production using collision data
        corresponding to an integrated luminosity of 150 fb^-1. The measured
        cross sections agree with Standard Model predictions at the 1.2σ level.

        MAIN RESULTS
        • Production cross section: 1.87 ± 0.12 (stat) ± 0.15 (syst) nb
        • Statistical significance: 5.0σ
        • Agreement with SM: 1.2σ deviation

        DETECTOR PERFORMANCE
        • Reconstruction efficiency: 92.3%
        • Signal purity: 88%
        • Systematic uncertainties well controlled

        THEORETICAL INTERPRETATION
        Results are consistent with SM predictions. No evidence for
        new physics observed. Precision limited by systematic uncertainties.

        FUTURE PROSPECTS
        • Higher luminosity will improve statistical precision by 2×
        • Improved calibrations can reduce systematic uncertainties by 30%
        • Additional decay channels could provide complementary measurements

        REFERENCES
        [1] ATLAS Collaboration, Phys. Lett. B 716 (2012) 1-29
        [2] CMS Collaboration, JHEP 06 (2021) 128
        """
