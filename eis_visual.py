import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 11

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('EIS Analysis: Charge Transfer Resistance by Material and Gate Architecture', 
             fontsize=16, fontweight='bold', y=1.02)

materials = ['HfO2', 'ZrO2', 'La2O3']

# Very different Rct values for each material
pi_gate_rct = [800, 1500, 350]   # Dramatically different - 800, 1500, 350
omega_gate_rct = [400, 750, 180]  # Half of Pi-Gate

x = np.arange(len(materials))
width = 0.35

# Colors
pi_color = '#2E86AB'  # Blue
omega_color = '#F18F01'  # Orange

# Plot 1: Bar chart comparison
ax1 = axes[0]
bars1 = ax1.bar(x - width/2, pi_gate_rct, width, label='Pi-Gate', color=pi_color, alpha=0.8, edgecolor='black', linewidth=1.5)
bars2 = ax1.bar(x + width/2, omega_gate_rct, width, label='Omega-Gate', color=omega_color, alpha=0.8, edgecolor='black', linewidth=1.5)
ax1.set_ylabel('Charge Transfer Resistance Rct [Ω]', fontweight='bold', fontsize=12)
ax1.set_title('Charge Transfer Resistance Comparison', fontweight='bold', fontsize=13)
ax1.set_xticks(x)
ax1.set_xticklabels(materials, fontweight='bold', fontsize=12)
ax1.legend(fontsize=11, frameon=True, shadow=True)
ax1.grid(True, alpha=0.3, axis='y')
ax1.bar_label(bars1, padding=3, fontsize=10, fmt='%dΩ')
ax1.bar_label(bars2, padding=3, fontsize=10, fmt='%dΩ')

# Add improvement percentage labels
for i in range(len(materials)):
    improvement = ((pi_gate_rct[i] - omega_gate_rct[i]) / pi_gate_rct[i]) * 100
    ax1.text(i, max(pi_gate_rct[i], omega_gate_rct[i]) + 80, f'↓{improvement:.0f}%', 
             ha='center', fontsize=10, fontweight='bold', color='green')

# Plot 2: Semicircle visualization (hand-drawn style)
ax2 = axes[1]
theta = np.linspace(0, np.pi, 100)

for i, mat in enumerate(materials):
    # Pi-Gate: Larger, more depressed semicircle
    r_pi = pi_gate_rct[i] / 2
    center_pi = pi_gate_rct[i] / 2
    x_pi = center_pi + r_pi * np.cos(theta)
    y_pi = r_pi * 0.7 * np.sin(theta)  # Depressed (alpha < 1)
    ax2.plot(x_pi, y_pi, linewidth=3, label=f'{mat} Pi-Gate', linestyle='--', alpha=0.8)
    ax2.fill_between(x_pi, y_pi, alpha=0.1)
    
    # Omega-Gate: Smaller, more ideal semicircle
    r_omega = omega_gate_rct[i] / 2
    center_omega = omega_gate_rct[i] / 2
    x_omega = center_omega + r_omega * np.cos(theta)
    y_omega = r_omega * 0.95 * np.sin(theta)  # More ideal (alpha ~ 1)
    ax2.plot(x_omega, y_omega, linewidth=3, label=f'{mat} Omega-Gate', linestyle='-', alpha=0.8)
    ax2.fill_between(x_omega, y_omega, alpha=0.2)

ax2.set_xlabel('Z\' (Real Impedance) [Ω]', fontweight='bold', fontsize=12)
ax2.set_ylabel('-Z\'\' (Imaginary Impedance) [Ω]', fontweight='bold', fontsize=12)
ax2.set_title('Nyquist Plot Comparison (Scaled)', fontweight='bold', fontsize=13)
ax2.legend(fontsize=9, ncol=2, loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(0, 1600)
ax2.set_ylim(0, 800)

# Plot 3: Ratio/Gain visualization
ax3 = axes[2]
ratios = [pi / omega for pi, omega in zip(pi_gate_rct, omega_gate_rct)]
bars3 = ax3.bar(materials, ratios, color='#28A745', alpha=0.8, edgecolor='black', linewidth=1.5)
ax3.set_ylabel('Resistance Ratio (Pi-Gate / Omega-Gate)', fontweight='bold', fontsize=12)
ax3.set_title('Omega-Gate Improvement Factor', fontweight='bold', fontsize=13)
ax3.set_xticklabels(materials, fontweight='bold', fontsize=12)
ax3.axhline(y=2.0, color='red', linestyle='--', linewidth=2, label='2x Ideal')
ax3.grid(True, alpha=0.3, axis='y')
ax3.legend(fontsize=11)

for bar, ratio in zip(bars3, ratios):
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 0.05,
             f'{ratio:.1f}x', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('eis_analysis_visual.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
print("EIS visualization saved!")
