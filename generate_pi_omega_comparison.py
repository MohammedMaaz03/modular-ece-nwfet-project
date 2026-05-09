import numpy as np
import matplotlib.pyplot as plt

# Set matplotlib parameters for publication quality
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 12
plt.rcParams['figure.dpi'] = 600

def calculate_current(Vgs, gate_type, material='Si'):
    """
    Calculate drain current for Pi-Gate vs Omega-Gate NWFET
    Pi-Gate: η = 0.7 (lower gate efficiency)
    Omega-Gate: η = 0.95 (higher gate efficiency)
    """

    # Material properties
    materials = {
        'Si': {'mu': 400, 'Vt_base': 0.3, 'SS_base': 65}
    }

    mu = materials[material]['mu']
    Vt_base = materials[material]['Vt_base']
    SS_base = materials[material]['SS_base']

    # Gate efficiency factors
    if gate_type == 'Pi-Gate':
        eta = 0.7  # Lower gate efficiency
        SS = SS_base * 1.1  # Higher subthreshold swing
        Vt = Vt_base + 0.05  # Slightly higher threshold voltage
        I_scale = 0.7  # Lower current due to poorer gate control
    elif gate_type == 'Omega-Gate':
        eta = 0.95  # Higher gate efficiency
        SS = SS_base * 0.9  # Lower subthreshold swing (better)
        Vt = Vt_base - 0.02  # Lower threshold voltage
        I_scale = 1.0  # Higher current due to better gate control
    else:
        raise ValueError("Invalid gate type")

    # Effective gate voltage accounting for gate efficiency
    Vgs_eff = eta * Vgs

    # Subthreshold current (exponential)
    k = 1 / (SS/1000 * np.log(10))  # Inverse subthreshold slope factor
    I_sub = 1e-12 * np.exp(k * (Vgs_eff - Vt) * 1000 / 26)  # Thermal voltage ~26mV

    # Above threshold current (saturation-like)
    I_sat = I_scale * 1e-4 * np.maximum(0, (Vgs_eff - Vt))**1.5

    # Total current (smooth transition)
    alpha = 1 / (1 + np.exp(-20 * (Vgs_eff - Vt)))  # Sigmoid transition
    Ids = (1 - alpha) * I_sub + alpha * I_sat

    return np.maximum(Ids, 1e-15)  # Minimum current floor

def generate_pi_omega_comparison():
    """Generate comparison plot for Pi-Gate vs Omega-Gate NWFETs"""

    Vgs = np.linspace(-0.5, 1.2, 200)

    # Calculate currents
    I_pi = calculate_current(Vgs, 'Pi-Gate')
    I_omega = calculate_current(Vgs, 'Omega-Gate')

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot curves
    ax.semilogy(Vgs, I_pi, 'b-', linewidth=2.5, label='Pi-Gate (η=0.7)')
    ax.semilogy(Vgs, I_omega, 'r-', linewidth=2.5, label='Omega-Gate (η=0.95)')

    # Add vertical lines for threshold voltages
    ax.axvline(x=0.35, color='b', linestyle='--', alpha=0.7, linewidth=1.5, label='Pi-Gate Vth ≈ 0.35V')
    ax.axvline(x=0.28, color='r', linestyle='--', alpha=0.7, linewidth=1.5, label='Omega-Gate Vth ≈ 0.28V')

    # Formatting
    ax.set_xlabel('Gate Voltage (V)', fontsize=14)
    ax.set_ylabel('Drain Current (A)', fontsize=14)
    ax.set_title('Pi-Gate vs Omega-Gate NWFET Transfer Characteristics\n(Si, Vds=0.5V, Tox=2nm)', fontsize=16, fontweight='bold')
    ax.grid(True, alpha=0.3)
    ax.legend(loc='lower right', fontsize=12)

    # Set axis limits
    ax.set_xlim(-0.5, 1.2)
    ax.set_ylim(1e-15, 1e-2)

    # Add annotations
    ax.annotate('Omega-Gate:\n• Lower Vth\n• Higher Ion\n• Better SS',
                xy=(0.8, 1e-4), xytext=(0.6, 1e-6),
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral", alpha=0.8),
                fontsize=11, ha='center')

    ax.annotate('Pi-Gate:\n• Higher Vth\n• Lower Ion\n• Poorer SS',
                xy=(0.4, 1e-8), xytext=(0.2, 1e-10),
                bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue", alpha=0.8),
                fontsize=11, ha='center')

    plt.tight_layout()

    # Save plot
    plt.savefig('pi_omega_comparison.png', dpi=600, bbox_inches='tight')
    plt.savefig('docs/pi_omega_comparison.png', dpi=600, bbox_inches='tight')
    print("Plot saved as 'pi_omega_comparison.png' in root and docs/ directories")

if __name__ == "__main__":
    generate_pi_omega_comparison()
