import matplotlib.pyplot as plt
import numpy as np

# Data
x_baseline = [0]  # Baseline only has one data point
x_start = np.arange(7) + 1  # START-X and START-M start from x=1
baseline = [89.8]  # Only one value for Baseline
start_x = [90.7, 90.8, 91.1, 91.6, 91.7, 91.3, 90.9]
start_m = [91.3, 91.4, 91.4, 91.7, 91.8, 91.4, 90.9]

# Bar width and positions
bar_width = 0.4  # Adjusted bar width

# Plot
plt.figure(figsize=(8, 6))

# Add Grid
plt.grid(axis='y', linestyle='--', alpha=0.7, zorder=0)  # Add grid with lower z-order

# Plot Baseline
plt.bar(x_baseline, baseline, color='tan', width=bar_width, edgecolor='black', label='Baseline', zorder=3)

# Plot START-X and START-M
plt.bar(x_start - bar_width/2, start_x, color='mediumturquoise', width=bar_width, edgecolor='black', label='START-X', zorder=3)
plt.bar(x_start + bar_width/2, start_m, color='lightsteelblue', width=bar_width, edgecolor='black', label='START-M', zorder=3)

# Labels and title
plt.xlabel('Ratio of Perturbed Tokens', fontsize=16, fontweight='bold')
plt.ylabel('Accuracy (%)', fontsize=16, fontweight='bold')

# Modified x-axis ticks
custom_xticks = ['0%', '15%', '30%', '45%', '60%', '75%', '90%', '100%']  # Custom tick labels
plt.xticks(np.concatenate(([0], x_start)), custom_xticks, fontsize=14)  # Combine Baseline and START ticks

# Y-axis limits and ticks
plt.ylim(89.5, 92.0)  # Set y-axis limits
plt.yticks(np.arange(89.5, 92.5, 0.5), fontsize=14)  # Adjust y-axis ticks and spacing

# Legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fontsize=15, frameon=True)  # Set legend to 1 row, 3 columns

# Show plot
plt.tight_layout()
plt.savefig('Ablation_P_Token.png')
