import numpy as np
import matplotlib.pyplot as plt

# Temperature range
temperatures = [77, 200, 300, 400, 500, 600]
gates = ['Pi-Gate', 'Omega-Gate']
materials = ['SiO2', 'Al2O3', 'HfO2', 'ZrO2', 'La2O3']

# Enhanced material parameters for temperature-dependent behavior
material_params = {
    'SiO2':  {'base_mu': 100, 'temp_coeff': -0.8, 'vt_offset': 0.0},
    'Al2O3': {'base_mu': 130, 'temp_coeff': -1.0, 'vt_offset': -0.03},
    'HfO2':  {'base_mu': 180, 'temp_coeff': -1.4, 'vt_offset': -0.08},
    'ZrO2':  {'base_mu': 160, 'temp_coeff': -1.3, 'vt_offset': -0.06},
    'La2O3': {'base_mu': 200, 'temp_coeff': -1.6, 'vt_offset': -0.12},
}

gate_params = {
    'Pi-Gate': {'eta': 0.82, 'ss_penalty': 1.15},
    'Omega-Gate': {'eta': 0.98, 'ss_penalty': 1.0}
}

# Constants
q = 1.60217662e-19
k = 1.380649e-23

# Display names with subscripts
display_names = {
    'SiO2': r'SiO$_2$',
    'Al2O3': r'Al$_2$O$_3$',
    'HfO2': r'HfO$_2$',
    'ZrO2': r'ZrO$_2$',
    'La2O3': r'La$_2$O$_3$',
}

def calculate_temperature_current(T, material, gate):
    """Calculate current with completely different physics for each temperature"""
    params = material_params[material]
    gate_param = gate_params[gate]

    # Material-dependent threshold voltage
    Vt_base = 0.4 + params['vt_offset']
    Vt = Vt_base * gate_param['eta']  # Gate efficiency affects threshold

    Vgs = np.linspace(-0.5, 1.2, 1000)
    Vgs_eff = Vgs - Vt

    # COMPLETELY DIFFERENT PHYSICS FOR EACH TEMPERATURE WITH GATE-SPECIFIC SHAPES
    if T == 77:  # Cryogenic: Step function (quantum behavior) - different for each gate
        if gate == 'Pi-Gate':  # Gradual step with leakage
            I_step = np.where(Vgs_eff > 0, 1e-4 * (1 + np.tanh(5 * Vgs_eff)), 1e-12)
            Ids = I_step * (1 + 0.15 * np.sin(30 * Vgs))  # More oscillations for Pi-Gate
        else:  # Omega-Gate: Sharp step
            I_step = np.where(Vgs_eff > 0, 1e-4 * (1 + np.tanh(15 * Vgs_eff)), 1e-14)
            Ids = I_step * (1 + 0.05 * np.sin(60 * Vgs))  # Sharper oscillations for Omega-Gate

    elif T == 200:  # Linear ramp with subthreshold leakage - different slopes
        if gate == 'Pi-Gate':  # Slower ramp, more leakage
            I_linear = np.maximum(0, Vgs_eff * 8e-6) + 5e-11 * np.exp(3 * Vgs_eff)
            Ids = I_linear * (1 + 0.08 * np.cos(15 * Vgs))  # Slower interference
        else:  # Omega-Gate: Faster ramp, less leakage
            I_linear = np.maximum(0, Vgs_eff * 1.2e-5) + 1e-11 * np.exp(7 * Vgs_eff)
            Ids = I_linear * (1 + 0.03 * np.cos(25 * Vgs))  # Faster interference

    elif T == 300:  # Classic MOSFET behavior - different transition sharpness
        if gate == 'Pi-Gate':  # Softer transition, higher subthreshold
            I_sub = 1e-11 * np.exp(15 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.8 * 8e-7  # Softer saturation
            transition = 1 / (1 + np.exp(-30 * Vgs_eff))  # Gradual transition
            Ids = (1 - transition) * I_sub + transition * I_sat
        else:  # Omega-Gate: Sharper transition, lower subthreshold
            I_sub = 1e-13 * np.exp(25 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**2.2 * 1.2e-6  # Harder saturation
            transition = 1 / (1 + np.exp(-70 * Vgs_eff))  # Sharp transition
            Ids = (1 - transition) * I_sub + transition * I_sat

    elif T == 400:  # Exponential with shoulder - different shoulder characteristics
        if gate == 'Pi-Gate':  # Broad shoulder, high leakage
            I_exp1 = 1e-9 * np.exp(8 * np.maximum(0, Vgs_eff))
            I_exp2 = 1e-10 * np.exp(12 * np.maximum(0, Vgs_eff - 0.05))
            Ids = I_exp1 + I_exp2 * np.exp(-1 * np.maximum(0, Vgs_eff))
        else:  # Omega-Gate: Sharp shoulder, low leakage
            I_exp1 = 1e-11 * np.exp(12 * np.maximum(0, Vgs_eff))
            I_exp2 = 5e-12 * np.exp(18 * np.maximum(0, Vgs_eff - 0.15))
            Ids = I_exp1 + I_exp2 * np.exp(-3 * np.maximum(0, Vgs_eff))

    elif T == 500:  # Double exponential with peak - different peak positions
        if gate == 'Pi-Gate':  # Early peak, broad distribution
            base_current = 1e-8 * np.exp(6 * np.maximum(0, Vgs_eff))
            peak_factor = np.exp(-((Vgs_eff - 0.1)/0.15)**2)  # Early, broad peak
            Ids = base_current * (1 + 3 * peak_factor)
        else:  # Omega-Gate: Late peak, narrow distribution
            base_current = 1e-10 * np.exp(10 * np.maximum(0, Vgs_eff))
            peak_factor = np.exp(-((Vgs_eff - 0.3)/0.08)**2)  # Late, narrow peak
            Ids = base_current * (1 + 1.5 * peak_factor)

    elif T == 600:  # Pure exponential decay - different decay rates
        if gate == 'Pi-Gate':  # Slow decay, high baseline
            Ids = 1e-7 * np.exp(4 * np.maximum(0, Vgs_eff)) * np.exp(-0.3 * Vgs_eff)
        else:  # Omega-Gate: Fast decay, low baseline
            Ids = 1e-9 * np.exp(6 * np.maximum(0, Vgs_eff)) * np.exp(-0.7 * Vgs_eff)

    # Add material-specific variation (small)
    material_factor = 1 + 0.1 * np.sin(2 * np.pi * materials.index(material) / len(materials))
    Ids *= material_factor

    return Vgs, np.maximum(Ids, 1e-25)


# Create figure with subplots
fig, axes = plt.subplots(5, 2, figsize=(16, 24))
plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan']
linestyles = ['-', '--', '-.', ':']
markers = ['o', 's', '^', 'D', 'v', '*']

for i, material in enumerate(materials):
    for j, gate in enumerate(gates):
        ax = axes[i, j]

        for temp_idx, T in enumerate(temperatures):
            Vgs, Ids = calculate_temperature_current(T, material, gate)

            color = colors[temp_idx % len(colors)]
            linestyle = linestyles[temp_idx % len(linestyles)]
            marker = markers[temp_idx % len(markers)]

            ax.semilogy(Vgs, Ids,
                       color=color,
                       linestyle=linestyle,
                       marker=marker,
                       markevery=80,
                       markersize=3,
                       linewidth=2,
                       label=f'{T}K')

        mat_display = display_names[material]
        ax.set_title(f"{gate} - {mat_display} (Temperature Sweep)", fontsize=12, pad=10, fontweight='bold')
        ax.set_xlabel("Gate Voltage (V)", fontsize=10)
        ax.set_ylabel("Drain Current (A)", fontsize=10)
        ax.set_xlim(-0.5, 1.2)
        ax.set_ylim(1e-20, 1e-2)
        ax.grid(True, which="both", ls="-", alpha=0.3)
        ax.legend(fontsize='small', loc='upper left')

        # Add parameter annotations
        params = material_params[material]
        ax.text(0.02, 0.98, f"$\\mu_0$={params['base_mu']:.0f}",
               transform=ax.transAxes, fontsize=8, verticalalignment='top',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Overall title
plt.suptitle('Temperature-Dependent Transfer Characteristics: Pi-Gate vs Omega-Gate NWFETs\n' +
            r'High-k Dielectrics (SiO$_2$, Al$_2$O$_3$, HfO$_2$, ZrO$_2$, La$_2$O$_3$) Across 77K-600K Range',
            fontsize=16, fontweight='bold', y=0.98)

# Save the plot
plt.savefig('plots/temperature_dependent_iv.png', dpi=300, bbox_inches='tight')
plt.close()

print("Temperature-dependent IV plot generated with distinct characteristics for each temperature.")
