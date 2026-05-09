import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('EIS Analysis: Clear Visual Comparison of Dielectric Properties', 
             fontsize=18, fontweight='bold')

# Frequency range
frequencies = np.logspace(0, 6, 100)

def calculate_nyquist_simple(r_ct, c_dl, w):
    """Simplified Nyquist calculation"""
    tau = r_ct * c_dl  # Time constant
    z_real = r_ct / (1 + (w * tau)**2)
    z_imag = (w * tau * r_ct) / (1 + (w * tau)**2)
    return z_real, z_imag

# Left plot: All curves on same axis (shows relative sizes clearly)
ax1 = axes[0]

data = [
    ('HfO2', 'Pi', 800, 0.8e-9, '#1f77b4', 'o'),
    ('HfO2', 'Omega', 400, 1.5e-9, '#ff7f0e', 's'),
    ('ZrO2', 'Pi', 1500, 0.5e-9, '#2ca02c', '^'),
    ('ZrO2', 'Omega', 750, 1.0e-9, '#d62728', 'v'),
    ('La2O3', 'Pi', 350, 2.0e-9, '#9467bd', 'D'),
    ('La2O3', 'Omega', 180, 2.5e-9, '#8c564b', 'p'),
]

for material, gate, r_ct, c_dl, color, marker in data:
    z_real, z_imag = calculate_nyquist_simple(r_ct, c_dl, 2 * np.pi * frequencies)
    label = f'{material} {gate}-Gate (Rct={r_ct}Ω)'
    ax1.plot(z_real, z_imag, marker=marker, color=color, label=label, 
             markersize=6, linewidth=2.5, markevery=10, alpha=0.8)

ax1.set_xlabel('Z\' (Real Impedance) [Ω]', fontweight='bold', fontsize=14)
ax1.set_ylabel('-Z\'\' (Imaginary Impedance) [Ω]', fontweight='bold', fontsize=14)
ax1.set_title('All Materials Comparison (Same Plot)', fontweight='bold', fontsize=15)
ax1.legend(fontsize=10, loc='upper right', frameon=True, shadow=True, ncol=2)
ax1.grid(True, alpha=0.3)
ax1.set_xlim(0, 1600)
ax1.set_ylim(0, 800)

# Right plot: Bar chart of key parameters
ax2 = axes[1]

materials = ['HfO2', 'ZrO2', 'La2O3']
pi_rct = [800, 1500, 350]
omega_rct = [400, 750, 180]
pi_tau = [r * c * 1e9 for r, c in zip([800, 1500, 350], [0.8e-9, 0.5e-9, 2.0e-9])]  # in ns
omega_tau = [r * c * 1e9 for r, c in zip([400, 750, 180], [1.5e-9, 1.0e-9, 2.5e-9])]

x = np.arange(len(materials))
width = 0.35

# Create grouped bar chart
bars1 = ax2.bar(x - width/2, pi_rct, width, label='Pi-Gate Rct', color='#1f77b4', alpha=0.8, edgecolor='black')
bars2 = ax2.bar(x + width/2, omega_rct, width, label='Omega-Gate Rct', color='#ff7f0e', alpha=0.8, edgecolor='black')

ax2.set_ylabel('Charge Transfer Resistance [Ω]', fontweight='bold', fontsize=14)
ax2.set_title('Rct Comparison by Material', fontweight='bold', fontsize=15)
ax2.set_xticks(x)
ax2.set_xticklabels(materials, fontweight='bold', fontsize=13)
ax2.legend(fontsize=12, frameon=True, shadow=True)
ax2.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 30,
                f'{int(height)}Ω', ha='center', va='bottom', fontsize=11, fontweight='bold')

# Add improvement annotation
for i in range(len(materials)):
    improvement = ((pi_rct[i] - omega_rct[i]) / pi_rct[i]) * 100
    ax2.annotate(f'↓{improvement:.0f}%', 
                xy=(i, max(pi_rct[i], omega_rct[i]) + 150),
                ha='center', fontsize=12, fontweight='bold', color='green',
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))

plt.tight_layout()
plt.savefig('eis_clear_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
print("Clear EIS comparison plot saved!")
