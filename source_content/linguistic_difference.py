import matplotlib.pyplot as plt
import numpy as np

# Data for the heatmaps
constituent_data = np.array([[0.055, 0.031],
                             [0.035, 0.013]])
pos_data = np.array([[0.088, 0.045],
                     [0.061, 0.033]])
entity_data = np.array([[0.145, 0.103],
                        [0.072, 0.046]])

# Titles for the x-axis labels
column_titles = ['Model-specific', 'Arbitrary-models']
row_titles = ['Fixed-domain', 'Arbitrary-domains']

# Create the figure and subplots
fig, axes = plt.subplots(1, 3, figsize=(12, 4))

# Heatmap 1: Constituent Distribution
im1 = axes[0].imshow(constituent_data, cmap='Blues', vmin=0, vmax=0.06)
for i in range(2):
    for j in range(2):
        text = axes[0].text(j, i, f'{constituent_data[i, j]:.3f}',
                            ha='center', va='center', color='white', fontsize=28)
axes[0].set_xticks([0, 1])
axes[0].set_xticklabels(column_titles)
axes[0].set_yticks([0, 1])
axes[0].set_yticklabels(row_titles,rotation=90,va='center',fontsize=12)
# axes[0].set_title("Constituent Distribution", fontsize=10, pad=10)

# Heatmap 2: Part-of-speech Distribution
im2 = axes[1].imshow(pos_data, cmap='Blues', vmin=0, vmax=0.1)
for i in range(2):
    for j in range(2):
        text = axes[1].text(j, i, f'{pos_data[i, j]:.3f}',
                            ha='center', va='center', color='white', fontsize=28)
axes[1].set_xticks([0, 1])
axes[1].set_xticklabels(column_titles)
axes[1].set_yticks([0, 1])
axes[1].set_yticklabels(row_titles,rotation=90,va='center',fontsize=12)
# axes[1].set_title("Part-of-speech Distribution", fontsize=10, pad=10)

# Heatmap 3: Named Entity Distribution
im3 = axes[2].imshow(entity_data, cmap='Blues', vmin=0, vmax=0.15)
for i in range(2):
    for j in range(2):
        text = axes[2].text(j, i, f'{entity_data[i, j]:.3f}',
                            ha='center', va='center', color='white', fontsize=28)
axes[2].set_xticks([0, 1])
axes[2].set_xticklabels(column_titles)
axes[2].set_yticks([0, 1])
axes[2].set_yticklabels(row_titles,rotation=90,va='center',fontsize=12)

# 调整 x 轴标签位置到顶部
axes[0].tick_params(axis='x', direction='out', length=3, width=1, labelsize=12, top=True, labeltop=True, bottom=False,labelbottom=False)
axes[1].tick_params(axis='x', direction='out', length=3, width=1, labelsize=12, top=True, labeltop=True, bottom=False,labelbottom=False)
axes[2].tick_params(axis='x', direction='out', length=3, width=1, labelsize=12, top=True, labeltop=True, bottom=False,labelbottom=False)

# 创建标题并放置在图片下方
fig.text(0.19, 0.08, "Constituent Distribution", ha='center', va='center', fontsize=16)
fig.text(0.50, 0.08, "Part-of-speech Distribution", ha='center', va='center', fontsize=16)
fig.text(0.81, 0.08, "Named Entity Distribution", ha='center', va='center', fontsize=16)

plt.subplots_adjust(bottom=0.5)
# Adjust layout and save the plot
plt.tight_layout()
plt.savefig("linguistic_difference.png")
