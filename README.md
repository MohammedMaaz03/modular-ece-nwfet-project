# Comparative Study of High-k Gate Dielectrics in Pi-Gate and Omega-Gate Silicon Nanowire FETs

## 📋 Project Overview

This project presents a comprehensive comparative analysis of Pi-Gate and Omega-Gate Silicon Nanowire Field Effect Transistors (NWFETs) using various high-k dielectric materials at cryogenic (77K) and elevated (600K) temperatures.

## 🔬 Research Focus

- **Gate Architectures**: Pi-Gate vs Omega-Gate NWFETs
- **High-k Dielectrics**: SiO₂, Al₂O₃, HfO₂, ZrO₂, La₂O₃
- **Temperature Range**: 77K to 600K
- **Analysis Types**: Electrical, Material, and Temperature-Dependent Characterization

## 🚀 Key Features

### Physics Models
- **Capacitance-Voltage (C-V) Modeling**: Analytical C-V characteristics with gate efficiency
- **Current-Voltage (I-V) Modeling**: Temperature-dependent drain current calculations
- **Material Properties**: Comprehensive database of high-k dielectric properties
- **Temperature Analysis**: Full thermal characterization from cryogenic to elevated temperatures

### Visualization & Analysis
- **2D Plotting**: Material comparisons, transfer characteristics
- **3D Surface Plots**: Temperature-dependent analysis with interactive visualization
- **EIS Analysis**: Electrochemical Impedance Spectroscopy with Nyquist and Bode plots
- **Interactive Web Interface**: Real-time parameter exploration and simulation

### Web Application
- **User Management**: Registration, authentication, and session management
- **Interactive Simulations**: Real-time parameter adjustment and visualization
- **Data Persistence**: User preferences and simulation history
- **Export Capabilities**: High-quality plot generation and data export
  - Temperature-dependent analysis
  - Electrochemical Impedance Spectroscopy (EIS)
  - 3D potential profiles
- **Flexible Configuration**: Centralized parameter management
- **High-Quality Visualization**: Publication-ready plots
- **Data Export**: CSV exports for further analysis
- **Comprehensive Logging**: Detailed logging for debugging and monitoring

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone or download the project
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running Simulations
Use the main script to run simulations:

```python
python main.py
```

This will run the C-V thickness sweep simulation by default. Modify `main.py` to run other simulations or all simulations.

### Available Simulations
- `cv_thickness`: C-V characteristics vs oxide thickness
- `iv_transfer`: I-V transfer characteristics
- `iv_output`: I-V output characteristics
- `temp_iv`: Temperature-dependent I-V analysis
- `eis`: EIS relaxation study
- `potential`: 3D potential profiles

### Custom Configuration
Edit `config/constants.py` to modify:
- Material properties
- Device parameters
- Simulation settings
- Plot configurations

### Output
- Plots saved to `reports/plots/`
- Data exported to `reports/data/`
- Logs written to `reports/simulation.log`

## Project Structure

```
modular_ece_project/
├── config/
│   └── constants.py          # Configuration constants
├── src/
│   ├── __init__.py
│   ├── physics_models.py     # Core physics calculation classes
│   ├── plotting.py           # Plotting and data export utilities
│   ├── simulations.py        # High-level simulation classes
│   └── logging_setup.py      # Logging configuration
├── tests/
│   └── test_physics_models.py # Unit tests
├── reports/
│   ├── plots/                # Generated plots
│   ├── data/                 # Exported data
│   └── simulation.log        # Log file
├── docs/
│   ├── flow_chart.md         # Process flow documentation
│   └── project_document.md   # Detailed project documentation
├── main.py                   # Main entry point
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Testing

Run the test suite:
```bash
pytest tests/
```

## Architecture

The project follows a modular architecture:

- **Configuration Layer**: Centralized constants and parameters
- **Model Layer**: Physics-based calculation classes
- **Visualization Layer**: Plotting and data export utilities
- **Simulation Layer**: High-level simulation orchestrators
- **Execution Layer**: Main runner and logging setup

See `docs/flow_chart.md` for detailed process flow.

## Dependencies

- numpy: Numerical computations
- matplotlib: Plotting and visualization
- pandas: Data manipulation and export

## Contributing

1. Follow PEP8 coding standards
2. Add unit tests for new features
3. Update documentation
4. Use proper logging

## License

This project is for educational and research purposes.

## Contact

For questions or contributions, please refer to the project documentation.
