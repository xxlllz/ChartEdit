import matplotlib.pyplot as plt
import numpy as np

# Data
datasets = ['iid', 'non-iid']
IPfedAvg = [22, 16]
fedEraser = [468, 480]

x = np.arange(len(datasets))  # the label locations
width = 0.3  # the width of the bars
sep_width = 0.02

# Plot
fig, ax = plt.subplots(figsize=(6, 5))
rects1 = ax.bar(x - (width + sep_width) / 2, IPfedAvg, width, label='IPfedAvg', color='blue')
rects2 = ax.bar(x + (width + sep_width) / 2, fedEraser, width, label='fedEraser', color='darkorange')

# Add some text for labels, title and axes ticks
ax.set_ylabel('Memory (GB)', fontsize=15)
ax.set_xlabel('CelebA Dataset', fontsize=15, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(datasets, fontsize=15)

# Increase the y-axis tick label size
plt.yticks(fontsize=15)

# Adjust the legend position and font size (centered)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), fontsize=15, ncol=2)

fig.tight_layout()

plt.savefig('celebA_convNet_Disk_space_Comparison.png')
