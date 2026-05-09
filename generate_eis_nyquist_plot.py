import numpy as np
import matplotlib.pyplot as plt

# Representative EIS data for Nyquist plot (simulated)
# Frequency range: 1 Hz to 1 MHz (log scale)
frequencies = np.logspace(0, 6, 100)  # Hz

# Pi-Gate parameters by material (higher resistance, less ideal)
pi_gate_params = {
    'HfO2': {'r_s': 10, 'r_ct': 500, 'c_dl': 1e-9, 'alpha': 0.85},
    'ZrO2': {'r_s': 12, 'r_ct': 550, 'c_dl': 0.9e-9, 'alpha': 0.80},
    'La2O3': {'r_s': 8, 'r_ct': 450, 'c_dl': 1.1e-9, 'alpha': 0.88}
}

# Omega-Gate parameters by material (lower resistance, more ideal)
omega_gate_params = {
    'HfO2': {'r_s': 8, 'r_ct': 300, 'c_dl': 1.2e-9, 'alpha': 0.92},
    'ZrO2': {'r_s': 9, 'r_ct': 320, 'c_dl': 1.1e-9, 'alpha': 0.90},
    'La2O3': {'r_s': 7, 'r_ct': 280, 'c_dl': 1.3e-9, 'alpha': 0.94}
}

# Materials: HfO2, ZrO2, La2O3
materials = ['HfO2', 'ZrO2', 'La2O3']

# Function to calculate impedance for CPE (Constant Phase Element)
def cpe_impedance(q, alpha, w):
    return 1 / (q * (1j * w)**alpha)

def calculate_nyquist(r_s, r_ct, q, alpha, w):
    z_cpe = cpe_impedance(q, alpha, w)
    z_total = r_s + r_ct / (1 + r_ct * z_cpe)
    return z_total.real, -z_total.imag  # Nyquist: Z_real vs -Z_imag

plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12
plt.rcParams['legend.fontsize'] = 12

fig, axes = plt.subplots(1, 3, figsize=(18, 6))
fig.suptitle('EIS Nyquist Plots: Pi-Gate vs Omega-Gate Comparison Across Materials\n(3 nm Oxide, 300 K)', fontsize=18, fontweight='bold')

for i, material in enumerate(materials):
    ax = axes[i]
    
    # Get Pi-Gate parameters for this material
    pi_params = pi_gate_params[material]
    z_real_pi, z_imag_pi = calculate_nyquist(pi_params['r_s'], pi_params['r_ct'], pi_params['c_dl'], pi_params['alpha'], 2 * np.pi * frequencies)
    ax.plot(z_real_pi, z_imag_pi, 'o-', label=f'Pi-Gate (η=0.82)', color='#1f77b4', markersize=4, linewidth=2, markerfacecolor='white', markeredgewidth=1)
    
    # Get Omega-Gate parameters for this material
    omega_params = omega_gate_params[material]
    z_real_omega, z_imag_omega = calculate_nyquist(omega_params['r_s'], omega_params['r_ct'], omega_params['c_dl'], omega_params['alpha'], 2 * np.pi * frequencies)
    ax.plot(z_real_omega, z_imag_omega, 's-', label=f'Omega-Gate (η=0.98)', color='#ff7f0e', markersize=4, linewidth=2, markerfacecolor='white', markeredgewidth=1)
    
    ax.set_xlabel('Z\' (Real Impedance) [Ω]', fontweight='bold')
    ax.set_ylabel('-Z\'\' (Imaginary Impedance) [Ω]', fontweight='bold')
    ax.set_title(f'{material} Dielectric', fontweight='bold')
    ax.legend(frameon=True, fancybox=True, shadow=True)
    ax.grid(True, alpha=0.3, linestyle='--')
    ax.axis('equal')  # Equal aspect ratio for semicircle
    
    # Add annotations for key points (adjusted for each material)
    ax.annotate('Series Resistance', xy=(min(z_real_pi), 0), xytext=(min(z_real_pi)-20, -10), 
                arrowprops=dict(arrowstyle='->', color='black'), fontsize=10)
    ax.annotate('Relaxation Peak', xy=(z_real_pi[len(z_real_pi)//2], z_imag_pi[len(z_imag_pi)//2]), 
                xytext=(z_real_pi[len(z_real_pi)//2]+50, z_imag_pi[len(z_imag_pi)//2]-20), 
                arrowprops=dict(arrowstyle='->', color='black'), fontsize=10)

plt.tight_layout()
plt.savefig('eis_nyquist_comparison_improved.png', dpi=300, bbox_inches='tight')
plt.show()
