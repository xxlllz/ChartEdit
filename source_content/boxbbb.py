import matplotlib.pyplot as plt
import numpy as np

# Data with more complex and modified values
stats = [
    dict(med=-0.5, q1=-1.5, q3=0.5, whislo=-3, whishi=2.5, fliers=[-5, -4, 4, 5], label='A'),
    dict(med=0, q1=-2.5, q3=2.5, whislo=-4, whishi=4, fliers=[-6, 6], label='B'),
    dict(med=1.5, q1=-1, q3=3, whislo=-5, whishi=5, fliers=[-7, 7], label='C'),
    dict(med=2, q1=0, q3=4, whislo=-6, whishi=6, fliers=[-8, 8], label='D'),
    dict(med=-1.2, q1=-3, q3=0, whislo=-4.5, whishi=3.5, fliers=[-9, 9], label='E')
]

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Custom colors for the boxes and whiskers
box_colors = ['#c0392b', '#8e44ad', '#16a085', '#f39c12', '#2980b9']  # Uncommon colors
whisker_colors = ['#f39c12', '#2980b9', '#c0392b', '#8e44ad', '#16a085']

# Custom properties for the boxplot elements
boxprops = {'facecolor': 'lightcoral', 'edgecolor': 'black', 'linewidth': 2}
flierprops = {'marker': 'o', 'markerfacecolor': 'darkred', 'markeredgewidth': 2, 'markersize': 8}

# Plot the boxplot with custom colors and properties
bp = ax.bxp(stats, patch_artist=True, boxprops=boxprops, whiskerprops={'color': 'black', 'linewidth': 1.5},
            capprops={'color': 'black', 'linewidth': 2}, flierprops=flierprops)

# Customizing box colors
for i, patch in enumerate(bp['boxes']):
    patch.set_facecolor(box_colors[i % len(box_colors)])

# Set custom x-ticks and y-ticks sizes
ax.tick_params(axis='x', labelsize=14)  # Increase font size for x-axis ticks
ax.tick_params(axis='y', labelsize=14)  # Increase font size for y-axis ticks

# Remove x-ticks
ax.set_xticks([])  # Hide x-ticks

# Increase legend size and move it to the bottom, with 6 columns
ax.legend([bp['boxes'][i] for i in range(len(bp['boxes']))], [s['label'] for s in stats],
          fontsize=15, loc='upper center', ncol=5,
          bbox_to_anchor=(0.5, 0))  # Adjust legend position to bottom center

# Adding grid for better visibility
ax.grid(True, which='both', linestyle='--', color='gray', alpha=0.5)

# Adjusting the layout
plt.tight_layout()

# Show the plot
plt.savefig('boxbbb.png')