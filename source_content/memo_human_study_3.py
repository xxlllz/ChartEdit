import matplotlib.pyplot as plt
import numpy as np

# Data

categories = [
    'Identity Consistency','Audio-Lip Sync.','Expression-Audio Align.',  'Motion Smoothness', 'Overall Quality'
]

values = np.array([
    [0.5, 0.2, 0.22, 0.1],
    [0.57, 0.2, 0.18, 0.1],
    [0.55, 0.25, 0.15, 0.1],
    [0.59, 0.23, 0.14, 0.1],
    [0.6, 0.2, 0.16, 0.1]
])

# Create plot
fig, ax = plt.subplots(figsize=(8, 4))
bar_width = 0.4
indices = np.arange(len(categories))

# Plot
ax.barh(indices, values[:, 0], color='lightcoral', label='16+f', align='center',height=bar_width,edgecolor='lightcoral')
ax.barh(indices, values[:, 1], left=values[:, 0], color='#8ebbd9', label='8f', align='center',height=bar_width,edgecolor='#8ebbd9')
ax.barh(indices, values[:, 2], left=values[:, 0] + values[:, 1], color='#98cf95', label='4f', align='center',height=bar_width,edgecolor='#98cf95')
ax.barh(indices, values[:, 3], left=values[:, 0] + values[:, 1] + values[:, 2], color='#ffbe7f', label='2f', align='center',height=bar_width,edgecolor='#ffbe7f')

# Labels, legend, and grid
ax.set_yticks(indices)
ax.set_yticklabels(categories, rotation=-45, ha='right', va='bottom',fontsize=12)
ax.set_xlim(0,1)
ax.set_xlabel('Preference Proportion', fontsize=18)
ax.legend(loc='lower center', bbox_to_anchor=(0.6,1.2), ncol=4, fontsize=14,edgecolor='none',facecolor='none',columnspacing=0.2)

plt.tight_layout()
plt.savefig('memo_human_study_3.png')