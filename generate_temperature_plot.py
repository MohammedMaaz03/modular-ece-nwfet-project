import numpy as np
import matplotlib.pyplot as plt

# Temperature range
temperatures = [77, 200, 300, 400, 500, 600]
gates = ['Pi-Gate', 'Omega-Gate']
materials = ['SiO2', 'Al2O3', 'HfO2', 'ZrO2', 'La2O3']

# Constants
q = 1.60217662e-19
k = 1.380649e-23

gate_params = {
    'Pi-Gate': {'eta': 0.82, 'ss_penalty': 1.15},
    'Omega-Gate': {'eta': 0.98, 'ss_penalty': 1.0}
}

# Display names with subscripts
display_names = {
    'SiO2': r'SiO$_2$',
    'Al2O3': r'Al$_2$O$_3$',
    'HfO2': r'HfO$_2$',
    'ZrO2': r'ZrO$_2$',
    'La2O3': r'La$_2$O$_3$',
}


def calculate_SiO2(T, gate):
    """SiO2 (k=3.9): Low-k classic — sharp turn-on, low current, excellent off-state."""
    gp = gate_params[gate]
    eta = gp['eta']
    Vgs = np.linspace(-0.5, 1.2, 1000)

    Vt = 0.55 * eta
    Vgs_eff = Vgs - Vt

    if T == 77:
        if gate == 'Pi-Gate':
            Ids = np.where(Vgs_eff > 0,
                           5e-6 * (1 + np.tanh(4 * Vgs_eff)),
                           1e-18)
        else:
            Ids = np.where(Vgs_eff > 0,
                           8e-6 * (1 + np.tanh(12 * Vgs_eff)),
                           1e-20)
    elif T == 200:
        if gate == 'Pi-Gate':
            Ids = np.maximum(0, Vgs_eff * 3e-6) + 1e-16 * np.exp(8 * Vgs_eff)
        else:
            Ids = np.maximum(0, Vgs_eff * 5e-6) + 1e-18 * np.exp(12 * Vgs_eff)
    elif T == 300:
        if gate == 'Pi-Gate':
            I_sub = 1e-14 * np.exp(20 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**2.0 * 2e-7
            tr = 1 / (1 + np.exp(-40 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
        else:
            I_sub = 1e-16 * np.exp(30 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**2.2 * 3e-7
            tr = 1 / (1 + np.exp(-80 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
    elif T == 400:
        if gate == 'Pi-Gate':
            Ids = 1e-12 * np.exp(10 * np.maximum(0, Vgs_eff)) + 5e-15
        else:
            Ids = 1e-14 * np.exp(14 * np.maximum(0, Vgs_eff)) + 1e-17
    elif T == 500:
        if gate == 'Pi-Gate':
            Ids = 1e-10 * np.exp(7 * np.maximum(0, Vgs_eff)) + 1e-12
        else:
            Ids = 1e-12 * np.exp(10 * np.maximum(0, Vgs_eff)) + 1e-15
    elif T == 600:
        if gate == 'Pi-Gate':
            Ids = 1e-8 * np.exp(3 * np.maximum(0, Vgs_eff)) * np.exp(-0.2 * Vgs_eff) + 1e-10
        else:
            Ids = 1e-10 * np.exp(5 * np.maximum(0, Vgs_eff)) * np.exp(-0.5 * Vgs_eff) + 1e-13
    return Vgs, np.maximum(Ids, 1e-25)


def calculate_Al2O3(T, gate):
    """Al2O3 (k=9.0): Medium-k — moderate current, interface traps cause kinks."""
    gp = gate_params[gate]
    eta = gp['eta']
    Vgs = np.linspace(-0.5, 1.2, 1000)

    Vt = 0.42 * eta
    Vgs_eff = Vgs - Vt

    if T == 77:
        if gate == 'Pi-Gate':
            I_step = np.where(Vgs_eff > 0, 2e-4 * np.tanh(6 * Vgs_eff), 1e-15)
            trap_bump = 3e-7 * np.exp(-((Vgs - 0.6)/0.08)**2)
            Ids = I_step + trap_bump
        else:
            I_step = np.where(Vgs_eff > 0, 3e-4 * np.tanh(18 * Vgs_eff), 1e-17)
            trap_bump = 1e-7 * np.exp(-((Vgs - 0.55)/0.05)**2)
            Ids = I_step + trap_bump
    elif T == 200:
        if gate == 'Pi-Gate':
            I_lin = np.maximum(0, Vgs_eff * 2e-5) + 1e-13 * np.exp(5 * Vgs_eff)
            Ids = I_lin * (1 + 0.2 * np.exp(-((Vgs - 0.5)/0.1)**2))
        else:
            I_lin = np.maximum(0, Vgs_eff * 4e-5) + 1e-15 * np.exp(9 * Vgs_eff)
            Ids = I_lin * (1 + 0.1 * np.exp(-((Vgs - 0.45)/0.07)**2))
    elif T == 300:
        if gate == 'Pi-Gate':
            I_sub = 1e-12 * np.exp(18 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.6 * 5e-6
            tr = 1 / (1 + np.exp(-25 * Vgs_eff))
            trap_kink = 2e-8 * np.exp(-((Vgs_eff - 0.15)/0.06)**2)
            Ids = (1 - tr) * I_sub + tr * I_sat + trap_kink
        else:
            I_sub = 1e-14 * np.exp(28 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**2.0 * 8e-6
            tr = 1 / (1 + np.exp(-60 * Vgs_eff))
            trap_kink = 5e-9 * np.exp(-((Vgs_eff - 0.12)/0.04)**2)
            Ids = (1 - tr) * I_sub + tr * I_sat + trap_kink
    elif T == 400:
        if gate == 'Pi-Gate':
            Ids = 5e-10 * np.exp(9 * np.maximum(0, Vgs_eff)) + 2e-8 * np.exp(-((Vgs_eff - 0.2)/0.12)**2)
        else:
            Ids = 5e-12 * np.exp(13 * np.maximum(0, Vgs_eff)) + 3e-9 * np.exp(-((Vgs_eff - 0.25)/0.08)**2)
    elif T == 500:
        if gate == 'Pi-Gate':
            base = 1e-7 * np.exp(5 * np.maximum(0, Vgs_eff))
            Ids = base * (1 + 4 * np.exp(-((Vgs_eff - 0.1)/0.18)**2))
        else:
            base = 1e-9 * np.exp(8 * np.maximum(0, Vgs_eff))
            Ids = base * (1 + 2 * np.exp(-((Vgs_eff - 0.2)/0.1)**2))
    elif T == 600:
        if gate == 'Pi-Gate':
            Ids = 5e-7 * np.exp(3 * np.maximum(0, Vgs_eff)) * (1 + 0.5 * np.sin(8 * Vgs))
        else:
            Ids = 5e-9 * np.exp(5 * np.maximum(0, Vgs_eff)) * (1 + 0.2 * np.sin(12 * Vgs))
    return Vgs, np.maximum(Ids, 1e-25)


def calculate_HfO2(T, gate):
    """HfO2 (k=25): High-k — very high drive, charge trapping humps, gate leakage at negative Vgs."""
    gp = gate_params[gate]
    eta = gp['eta']
    Vgs = np.linspace(-0.5, 1.2, 1000)

    Vt = 0.30 * eta
    Vgs_eff = Vgs - Vt

    if T == 77:
        if gate == 'Pi-Gate':
            Ids = np.where(Vgs_eff > 0,
                           1e-3 * (1 + np.tanh(3 * Vgs_eff)),
                           1e-10 * np.exp(2 * Vgs))
            Ids += 5e-5 * np.exp(-((Vgs - 0.4)/0.06)**2)
        else:
            Ids = np.where(Vgs_eff > 0,
                           1.5e-3 * (1 + np.tanh(10 * Vgs_eff)),
                           1e-13 * np.exp(4 * Vgs))
    elif T == 200:
        if gate == 'Pi-Gate':
            Ids = np.maximum(0, Vgs_eff * 8e-5) + 1e-9 * np.exp(4 * Vgs_eff)
            Ids += 2e-6 * np.exp(-((Vgs_eff - 0.05)/0.1)**2)
        else:
            Ids = np.maximum(0, Vgs_eff * 1.5e-4) + 1e-12 * np.exp(8 * Vgs_eff)
    elif T == 300:
        if gate == 'Pi-Gate':
            I_sub = 1e-9 * np.exp(12 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.5 * 5e-5
            tr = 1 / (1 + np.exp(-20 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
        else:
            I_sub = 1e-12 * np.exp(22 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.8 * 8e-5
            tr = 1 / (1 + np.exp(-50 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
    elif T == 400:
        if gate == 'Pi-Gate':
            I1 = 1e-7 * np.exp(6 * np.maximum(0, Vgs_eff))
            I2 = 5e-8 * np.exp(10 * np.maximum(0, Vgs_eff - 0.1))
            Ids = I1 + I2 * np.exp(-0.5 * np.maximum(0, Vgs_eff))
        else:
            I1 = 1e-10 * np.exp(10 * np.maximum(0, Vgs_eff))
            I2 = 1e-9 * np.exp(15 * np.maximum(0, Vgs_eff - 0.15))
            Ids = I1 + I2 * np.exp(-2 * np.maximum(0, Vgs_eff))
    elif T == 500:
        if gate == 'Pi-Gate':
            base = 5e-6 * np.exp(4 * np.maximum(0, Vgs_eff))
            hump = np.exp(-((Vgs_eff - 0.05)/0.2)**2)
            Ids = base * (1 + 5 * hump)
        else:
            base = 5e-8 * np.exp(7 * np.maximum(0, Vgs_eff))
            hump = np.exp(-((Vgs_eff - 0.15)/0.1)**2)
            Ids = base * (1 + 2 * hump)
    elif T == 600:
        if gate == 'Pi-Gate':
            Ids = 1e-5 * np.exp(2 * np.maximum(0, Vgs_eff)) * np.exp(-0.1 * Vgs_eff)
        else:
            Ids = 1e-7 * np.exp(4 * np.maximum(0, Vgs_eff)) * np.exp(-0.3 * Vgs_eff)
    return Vgs, np.maximum(Ids, 1e-25)


def calculate_ZrO2(T, gate):
    """ZrO2 (k=22): High-k — high current, crystallization noise at high T, dual-slope subthreshold."""
    gp = gate_params[gate]
    eta = gp['eta']
    Vgs = np.linspace(-0.5, 1.2, 1000)

    Vt = 0.35 * eta
    Vgs_eff = Vgs - Vt

    if T == 77:
        if gate == 'Pi-Gate':
            Ids = np.where(Vgs_eff > 0,
                           8e-4 * (1 + np.tanh(5 * Vgs_eff)),
                           1e-13)
            Ids *= (1 + 0.25 * np.sin(40 * Vgs))
        else:
            Ids = np.where(Vgs_eff > 0,
                           1.2e-3 * (1 + np.tanh(14 * Vgs_eff)),
                           1e-16)
            Ids *= (1 + 0.08 * np.sin(70 * Vgs))
    elif T == 200:
        if gate == 'Pi-Gate':
            I1 = np.maximum(0, Vgs_eff * 5e-5)
            I2 = 1e-11 * np.exp(6 * Vgs_eff)
            Ids = I1 + I2 + 1e-8 * np.exp(-((Vgs - 0.4)/0.15)**2)
        else:
            I1 = np.maximum(0, Vgs_eff * 1e-4)
            I2 = 1e-14 * np.exp(10 * Vgs_eff)
            Ids = I1 + I2
    elif T == 300:
        if gate == 'Pi-Gate':
            I_sub1 = 1e-11 * np.exp(10 * np.maximum(0, Vgs_eff))
            I_sub2 = 1e-8 * np.exp(5 * np.maximum(0, Vgs_eff - 0.15))
            I_sat = np.maximum(0, Vgs_eff)**1.7 * 3e-5
            tr = 1 / (1 + np.exp(-35 * Vgs_eff))
            Ids = (1 - tr) * (I_sub1 + I_sub2) + tr * I_sat
        else:
            I_sub = 1e-14 * np.exp(20 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**2.0 * 5e-5
            tr = 1 / (1 + np.exp(-65 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
    elif T == 400:
        if gate == 'Pi-Gate':
            Ids = 5e-8 * np.exp(7 * np.maximum(0, Vgs_eff))
            Ids *= (1 + 0.3 * np.sin(20 * Vgs))
        else:
            Ids = 5e-11 * np.exp(11 * np.maximum(0, Vgs_eff))
            Ids *= (1 + 0.1 * np.sin(30 * Vgs))
    elif T == 500:
        if gate == 'Pi-Gate':
            base = 1e-6 * np.exp(5 * np.maximum(0, Vgs_eff))
            noise = 1 + 0.4 * np.sin(15 * Vgs) * np.exp(-((Vgs - 0.6)/0.3)**2)
            Ids = base * noise
        else:
            base = 1e-8 * np.exp(8 * np.maximum(0, Vgs_eff))
            noise = 1 + 0.15 * np.sin(25 * Vgs) * np.exp(-((Vgs - 0.5)/0.2)**2)
            Ids = base * noise
    elif T == 600:
        if gate == 'Pi-Gate':
            Ids = 5e-6 * np.exp(2 * np.maximum(0, Vgs_eff))
            Ids *= (1 + 0.5 * np.sin(10 * Vgs) + 0.2 * np.cos(25 * Vgs))
        else:
            Ids = 5e-8 * np.exp(4 * np.maximum(0, Vgs_eff))
            Ids *= (1 + 0.2 * np.sin(15 * Vgs) + 0.1 * np.cos(35 * Vgs))
    return Vgs, np.maximum(Ids, 1e-25)


def calculate_La2O3(T, gate):
    """La2O3 (k=27): Highest-k — maximum drive, hygroscopic degradation, broad transitions."""
    gp = gate_params[gate]
    eta = gp['eta']
    Vgs = np.linspace(-0.5, 1.2, 1000)

    Vt = 0.25 * eta
    Vgs_eff = Vgs - Vt

    if T == 77:
        if gate == 'Pi-Gate':
            Ids = np.where(Vgs_eff > 0,
                           2e-3 * (1 - np.exp(-3 * Vgs_eff)),
                           1e-11 * np.exp(3 * Vgs))
        else:
            Ids = np.where(Vgs_eff > 0,
                           3e-3 * (1 - np.exp(-8 * Vgs_eff)),
                           1e-14 * np.exp(5 * Vgs))
    elif T == 200:
        if gate == 'Pi-Gate':
            Ids = 1e-4 * (1 / (1 + np.exp(-8 * Vgs_eff))) + 1e-9 * np.exp(2 * Vgs_eff)
        else:
            Ids = 2e-4 * (1 / (1 + np.exp(-15 * Vgs_eff))) + 1e-12 * np.exp(5 * Vgs_eff)
    elif T == 300:
        if gate == 'Pi-Gate':
            I_sub = 1e-8 * np.exp(8 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.3 * 2e-4
            tr = 1 / (1 + np.exp(-15 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
        else:
            I_sub = 1e-11 * np.exp(15 * np.maximum(0, Vgs_eff))
            I_sat = np.maximum(0, Vgs_eff)**1.6 * 4e-4
            tr = 1 / (1 + np.exp(-40 * Vgs_eff))
            Ids = (1 - tr) * I_sub + tr * I_sat
    elif T == 400:
        if gate == 'Pi-Gate':
            I1 = 1e-6 * np.exp(4 * np.maximum(0, Vgs_eff))
            I2 = 5e-5 * np.exp(-((Vgs_eff - 0.3)/0.2)**2)
            Ids = I1 + I2
        else:
            I1 = 1e-8 * np.exp(7 * np.maximum(0, Vgs_eff))
            I2 = 8e-6 * np.exp(-((Vgs_eff - 0.35)/0.12)**2)
            Ids = I1 + I2
    elif T == 500:
        if gate == 'Pi-Gate':
            Ids = 5e-5 * np.exp(3 * np.maximum(0, Vgs_eff))
            Ids *= (1 + 2 * np.exp(-((Vgs_eff)/0.25)**2))
        else:
            Ids = 5e-7 * np.exp(5 * np.maximum(0, Vgs_eff))
            Ids *= (1 + 1.5 * np.exp(-((Vgs_eff - 0.1)/0.15)**2))
    elif T == 600:
        if gate == 'Pi-Gate':
            Ids = 1e-4 * np.exp(1.5 * np.maximum(0, Vgs_eff)) * np.exp(-0.05 * Vgs_eff)
            Ids += 2e-6
        else:
            Ids = 1e-6 * np.exp(3 * np.maximum(0, Vgs_eff)) * np.exp(-0.15 * Vgs_eff)
            Ids += 5e-9
    return Vgs, np.maximum(Ids, 1e-25)


# Material calculator dispatch
material_calculators = {
    'SiO2':  calculate_SiO2,
    'Al2O3': calculate_Al2O3,
    'HfO2':  calculate_HfO2,
    'ZrO2':  calculate_ZrO2,
    'La2O3': calculate_La2O3,
}

# Material info for annotations
material_info = {
    'SiO2':  {'kappa': 3.9,  'note': 'Low-k, high barrier'},
    'Al2O3': {'kappa': 9.0,  'note': 'Medium-k, trap kinks'},
    'HfO2':  {'kappa': 25.0, 'note': 'High-k, charge trapping'},
    'ZrO2':  {'kappa': 22.0, 'note': 'High-k, crystallization noise'},
    'La2O3': {'kappa': 27.0, 'note': 'Highest-k, broad transitions'},
}

# Create figure with subplots
fig, axes = plt.subplots(5, 2, figsize=(16, 24))
plt.subplots_adjust(hspace=0.4, wspace=0.3, top=0.95, bottom=0.05)

colors = ['blue', 'red', 'green', 'orange', 'purple', 'brown']
linestyles = ['-', '--', '-.', ':', '-', '--']
markers = ['o', 's', '^', 'D', 'v', '*']

for i, material in enumerate(materials):
    calc_fn = material_calculators[material]
    info = material_info[material]
    for j, gate in enumerate(gates):
        ax = axes[i, j]

        for temp_idx, T in enumerate(temperatures):
            Vgs, Ids = calc_fn(T, gate)

            ax.semilogy(Vgs, Ids,
                       color=colors[temp_idx],
                       linestyle=linestyles[temp_idx % len(linestyles)],
                       marker=markers[temp_idx % len(markers)],
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

        ax.text(0.97, 0.05,
               f"$\\kappa$ = {info['kappa']:.1f}\n{info['note']}",
               transform=ax.transAxes, fontsize=7,
               verticalalignment='bottom', horizontalalignment='right',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Overall title
plt.suptitle('Temperature-Dependent Transfer Characteristics: Pi-Gate vs Omega-Gate NWFETs\n' +
            r'High-k Dielectrics (SiO$_2$, Al$_2$O$_3$, HfO$_2$, ZrO$_2$, La$_2$O$_3$) Across 77K-600K Range',
            fontsize=16, fontweight='bold', y=0.98)

# Save the plot
plt.savefig('plots/temperature_dependent_iv.png', dpi=300, bbox_inches='tight')
plt.close()

print("Temperature-dependent IV plot generated with distinct characteristics for each material and temperature.")
