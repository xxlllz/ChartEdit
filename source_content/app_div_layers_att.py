import matplotlib.pyplot as plt
import numpy as np

# Sample data
np.random.seed(10)
data1 = np.random.normal(20, 2, 100)
data2 = 10 * np.random.beta(2, 5, 100) + 24
data3 = np.random.exponential(2, 100) + 17

data = [data1, data2, data3]

# Create figure and axis
fig, ax = plt.subplots(figsize=(8, 6))

# Colors
colors = ['#ffa07a', '#cd5c5c', '#87ceeb']  # Original colors
darker_colors = ['#ff7f50', '#b22222', '#4682b4']  # Darker shades

# Create individual boxplots
for i in range(len(data)):
    box = ax.boxplot(data[i], patch_artist=True, notch=False, vert=True, widths=0.5,
                     positions=[i + 1],  # Position each boxplot separately
                     whiskerprops=dict(linestyle='-', linewidth=2, color=darker_colors[i]),
                     capprops=dict(linewidth=2, color=darker_colors[i]),  # Set cap color
                     medianprops=dict(linestyle='-', linewidth=2, color='black'),  # Set median line color
                     meanprops=dict(marker='s', markerfacecolor='white',
                                    markeredgecolor='black', markersize=10),
                     showmeans=True)

    # Set face and edge colors
    for patch in box['boxes']:
        patch.set_facecolor(colors[i])
        patch.set_edgecolor(darker_colors[i])  # Set edge color to a darker shade


# Set titles and labels
ax.set_xticklabels(['First Half', 'Second Half', 'All'])
ax.set_ylabel('Attribute Score', fontsize=22)

# Show grid
ax.yaxis.grid(True)

# Set limits and modify tick_params for appearance
ax.set_ylim([14, 32])
ax.tick_params(axis='x', labelsize=18)  # Increase font size for x ticks
ax.tick_params(axis='y', labelsize=18)  # Increase font size for y ticks
ax.set_yticks(np.arange(14, 33, 2))

plt.tight_layout()
# Show plot
plt.savefig('app_div_layers_att.png')
plt.show()