import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Data
labels = np.array(['Clean', 'Slight', 'Medium', 'Heavy', 'Union'])
first_turn = np.array([40, 36, 46, 23, 32])
third_turn = np.array([72, 62, 64, 50, 41])

# Calculate angles
num_vars = len(labels)
angles = np.linspace(0.5 * np.pi, 2.5 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]  # Repeat the first angle to close the pentagon
# Extend data to close the shape
first_turn = np.concatenate((first_turn, [first_turn[0]]))
third_turn = np.concatenate((third_turn, [third_turn[0]]))

# Create the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')  # Ensure equal aspect ratio

# Draw the pentagon background and add data labels
levels = np.linspace(0, 100, 6)  # Levels for the pentagon (0, 20, 40, 60, 80, 100)
for level in levels:
    level_points = [(level * np.cos(angle), level * np.sin(angle)) for angle in angles]
    polygon = plt.Polygon(level_points, closed=True, edgecolor='gray', linestyle='--', linewidth=0.5, fill=None)
    ax.add_patch(polygon)
    # Add data labels for each level
    ax.text(-10, level, f"{int(level)}", ha='center', va='center', fontsize=12, color='black')  # Above center

# Draw the axes and labels
for i, angle in enumerate(angles[:-1]):
    x = 100 * np.cos(angle)
    y = 100 * np.sin(angle)
    ax.plot([0, x], [0, y], color='gray', linestyle='--', linewidth=0.5)
    label_x = 112 * np.cos(angle)  # Adjusted distance for labels
    label_y = 112 * np.sin(angle)  # Adjusted distance for labels
    ax.text(label_x, label_y, labels[i], ha='center', va='center', fontsize=12, fontweight='bold')

# Plot data
first_points = [(r * np.cos(angle), r * np.sin(angle)) for r, angle in zip(first_turn, angles)]
third_points = [(r * np.cos(angle), r * np.sin(angle)) for r, angle in zip(third_turn, angles)]

# Fill the areas
ax.fill(*zip(*first_points), color='limegreen', alpha=0.3, label='First Turn')
ax.fill(*zip(*third_points), color='royalblue', alpha=0.2, label='Third Turn')

# Draw the data lines
ax.plot(*zip(*first_points), color='limegreen', alpha=0.4, linewidth=2)
ax.plot(*zip(*third_points), color='royalblue', alpha=0.25, linewidth=2)

# Style adjustments
ax.set_xlim(-120, 120)
ax.set_ylim(-120, 120)
ax.axis('off')  # Turn off the default axes

# Add legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2, fontsize=16)
plt.tight_layout()

# Show plot
plt.savefig('pentagon_radar_chart.png')
