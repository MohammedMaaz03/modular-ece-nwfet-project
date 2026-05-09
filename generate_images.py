import matplotlib.pyplot as plt
import numpy as np

# Table 2: Comparative Performance Metrics
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

table_data = [
    ['Material', 'Gate Type', 'Vth (V)', 'Ion (µA)', 'Ioff (nA)', 'SS (mV/dec)', 'Ion/Ioff Ratio'],
    ['SiO2', 'Pi-Gate', '0.45', '120', '50', '75', '2.4e6'],
    ['SiO2', 'Omega-Gate', '0.42', '145', '30', '65', '4.8e6'],
    ['Al2O3', 'Pi-Gate', '0.40', '135', '40', '70', '3.4e6'],
    ['Al2O3', 'Omega-Gate', '0.38', '160', '25', '60', '6.4e6'],
    ['HfO2', 'Pi-Gate', '0.35', '150', '35', '68', '4.3e6'],
    ['HfO2', 'Omega-Gate', '0.33', '180', '20', '58', '9.0e6'],
    ['ZrO2', 'Pi-Gate', '0.38', '140', '38', '72', '3.7e6'],
    ['ZrO2', 'Omega-Gate', '0.36', '165', '22', '62', '7.5e6'],
    ['La2O3', 'Pi-Gate', '0.32', '155', '32', '66', '4.8e6'],
    ['La2O3', 'Omega-Gate', '0.30', '185', '18', '56', '10.3e6']
]

table = ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1.2, 1.2)

plt.title('Table 2: Comparative Performance Metrics for Pi-Gate and Omega-Gate NWFETs', fontsize=14, pad=20)
plt.savefig('docs/table2.png', bbox_inches='tight', dpi=300)
plt.close()

# Table 3: Literature Findings Summary
fig, ax = plt.subplots(figsize=(16, 8))
ax.axis('off')

table_data = [
    ['Research Theme', 'Key Findings', 'Implications for NWFET Design'],
    ['Gate Architecture', 'Omega-Gate provides superior\nelectrostatic control with\nη ≈ 0.98 vs. Pi-Gate η ≈ 0.82', 'Prefer Omega-Gate for\nhigh-performance applications'],
    ['High-K Dielectrics', 'HfO2, ZrO2, La2O3 offer better\ncapacitance than SiO2 but\nintroduce interface challenges', 'Material selection must balance\npermittivity with interface quality'],
    ['Temperature Effects', 'Cryogenic operation improves\nmobility; high temperatures\nincrease leakage', 'Design for specific temperature\nranges based on application needs'],
    ['EIS Studies', 'Reveals dielectric relaxation\nmechanisms and trap densities', 'Use for reliability assessment\nand material optimization'],
    ['Fabrication Challenges', 'Complex 3D structures require\nadvanced lithography and\ndeposition', 'Process innovation needed for\nmanufacturable NWFETs'],
    ['Performance Benchmarking', 'NWFETs outperform FinFETs in\nelectrostatic control but lag in\nparasitic effects', 'Focus on reducing parasitics for\ncompetitive performance']
]

table = ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.4, 1.4)

plt.title('Table 3: Summary of Key Literature Findings on NWFET Research Themes', fontsize=14, pad=20)
plt.savefig('docs/table3.png', bbox_inches='tight', dpi=300)
plt.close()

# Table 4: Omega-Gate Advantages Summary
fig, ax = plt.subplots(figsize=(14, 8))
ax.axis('off')

table_data = [
    ['Evaluation Criterion', 'Omega-Gate Advantage', 'Typical Improvement', 'Key Contributing Factors'],
    ['Electrostatic Control', 'Superior gate efficiency', 'η = 0.98 vs. 0.82', 'Enhanced wrap-around geometry'],
    ['Current Drive', 'Higher Ion', '30-40% increase', 'Better channel control, reduced scattering'],
    ['Subthreshold Characteristics', 'Lower SS', '10-15 mV/dec reduction', 'Improved gate coupling'],
    ['Temperature Stability', 'Better thermal performance', '20-30% less degradation', 'Enhanced gate isolation'],
    ['Dielectric Quality', 'Lower interface traps', '25-35% reduction', 'Superior gate uniformity'],
    ['Scaling Potential', 'Extended sub-10 nm operation', '2-3 nm smaller nodes', 'Improved short-channel control'],
    ['Reliability', 'Better hot-carrier immunity', '40-50% longer lifetime', 'Reduced electric field concentration'],
    ['Material Compatibility', 'Broader optimal range', 'More material options', 'Less sensitivity to interface quality']
]

table = ax.table(cellText=table_data, colLabels=None, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1.2, 1.2)

plt.title('Table 4: Summary of Omega-Gate Advantages over Pi-Gate NWFETs', fontsize=14, pad=20)
plt.savefig('docs/table4.png', bbox_inches='tight', dpi=300)
plt.close()

# Flow Chart 1: Thesis Structure
fig, ax = plt.subplots(figsize=(12, 14))
ax.axis('off')

# Draw rectangles
rects = [
    plt.Rectangle((0.4, 0.92), 0.2, 0.06, fill=True, color='lightblue', ec='black'),
    plt.Rectangle((0.4, 0.81), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.4, 0.70), 0.2, 0.06, fill=True, color='lightyellow', ec='black'),
    plt.Rectangle((0.15, 0.52), 0.2, 0.06, fill=True, color='lightcoral', ec='black'),
    plt.Rectangle((0.4, 0.52), 0.2, 0.06, fill=True, color='lightcoral', ec='black'),
    plt.Rectangle((0.65, 0.52), 0.2, 0.06, fill=True, color='lightcoral', ec='black'),
    plt.Rectangle((0.4, 0.37), 0.2, 0.06, fill=True, color='lightpink', ec='black'),
    plt.Rectangle((0.4, 0.26), 0.2, 0.06, fill=True, color='lightcyan', ec='black'),
    plt.Rectangle((0.4, 0.15), 0.2, 0.06, fill=True, color='lightgray', ec='black')
]

for rect in rects:
    ax.add_patch(rect)

# Add text
texts = [
    'Introduction',
    'Literature Review',
    'Materials and Methods',
    'Pi vs Omega Comparison',
    'Temperature Effects',
    'EIS Analysis',
    'Results and Discussion',
    'Conclusion',
    'Future Scope'
]

y_positions = [0.935, 0.835, 0.735, 0.55, 0.55, 0.55, 0.40, 0.29, 0.18]
x_positions = [0.5, 0.5, 0.5, 0.25, 0.5, 0.75, 0.5, 0.5, 0.5]

for text, x, y in zip(texts, x_positions, y_positions):
    ax.text(x, y, text, ha='center', va='center', fontsize=8)

# Draw arrows
ax.arrow(0.5, 0.875, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.755, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.635, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.575, -0.25, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.575, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.575, 0.25, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.425, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.305, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.185, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')

plt.title('Figure 1.1: Overall Thesis Structure Flow Chart', fontsize=14, pad=20)
plt.savefig('docs/flowchart1.png', bbox_inches='tight', dpi=300)
plt.close()

# Flow Chart 2: Simulation Methodology
fig, ax = plt.subplots(figsize=(12, 12))
ax.axis('off')

# Rectangles
rects = [
    plt.Rectangle((0.4, 0.9), 0.2, 0.06, fill=True, color='lightblue', ec='black'),
    plt.Rectangle((0.15, 0.7), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.4, 0.7), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.65, 0.7), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.4, 0.5), 0.2, 0.06, fill=True, color='lightyellow', ec='black'),
    plt.Rectangle((0.4, 0.35), 0.2, 0.06, fill=True, color='lightcoral', ec='black'),
    plt.Rectangle((0.4, 0.2), 0.2, 0.06, fill=True, color='lightpink', ec='black')
]

for rect in rects:
    ax.add_patch(rect)

# Texts
texts = [
    'Input Parameters',
    'C-V Models',
    'I-V Models',
    'EIS Models',
    'Numerical Computation',
    'Validation',
    'Output Results'
]

y_positions = [0.93, 0.73, 0.73, 0.73, 0.53, 0.38, 0.23]
x_positions = [0.5, 0.25, 0.5, 0.75, 0.5, 0.5, 0.5]

for text, x, y in zip(texts, x_positions, y_positions):
    ax.text(x, y, text, ha='center', va='center', fontsize=8)

# Arrows
ax.arrow(0.5, 0.875, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.675, -0.25, 0, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.675, 0, 0, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.675, 0.25, 0, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.25, 0.76, 0, 0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.76, 0, 0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.75, 0.76, 0, 0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.475, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.325, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.175, 0, -0.05, head_width=0.01, head_length=0.01, fc='black', ec='black')

plt.title('Figure 3.1: Simulation Framework Flow Chart', fontsize=14, pad=20)
plt.savefig('docs/flowchart2.png', bbox_inches='tight', dpi=300)
plt.close()

# Flow Chart 3: Results Analysis Process
fig, ax = plt.subplots(figsize=(12, 12))
ax.axis('off')

# Rectangles
rects = [
    plt.Rectangle((0.4, 0.9), 0.2, 0.06, fill=True, color='lightblue', ec='black'),
    plt.Rectangle((0.15, 0.7), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.4, 0.7), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.65, 0.7), 0.2, 0.06, fill=True, color='lightgreen', ec='black'),
    plt.Rectangle((0.4, 0.5), 0.2, 0.06, fill=True, color='lightyellow', ec='black'),
    plt.Rectangle((0.4, 0.35), 0.2, 0.06, fill=True, color='lightcoral', ec='black'),
    plt.Rectangle((0.4, 0.2), 0.2, 0.06, fill=True, color='lightpink', ec='black')
]

for rect in rects:
    ax.add_patch(rect)

# Texts
texts = [
    'Simulation Data',
    'Performance Metrics',
    'Material Comparison',
    'Temperature Analysis',
    'EIS Insights',
    'Key Findings',
    'Conclusions'
]

y_positions = [0.93, 0.73, 0.73, 0.73, 0.73, 0.53, 0.38]
x_positions = [0.5, 0.275, 0.525, 0.775, 0.525, 0.5, 0.5]

for text, x, y in zip(texts, x_positions, y_positions):
    ax.text(x, y, text, ha='center', va='center', fontsize=8)

# Arrows
ax.arrow(0.5, 0.875, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.675, -0.25, 0, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.675, 0, 0, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.675, 0.25, 0, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.25, 0.76, 0, 0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.76, 0, 0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.75, 0.76, 0, 0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.475, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')
ax.arrow(0.5, 0.325, 0, -0.06, head_width=0.01, head_length=0.01, fc='black', ec='black')

plt.title('Figure 8.1: Results Analysis Process Flow Chart', fontsize=14, pad=20)
plt.savefig('docs/flowchart3.png', bbox_inches='tight', dpi=300)
plt.close()

print("Images generated and saved in docs/ folder.")
