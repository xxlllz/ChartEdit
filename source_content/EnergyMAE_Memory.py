import matplotlib.pyplot as plt
import numpy as np

# Data (updated to match the provided image)
x = [1.1, 1.2, 2.3, 1.6, 5.3, 2.3, 6.1]
y = [228, 217, 213, 232, 230, 252, 243]
sizes = np.array([83, 146, 317, 31, 153, 216, 200]) * 10
labels = ['83M', '146M', '317M', '31M', '153M', '216M', '200M']  # Bubble labels, updated
colors = ['violet', 'violet', 'violet', 'lime', 'lime', 'deepskyblue', 'orange']

# Legend labels corresponding to colors
legend_labels = ['GemNet-OC', 'eSCN', 'EScAIP', 'EquiformerV2']

# Corresponding unique colors for the legend
unique_colors = ['deepskyblue', 'orange', 'violet', 'lime']

# Create plot
fig, ax = plt.subplots(figsize=(8, 6))
scatter = ax.scatter(x, y, s=sizes, c=colors, alpha=0.6, edgecolors=colors, linewidth=2, zorder=3)

# Adding labels next to each bubble (adjusting vertical offset)
for i, txt in enumerate(labels):
    ax.annotate(txt, (x[i], y[i]), xytext=(0, sizes[i]/100), fontsize=16, ha='center', va='bottom', textcoords='offset points', zorder=4)

# Drawing connecting lines (updated)
ax.plot([1.1, 1.2, 2.3], [228, 217, 213], 'k--', alpha=0.3, zorder=1)
ax.plot([1.6, 5.3], [232, 230], 'k--', alpha=0.3, zorder=1)

# Legend
legend_scatters = [
    plt.Line2D([0], [0], marker='o', color='w', label=label,
               markerfacecolor=color, markersize=10, alpha=0.7) 
    for label, color in zip(legend_labels, unique_colors)
]
plt.legend(handles=legend_scatters, loc='upper right', bbox_to_anchor=(0.8, 1), scatterpoints=1, frameon=True, fontsize=16)

# Axes labels
plt.xlabel('Inference Memory (GB/Sample)', fontsize=20)
plt.ylabel('Energy MAE (meV)', fontsize=20)

plt.xlim(0, 7)
plt.ylim(205, 260)

# Customize ticks: Remove tick marks
ax.tick_params(axis='x', labelsize=16, bottom=False)  # Remove x ticks
ax.tick_params(axis='y', labelsize=16, left=False)  # Remove y ticks

# Set borders to gray
for spine in ax.spines.values():
    spine.set_color('gray')
    spine.set_linewidth(1)

# Grid
plt.grid(True, which='both', linestyle='-', linewidth=0.5, color='gray', alpha=0.7, zorder=0)

# Save and display plot
plt.tight_layout()
plt.savefig('EnergyMAE_Memory.png')
