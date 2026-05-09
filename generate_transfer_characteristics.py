import numpy as np
import matplotlib.pyplot as plt

# Define parameters
temperatures = np.array([77, 200, 300, 400, 500])  # K
gate_voltages = np.linspace(-1, 1, 200)  # V

# Materials with distinct properties
materials = ['Si', 'Ge', 'GaAs', 'InAs', 'GaN']
band_gaps = [1.12, 0.66, 1.42, 0.36, 3.4]  # eV
electron_mobility = [1400, 3900, 8500, 20000, 1500]  # cm²/V·s
dielectric_constant = [11.7, 16.2, 12.9, 15.1, 9.0]

# Physics-based drain current calculation
def calculate_drain_current(Vg, T, material, gate_type):
    idx = materials.index(material)
    Eg = band_gaps[idx]
    mu = electron_mobility[idx]
    eps = dielectric_constant[idx]

    # Threshold voltage with temperature dependence
    Vt0 = 0.5  # Base Vt
    alpha = 1e-3  # Temperature coefficient
    Vt = Vt0 - alpha * (T - 300)

    # Gate efficiency
    if gate_type == 'Pi-Gate':
        eta = 0.82
        mobility_factor = 0.8  # Lower mobility due to partial gate
    else:  # Omega-Gate
        eta = 0.98
        mobility_factor = 1.2  # Higher mobility due to full gate

    # Effective mobility with temperature
    mu_eff = mu * mobility_factor * (T / 300)**(-1.5)  # Temperature dependence

    # Subthreshold slope (SS) in mV/dec
    SS = 60 * (1 + (eps * 3.9) / (Eg * 0.0259 * T))  # Physics-based SS

    # Drain current in subthreshold
    n = SS / 60  # Body factor
    Id_sub = 1e-9 * np.exp((Vg - Vt) / (n * 0.0259))  # Subthreshold current

    # Above threshold (linear + saturation)
    Cox = eps * 8.85e-14 / 2e-9  # Oxide capacitance (assume 2nm oxide)
    W_L = 10  # Width/Length ratio
    Vds = 0.5  # Drain voltage
    Id_sat = (mu_eff * Cox * W_L / 2) * (Vg - Vt)**2 * (1 + lambda_term(Vg, Vds)) if Vg > Vt else 0

    # Transition region
    transition = 1 / (1 + np.exp(-10 * (Vg - Vt)))
    Id = Id_sub * (1 - transition) + Id_sat * transition

    # Material-specific scaling
    material_scale = 1 + (Eg - 1.12) * 0.2  # Band gap effect
    Id *= material_scale

    return np.maximum(Id, 1e-12)  # Minimum current

def lambda_term(Vg, Vds):
    # Channel length modulation
    lambda_mod = 0.1
    return lambda_mod * Vds

# Create figure with 5 subplots (one per material)
fig, axes = plt.subplots(5, 1, figsize=(10, 20))
fig.suptitle('Temperature-Dependent Transfer Characteristics: Pi-Gate vs Omega-Gate NWFETs', fontsize=16, fontweight='bold')

colors_pi = ['blue', 'orange', 'green', 'red', 'purple']
colors_omega = ['cyan', 'magenta', 'lime', 'pink', 'yellow']
linestyles = ['-', '--', '-.', ':', '-.']
markers = ['o', 's', '^', 'D', 'v']

for i, material in enumerate(materials):
    ax = axes[i]
    ax.set_title(f'{material} Nanowire: Pi-Gate vs Omega-Gate', fontsize=14)
    ax.set_xlabel('Gate Voltage (V)')
    ax.set_ylabel('Drain Current (A)')
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    ax.set_xlim(-1, 1)
    ax.set_ylim(1e-12, 1e-2)

    for j, T in enumerate(temperatures):
        # Pi-Gate
        Id_pi = calculate_drain_current(gate_voltages, T, material, 'Pi-Gate')
        label_pi = f'Pi-Gate, {T}K' if j == 2 else "_nolegend_"
        ax.plot(gate_voltages, Id_pi, color=colors_pi[i], linestyle=linestyles[j], marker=markers[j], markersize=2, linewidth=1.5, label=label_pi, alpha=0.9)

        # Omega-Gate
        Id_omega = calculate_drain_current(gate_voltages, T, material, 'Omega-Gate')
        label_omega = f'Omega-Gate, {T}K' if j == 2 else "_nolegend_"
        ax.plot(gate_voltages, Id_omega, color=colors_omega[i], linestyle=linestyles[j], marker=markers[j], markersize=2, linewidth=1.5, label=label_omega, alpha=0.9)

    # Annotations for differences
    ax.annotate('Pi-Gate\n(Lower I, Steeper SS)', xy=(-0.5, 1e-8), xytext=(-0.8, 1e-7), arrowprops=dict(arrowstyle='->', color=colors_pi[i]), fontsize=8)
    ax.annotate('Omega-Gate\n(Higher I, Better Control)', xy=(0.5, 1e-4), xytext=(0.2, 1e-3), arrowprops=dict(arrowstyle='->', color=colors_omega[i]), fontsize=8)

    ax.legend(loc='upper left', fontsize=8)

plt.tight_layout()
plt.savefig('plots/temperature_dependent_iv.png', dpi=300, bbox_inches='tight')
plt.show()
