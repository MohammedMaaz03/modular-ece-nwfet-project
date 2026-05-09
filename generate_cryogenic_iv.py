import numpy as np
import matplotlib.pyplot as plt

# Material properties at 77K (cryogenic temperature)
materials = ['Si', 'Ge', 'GaAs', 'InAs', 'GaN']
gates = ['Pi-Gate', 'Omega-Gate']

# Dramatically enhanced material parameters for cryogenic operation
material_params = {
    'Si': {'Vt_offset': 0.20, 'mu_factor': 2.0, 'ss_factor': 1.4, 'bandgap': 1.12},
    'Ge': {'Vt_offset': 0.12, 'mu_factor': 6.0, 'ss_factor': 1.1, 'bandgap': 0.66},
    'GaAs': {'Vt_offset': 0.25, 'mu_factor': 10.0, 'ss_factor': 1.0, 'bandgap': 1.42},
    'InAs': {'Vt_offset': 0.08, 'mu_factor': 15.0, 'ss_factor': 0.9, 'bandgap': 0.36},
    'GaN': {'Vt_offset': 0.30, 'mu_factor': 8.0, 'ss_factor': 0.95, 'bandgap': 3.4}
}

gate_params = {
    'Pi-Gate': {'eta': 0.82, 'ss_penalty': 1.1},
    'Omega-Gate': {'eta': 0.98, 'ss_penalty': 1.0}
}

# Temperature and constants
T = 77  # K
k = 1.380649e-23
q = 1.60217662e-19
kT_q = k * T / q

# Gate voltage range
Vgs = np.linspace(-0.5, 1.2, 1000)

def calculate_cryogenic_current(Vgs, material, gate):
    """Calculate drain current with cryogenic-specific physics"""
    params = material_params[material]
    gate_param = gate_params[gate]

    # Base threshold voltage with material and gate dependencies
    Vt_base = 0.3
    Vt = Vt_base - params['Vt_offset'] * (1 + (1 - gate_param['eta']) * 0.2)

    # Enhanced mobility at cryogenic temperature
    mu_cryo = params['mu_factor'] * 1e-2  # cm²/Vs

    # Subthreshold swing with cryogenic improvement
    ss_theoretical = kT_q * np.log(10)  # ~6.7 mV/dec at 77K
    ss = ss_theoretical * params['ss_factor'] * gate_param['ss_penalty']

    # Cox approximation (3 nm SiO2 equivalent)
    Cox = 1.15e-6  # F/cm²

    # Current calculation with cryogenic-specific features
    Vgs_eff = Vgs - Vt

    # Subthreshold current (exponential behavior)
    I_sub = np.exp(Vgs_eff / (ss / np.log(10))) * 1e-12

    # Above threshold current (saturation-like)
    I_sat = mu_cryo * Cox * (Vgs_eff**2) * 1e-6

    # Smooth transition
    alpha = 1 / (1 + np.exp(-10 * Vgs_eff))
    Ids = (1 - alpha) * I_sub + alpha * I_sat

    # Add material-specific noise/quantization effects at low T
    noise_factor = 0.01 * (1 + np.sin(Vgs * 20) * np.exp(-np.abs(Vgs_eff) / 0.1))
    Ids *= (1 + noise_factor)

    return np.maximum(Ids, 1e-18)  # Minimum current floor

# Color and style schemes for distinct visualization
colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
linestyles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'D', 'v']

# Create figure with subplots
fig, axes = plt.subplots(5, 2, figsize=(16, 24))
plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

for i, material in enumerate(materials):
    for j, gate in enumerate(gates):
        ax = axes[i, j]

        # Calculate current
        Ids = calculate_cryogenic_current(Vgs, material, gate)

        # Plot with distinct styling
        color_idx = (i * 2 + j) % len(colors)
        linestyle = linestyles[j % len(linestyles)]
        marker = markers[i % len(markers)]

        ax.semilogy(Vgs, Ids,
                   color=colors[color_idx],
                   linestyle=linestyle,
                   marker=marker,
                   markevery=50,
                   markersize=4,
                   linewidth=2,
                   label=f'{gate}')

        # Enhanced axis formatting
        ax.set_title(f"{gate} - {material} (77K)", fontsize=12, pad=10, fontweight='bold')
        ax.set_xlabel("Gate Voltage (V)", fontsize=10)
        ax.set_ylabel("Drain Current (A)", fontsize=10)
        ax.set_xlim(-0.5, 1.2)
        ax.set_ylim(1e-18, 1e-2)
        ax.grid(True, which="both", ls="-", alpha=0.3)
        ax.legend(fontsize='small', loc='upper left')

        # Add parameter annotations
        params = material_params[material]
        gate_param = gate_params[gate]
        ax.text(0.02, 0.98, '.3f',
               transform=ax.transAxes, fontsize=8, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Overall title
plt.suptitle('Cryogenic IV Characteristics (77K): Pi-Gate vs Omega-Gate NWFETs\n' +
            'Enhanced Material Differentiation with Cryogenic-Specific Physics',
            fontsize=16, fontweight='bold', y=0.98)

# Save the plot
plt.savefig('cryogenic_iv_comparison.png', dpi=300, bbox_inches='tight')
plt.close()

print("Cryogenic IV comparison plot generated with distinct characteristics for each material and gate type at 77K.")
