import matplotlib.pyplot as plt
import numpy as np

# Data
methods = ['GaitSet', 'MTSGait', 'GaitBase', 'DyGait', 'ParsingGait', 'XGait (Ours)']
accuracies = [36.7, 48.7, 64.6, 66.3, 76.2, 80.5]
colors = ['#1f77b4', '#aec7e8', '#17becf', '#bcbd22', '#c49c94', '#e377c2']

# Create bar chart
fig, ax = plt.subplots(figsize=(9, 6))  # Adjust figure size
bar_positions = np.arange(len(methods))
bars = plt.bar(bar_positions, accuracies, color=colors, zorder=3)  # Bars are on top of the gridlines

# Add horizontal line at 80
ty_max = 80
plt.axhline(y=ty_max, color='red', linewidth=1.5, linestyle='-', label='Baseline (80%)', zorder=3)

# Annotate bars with values
for bar, accuracy in zip(bars, accuracies):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, f'{accuracy:.1f}', 
            ha='center', va='bottom', fontsize=15, fontweight='bold')  # Bold text for annotations

# Customize the axes labels, title, and ticks
plt.xlabel('Gait3D', fontsize=20, fontweight='bold')  # Bold xlabel
plt.ylabel('Rank-1 Accuracy (%)', fontsize=20, fontweight='bold')  # Bold ylabel
plt.xticks([])  # Remove x-axis ticks
plt.yticks([35, 45, 55, 65, 75, 85], fontsize=18, fontweight='bold')  # Increase y-axis tick size and bold

# Customize the legend to represent methods
handles = [plt.Rectangle((0, 0), 1, 1, color=color) for color in colors]
labels = methods
ax.legend(handles, labels, loc='upper left', bbox_to_anchor=(0., 0.85), fontsize=16, 
          frameon=False, title_fontsize=13)  # Move legend down and bold text

# Set limits
ty_min, y_lim_max = 35, 85
plt.ylim(ty_min, y_lim_max)

# Adjust grid
plt.grid(True, axis='y', linestyle='-', alpha=0.7, zorder=1)  # Gridlines under bars

# Save the plot
plt.tight_layout()  # Ensure everything fits within the figure
plt.savefig('fig_one_cut.png', dpi=300)