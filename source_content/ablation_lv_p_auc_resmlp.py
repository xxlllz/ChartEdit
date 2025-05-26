import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
data = np.array([
    [90.32, 91.93, 91.56, 91.12, 90.47],
    [90.55, 92.03, 92.12, 90.98, 90.80],
    [90.28, 92.03, 91.84, 91.12, 90.66],
    [90.70, 91.13, 92.13, 91.64, 91.30]
])

# Axis labels
noise_ratio = [1.0, 0.8, 0.5, 0.2]  # Corrected order for y-axis
noise_level = [0.1, 0.5, 1, 3, 5]

plt.figure(figsize=(10, 7))  # Adjusted figure size for better visibility

# Create a heatmap without internal borders
ax = sns.heatmap(
    data,
    annot=True,
    fmt='.2f',
    cmap='OrRd',
    xticklabels=noise_level,
    yticklabels=noise_ratio,
    annot_kws={"size": 24, "color": "black"},  # Adjust annotation font size and color
    square=True
)

# Add labels and title with larger font size
plt.xlabel('Noise Level', fontsize=24, fontweight='bold', color='black')  # X-axis label
plt.ylabel('Noise Ratio', fontsize=24, fontweight='bold', color='black')  # Y-axis label
plt.title('Mean AUC on ResMLP', fontsize=30, fontweight='bold', pad=10, color='black')  # Title

# Customize tick labels font size and color
plt.xticks(fontsize=20, fontweight='bold', color='black')  # X-axis ticks
plt.yticks(fontsize=20, fontweight='bold', color='black')  # Y-axis ticks

# Add a border to the entire plot (not the internal grid)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(2)

# Add a border around the colorbar
cbar = ax.collections[0].colorbar
cbar.outline.set_edgecolor('black')  # Set colorbar border color
cbar.outline.set_linewidth(2)  # Set colorbar border width

# Reduce colorbar ticks
cbar.set_ticks([90.5, 91.0, 91.5, 92.0])  # Set fewer ticks on colorbar

# Adjust colorbar tick font size
cbar.ax.yaxis.set_tick_params(labelsize=18, color='black')  # Increase colorbar tick font size


# Adjust layout to fit everything neatly
plt.tight_layout()

# Save the figure
plt.savefig('ablation_lv_p_auc_resmlp.png', bbox_inches='tight')
