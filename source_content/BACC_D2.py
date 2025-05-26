import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [2, 3, 4, 5, 6, 7, 8]

uw_pc = [3.3, 3.8, 4.3, 4.9, 4.9, 5.1, 5.3]
uw_pcc = [3.0, 3.6, 4.1, 4.7, 4.9, 5.0, 5.1]
wa_pc = [2.9, 3.6, 3.9, 4.4, 4.4, 4.5, 4.5]
wa_pcc = [2.7, 3.2, 3.7, 4.2, 4.1, 4.1, 4.2]
de = [1.0, 1.4, 1.7, 2.3, 2.1, 2.2, 2.4]
bma = [1.4, 1.8, 2.4, 3.0, 3.1, 3.4, 3.5]

avg = [np.mean([uw_pc[i], uw_pcc[i], wa_pc[i], wa_pcc[i], de[i], bma[i]]) for i in range(len(categories))]

bar_width = 0.1
sep_width = 0.02

# Plot
fig, ax = plt.subplots(figsize=(14, 7))
index = np.arange(len(categories))

# Add grid first with a lower z-order
ax.yaxis.grid(True, linestyle='-', alpha=0.6, zorder=0)

# Draw bars with a higher z-order
rects1 = ax.bar(index, uw_pc, bar_width, label='UW-PC', color='lightblue', zorder=2)
rects2 = ax.bar(index + (bar_width + sep_width), uw_pcc, bar_width, label='UW-PCC', color='orange', zorder=2)
rects3 = ax.bar(index + 2 * (bar_width + sep_width), wa_pc, bar_width, label='WA-PC', color='lightgreen', zorder=2)
rects4 = ax.bar(index + 3 * (bar_width + sep_width), wa_pcc, bar_width, label='WA-PCC', color='orangered', zorder=2)
rects5 = ax.bar(index + 4 * (bar_width + sep_width), de, bar_width, label='DE', color='orchid', zorder=2)
rects6 = ax.bar(index + 5 * (bar_width + sep_width), bma, bar_width, label='BMA', color='gray', zorder=2)

# Line
ax.plot(index + 2.5 * bar_width, avg, label='Avg', marker='o', linestyle='--', color='black', zorder=3)

# Set labels and ticks
ax.set_xlabel('Number of Classifiers $(K)$', fontsize=20)
ax.set_ylabel('Bal. Accuracy Increase (%)', fontsize=24)
ax.set_xticks(index + 2.5 * bar_width)
ax.set_xticklabels(categories, fontsize=18)
ax.set_yticks(np.arange(0, 8, 1))
ax.tick_params(axis='y', labelsize=18, which='both', length=0)  # Removes small tick marks
ax.tick_params(axis='x', labelsize=18, which='both', length=0)  # Removes small tick marks

# Remove spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Adjust legend
ax.legend(loc='lower center', ncol=7, bbox_to_anchor=(0.5, -0.25), fontsize=16, frameon=False)

# Tight layout and save
fig.tight_layout()
plt.savefig('BACC_D2.png')
plt.show()
