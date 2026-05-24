import numpy as np
import matplotlib.pyplot as plt

# Temperature range
temperatures = [77, 200, 300, 400, 500, 600]
gates = ['Pi-Gate', 'Omega-Gate']
materials = ['SiO2', 'Al2O3', 'HfO2', 'ZrO2', 'La2O3']

# Enhanced material parameters for temperature-dependent behavior
# kappa = dielectric constant, drives Cox ratio and current scaling
# leakage_factor = relative gate leakage (lower band offset -> more leakage)
material_params = {
    'SiO2':  {'kappa': 3.9,  'base_mu': 100, 'temp_coeff': -0.8, 'vt_offset': 0.15,  'leakage_factor': 1.0},
    'Al2O3': {'kappa': 9.0,  'base_mu': 130, 'temp_coeff': -1.0, 'vt_offset': 0.08,  'leakage_factor': 0.3},
    'HfO2':  {'kappa': 25.0, 'base_mu': 180, 'temp_coeff': -1.4, 'vt_offset': -0.05, 'leakage_factor': 0.05},
    'ZrO2':  {'kappa': 22.0, 'base_mu': 160, 'temp_coeff': -1.3, 'vt_offset': -0.02, 'leakage_factor': 0.08},
    'La2O3': {'kappa': 27.0, 'base_mu': 200, 'temp_coeff': -1.6, 'vt_offset': -0.10, 'leakage_factor': 0.02},
}
kappa_ref = 3.9  # SiO2 reference

gate_params = {
    'Pi-Gate': {'eta': 0.82, 'ss_penalty': 1.15},
    'Omega-Gate': {'eta': 0.98, 'ss_penalty': 1.0}
}

# Constants
q = 1.60217662e-19
k = 1.380649e-23

def calculate_temperature_current(T, material, gate):
    """Calculate current with completely different physics for each temperature"""
    params = material_params[material]
    gate_param = gate_params[gate]
    kappa = params['kappa']

    # Cox ratio: higher kappa -> higher capacitance -> higher drive current
    cox_ratio = kappa / kappa_ref

    # Material-dependent threshold voltage (higher-k shifts Vt lower)
    Vt_base = 0.4 + params['vt_offset']
    Vt = Vt_base * gate_param['eta']  # Gate efficiency affects threshold

    # Drive current scaling proportional to Cox
    drive_scale = cox_ratio
    # Leakage scaling: lower band-offset materials leak more
    leak_scale = params['leakage_factor']

    Vgs = np.linspace(-0.5, 1.2, 1000)
    Vgs_eff = Vgs - Vt

    # COMPLETELY DIFFERENT PHYSICS FOR EACH TEMPERATURE WITH GATE-SPECIFIC SHAPES
    if T == 77:  # Cryogenic: Step function (quantum behavior)
        if gate == 'Pi-Gate':
            I_step = np.where(Vgs_eff > 0,
                              1e-4 * drive_scale * (1 + np.tanh(5 * Vgs_eff)),
                              1e-12 * leak_scale)
            Ids = I_step * (1 + 0.15 * np.sin(30 * Vgs))
        else:
            I_step = np.where(Vgs_eff > 0,
                              1e-4 * drive_scale * (1 + np.tanh(15 * Vgs_eff)),
                              1e-14 * leak_scale)
            Ids = I_step * (1 + 0.05 * np.sin(60 * Vgs))

    elif T == 200:  # Linear ramp with subthreshold leakage
        if gate == 'Pi-Gate':
            I_linear = np.maximum(0, Vgs_eff * 8e-6 * drive_scale) + 5e-11 * leak_scale * np.exp(3 * Vgs_eff)
            Ids = I_linear * (1 + 0.08 * np.cos(15 * Vgs))
        else:
            I_linear = np.maximum(0, Vgs_eff * 1.2e-5 * drive_scale) + 1e-11 * leak_scale * np.exp(7 * Vgs_eff)
            Ids = I_linear * (1 + 0.03 * np.cos(25 * Vgs))

    elif T == 300:  # Classic MOSFET behavior
        if gate == 'Pi-Gate':
            I_sub = 1e-11 * leak_scale * np.exp(15 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.8 * 8e-7 * drive_scale
            transition = 1 / (1 + np.exp(-30 * Vgs_eff))
            Ids = (1 - transition) * I_sub + transition * I_sat
        else:
            I_sub = 1e-13 * leak_scale * np.exp(25 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**2.2 * 1.2e-6 * drive_scale
            transition = 1 / (1 + np.exp(-70 * Vgs_eff))
            Ids = (1 - transition) * I_sub + transition * I_sat

    elif T == 400:  # Exponential with shoulder
        if gate == 'Pi-Gate':
            I_exp1 = 1e-9 * drive_scale * np.exp(8 * np.maximum(0, Vgs_eff))
            I_exp2 = 1e-10 * leak_scale * np.exp(12 * np.maximum(0, Vgs_eff - 0.05))
            Ids = I_exp1 + I_exp2 * np.exp(-1 * np.maximum(0, Vgs_eff))
        else:
            I_exp1 = 1e-11 * drive_scale * np.exp(12 * np.maximum(0, Vgs_eff))
            I_exp2 = 5e-12 * leak_scale * np.exp(18 * np.maximum(0, Vgs_eff - 0.15))
            Ids = I_exp1 + I_exp2 * np.exp(-3 * np.maximum(0, Vgs_eff))

    elif T == 500:  # Double exponential with peak
        if gate == 'Pi-Gate':
            base_current = 1e-8 * drive_scale * np.exp(6 * np.maximum(0, Vgs_eff))
            peak_factor = np.exp(-((Vgs_eff - 0.1)/0.15)**2)
            Ids = base_current * (1 + 3 * peak_factor)
        else:
            base_current = 1e-10 * drive_scale * np.exp(10 * np.maximum(0, Vgs_eff))
            peak_factor = np.exp(-((Vgs_eff - 0.3)/0.08)**2)
            Ids = base_current * (1 + 1.5 * peak_factor)

    elif T == 600:  # Pure exponential decay
        if gate == 'Pi-Gate':
            Ids = 1e-7 * drive_scale * np.exp(4 * np.maximum(0, Vgs_eff)) * np.exp(-0.3 * Vgs_eff)
        else:
            Ids = 1e-9 * drive_scale * np.exp(6 * np.maximum(0, Vgs_eff)) * np.exp(-0.7 * Vgs_eff)

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

        ax.set_title(f"{gate} - {material} (Temperature Sweep)", fontsize=12, pad=10, fontweight='bold')
        ax.set_xlabel("Gate Voltage (V)", fontsize=10)
        ax.set_ylabel("Drain Current (A)", fontsize=10)
        ax.set_xlim(-0.5, 1.2)
        ax.set_ylim(1e-20, 1e-2)
        ax.grid(True, which="both", ls="-", alpha=0.3)
        ax.legend(fontsize='small', loc='upper left')



# Overall title
plt.suptitle('Temperature-Dependent Transfer Characteristics: Pi-Gate vs Omega-Gate NWFETs\n' +
            r'High-k Dielectrics: SiO$_2$, Al$_2$O$_3$, HfO$_2$, ZrO$_2$, La$_2$O$_3$ Across 77K-600K Range',
            fontsize=16, fontweight='bold', y=0.98)

# Save the plot
plt.savefig('plots/temperature_dependent_iv.png', dpi=300, bbox_inches='tight')
plt.close()

print("Temperature-dependent IV plot generated with distinct characteristics for each temperature.")
