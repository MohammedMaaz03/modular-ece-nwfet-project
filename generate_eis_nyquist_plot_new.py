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

# Different parameters for each material to show clear differences
materials_data = [
    {
        'name': 'HfO2',
        'pi': {'r_s': 10, 'r_ct': 500, 'c_dl': 1e-9, 'alpha': 0.85},
        'omega': {'r_s': 8, 'r_ct': 300, 'c_dl': 1.2e-9, 'alpha': 0.92}
    },
    {
        'name': 'ZrO2',
        'pi': {'r_s': 12, 'r_ct': 550, 'c_dl': 0.9e-9, 'alpha': 0.80},
        'omega': {'r_s': 9, 'r_ct': 320, 'c_dl': 1.1e-9, 'alpha': 0.90}
    },
    {
        'name': 'La2O3',
        'pi': {'r_s': 8, 'r_ct': 450, 'c_dl': 1.1e-9, 'alpha': 0.88},
        'omega': {'r_s': 7, 'r_ct': 280, 'c_dl': 1.3e-9, 'alpha': 0.94}
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
    
    # Plot with distinct markers and colors
    ax.plot(z_real_pi, z_imag_pi, 'o-', label='Pi-Gate (η=0.82)', color='#1f77b4', 
            markersize=5, linewidth=2.5, markerfacecolor='white', markeredgewidth=1.5)
    ax.plot(z_real_omega, z_imag_omega, 's-', label='Omega-Gate (η=0.98)', color='#ff7f0e', 
            markersize=5, linewidth=2.5, markerfacecolor='white', markeredgewidth=1.5)
    
    # Set labels and title
    ax.set_xlabel('Z\' (Real Impedance) [Ω]', fontweight='bold')
    ax.set_ylabel('-Z\'\' (Imaginary Impedance) [Ω]', fontweight='bold')
    ax.set_title(f'{data["name"]} Dielectric', fontweight='bold')
    ax.legend(frameon=True, fancybox=True, shadow=True, loc='upper right')
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Set axis limits to show the semicircle clearly
    max_z = max(max(z_real_pi), max(z_real_omega)) * 1.1
    max_z_imag = max(max(z_imag_pi), max(z_imag_omega)) * 1.1
    ax.set_xlim(0, max_z)
    ax.set_ylim(0, max_z_imag)
    ax.set_aspect('equal', adjustable='box')
    
    # Add frequency annotations at key points
    freq_indices = [0, len(frequencies)//4, len(frequencies)//2, 3*len(frequencies)//4, -1]
    for idx in freq_indices:
        if idx < len(z_real_pi):
            ax.annotate(f'{frequencies[idx]:.0f} Hz', 
                       xy=(z_real_pi[idx], z_imag_pi[idx]), 
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=8, alpha=0.7)

plt.tight_layout()
plt.savefig('eis_nyquist_comparison_improved.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.show()
