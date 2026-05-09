import numpy as np
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

print("--- Generating 3D Temp vs VGS vs ID Surface (Full 5 Materials for both gates) ---")

# 1. SETUP AXES
vgs = np.linspace(0, 1.2, 50)
temp = np.linspace(400, 600, 50)  # for high temp
VGS_grid, T_grid = np.meshgrid(vgs, temp)

# 2. COMPLETE MATERIAL PARAMETERS
materials = {
    "SiO2": [3.9, 0.45], 
    "Al2O3": [9.0, 0.42],
    "ZrO2": [22.0, 0.39],
    "HfO2": [25.0, 0.38], 
    "La2O3": [27.0, 0.35]
}

# 3. ARCHITECTURE SETTINGS
gate_configs = {
    "PiGate": {"eta": 0.82, "mu_ref": 0.04},
    "OmegaGate": {"eta": 0.98, "mu_ref": 0.06}
}

fig = plt.figure(figsize=(20, 12))
fig.suptitle(f'3D Transfer Analysis: $I_D$ vs $V_{{GS}}$ vs Temp for PiGate and OmegaGate NWFETs', fontsize=18, fontweight='bold', y=0.96)

idx = 0
for gate_name, par in gate_configs.items():
    for m_name, m_data in materials.items():
        k_val, vth0 = m_data
        ax = fig.add_subplot(2, 5, idx+1, projection='3d')
        
        # 4. PHYSICS MODEL
        vth_t = vth0 - 0.0005 * (T_grid - 300)
        
        mu_t = par['mu_ref'] * (np.maximum(T_grid, 10) / 300)**-1.5
        
        eps0 = 8.854e-12
        tox = 2e-9
        Cox = (eps0 * k_val) / tox
        W, L = 10e-9, 10e-9
        
        v_od = np.maximum(VGS_grid - vth_t, 0)
        ID = 0.5 * mu_t * Cox * par['eta'] * (W/L) * v_od**2
        ID_uA = ID * 1e6
        
        # 5. PLOTTING
        cs = ax.contourf(VGS_grid, T_grid, ID_uA, cmap='turbo', levels=20)
        
        ax.set_title(f'{gate_name} - {m_name}', fontsize=12, fontweight='bold', pad=10)
        ax.set_xlabel('$V_{GS}$ (V)', fontsize=8)
        ax.set_ylabel('Temp (K)', fontsize=8)
        
        idx += 1

filename = "docs/plots/high_temperature_reliability.png"
os.makedirs(os.path.dirname(filename), exist_ok=True)
plt.savefig(filename, dpi=300)
print(f"SUCCESS: Created {filename}")
plt.close(fig)

print("--- 3D Transfer surface generated successfully! ---")
