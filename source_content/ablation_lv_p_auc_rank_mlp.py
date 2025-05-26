import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Data
data = np.array([
    [13.75, 9.58, 8.21, 8.96, 10.58],
    [13.58, 8.71, 9.12, 8.83, 8.54],
    [11.92, 9.33, 9.04, 9.04, 10.62],
    [12.25, 11.75, 10.75, 12.04, 10.62]
])

# Axis labels
noise_ratio = [1.0, 0.8, 0.5, 0.2]  # Corrected order for y-axis
noise_level = [0.1, 0.5, 1, 3, 5]

plt.figure(figsize=(10, 8))  # Adjusted figure size for better visibility

# Create a heatmap without internal borders
ax = sns.heatmap(
    data,
    annot=True,
    fmt='.2f',
    cmap='OrRd',
    xticklabels=noise_level,
    yticklabels=noise_ratio,
    annot_kws={"size": 24, "color": "black"},  # Change annotation font color to black
    square=True
)

# Add labels and title with larger font size
plt.xlabel('Noise Level', fontsize=25, fontweight='bold', color='black')  # Set font color to black
plt.ylabel('Noise Ratio', fontsize=25, fontweight='bold', color='black')  # Set font color to black
plt.title('Mean AUC rank on MLP', fontsize=30, fontweight='bold', pad=20, color='black')  # Set font color to black

# Customize tick labels font size and color
plt.xticks(fontsize=20, fontweight='bold', color='black')  # Set x-axis tick font color to black
plt.yticks(fontsize=20, fontweight='bold', color='black')  # Set y-axis tick font color to black

# Add a border to the entire plot (not the internal grid)
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(2)

# Add a border around the colorbar
cbar = ax.collections[0].colorbar
cbar.outline.set_edgecolor('black')  # Set colorbar border color
cbar.outline.set_linewidth(3)  # Set colorbar border width

# Reduce colorbar height
cbar.ax.yaxis.set_tick_params(labelsize=24, color='black')  # Adjust colorbar tick label size and color

plt.tight_layout()
# Save the figure
plt.savefig('ablation_lv_p_auc_rank_mlp.png')