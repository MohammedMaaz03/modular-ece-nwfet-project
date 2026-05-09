import numpy as np
import matplotlib.pyplot as plt

# Set matplotlib parameters for publication quality
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 600

# Material properties (high-k dielectrics)
materials = {
    'SiO2': {'k': 3.9, 'Vt_offset': 0.1, 'mu_factor': 0.8},
    'Al2O3': {'k': 9.0, 'Vt_offset': 0.05, 'mu_factor': 0.9},
    'HfO2': {'k': 25, 'Vt_offset': -0.02, 'mu_factor': 1.0},
    'ZrO2': {'k': 22, 'Vt_offset': -0.01, 'mu_factor': 0.95},
    'La2O3': {'k': 27, 'Vt_offset': -0.03, 'mu_factor': 1.1}
}

def calculate_current(Vgs, gate_type, material):
    """Calculate drain current for different materials and gate types"""
    props = materials[material]
    k = props['k']
    Vt_offset = props['Vt_offset']
    mu_factor = props['mu_factor']

    # Base parameters
    Vt_base = 0.3 + Vt_offset  # Material-dependent threshold voltage
    SS_base = 65  # mV/dec

    if gate_type == 'Pi-Gate':
        eta = 0.7  # Lower gate efficiency
        SS = SS_base * 1.1
        Vt = Vt_base + 0.05
        I_scale = 0.7 * mu_factor
    elif gate_type == 'Omega-Gate':
        eta = 0.95  # Higher gate efficiency
        SS = SS_base * 0.9
        Vt = Vt_base - 0.02
        I_scale = 1.0 * mu_factor
    else:
        raise ValueError("Invalid gate type")

    # Effective gate voltage accounting for gate efficiency and dielectric constant
    Vgs_eff = eta * Vgs * np.sqrt(k / 3.9)  # Normalized to SiO2

    # Subthreshold current (exponential)
    k_factor = 1 / (SS/1000 * np.log(10))
    I_sub = 1e-12 * np.exp(k_factor * (Vgs_eff - Vt) * 1000 / 26)

    # Above threshold current (saturation-like)
    I_sat = I_scale * 1e-4 * np.maximum(0, (Vgs_eff - Vt))**1.5

    # Total current (smooth transition)
    alpha = 1 / (1 + np.exp(-20 * (Vgs_eff - Vt)))
    Ids = (1 - alpha) * I_sub + alpha * I_sat

    return np.maximum(Ids, 1e-15)

def generate_material_comparison_plot():
    """Generate comparison plot for all 5 materials showing Pi-Gate vs Omega-Gate"""

    Vgs = np.linspace(-0.5, 1.2, 200)

    # Create 5 subplots for 5 materials
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()

    material_names = list(materials.keys())
    colors_pi = ['blue', 'cyan', 'purple', 'brown', 'gray']
    colors_omega = ['red', 'orange', 'green', 'magenta', 'black']

    for i, material in enumerate(material_names):
        if i < 5:  # Only 5 materials
            ax = axes[i]

            # Calculate currents
            I_pi = calculate_current(Vgs, 'Pi-Gate', material)
            I_omega = calculate_current(Vgs, 'Omega-Gate', material)

            # Plot curves
            ax.semilogy(Vgs, I_pi, color=colors_pi[i], linewidth=2, linestyle='-',
                       label=f'Pi-Gate (η=0.7)')
            ax.semilogy(Vgs, I_omega, color=colors_omega[i], linewidth=2, linestyle='-',
                       label=f'Omega-Gate (η=0.95)')

            # Add threshold voltage lines
            Vt_pi = 0.3 + materials[material]['Vt_offset'] + 0.05
            Vt_omega = 0.3 + materials[material]['Vt_offset'] - 0.02

            ax.axvline(x=Vt_pi, color=colors_pi[i], linestyle='--', alpha=0.7, linewidth=1)
            ax.axvline(x=Vt_omega, color=colors_omega[i], linestyle='--', alpha=0.7, linewidth=1)

            # Formatting
            ax.set_xlabel('Gate Voltage (V)', fontsize=12)
            ax.set_ylabel('Drain Current (A)', fontsize=12)
            ax.set_title(f'{material} (k={materials[material]["k"]})\nPi-Gate vs Omega-Gate', fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend(loc='lower right', fontsize=10)
            ax.set_xlim(-0.5, 1.2)
            ax.set_ylim(1e-15, 1e-2)

    # Hide the empty subplot if any
    if len(material_names) < 6:
        axes[-1].set_visible(False)

    plt.tight_layout()

    # Save to desktop
    plt.savefig('C:/Users/Maaz_PC/Desktop/pi_omega_all_materials_comparison.png', dpi=600, bbox_inches='tight')
    plt.savefig('pi_omega_all_materials_comparison.png', dpi=600, bbox_inches='tight')
    print("Plot saved as 'pi_omega_all_materials_comparison.png' on desktop and project folder")

if __name__ == "__main__":
    generate_material_comparison_plot()
