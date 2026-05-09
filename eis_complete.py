import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12

fig = plt.figure(figsize=(18, 10))

# Create a 2x2 grid
gs = fig.add_gridspec(2, 2, hspace=0.3, wspace=0.3)
ax1 = fig.add_subplot(gs[0, :])  # Top: Bar chart spanning both columns
ax2 = fig.add_subplot(gs[1, 0])  # Bottom left: Bode magnitude
ax3 = fig.add_subplot(gs[1, 1])  # Bottom right: Bode phase

fig.suptitle('EIS Analysis: Electrochemical Impedance Spectroscopy Results', 
             fontsize=20, fontweight='bold', y=0.98)

# Data
materials = ['HfO2', 'ZrO2', 'La2O3']
pi_gate = {'r_ct': [800, 1500, 350], 'c_dl': [0.8e-9, 0.5e-9, 2.0e-9], 'color': '#2E86AB'}
omega_gate = {'r_ct': [400, 750, 180], 'c_dl': [1.5e-9, 1.0e-9, 2.5e-9], 'color': '#F18F01'}

# Top plot: Grouped bar chart
x = np.arange(len(materials))
width = 0.35

bars1 = ax1.bar(x - width/2, pi_gate['r_ct'], width, label='Pi-Gate', 
                color=pi_gate['color'], alpha=0.85, edgecolor='black', linewidth=2)
bars2 = ax1.bar(x + width/2, omega_gate['r_ct'], width, label='Omega-Gate', 
                color=omega_gate['color'], alpha=0.85, edgecolor='black', linewidth=2)

ax1.set_ylabel('Charge Transfer Resistance Rct [Ω]', fontweight='bold', fontsize=14)
ax1.set_title('Key Finding: Omega-Gate Reduces Charge Transfer Resistance by ~50%', 
              fontweight='bold', fontsize=15, pad=10)
ax1.set_xticks(x)
ax1.set_xticklabels(materials, fontweight='bold', fontsize=14)
ax1.legend(fontsize=13, frameon=True, shadow=True)
ax1.grid(True, alpha=0.3, axis='y', linestyle='--')
ax1.set_ylim(0, 1800)

# Add value labels
for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 40,
            f'{int(height)}Ω', ha='center', va='bottom', fontsize=12, fontweight='bold')
for bar in bars2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 40,
            f'{int(height)}Ω', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Add improvement arrows
for i in range(len(materials)):
    improvement = ((pi_gate['r_ct'][i] - omega_gate['r_ct'][i]) / pi_gate['r_ct'][i]) * 100
    ax1.annotate('', xy=(i + width/2, omega_gate['r_ct'][i] + 100), 
                xytext=(i - width/2, pi_gate['r_ct'][i] - 100),
                arrowprops=dict(arrowstyle='->', color='green', lw=3))
    ax1.text(i, (pi_gate['r_ct'][i] + omega_gate['r_ct'][i])/2, 
             f'{improvement:.0f}%\nBetter', ha='center', fontsize=11, 
             fontweight='bold', color='green',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

# Bode plots - calculate impedance for each material
frequencies = np.logspace(0, 6, 200)
w = 2 * np.pi * frequencies

# Bottom left: Magnitude
colors = ['#E63946', '#06D6A0', '#118AB2']  # Red, Green, Blue for HfO2, ZrO2, La2O3
markers = ['o', 's', '^']

for i, mat in enumerate(materials):
    # Pi-Gate
    tau_pi = pi_gate['r_ct'][i] * pi_gate['c_dl'][i]
    z_pi = pi_gate['r_ct'][i] / (1 + 1j * w * tau_pi)
    mag_pi = 20 * np.log10(np.abs(z_pi))
    ax2.semilogx(frequencies, mag_pi, color=colors[i], linewidth=2.5, 
                linestyle='--', marker=markers[i], markersize=4, markevery=20,
                label=f'{mat} Pi-Gate')
    
    # Omega-Gate
    tau_omega = omega_gate['r_ct'][i] * omega_gate['c_dl'][i]
    z_omega = omega_gate['r_ct'][i] / (1 + 1j * w * tau_omega)
    mag_omega = 20 * np.log10(np.abs(z_omega))
    ax2.semilogx(frequencies, mag_omega, color=colors[i], linewidth=2.5, 
                linestyle='-', marker=markers[i], markersize=4, markevery=20,
                label=f'{mat} Omega-Gate')

ax2.set_xlabel('Frequency [Hz]', fontweight='bold', fontsize=13)
ax2.set_ylabel('|Z| [dB]', fontweight='bold', fontsize=13)
ax2.set_title('Bode Plot: Impedance Magnitude', fontweight='bold', fontsize=14)
ax2.legend(fontsize=9, ncol=2, loc='upper right')
ax2.grid(True, alpha=0.3, which='both')

# Bottom right: Phase
for i, mat in enumerate(materials):
    # Pi-Gate
    tau_pi = pi_gate['r_ct'][i] * pi_gate['c_dl'][i]
    z_pi = pi_gate['r_ct'][i] / (1 + 1j * w * tau_pi)
    phase_pi = np.angle(z_pi, deg=True)
    ax3.semilogx(frequencies, phase_pi, color=colors[i], linewidth=2.5, 
                linestyle='--', marker=markers[i], markersize=4, markevery=20)
    
    # Omega-Gate
    tau_omega = omega_gate['r_ct'][i] * omega_gate['c_dl'][i]
    z_omega = omega_gate['r_ct'][i] / (1 + 1j * w * tau_omega)
    phase_omega = np.angle(z_omega, deg=True)
    ax3.semilogx(frequencies, phase_omega, color=colors[i], linewidth=2.5, 
                linestyle='-', marker=markers[i], markersize=4, markevery=20,
                label=mat)

ax3.set_xlabel('Frequency [Hz]', fontweight='bold', fontsize=13)
ax3.set_ylabel('Phase [degrees]', fontweight='bold', fontsize=13)
ax3.set_title('Bode Plot: Impedance Phase', fontweight='bold', fontsize=14)
ax3.legend(fontsize=10, loc='lower left')
ax3.grid(True, alpha=0.3, which='both')
ax3.set_ylim(-90, 0)

# Add solid/dashed line explanation
from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='black', lw=2, linestyle='--', label='Pi-Gate'),
                   Line2D([0], [0], color='black', lw=2, linestyle='-', label='Omega-Gate')]
fig.legend(handles=legend_elements, loc='lower center', ncol=2, fontsize=12, 
          frameon=True, bbox_to_anchor=(0.5, -0.02))

plt.savefig('eis_complete_analysis.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
print("Complete EIS analysis plot saved!")
