import numpy as np
import matplotlib.pyplot as plt

# Variables
categories = [ 'humanities', 'extraction','coding', 'writing', 'stem', 'roleplay', 'reasoning', 'math',]

values = np.array([
    [17.7, 5.5, 2, 14.5, 14.5, 13.6, 5.3, 2.5],  # Multi-task learning
    [17.8,11.5, 1.5, 16, 13, 13.6, 4.7, 2],   # Sequential Training
    [17.9, 8, 2.5, 16, 14.4, 12, 6.7, 2.3],   # Mixed Sequential Training
    [18, 7, 2.5, 15.7, 14.5, 13.8, 7, 3.3]   # DMT(k=1/256)
])

# Repeat the first value to close the circle
values = np.concatenate((values, values[:, [0]]), axis=1)

# The number of variables
num_vars = len(categories)

# Compute angle such that plot is formed in a circle
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# Create a polar subplot
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Plot each individual group
colors = ['b', 'orange', 'green', 'r']
labels = ['Multi-task learning', 'Sequential Training', 'Mixed Sequential Training', 'DMT(k=1/256)']

for idx, color in enumerate(colors):
    ax.fill(angles, values[idx], color=color, alpha=0.25)
    ax.plot(angles, values[idx], color=color, linewidth=1, label=labels[idx])

# Draw a fine-grid circle and control yticks manually
# Define the positions of the ticks manually
yticks_positions = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()


# Set the radial ticks at these positions
ax.set_yticks(np.arange(-5, 16, 5))  # Positions for y-ticks
yticklabels = ax.set_yticklabels([], color="grey", size=7)  # Customize tick labels

ax.set_xticks(angles[:-1])  # Positions of the x-ticks
ax.set_xticklabels(categories, size=10)  # Set category labels

# Manually control rotation of the y-tick labels (radial labels)
yticks_values = np.arange(0, 16, 5)  # Values to plot on y-ticks
yticks_angles = np.linspace(0, 2 * np.pi, len(yticks_values), endpoint=False)  # Get corresponding angles

# Loop through each tick to place the label with rotation
for idx, value in enumerate(yticks_values):
    # Place the text at the 90-degree position (top of the plot)
    if idx!=0:
        ax.text(np.pi / 2 - 0.04, value+0.2, str(value), color="grey", size=9,
                horizontalalignment='center', verticalalignment='center', rotation=0)


# Add title, grid, and legend
plt.title('MT-Bench Scores (13B)', size=13, pad=22,fontweight='bold')
ax.grid(True, linestyle='--', linewidth=0.5, color='grey', alpha=0.7)
plt.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))

# Save and show the plot
plt.tight_layout()
plt.savefig("mt13b.png")
