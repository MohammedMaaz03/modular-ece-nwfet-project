import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('EIS Analysis Results: Pi-Gate vs Omega-Gate Comparison', 
             fontsize=16, fontweight='bold')

materials = ['HfO2', 'ZrO2', 'La2O3']
colors = ['#E63946', '#06D6A0', '#118AB2']

# Data with CLEAR differences
pi_rct = [800, 1500, 350]
omega_rct = [400, 750, 180]
pi_cap = [0.8, 0.5, 2.0]  # nF
omega_cap = [1.5, 1.0, 2.5]  # nF

# Plot 1: Bar chart - Rct comparison
ax1 = axes[0, 0]
x = np.arange(len(materials))
width = 0.35
bars1 = ax1.bar(x - width/2, pi_rct, width, label='Pi-Gate', color='#2E86AB', edgecolor='black')
bars2 = ax1.bar(x + width/2, omega_rct, width, label='Omega-Gate', color='#F18F01', edgecolor='black')
ax1.set_ylabel('Rct [Ω]', fontweight='bold')
ax1.set_title('Charge Transfer Resistance', fontweight='bold')
ax1.set_xticks(x)
ax1.set_xticklabels(materials)
ax1.legend()
ax1.grid(axis='y', alpha=0.3)
for bar in bars1:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30, 
             f'{int(bar.get_height())}', ha='center', fontsize=10)
for bar in bars2:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 30, 
             f'{int(bar.get_height())}', ha='center', fontsize=10)

# Plot 2: Bar chart - Capacitance comparison
ax2 = axes[0, 1]
bars3 = ax2.bar(x - width/2, pi_cap, width, label='Pi-Gate', color='#2E86AB', edgecolor='black')
bars4 = ax2.bar(x + width/2, omega_cap, width, label='Omega-Gate', color='#F18F01', edgecolor='black')
ax2.set_ylabel('Cdl [nF]', fontweight='bold')
ax2.set_title('Double Layer Capacitance', fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(materials)
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

# Plot 3: Time constant comparison
ax3 = axes[1, 0]
pi_tau = [r * c * 1e-9 * 1e6 for r, c in zip(pi_rct, pi_cap)]  # µs
omega_tau = [r * c * 1e-9 * 1e6 for r, c in zip(omega_rct, omega_cap)]
bars5 = ax3.bar(x - width/2, pi_tau, width, label='Pi-Gate', color='#2E86AB', edgecolor='black')
bars6 = ax3.bar(x + width/2, omega_tau, width, label='Omega-Gate', color='#F18F01', edgecolor='black')
ax3.set_ylabel('τ [µs]', fontweight='bold')
ax3.set_title('Relaxation Time Constant', fontweight='bold')
ax3.set_xticks(x)
ax3.set_xticklabels(materials)
ax3.legend()
ax3.grid(axis='y', alpha=0.3)

# Plot 4: Impedance at specific frequencies
ax4 = axes[1, 1]
freqs = [1, 100, 10000]  # Hz
freq_labels = ['1 Hz', '100 Hz', '10 kHz']

# Calculate |Z| at each frequency for each material
for i, (mat, color) in enumerate(zip(materials, colors)):
    pi_z = []
    omega_z = []
    for f in freqs:
        w = 2 * np.pi * f
        tau_pi = pi_rct[i] * pi_cap[i] * 1e-9
        tau_omega = omega_rct[i] * omega_cap[i] * 1e-9
        z_pi = pi_rct[i] / np.sqrt(1 + (w * tau_pi)**2)
        z_omega = omega_rct[i] / np.sqrt(1 + (w * tau_omega)**2)
        pi_z.append(z_pi)
        omega_z.append(z_omega)
    
    x_pos = np.array([0, 1, 2]) + i * 0.25
    ax4.plot(x_pos, pi_z, 'o--', color=color, label=f'{mat} Pi', markersize=8, linewidth=2)
    ax4.plot(x_pos, omega_z, 's-', color=color, label=f'{mat} Omega', markersize=8, linewidth=2)

ax4.set_xticks([0, 1, 2])
ax4.set_xticklabels(freq_labels)
ax4.set_ylabel('|Z| [Ω]', fontweight='bold')
ax4.set_title('Impedance vs Frequency', fontweight='bold')
ax4.legend(fontsize=8, ncol=3)
ax4.grid(alpha=0.3)

plt.tight_layout()
plt.savefig('eis_four_panel.png', dpi=300, bbox_inches='tight')
plt.show()
print("Four-panel EIS plot saved!")
