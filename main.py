"""
Main entry point for the Modular NWFET Simulation Project.
"""

from src.logging_setup import setup_logging
from src.simulations import SimulationRunner

# Setup logging
setup_logging()

# Run simulations
if __name__ == "__main__":
    runner = SimulationRunner()
    # Run a specific simulation or all
    # runner.run_simulation('cv_thickness')  # Example
    runner.run_all()  # To run all simulations
