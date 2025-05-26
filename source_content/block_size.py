import matplotlib.pyplot as plt
import numpy as np

# Data
block_sizes = [1, 2, 4, 8, 64, 128, 256, 512]
VSRN = [479, 482, 480, 478, 474, 475, 472, 467]
SCAN_t2i = [477, 478, 477, 481, 483, 484, 485, 483]
SCAN_i2t = [464, 466, 466, 467, 472, 476, 478, 473]

x = np.arange(len(block_sizes))  # the label locations
width = 0.2  # the width of the bars
sep_width = 0.04
fig, ax = plt.subplots(figsize=(8, 6))

# Plot each dataset as a group of bars
bars1 = ax.bar(x - (width + sep_width), VSRN, width, label='VSRN', color='#FFCC33', edgecolor='black')
bars2 = ax.bar(x, SCAN_t2i, width, label='SCAN(t2i)', color='#99CCFF', edgecolor='black')
bars3 = ax.bar(x + (width + sep_width), SCAN_i2t, width, label='SCAN(i2t)', color='#99FF99', edgecolor='black')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('rSum', fontsize=16, fontweight='bold')
ax.set_xlabel('block size', fontsize=16, fontweight='bold')
plt.ylim([450, 485])
ax.set_xticks(x)
ax.set_xticklabels(block_sizes, fontsize=14)

# Add horizontal grid lines on y-axis
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='gray', alpha=0.7)  # Add grid lines
ax.set_axisbelow(True)  # Ensure grid lines are below bars

# Remove small tick marks
ax.tick_params(axis='both', which='both', length=0)

# Customize legend
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fontsize=12, frameon=False)

# Remove the outer border of the plot
for spine in ax.spines.values():
    spine.set_visible(False)

plt.yticks(fontsize=14)
plt.xticks(fontsize=14)

plt.tight_layout()
# Show the plot
plt.savefig('block_size.png')
