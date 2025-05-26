import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['W/O Norm', 'W/O Filter', 'W/O FFN']
original = [0.375, 0.376, 0.375]
wo = [0.378, 0.398, 0.393]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(7, 5))  # Adjust figure size if needed
rects1 = ax.bar(x - width/2, original, width, label='Original', color='#008080')
rects2 = ax.bar(x + width/2, wo, width, label='W/O', color='#D2B48C')

# Add labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('MSE', fontsize=18, fontweight='bold')  # Increase y-axis label font size
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14, fontweight='bold')  # Increase x-axis label font size

# Set y-axis label fontsize and tick fontsize
ax.yaxis.set_tick_params(labelsize=14)  # Increase y-axis tick label font size

# Increase the legend font size
ax.legend(fontsize=14)  # Increase legend font size

# Set y-axis limit to match the source image
ax.set_ylim(0.35, 0.4)

fig.tight_layout()  # Automatically adjusts layout to prevent clipping

# Save the figure
plt.savefig('ablation_ETTh1-1.png')
