import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['10', '30', '50', '70', '90', '110', '130', '150']
values_high_hot = [1.31, 1.42, 1.41, 1.4, 1.42, 1.415, 1.4, 1.38]
values_med_hot = [1.45, 1.54, 1.55, 1.53, 1.505, 1.48, 1.495, 1.49]

x = np.arange(len(groups))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(6, 3.5))
rects1 = ax.bar(x - width/2, values_high_hot, width, label='high hot', color='royalblue',edgecolor='black',linewidth=1.5,zorder=2)
rects2 = ax.bar(x + width/2, values_med_hot, width, label='med hot', color='#ed7d31',edgecolor='black',linewidth=1.5,zorder=2)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Pooling Factor', fontsize=14,labelpad=10, fontweight='bold')
ax.set_ylabel('Speedup over Base PyTorch', fontsize=12,labelpad=10, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(groups, fontsize=12, fontweight='bold')
ax.set_ylim(1.1, 1.6)
ax.set_yticklabels(labels=[1.1,1.2,1.3,1.4,1.5,1.6],fontsize=12, fontweight='bold')
ax.legend(fontsize=12, loc='upper right', fancybox=True, edgecolor='none',ncol=2,handlelength=0.8, handleheight=0.8,bbox_to_anchor = (0.85,1.03),columnspacing=1,facecolor='none',framealpha=0.5)
ax.tick_params(axis='x', length=0,pad=15)
ax.tick_params(axis='y', length=0)
ax.grid(True,axis='y', linestyle='-', linewidth=0.5, alpha=0.7,zorder=0)


fig.tight_layout()

plt.savefig('l2_pinning_OptMT.png')