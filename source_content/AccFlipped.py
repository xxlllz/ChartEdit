import matplotlib.pyplot as plt
import numpy as np

categories = ['Regular', 'Upside-Down']
labels = ['Gemini-1.5', 'GPT4-Turbo', 'GPT4-Omni', 'MiDaS-CNN', 'MiDaS-DPT', 'Humans']
colors = ['#1f77b4', '#aec7e8', '#9edae5', '#ff7f0e', '#ffbb78', '#98df8a']

# Data and error
accuracy_means = np.array([
    [0.6, 0.55, 0.7, 0.85, 0.9, 0.83],  # Regular
    [0.56, 0.45, 0.52, 0.71, 0.73, 0.85]   # Upside-Down
])
accuracy_std = np.array([
    [0.05, 0.06, 0.04, 0.03, 0.03, 0.04],  # Errors for Regular
    [0.08, 0.07, 0.08, 0.07, 0.07, 0.06]   # Errors for Upside-Down
])

x = np.arange(len(categories))  # the label locations
width = 0.1 
sep_width = 0.02
fig, ax = plt.subplots(figsize=(12, 6))  # Increased figure size

for i, label in enumerate(labels):
    ax.bar(
        x + i * (width + sep_width), 
        accuracy_means[:, i], 
        width, 
        yerr=accuracy_std[:, i], 
        label=label, 
        color=colors[i], 
        capsize=5, 
        ecolor='gray'  # Set error bar color to gray
    )

# Add labels, title, and custom x-axis tick labels
ax.set_ylabel('Accuracy', fontsize=20, fontweight='bold', labelpad=10)
ax.set_title('Accuracy for Regular and Flipped Images', fontsize=24, fontweight='bold', pad=15)
ax.set_xticks(x + (width + sep_width) * 2.5)
ax.set_xticklabels(categories, fontsize=18, fontweight='bold')
ax.set_ylim(0.4, 1.0)  # Adjust Y-axis range
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=20, frameon=True)

# Customize ticks
ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='x', labelsize=18)

# Adjust layout to prevent clipping
fig.tight_layout()  # Leave space for the legend on the right
plt.savefig('AccFlipped.png', dpi=300)
