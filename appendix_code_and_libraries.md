# APPENDIX - CODE AND LIBRARIES

## A. LIBRARIES USED THROUGHOUT THE PROJECT

### A.1 Core Python Libraries
- **numpy** (>=1.21.0) - Numerical computations and array operations
- **matplotlib** (>=3.5.0) - Plotting and visualization
- **pandas** (>=1.3.0) - Data manipulation and analysis
- **logging** - Python standard library for logging
- **sqlite3** - Database management for web application
- **threading** - Concurrent programming for web server
- **hashlib** - Cryptographic hash functions
- **json** - JSON data handling
- **os**, **sys**, **pathlib** - System operations and path handling
- **datetime**, **time** - Date and time operations
- **http.server**, **urllib.parse** - Web server functionality

### A.2 Third-Party Libraries
- **python-docx** - Word document processing
- **mpl_toolkits.axes_grid1** - Advanced matplotlib plotting utilities

## B. MAIN CODE STRUCTURE

### B.1 Core Simulation Modules

#### B.1.1 `src/physics_models.py`
```python
"""
Physics models for NWFET simulations.
Contains classes and methods for analytical calculations.
"""

import numpy as np
import logging
from config.constants import (
    EPS0, ELEMENTARY_CHARGE, BOLTZMANN_CONSTANT,
    DEVICE_PARAMETERS, MATERIALS, GATE_CONFIGURATIONS
)

class CapacitanceVoltageModel:
    """Model for capacitance-voltage characteristics."""
    
    def calculate_capacitance(self, voltage, dielectric_constant, 
                            oxide_thickness, gate_efficiency, 
                            flatband_shift, dip_width):
        """Calculate C-V characteristics."""
        c_max = (EPS0 * dielectric_constant) / oxide_thickness
        dip_depth = 0.5 * (dielectric_constant / 3.9) ** 0.1
        flatband_voltage = flatband_shift
        capacitance = c_max * gate_efficiency * (
            1 - dip_depth * np.exp(-(voltage - flatband_voltage) ** 2 / dip_width)
        )
        return capacitance

class CurrentVoltageModel:
    """Model for current-voltage characteristics."""
    
    def calculate_drain_current(self, vgs, vds, material_params, 
                              gate_config, temperature):
        """Calculate drain current using analytical models."""
        # Implementation includes temperature-dependent mobility,
        # threshold voltage, and subthreshold swing
        pass
```

#### B.1.2 `src/plotting.py`
```python
"""
Plotting utilities for NWFET simulations.
Contains classes for 2D and 3D plotting.
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from config.constants import PLOT_SETTINGS, OUTPUT_DIRECTORIES

class Plotter2D:
    """2D plotting utilities."""
    
    def plot_material_grid(self, results, gate, vgs, filename):
        """Plot material grid for I-V characteristics."""
        # Implementation for material comparison plots
        pass
    
    def plot_temperature_dependence(self, results, filename):
        """Plot temperature-dependent characteristics."""
        # Implementation for temperature analysis
        pass

class Plotter3D:
    """3D plotting utilities."""
    
    def plot_surface_3d(self, x_data, y_data, z_data, 
                       xlabel, ylabel, zlabel, filename):
        """Create 3D surface plots."""
        # Implementation for 3D visualization
        pass
```

#### B.1.3 `src/simulations.py`
```python
"""
Simulation engine for NWFET analysis.
Main simulation controller and data processing.
"""

import numpy as np
import logging
from .physics_models import CapacitanceVoltageModel, CurrentVoltageModel
from .plotting import Plotter2D, Plotter3D
from config.constants import SIMULATION_PARAMETERS, MATERIALS, GATE_CONFIGURATIONS

class SimulationEngine:
    """Main simulation controller."""
    
    def __init__(self):
        self.cv_model = CapacitanceVoltageModel()
        self.iv_model = CurrentVoltageModel()
        self.plotter_2d = Plotter2D()
        self.plotter_3d = Plotter3D()
    
    def run_comparative_analysis(self):
        """Run comparative analysis of Pi-Gate vs Omega-Gate."""
        # Implementation for main comparative study
        pass
    
    def run_temperature_analysis(self):
        """Run temperature-dependent analysis."""
        # Implementation for temperature studies (77K to 600K)
        pass
```

### B.2 Configuration and Constants

#### B.2.1 `config/constants.py`
```python
"""
Constants and configuration for the Modular NWFET Simulation Project.
"""

# Physical constants
EPS0 = 8.854e-12  # Permittivity of free space (F/m)
ELEMENTARY_CHARGE = 1.602e-19  # Elementary charge (C)
BOLTZMANN_CONSTANT = 1.38e-23  # Boltzmann constant (J/K)

# Device parameters
DEVICE_PARAMETERS = {
    'channel_length': 10e-9,  # Channel length (m)
    'channel_width': 10e-9,   # Channel width (m)
    'oxide_thickness': 1e-9,  # Oxide thickness (m)
    'reference_mobility': 0.05,  # Reference mobility (m²/V·s)
    'temperature_coefficient': 0.0005,  # Temperature coefficient for Vth
    'threshold_voltage_reference': 0.35,  # Threshold voltage at reference temp (V)
    'channel_length_modulation': 0.05,  # Channel length modulation parameter
}

# Materials: {name: [k_value, v_shift, d_width, C0_factor]}
MATERIALS = {
    "SiO2": [3.9, 0.1, 1.8, 1e-10],
    "Al2O3": [9.0, 0.4, 2.2, 5e-10],
    "HfO2": [25.0, 0.8, 2.8, 1.2e-9],
    "ZrO2": [22.0, 0.7, 2.5, 1.1e-9],
    "La2O3": [27.0, 1.1, 3.2, 1.5e-9],
}

# Gate architectures: {name: {eta, series_resistance, mobility_reference}}
GATE_CONFIGURATIONS = {
    "PiGate": {"eta": 0.82, "series_resistance": 150, "mobility_reference": 0.04},
    "OmegaGate": {"eta": 0.98, "series_resistance": 50, "mobility_reference": 0.06},
}
```

### B.3 Web Application

#### B.3.1 `web_app/manage.py`
```python
#!/usr/bin/env python3
"""
NWFET Energy Band Diagram Program - Server Application.
Similar to Django's manage.py runserver functionality.
"""

import os
import sys
import json
import hashlib
import sqlite3
import threading
import time
from datetime import datetime, timedelta
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path

class DatabaseManager:
    """Handle database operations for users and sessions."""
    
    def __init__(self, db_path='database/nwfet_app.db'):
        """Initialize database manager with proper path resolution."""
        current_dir = os.path.dirname(os.path.abspath(__file__))
        self.db_path = os.path.join(current_dir, db_path)
        self.init_database()
    
    def init_database(self):
        """Initialize database tables with proper error handling."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                self._create_users_table(cursor)
                self._create_sessions_table(cursor)
                self._create_user_preferences_table(cursor)
                conn.commit()
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            raise

class NWFETRequestHandler(BaseHTTPRequestHandler):
    """HTTP request handler for NWFET web application."""
    
    def do_GET(self):
        """Handle GET requests."""
        # Implementation for serving web pages and API endpoints
        pass
    
    def do_POST(self):
        """Handle POST requests."""
        # Implementation for form submissions and data processing
        pass

def main():
    """Main server function."""
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, NWFETRequestHandler)
    print(f"NWFET Server running on port 8000")
    httpd.serve_forever()

if __name__ == "__main__":
    main()
```

## C. UTILITY SCRIPTS

### C.1 Data Generation Scripts
- `generate_comparison_plot.py` - Generate Pi-Gate vs Omega-Gate comparison plots
- `generate_temperature_plot.py` - Temperature-dependent analysis plots
- `generate_material_comparison.py` - Material performance comparison
- `generate_transfer_characteristics.py` - Transfer characteristics plots
- `generate_cryogenic_iv.py` - Cryogenic I-V characteristics

### C.2 EIS Analysis Scripts
- `eis_complete.py` - Complete Electrochemical Impedance Spectroscopy analysis
- `eis_visual.py` - Visualization of EIS data
- `eis_nyquist_plot.py` - Nyquist plot generation
- `generate_eis_plot_final.py` - Final EIS plot generation

## D. PROJECT STRUCTURE

```
modular_ece_project/
├── config/
│   ├── __init__.py
│   └── constants.py              # Physical constants and configuration
├── src/
│   ├── __init__.py
│   ├── physics_models.py         # Core physics simulation models
│   ├── plotting.py              # 2D and 3D plotting utilities
│   ├── simulations.py           # Main simulation engine
│   └── logging_setup.py         # Logging configuration
├── web_app/
│   ├── manage.py                # Web application server
│   ├── index.html              # Main web interface
│   ├── templates/              # HTML templates
│   ├── css/                    # Stylesheets
│   ├── js/                     # JavaScript files
│   └── database/               # SQLite database
├── tests/
│   └── test_physics_models.py   # Unit tests
├── reports/
│   ├── data/                   # Generated data
│   └── plots/                  # Generated plots
├── docs/                       # Documentation
├── requirements.txt            # Python dependencies
└── main.py                    # Main entry point
```

## E. INSTALLATION AND USAGE

### E.1 Environment Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install python-docx  # For document processing
```

### E.2 Running Simulations
```bash
# Run main simulation
python main.py

# Generate specific plots
python generate_comparison_plot.py
python generate_temperature_plot.py

# Run web application
cd web_app
python manage.py
```

## F. KEY FEATURES

### F.1 Physics Models
- **Capacitance-Voltage Modeling**: Analytical C-V characteristics with gate efficiency
- **Current-Voltage Modeling**: Temperature-dependent drain current calculations
- **Material Properties**: Five high-k dielectrics (SiO2, Al2O3, HfO2, ZrO2, La2O3)
- **Temperature Analysis**: 77K to 600K operating range

### F.2 Visualization Capabilities
- **2D Plotting**: Material comparisons, transfer characteristics
- **3D Surface Plots**: Temperature-dependent analysis
- **EIS Visualization**: Nyquist and Bode plots
- **Interactive Web Interface**: Real-time parameter exploration

### F.3 Web Application Features
- **User Management**: Registration and authentication
- **Interactive Simulations**: Real-time parameter adjustment
- **Data Persistence**: User preferences and session management
- **Export Capabilities**: Plot generation and data export

================================================================
This appendix provides a comprehensive overview of all libraries and main code components used throughout the NWFET simulation project.
