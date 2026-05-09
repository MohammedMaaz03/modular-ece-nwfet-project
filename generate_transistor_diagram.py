import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Arc, Circle, Arrow

# Create figure with 2x2 subplots: 2D and 3D views for Pi and Omega
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Pi-Gate and Omega-Gate NWFET Structures with Current Flow', fontsize=16, fontweight='bold')

# Colors
gate_color_pi = 'skyblue'
gate_color_omega = 'lightgreen'
wire_color = 'gray'
current_color = 'red'
label_color = 'black'

# 2D Pi-Gate
ax1 = axes[0, 0]
ax1.set_title('2D Pi-Gate (η ≈ 0.82)', fontsize=14)
ax1.axis('equal')
ax1.axis('off')

# Nanowire cross-section (circle)
wire = Circle((0, 0), 0.5, color=wire_color, fill=True)
ax1.add_patch(wire)

# Pi-Gate: partial arc (82% wrap)
pi_gate = Arc((0, 0), 1.5, 1.5, theta1=0, theta2=295, color=gate_color_pi, linewidth=3)
ax1.add_patch(pi_gate)

# Labels
ax1.text(0, 0, 'Si NW', ha='center', va='center', color='white', fontweight='bold')
ax1.text(0, 1.2, 'Gate', ha='center', color=label_color)
ax1.text(-0.7, -0.7, 'S', ha='center', va='center', fontsize=12, color=label_color)
ax1.text(0.7, -0.7, 'D', ha='center', va='center', fontsize=12, color=label_color)

# Current flow arrows
arrow1 = Arrow(-0.5, 0, 1, 0, width=0.1, color=current_color)
ax1.add_patch(arrow1)
ax1.text(0, -0.3, 'Current Flow', ha='center', color=current_color, fontsize=10)

# 2D Omega-Gate
ax2 = axes[0, 1]
ax2.set_title('2D Omega-Gate (η ≈ 0.98)', fontsize=14)
ax2.axis('equal')
ax2.axis('off')

# Nanowire cross-section
wire2 = Circle((0, 0), 0.5, color=wire_color, fill=True)
ax2.add_patch(wire2)

# Omega-Gate: nearly full arc (98% wrap)
omega_gate = Arc((0, 0), 1.5, 1.5, theta1=0, theta2=352, color=gate_color_omega, linewidth=3)
ax2.add_patch(omega_gate)

# Labels
ax2.text(0, 0, 'Si NW', ha='center', va='center', color='white', fontweight='bold')
ax2.text(0, 1.2, 'Gate', ha='center', color=label_color)
ax2.text(-0.7, -0.7, 'S', ha='center', va='center', fontsize=12, color=label_color)
ax2.text(0.7, -0.7, 'D', ha='center', va='center', fontsize=12, color=label_color)

# Current flow arrows
arrow2 = Arrow(-0.5, 0, 1, 0, width=0.1, color=current_color)
ax2.add_patch(arrow2)
ax2.text(0, -0.3, 'Current Flow', ha='center', color=current_color, fontsize=10)

# 3D Pi-Gate (simplified perspective)
ax3 = axes[1, 0]
ax3.set_title('3D Pi-Gate (η ≈ 0.82)', fontsize=14)
ax3.axis('equal')
ax3.axis('off')

# Nanowire as ellipse for 3D effect
wire3 = patches.Ellipse((0, 0), 1, 0.5, color=wire_color, fill=True)
ax3.add_patch(wire3)

# Pi-Gate partial wrap in 3D (arcs)
pi_gate_3d = Arc((0, 0), 1.8, 1.2, theta1=0, theta2=295, color=gate_color_pi, linewidth=3)
ax3.add_patch(pi_gate_3d)

# Labels
ax3.text(0, 0, 'Si NW', ha='center', va='center', color='white', fontweight='bold')
ax3.text(0, 0.8, 'Gate', ha='center', color=label_color)
ax3.text(-0.5, -0.3, 'S', ha='center', va='center', fontsize=12, color=label_color)
ax3.text(0.5, -0.3, 'D', ha='center', va='center', fontsize=12, color=label_color)

# Current flow arrows (curved for 3D)
arrow3 = Arrow(-0.4, 0, 0.8, 0, width=0.1, color=current_color)
ax3.add_patch(arrow3)
ax3.text(0, -0.5, 'Current Flow', ha='center', color=current_color, fontsize=10)

# 3D Omega-Gate (simplified perspective)
ax4 = axes[1, 1]
ax4.set_title('3D Omega-Gate (η ≈ 0.98)', fontsize=14)
ax4.axis('equal')
ax4.axis('off')

# Nanowire as ellipse
wire4 = patches.Ellipse((0, 0), 1, 0.5, color=wire_color, fill=True)
ax4.add_patch(wire4)

# Omega-Gate full wrap in 3D
omega_gate_3d = Arc((0, 0), 1.8, 1.2, theta1=0, theta2=352, color=gate_color_omega, linewidth=3)
ax4.add_patch(omega_gate_3d)

# Labels
ax4.text(0, 0, 'Si NW', ha='center', va='center', color='white', fontweight='bold')
ax4.text(0, 0.8, 'Gate', ha='center', color=label_color)
ax4.text(-0.5, -0.3, 'S', ha='center', va='center', fontsize=12, color=label_color)
ax4.text(0.5, -0.3, 'D', ha='center', va='center', fontsize=12, color=label_color)

# Current flow arrows
arrow4 = Arrow(-0.4, 0, 0.8, 0, width=0.1, color=current_color)
ax4.add_patch(arrow4)
ax4.text(0, -0.5, 'Current Flow', ha='center', color=current_color, fontsize=10)

plt.tight_layout()
plt.savefig('nwfet_structures_diagram.png', dpi=300, bbox_inches='tight')
plt.show()
