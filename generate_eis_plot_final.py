import numpy as np
import matplotlib.pyplot as plt

# Set up the figure with better layout
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

fig, axes = plt.subplots(1, 3, figsize=(20, 6))
fig.suptitle('EIS Nyquist Plots: Pi-Gate vs Omega-Gate Comparison Across Materials\n(3 nm Oxide, 300 K)', fontsize=18, fontweight='bold')

# Frequency range
frequencies = np.logspace(0, 6, 100)  # 1 Hz to 1 MHz

# DRAMATICALLY different parameters for each material to show CLEAR visual differences
materials_data = [
    {
        'name': 'HfO2',
        'pi': {'r_s': 15, 'r_ct': 800, 'c_dl': 0.8e-9, 'alpha': 0.75},
        'omega': {'r_s': 10, 'r_ct': 400, 'c_dl': 1.5e-9, 'alpha': 0.95}
    },
    {
        'name': 'ZrO2',
        'pi': {'r_s': 25, 'r_ct': 1200, 'c_dl': 0.5e-9, 'alpha': 0.70},
        'omega': {'r_s': 18, 'r_ct': 600, 'c_dl': 1.0e-9, 'alpha': 0.90}
    },
    {
        'name': 'La2O3',
        'pi': {'r_s': 8, 'r_ct': 300, 'c_dl': 2.0e-9, 'alpha': 0.88},
        'omega': {'r_s': 5, 'r_ct': 150, 'c_dl': 2.5e-9, 'alpha': 0.98}
    }
]

def cpe_impedance(q, alpha, w):
    return 1 / (q * (1j * w)**alpha)

def calculate_nyquist(r_s, r_ct, q, alpha, w):
    z_cpe = cpe_impedance(q, alpha, w)
    z_total = r_s + r_ct / (1 + r_ct * z_cpe)
    return z_total.real, -z_total.imag

for i, data in enumerate(materials_data):
    ax = axes[i]
    
    # Calculate Pi-Gate
    pi = data['pi']
    z_real_pi, z_imag_pi = calculate_nyquist(pi['r_s'], pi['r_ct'], pi['c_dl'], pi['alpha'], 2 * np.pi * frequencies)
    
    # Calculate Omega-Gate
    omega = data['omega']
    z_real_omega, z_imag_omega = calculate_nyquist(omega['r_s'], omega['r_ct'], omega['c_dl'], omega['alpha'], 2 * np.pi * frequencies)
    
    # Plot with distinct markers and colors - Pi-Gate as depressed semicircle
    ax.plot(z_real_pi, z_imag_pi, 'o-', label='Pi-Gate (η=0.82)', color='#1f77b4', 
            markersize=6, linewidth=3, markerfacecolor='white', markeredgewidth=2, alpha=0.9)
    
    # Omega-Gate as more ideal semicircle
    ax.plot(z_real_omega, z_imag_omega, 's-', label='Omega-Gate (η=0.98)', color='#ff7f0e', 
            markersize=6, linewidth=3, markerfacecolor='white', markeredgewidth=2, alpha=0.9)
    
    # Set labels and title
    ax.set_xlabel('Z\' (Real Impedance) [Ω]', fontweight='bold')
    ax.set_ylabel('-Z\'\' (Imaginary Impedance) [Ω]', fontweight='bold')
    ax.set_title(f'{data["name"]} Dielectric', fontweight='bold', fontsize=16)
    ax.legend(frameon=True, fancybox=True, shadow=True, loc='upper right', fontsize=11)
    ax.grid(True, alpha=0.4, linestyle='--', linewidth=0.8)
    
    # Set axis limits - each subplot will have different scales
    max_z = max(max(z_real_pi), max(z_real_omega)) * 1.15
    max_z_imag = max(max(z_imag_pi), max(z_imag_omega)) * 1.15
    ax.set_xlim(0, max_z)
    ax.set_ylim(0, max_z_imag)
    ax.set_aspect('equal', adjustable='box')
    
    # Add clear annotations showing the key difference
    ax.text(0.5, 0.95, f'Rct(π): {pi["r_ct"]}Ω\nRct(Ω): {omega["r_ct"]}Ω', 
            transform=ax.transAxes, fontsize=11, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.tight_layout()
plt.savefig('eis_nyquist_comparison_final.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
print("Plot saved successfully!")
