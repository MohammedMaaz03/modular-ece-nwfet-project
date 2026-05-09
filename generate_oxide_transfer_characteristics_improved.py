import matplotlib.pyplot as plt
import numpy as np
import os

# Ensure docs directory exists
os.makedirs('docs', exist_ok=True)

# Set up the data parameters
materials = ["SiO₂", "Al₂O₃", "HfO₂", "ZrO₂", "La₂O₃"]
dielectric_constants = [3.9, 9, 25, 25, 27]  # Corrected La₂O₃ to 27
gates = ["Pi-Gate", "Omega-Gate"]
temps = [77, 300, 600]
colors = {77: 'tab:blue', 300: 'tab:orange', 600: 'tab:red'}  # Changed 600 to red for distinction

vgs = np.linspace(0, 1.2, 200)

def calculate_ids(vgs, temp, k_val, gate_type):
    """
    Improved simplified MOSFET transfer characteristic.
    Adjusts Vth and SS based on temperature and dielectric constant.
    """
    # Base Vth shifts with temperature
    v_th_base = 0.5 - (temp - 300) * 0.0005
    
    # Omega-Gate is slightly more efficient (lower Vth)
    if gate_type == "Omega-Gate":
        v_th = v_th_base - 0.05
    else:
        v_th = v_th_base
    
    # Subthreshold swing (SS) increases with Temp, decreases with high-k
    ss = (temp / 300) * (60 / (k_val**0.3))  # Improved exponent
    ss_v = ss / 1000  # convert to V/dec
    
    # Subthreshold region
    ids_sub = 1e-15 * 10**((vgs - v_th) / ss_v)
    
    # Linear/Saturation region approximation
    ids_on = np.where(vgs > v_th, 1e-3 * (k_val / 4) * (vgs - v_th)**2, 0)
    
    # Smooth transition using sigmoid
    transition_factor = 1 / (1 + np.exp(-20 * (vgs - v_th)))
    ids = ids_sub * (1 - transition_factor) + ids_on * transition_factor
    
    # Add a floor to prevent log errors
    return np.clip(ids, 1e-18, 1e-2)

# Plotting
fig, axes = plt.subplots(5, 2, figsize=(16, 24), sharex=True)
plt.subplots_adjust(hspace=0.6, wspace=0.5, top=0.90, bottom=0.08, left=0.12, right=0.95)

for i, mat in enumerate(materials):
    for j, gate in enumerate(gates):
        ax = axes[i, j]
        k = dielectric_constants[i]
        
        for t in temps:
            ids = calculate_ids(vgs, t, k, gate)
            ax.plot(vgs, ids, label=f'{t} K', color=colors[t], linewidth=2)
        
        ax.set_yscale('log')
        ax.set_title(f"{gate} - {mat}", fontsize=12, pad=15)
        ax.set_ylabel("$I_{DS}$ (A)", fontsize=10)
        ax.set_xlabel("$V_{GS}$ (V)", fontsize=10)
        ax.set_ylim(1e-18, 1e-2)
        ax.grid(True, which="both", ls="-", alpha=0.5)
        ax.legend(fontsize='small', loc='upper left')

plt.suptitle('Oxide-Dependent Transfer Characteristics: Pi-Gate vs Omega-Gate NWFETs', fontsize=18, fontweight='bold', y=0.95)
plt.tight_layout(rect=[0.12, 0.1, 0.95, 0.92])
plt.savefig('docs/oxide_dependent_iv_improved.png', dpi=300, bbox_inches='tight')
plt.show()
