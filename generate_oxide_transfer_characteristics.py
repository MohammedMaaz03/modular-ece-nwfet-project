import numpy as np
import matplotlib.pyplot as plt
import os

# Define parameters
temperatures = np.array([77, 200, 300, 400, 500])  # K
gate_voltages = np.linspace(-1, 1, 200)  # V

# Oxide materials with distinct properties
oxides = ['SiO₂', 'Al₂O₃', 'HfO₂', 'ZrO₂', 'La₂O₃']
dielectric_constants = [3.9, 9, 25, 25, 27]
band_gaps_oxide = [9.0, 6.7, 5.7, 7.8, 5.6]  # eV
thicknesses = [2e-9, 2e-9, 2e-9, 2e-9, 2e-9]  # 2nm for all

# Semiconductor material (assume Si nanowire for simplicity)
semiconductor = 'Si'
Eg_sem = 1.12  # eV
mu = 1400  # cm²/V·s

# Physics-based drain current calculation varying with oxide
def calculate_drain_current(Vg, T, oxide, gate_type):
    idx = oxides.index(oxide)
    k_ox = dielectric_constants[idx]
    Eg_ox = band_gaps_oxide[idx]
    tox = thicknesses[idx]

    # Oxide capacitance
    Cox = k_ox * 8.85e-14 / tox

    # Threshold voltage with oxide effects
    phi_ms = 0.5  # Metal-semiconductor work function
    Vt0 = phi_ms + (np.sqrt(4 * Eg_sem * 0.0259 * T * np.log(1e10)) / Cox) + (Eg_ox / 2)
    alpha = 1e-3
    Vt = Vt0 - alpha * (T - 300)

    # Gate efficiency
    if gate_type == 'Pi-Gate':
        eta = 0.82
        mobility_factor = 0.8
    else:  # Omega-Gate
        eta = 0.98
        mobility_factor = 1.2

    # Effective mobility
    mu_eff = mu * mobility_factor * (T / 300)**(-1.5)

    # Subthreshold slope affected by oxide capacitance
    SS = 60 * (1 + (k_ox * Eg_sem) / (Eg_ox * 0.0259 * T))
    n = SS / 60
    Id_sub = 1e-9 * np.exp((Vg - Vt) / (n * 0.0259))

    # Above threshold
    W_L = 10
    Vds = 0.5
    Id_sat = np.where(Vg > Vt, (mu_eff * Cox * W_L / 2) * (Vg - Vt)**2 * (1 + 0.1 * Vds), 0)

    # Transition
    transition = 1 / (1 + np.exp(-10 * (Vg - Vt)))
    Id = Id_sub * (1 - transition) + Id_sat * transition

    return np.maximum(Id, 1e-12)

# Create figure with 5 subplots (one per oxide)
fig, axes = plt.subplots(5, 1, figsize=(10, 20))
fig.suptitle('Oxide-Dependent Transfer Characteristics: Pi-Gate vs Omega-Gate NWFETs (Si Nanowire)', fontsize=16, fontweight='bold')

colors_pi = ['blue', 'orange', 'green', 'red', 'purple']
colors_omega = ['cyan', 'magenta', 'lime', 'pink', 'yellow']
linestyles = ['-', '--', '-.', ':', '-.']
markers = ['o', 's', '^', 'D', 'v']

for i, oxide in enumerate(oxides):
    ax = axes[i]
    ax.set_title(f'{oxide} Gate Oxide: Pi-Gate vs Omega-Gate', fontsize=14)
    ax.set_xlabel('Gate Voltage (V)')
    ax.set_ylabel('Drain Current (A)')
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')
    ax.set_xlim(-1, 1)
    ax.set_ylim(1e-12, 1e-2)

    for j, T in enumerate(temperatures):
        # Pi-Gate
        Id_pi = calculate_drain_current(gate_voltages, T, oxide, 'Pi-Gate')
        label_pi = f'Pi-Gate, {T}K' if j == 2 else "_nolegend_"
        ax.plot(gate_voltages, Id_pi, color=colors_pi[i], linestyle=linestyles[j], marker=markers[j], markersize=2, linewidth=1.5, label=label_pi, alpha=0.9)

        # Omega-Gate
        Id_omega = calculate_drain_current(gate_voltages, T, oxide, 'Omega-Gate')
        label_omega = f'Omega-Gate, {T}K' if j == 2 else "_nolegend_"
        ax.plot(gate_voltages, Id_omega, color=colors_omega[i], linestyle=linestyles[j], marker=markers[j], markersize=2, linewidth=1.5, label=label_omega, alpha=0.9)

    # Annotations
    ax.annotate('Pi-Gate\n(Higher Vt, Lower I)', xy=(-0.5, 1e-9), xytext=(-0.8, 1e-8), arrowprops=dict(arrowstyle='->', color=colors_pi[i]), fontsize=8)
    ax.annotate('Omega-Gate\n(Lower Vt, Higher I)', xy=(0.5, 1e-4), xytext=(0.2, 1e-3), arrowprops=dict(arrowstyle='->', color=colors_omega[i]), fontsize=8)

    ax.legend(loc='upper left', fontsize=8)

plt.tight_layout()
plt.savefig('docs/oxide_dependent_iv.png', dpi=300, bbox_inches='tight')
plt.show()
