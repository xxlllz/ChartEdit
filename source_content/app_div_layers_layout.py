import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(10)
data1 = np.random.normal(loc=15, scale=4, size=100)
data2 = 10 * np.random.beta(2, 5, size=100) + 15
data3 = np.random.exponential(scale=4, size=100) + 10 # Exponential distribution


data = [data1, data2, data3]

# Colors
colors = ['#fd8e58', '#c87979', '#84d2e7']
darker_colors = ['#e8743b', '#a85252', '#6dbbd7']  # Darker shades for edges

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Create individual boxplots
for i in range(len(data)):
    box = ax.boxplot(data[i], patch_artist=True, notch=False, vert=True, widths=0.5,
                     positions=[i + 1],  # Position each boxplot separately
                     whiskerprops=dict(linestyle='-', linewidth=2, color=darker_colors[i]),
                     capprops=dict(linewidth=2, color=darker_colors[i]),  # Set cap color
                     medianprops=dict(linestyle='-', linewidth=2, color='white'),  # Set median line color
                     meanprops=dict(marker='s', markerfacecolor='white',
                                    markeredgecolor='black', markersize=10),
                     showmeans=True)

    # Set face and edge colors
    for patch in box['boxes']:
        patch.set_facecolor(colors[i])
        patch.set_edgecolor(darker_colors[i])  # Set edge color to a darker shade

# Set titles and labels
plt.xticks([1, 2, 3], ['First Half', 'Second Half', 'All'], fontsize=14)
plt.yticks(fontsize=14)
ax.set_ylabel('Layout Score', fontsize=22)

# Add grid lines
ax.yaxis.grid(True, linestyle='--', alpha=0.6)

# Set limits and modify tick_params for appearance
plt.ylim(0, 28)
ax.tick_params(axis='x', labelsize=18)  # Increase font size for x ticks
ax.tick_params(axis='y', labelsize=18)  # Increase font size for y ticks
ax.xaxis.set_tick_params(length=0)  # Remove x-axis ticks

plt.tight_layout()
# Save plot
plt.savefig('app_div_layers_layout.png')
