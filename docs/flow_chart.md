# Flow Chart: Modular NWFET Simulation Project

## Overall Process Flow

```
Start
├── Setup Environment
│   ├── Install Dependencies (numpy, matplotlib, pandas)
│   ├── Configure Logging
│   └── Load Constants from config/constants.py
├── Initialize Components
│   ├── Create NWFETSimulator (integrates all physics models)
│   ├── Create Plotters (2D and 3D plotting utilities)
│   ├── Create Data Exporter
│   └── Create Simulation Runner
├── Select and Run Simulations
│   ├── C-V Thickness Sweep
│   │   ├── Loop over materials and thicknesses
│   │   ├── Calculate capacitance using CapacitanceVoltageModel
│   │   ├── Plot using Plotter2D
│   │   └── Save to reports/plots/
│   ├── I-V Transfer Characteristics
│   │   ├── Calculate current using CurrentVoltageModel
│   │   ├── Plot I_D vs V_GS
│   │   └── Save plot
│   ├── I-V Output Characteristics
│   │   ├── Calculate current vs V_DS
│   │   ├── Plot I_D vs V_DS
│   │   └── Save plot
│   ├── Temperature-Dependent I-V
│   │   ├── Sweep temperature and voltage
│   │   ├── Calculate 3D current surface
│   │   ├── Plot using Plotter3D
│   │   └── Save 3D plot
│   ├── EIS Relaxation Study
│   │   ├── Calculate impedance using ImpedanceModel
│   │   ├── Plot Z'' vs frequency
│   │   └── Save plot
│   └── 3D Potential Profiles
│       ├── Model potential distribution
│       ├── Plot 3D surface
│       └── Save plot
├── Data Export
│   ├── Export simulation data to CSV
│   └── Save to reports/data/
├── Logging and Monitoring
│   ├── Log progress and errors
│   ├── Save log to reports/simulation.log
│   └── Console output for user feedback
└── Completion
    ├── Generate summary report
    └── End
```

## Key Components Interaction

- **Constants (config/constants.py)**: Central configuration for all parameters
- **Physics Models (src/physics_models.py)**: Core calculation classes
- **Plotting (src/plotting.py)**: Visualization classes
- **Simulations (src/simulations.py)**: High-level simulation orchestrators
- **Main (main.py)**: Entry point and runner

## Data Flow

1. **Input**: Constants and simulation parameters
2. **Processing**: Physics calculations using vectorized NumPy operations
3. **Visualization**: Matplotlib plotting with automatic saving
4. **Output**: PNG plots and CSV data in reports/ directory
5. **Logging**: Structured logging for debugging and monitoring

## Error Handling Flow

```
Any Error Occurs
├── Log error details
├── Attempt recovery if possible
├── Skip problematic simulation
└── Continue with next simulation
```

This flow ensures modular, maintainable, and scalable simulation framework.
