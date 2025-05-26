import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Forward Belief', 'Forward Action', 'Backward Belief']
complete_method = [0.92, 0.7, 0.71]  # Data for complete method
without_constraints = [0.9, 0.6, 0.62]  # Data for w/o constraints

# Bar width and positions
x = np.arange(len(categories))
bar_width = 0.2

# Plot
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size for better clarity

# Colors
complete_method_color = '#1f77b4'  # Updated to a distinct blue
without_constraints_color = '#87CEEB'  # Updated to a softer light blue

# Bars
ax.bar(
    x - bar_width / 2, complete_method, bar_width, 
    label='Complete Method', color=complete_method_color, linewidth=0.8
)
ax.bar(
    x + bar_width / 2, without_constraints, bar_width, 
    label='W/O Constraints', color=without_constraints_color, linewidth=0.8
)

# Labels and Title
ax.set_ylabel(r'TB $\times$ FB', fontsize=16, fontweight='bold', labelpad=10)
ax.set_ylim(0.5, 1.0)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14, fontweight='bold')

# Increase y-tick size
ax.tick_params(axis='y', labelsize=14)  # Adjusted y-tick label size

# Add legend
ax.legend(fontsize=14, frameon=True, loc='upper right')

# Layout
plt.tight_layout()

# Save and display the plot
plt.savefig('Analyses_of_Constraints_crop.png')