import numpy as np
import matplotlib.pyplot as plt

# Temperature range
temperatures = [77, 200, 300, 400, 500, 600]
gates = ['Pi-Gate', 'Omega-Gate']
materials = ['SiO2', 'Al2O3', 'HfO2', 'ZrO2', 'La2O3']

# Physical constants
q = 1.60217662e-19
k_B = 1.380649e-23
eps0 = 8.854e-12
t_ox = 1e-9  # oxide thickness (m)

# Material parameters: dielectric constant, band offset (eV), phonon coupling
material_params = {
    'SiO2':  {'k': 3.9,  'band_offset': 3.5,  'phonon': 0.063, 'trap_density': 1e10},
    'Al2O3': {'k': 9.0,  'band_offset': 2.8,  'phonon': 0.048, 'trap_density': 5e10},
    'HfO2':  {'k': 25.0, 'band_offset': 1.5,  'phonon': 0.035, 'trap_density': 1e11},
    'ZrO2':  {'k': 22.0, 'band_offset': 1.4,  'phonon': 0.038, 'trap_density': 8e10},
    'La2O3': {'k': 27.0, 'band_offset': 2.3,  'phonon': 0.030, 'trap_density': 2e11},
}

gate_params = {
    'Pi-Gate':    {'eta': 0.82, 'ss_factor': 1.15, 'R_s': 150},
    'Omega-Gate': {'eta': 0.98, 'ss_factor': 1.0,  'R_s': 50},
}

# Device parameters
W = 10e-9   # channel width
L = 10e-9   # channel length
mu_ref = 0.05  # reference mobility m^2/V·s


def calculate_temperature_current(T, material, gate):
    """Calculate temperature-dependent IV for a given oxide material and gate type."""
    mp = material_params[material]
    gp = gate_params[gate]

    kappa = mp['k']
    eta = gp['eta']
    ss_factor = gp['ss_factor']

    # Gate oxide capacitance
    C_ox = eps0 * kappa / t_ox

    # Thermal voltage
    V_T = k_B * T / q

    # Temperature-dependent threshold voltage
    Vth_ref = 0.35
    alpha_Vth = 0.0005  # V/K
    Vth = Vth_ref - alpha_Vth * (T - 300)

    # Higher-k materials shift Vth due to fixed charges
    Vth += q * mp['trap_density'] / C_ox

    # Gate efficiency correction
    Vth_eff = Vth / eta

    # Temperature-dependent mobility (phonon scattering)
    mu = mu_ref * (300 / T) ** 1.5
    # High-k materials have remote phonon scattering degradation
    mu *= np.exp(-mp['phonon'] * T / 300)

    # Subthreshold swing
    SS = ss_factor * 2.3 * V_T  # V/decade (ideal ~60mV at 300K)

    Vgs = np.linspace(-0.5, 1.2, 1000)
    Ids = np.zeros_like(Vgs)
    beta = mu * C_ox * eta * (W / L)

    for i, vgs in enumerate(Vgs):
        V_ov = vgs - Vth_eff

        if vgs < Vth_eff:
            # Subthreshold regime
            Ids[i] = 1e-12 * np.exp((vgs - Vth_eff) / (SS / 2.3))
            # Gate leakage through oxide (Fowler-Nordheim tunneling)
            E_ox = abs(vgs) / t_ox if abs(vgs) > 0.01 else 0
            barrier = mp['band_offset'] * q
            if E_ox > 1e6:
                tunnel = 1e-15 * (E_ox ** 2) * np.exp(
                    -4 * np.sqrt(2 * 9.109e-31 * barrier) * barrier / (3 * q * 1.054e-34 * E_ox)
                )
                Ids[i] = max(Ids[i], tunnel)
        else:
            V_DS = 0.5  # moderate drain bias
            if V_DS < V_ov:
                # Linear region
                Ids[i] = beta * (V_ov * V_DS - 0.5 * V_DS ** 2)
            else:
                # Saturation region
                Ids[i] = 0.5 * beta * V_ov ** 2 * (1 + 0.05 * V_DS)

        # Temperature-dependent leakage floor (thermal generation)
        I_leak = 1e-14 * np.exp(-0.5 * q / (k_B * T))
        Ids[i] = max(Ids[i], I_leak)

    return Vgs, np.array(Ids)


# Create figure with subplots: 5 materials x 2 gate types
fig, axes = plt.subplots(5, 2, figsize=(16, 28))
plt.subplots_adjust(hspace=0.45, wspace=0.3, top=0.94, bottom=0.04)

colors = ['#1f77b4', '#d62728', '#2ca02c', '#ff7f0e', '#9467bd', '#8c564b']
linestyles = ['-', '--', '-.', ':', '-', '--']
markers = ['o', 's', '^', 'D', 'v', '*']

# Material display names with subscripts
display_names = {
    'SiO2': r'SiO$_2$',
    'Al2O3': r'Al$_2$O$_3$',
    'HfO2': r'HfO$_2$',
    'ZrO2': r'ZrO$_2$',
    'La2O3': r'La$_2$O$_3$',
}

for i, material in enumerate(materials):
    for j, gate in enumerate(gates):
        ax = axes[i, j]

        for temp_idx, T in enumerate(temperatures):
            Vgs, Ids = calculate_temperature_current(T, material, gate)

            ax.semilogy(Vgs, Ids,
                        color=colors[temp_idx],
                        linestyle=linestyles[temp_idx % len(linestyles)],
                        marker=markers[temp_idx % len(markers)],
                        markevery=80,
                        markersize=3,
                        linewidth=2,
                        label=f'{T} K')

        mat_display = display_names[material]
        ax.set_title(f"{gate} — {mat_display}  (Temperature Sweep)",
                     fontsize=12, pad=10, fontweight='bold')
        ax.set_xlabel("Gate Voltage $V_{GS}$ (V)", fontsize=10)
        ax.set_ylabel("Drain Current $I_{DS}$ (A)", fontsize=10)
        ax.set_xlim(-0.5, 1.2)
        ax.set_ylim(1e-20, 1e-2)
        ax.grid(True, which="both", ls="-", alpha=0.3)
        ax.legend(fontsize='small', loc='upper left', framealpha=0.9)

        # Annotate material properties
        mp = material_params[material]
        info = f"$\\kappa$ = {mp['k']:.1f}\n$\\phi_B$ = {mp['band_offset']:.1f} eV"
        ax.text(0.97, 0.05, info,
                transform=ax.transAxes, fontsize=8,
                verticalalignment='bottom', horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9))

fig.suptitle(
    'Temperature-Dependent I-V Characteristics: High-k Gate Dielectrics\n'
    'Pi-Gate vs Omega-Gate NWFETs — '
    r'SiO$_2$, Al$_2$O$_3$, HfO$_2$, ZrO$_2$, La$_2$O$_3$ '
    '(77 K – 600 K)',
    fontsize=15, fontweight='bold', y=0.98)

plt.savefig('plots/temperature_dependent_iv.png', dpi=300, bbox_inches='tight')
plt.close()

print("Temperature-dependent IV plot generated for high-k dielectric materials.")
