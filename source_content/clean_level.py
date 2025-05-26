import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

# Data
categories = ['Tool Selection', 'Parameter Identification', 'Content Filling']
subtasks = ['Slight', 'Medium', 'Heavy']
union = ['Union']
tools_data = [
    [11, 9, 36],  # Tool Selection (Slight, Medium, Heavy)
    [7, 6, 24],  # Parameter Identification
    [5, 4, 13]   # Content Filling
]
params_data = [
    [0, 1, 0.5],  # Tool Selection (Slight, Medium, Heavy)
    [4.5, 2.5, 11],  # Parameter Identification
    [2, 1.5, 9]  # Content Filling
]
union_data = [[20], [14], [11]]

# Bar positions
x = np.arange(len(categories))  # Position of each category
width = 0.1  # Width of each bar
bar_offset = np.linspace(-width * 3.5, width * 3.5, len(subtasks) * 2 + 1)

# Plot
fig, ax = plt.subplots(figsize=(8, 5))
colors = ['skyblue', 'lightgreen', 'peachpuff', 'royalblue', 'darkgreen', 'peru', 'silver']
labels = [f'{subtask} (Tool)' for subtask in subtasks] + [f'{subtask} (Param)' for subtask in subtasks] + union
datasets = [tools_data, params_data, union_data]

# Add bars for each subtask
for i, (offset, color, label) in enumerate(zip(bar_offset, colors, labels)):
    data = datasets[i // 3]  # Choose the dataset based on i
    subtask_index = i % 3
    heights = [row[subtask_index] if subtask_index < len(row) else 0 for row in data]
    
    # Add bars with darker edge colors
    edge_color = mcolors.to_rgba(color)  # Darker color
    edge_color = tuple(q * 0.7 for c in edge_color[:3]) + (edge_color[3],)  # Darker RGBA color
    ax.bar(
        x + offset,
        heights,
        width,
        label=label,
        color=color,
        edgecolor=edge_color,
        linewidth=1.5,
        alpha=0.6
    )

# Styling
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')
ax.set_ylim(0, 40)
# Hide tick marks but keep labels, and bold y-tick labels
ax.tick_params(axis='x', which='both', bottom=False, top=False)  # Hide x-axis tick marks
ax.tick_params(axis='y', which='both', left=False, right=False, labelsize=15, labelcolor='black')  # Hide y-axis tick marks
for label in ax.get_yticklabels():
    label.set_fontweight('bold')  # Make y-tick labels bold

ax.legend(loc='upper right', fontsize=12)
plt.tight_layout()

# Save or show
plt.savefig("clean_level.png")
plt.show()
