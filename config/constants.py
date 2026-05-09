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

# Simulation parameters
SIMULATION_PARAMETERS = {
    'voltage_range': [-5, 5],
    'voltage_points': 400,
    'temperature_range': [77, 600],
    'temperature_points': 50,
    'drain_voltage_range': [0, 1.2],
    'drain_voltage_points': 50,
    'frequency_range': [0, 7],  # log10 Hz
    'frequency_points': 71,
    'thickness_sweep': [1e-9, 5e-9, 10e-9, 15e-9, 20e-9, 25e-9, 30e-9],
}

# Plot settings
PLOT_SETTINGS = {
    'dpi': 300,
    'figsize_2d': (18, 11),
    'figsize_3d': (18, 10),
    'font_family': 'serif',
    'font_size': 11,
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'file': 'reports/simulation.log',
}

# Output directories
OUTPUT_DIRECTORIES = {
    'plots': './',
    'logs': 'reports/',
    'data': 'data/'
}
