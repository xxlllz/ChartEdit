import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Vector Search', 'GPT-3.5-Turbo', 'SetFit Model']
f1_scores = [0.40, 0.73, 0.8]
accuracies = [0.45, 0.70, 0.8]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars
spe_width = 0.02

# Create the plot
fig, ax = plt.subplots(figsize=(6, 4))

# Add horizontal gridlines (placed before bars to be underneath)
ax.grid(axis='y', linestyle='-', alpha=0.5, zorder=0)

# Bars
rects1 = ax.bar(
    x - (width + spe_width)/2, f1_scores, width, label='F1-Score', 
    color='#788bbf', alpha=0.6, zorder=2
)
rects2 = ax.bar(
    x + (width + spe_width)/2, accuracies, width, label='Accuracy', 
    color='#cbb2d4', alpha=0.7, zorder=2
)

# Add labels and ticks
ax.set_ylabel('Score', fontsize=16)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14)
ax.tick_params(axis='y', labelsize=14)

# Add legend
ax.legend(
    loc='upper center',
    bbox_to_anchor=(0.5, 1.2),
    fancybox=True,
    shadow=False,
    ncol=2,
    fontsize=16  # Enlarged legend font size
)

# Change spines to gray
for spine in ax.spines.values():
    spine.set_edgecolor('gray')

# Add a gray bottom line
ax.axhline(y=0, color='gray', linewidth=1.5, zorder=1)

# Move the title to the bottom
fig.suptitle('Topic Classification Approach', fontsize=16, y=0.05)

# Layout
fig.tight_layout(rect=[0, 0.05, 1, 1.1])  # Leave space at the bottom for the title
plt.savefig('bar-scores.png', dpi=300)
