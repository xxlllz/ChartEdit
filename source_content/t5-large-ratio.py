import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D  # Import Line2D for custom legend

# Sample data
x = np.array([0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6])
y1 = np.array([80.3, 80.3, 79.5, 78.7, 78, 77.6, 75.8, 74.7, 74.9, 74.7, 74.8, 74.5])  # TIES-Merging
y2 = np.array([82.1, 81.1, 80.8, 80.3, 79.8, 78.8, 77, 75.2, 75.4, 75.2, 74.6, 74.7])  # PCB-Merging (ours)

plt.figure(figsize=(24, 12))

# Plotting TIES-Merging with markers
plt.plot(x, y1, 'b-o', label='TIES-Merging', linewidth=6, markersize=28, linestyle='-')

# Plotting PCB-Merging (ours) with markers
plt.plot(x, y2, 'r-s', label='PCB-Merging (ours)', linewidth=6, markersize=28, linestyle='-')

# Title and labels
plt.title('T5-large', fontsize=60, fontweight='bold')
plt.xlabel('various $r$ with the optimal $\lambda$', fontsize=60)
plt.ylabel('Avg. Performance', fontsize=60)

# Custom legend with only lines (no markers)
line1 = Line2D([0], [0], color='b', lw=6)  # Blue line for legend
line2 = Line2D([0], [0], color='r', lw=6)  # Red line for legend
plt.legend(handles=[line1, line2], labels=['TIES-Merging', 'PCB-Merging (ours)'], fontsize=50, loc='upper right', frameon=True, handletextpad=1)

# Adjusting the ticks
plt.ylim(73.6, 82.5)  # Ensure the lower limit is below 74 to include grid lines at 74

plt.xticks(fontsize=60)
plt.yticks(np.arange(74, 82.1, 2), fontsize=60, family='Microsoft YaHei')
plt.tick_params(axis='both', which='major', length=10, width=3, direction='out', grid_alpha=0.5)

# Display grid
plt.grid(axis='y')  # Show grid lines only for y-axis (vertical grid lines)

# Hide the top and right spines (top and right lines of the plot)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Save the figure
plt.savefig('t5-large-ratio.png', bbox_inches='tight')
