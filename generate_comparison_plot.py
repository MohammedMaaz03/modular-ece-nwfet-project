import numpy as np
import matplotlib.pyplot as plt

# Data for Pi-Gate vs Omega-Gate comparison (representative values from simulations)
materials = ['SiO2', 'Al2O3', 'HfO2', 'ZrO2', 'La2O3']
pi_gate_ion = [120, 135, 150, 140, 155]  # On-current in µA
omega_gate_ion = [145, 160, 180, 165, 185]
pi_gate_vth = [0.45, 0.40, 0.35, 0.38, 0.32]  # Threshold voltage in V
omega_gate_vth = [0.42, 0.38, 0.33, 0.36, 0.30]
pi_gate_ss = [75, 70, 68, 72, 66]  # Subthreshold swing in mV/dec
omega_gate_ss = [65, 60, 58, 62, 56]

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Pi-Gate vs Omega-Gate NWFET Performance Comparison\n(3 nm Oxide, 300 K)', fontsize=18, fontweight='bold')

# On-current comparison
x = np.arange(len(materials))
width = 0.35
bars1 = ax1.bar(x - width/2, pi_gate_ion, width, label='Pi-Gate', alpha=0.9, color='#1f77b4', edgecolor='black', linewidth=1)
bars2 = ax1.bar(x + width/2, omega_gate_ion, width, label='Omega-Gate', alpha=0.9, color='#ff7f0e', edgecolor='black', linewidth=1)
ax1.set_ylabel('On-Current (µA)', fontweight='bold')
ax1.set_title('On-Current Comparison', fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(materials, fontweight='bold')
ax1.legend(frameon=True, fancybox=True, shadow=True)
ax1.grid(True, alpha=0.3, linestyle='--')
ax1.bar_label(bars1, padding=3, fontsize=10)
ax1.bar_label(bars2, padding=3, fontsize=10)

# Threshold voltage comparison
bars3 = ax2.bar(x - width/2, pi_gate_vth, width, label='Pi-Gate', alpha=0.9, color='#1f77b4', edgecolor='black', linewidth=1)
bars4 = ax2.bar(x + width/2, omega_gate_vth, width, label='Omega-Gate', alpha=0.9, color='#ff7f0e', edgecolor='black', linewidth=1)
ax2.set_ylabel('Threshold Voltage (V)', fontweight='bold')
ax2.set_title('Threshold Voltage Comparison', fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(materials, fontweight='bold')
ax2.legend(frameon=True, fancybox=True, shadow=True)
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.bar_label(bars3, padding=3, fontsize=10, fmt='%.2f')
ax2.bar_label(bars4, padding=3, fontsize=10, fmt='%.2f')

# Subthreshold swing comparison
bars5 = ax3.bar(x - width/2, pi_gate_ss, width, label='Pi-Gate', alpha=0.9, color='#1f77b4', edgecolor='black', linewidth=1)
bars6 = ax3.bar(x + width/2, omega_gate_ss, width, label='Omega-Gate', alpha=0.9, color='#ff7f0e', edgecolor='black', linewidth=1)
ax3.set_ylabel('Subthreshold Swing (mV/dec)', fontweight='bold')
ax3.set_title('Subthreshold Swing Comparison', fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(materials, fontweight='bold')
ax3.legend(frameon=True, fancybox=True, shadow=True)
ax3.grid(True, alpha=0.3, linestyle='--')
ax3.bar_label(bars5, padding=3, fontsize=10)
ax3.bar_label(bars6, padding=3, fontsize=10)

# Ion/Ioff ratio comparison (calculated)
pi_gate_ioff = [50, 40, 35, 38, 32]  # Off-current in nA
omega_gate_ioff = [30, 25, 20, 22, 18]
pi_gate_ratio = [ion / (ioff * 1e-3) for ion, ioff in zip(pi_gate_ion, pi_gate_ioff)]
omega_gate_ratio = [ion / (ioff * 1e-3) for ion, ioff in zip(omega_gate_ion, omega_gate_ioff)]

bars7 = ax4.bar(x - width/2, pi_gate_ratio, width, label='Pi-Gate', alpha=0.9, color='#1f77b4', edgecolor='black', linewidth=1)
bars8 = ax4.bar(x + width/2, omega_gate_ratio, width, label='Omega-Gate', alpha=0.9, color='#ff7f0e', edgecolor='black', linewidth=1)
ax4.set_ylabel('Ion/Ioff Ratio (×10³)', fontweight='bold')
ax4.set_title('Ion/Ioff Ratio Comparison', fontweight='bold')
ax4.set_xticks(x)
ax4.set_xticklabels(materials, fontweight='bold')
ax4.legend(frameon=True, fancybox=True, shadow=True)
ax4.grid(True, alpha=0.3, linestyle='--')
ax4.bar_label(bars7, padding=3, fontsize=10, fmt='%.1f')
ax4.bar_label(bars8, padding=3, fontsize=10, fmt='%.1f')

plt.tight_layout()
plt.savefig('pi_omega_comparison_bar_chart_improved.png', dpi=300, bbox_inches='tight')
plt.show()
