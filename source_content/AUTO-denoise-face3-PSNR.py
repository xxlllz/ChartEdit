import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [2.2, 1.7, 1.4, 1.0, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.0]
y = [31.02, 31.18, 31.05, 31.08, 30.97, 31.04, 31.02, 31.1, 31.02, 30.98, 30.2]

# Create the plot
plt.figure(figsize=(8, 6))
plt.axhline(y=31.02, color='r', linestyle='--', zorder=1, linewidth=1.5)  # Lower zorder for the line
plt.plot(x, y, label='Subnetwork', linewidth=3, zorder=2)  # Higher zorder for the line

# Highlight specific points with larger markers
plt.scatter([x[0], x[-3]], [y[0], y[-3]], color='yellow', s=800, marker='*', label='Matching Subnetwork', zorder=4)  # Higher zorder for scatter
plt.scatter([x[0]], [y[0]], color='lightgreen', s=800, marker='*', label='Dense Model LIP', zorder=4)  # Higher zorder for scatter

# Customize the plot
plt.xlabel('Parameter Count (M)', fontsize=18)
plt.ylabel('PSNR', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.xlim(2.3, 0)
plt.ylim(30.4, 31.5)
plt.legend(loc='lower left', fontsize=15, labelspacing=1.2)  # Increase legend spacing
plt.grid(True, zorder=0, linestyle='-', alpha=0.6)  # Lowest zorder for the grid

# # Show the plot
# plt.tight_layout()
plt.savefig('AUTO-denoise-face3-PSNR.png')
