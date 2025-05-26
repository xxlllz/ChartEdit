import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['W/O Norm', 'W/O Filter', 'W/O FFN']
original = [0.156, 0.156, 0.156]
wo = [0.162, 0.173, 0.160]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars

# Modify figsize here, for example (8, 5) for wider figure
fig, ax = plt.subplots(figsize=(8, 5))  # Adjusted figure size
rects1 = ax.bar(x - width/2, original, width, label='Original', color='#008080')
rects2 = ax.bar(x + width/2, wo, width, label='W/O', color='#D2B48C')

# Add labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('MSE', fontsize=15, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12, fontweight='bold')

# Set y-axis label fontsize and tick fontsize
ax.yaxis.set_tick_params(labelsize=14)  # Increase y-axis tick label size
ax.set_ylabel('MSE', fontsize=18, fontweight='bold')  # Larger y-axis label fontsize

# Legend with increased font size
ax.legend(fontsize=14)

# Set y-axis limit to match the source image
ax.set_ylim(0.15, 0.18)

fig.tight_layout()
plt.savefig('ablation_electricity-1.png')
