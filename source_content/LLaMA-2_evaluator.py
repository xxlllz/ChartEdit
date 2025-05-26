import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Data for the plot
groups = ['white', 'black', 'asian', 'straight', 'queer', 'man', 'woman', 'non-binary']
data1 = [0.38, 0.43, 0.08, 0.36, 0.62, 0.21, 0.38, 0.38]
data2 = [0.4, 0.29, 0.13, 0.35, 0.63, 0.38, 0.39, 0.24]
data3 = [0.31, 0.46, 0.14, 0.32, 0.66, 0.23, 0.45, 0.26]

# Add a closure value to complete the radar chart
data1 += data1[:1]
data2 += data2[:1]
data3 += data3[:1]

# Angles for the radar chart
angles = [n / float(len(groups)) * 2 * pi for n in range(len(groups))]
angles += angles[:1]

# Initialize the radar plot
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'polar': True})

# Plot data1
ax.plot(angles, data1, label='Group 1', c='#86AE60', alpha=0.8,linewidth=4,zorder=4)
ax.fill(angles, data1, c='#86AE60', alpha=0.15)
ax.scatter(angles, data1, marker='o', c='none', edgecolors='#86AE60', s=120, linewidths=3.5,alpha=0.8,zorder=4)  # 设置空心圆标记和边框粗细


# Plot data2
ax.plot(angles, data2, label='Group 2', c='#C37073',  alpha=1,linewidth=4,zorder=3)
ax.fill(angles, data2, c='#C37073', alpha=0.15)
ax.scatter(angles, data2, marker='o', c='none', edgecolors='#C37073', s=120, linewidths=3.5,alpha=1,zorder=3)  # 设置空心圆标记和边框粗细

# Plot data3
ax.plot(angles, data3, label='Group 3', c='#777593', alpha=0.8,linewidth=4,zorder=0)
ax.fill(angles, data3, c='#777593', alpha=0.15)
ax.scatter(angles, data3, marker='o', c='none', edgecolors='#777593', s=120, linewidths=3.5,alpha=0.8,zorder=1)  # 设置空心圆标记和边框粗细

# Add specific markers to the labels
markers = ['*', '*', '*', '^', '^', '^', 'P', 'P']  # Replace Unicode with valid markers

# Add annotations for each axis
group_labels = ['\u22c6 white', '\u22c6 black', '\u22c6 asian', '\u25c7 straight', '\u25c7 queer', '\u25b3 man', '\u25b3 woman', '\u25b3 non-binary']

ax.set_xticks(angles[:-1])
ax.set_xticklabels([], fontsize=14, ha='left')
ax.set_ylim(0, 0.8)
ax.set_yticks([0.2, 0.4, 0.6, 0.8])
ax.set_yticklabels([])
ax.plot([0,0],[0,1],c='black',linewidth=1.5)


for i, label in enumerate(group_labels):
    angle = angles[i]
    if i == 0 or i == 1 or i == 7:  # Left-aligned labels
        ax.text(angle, 0.8, label, horizontalalignment='left', verticalalignment='center', fontsize=16, color='black')
    elif i == 2 or i == 6:  # Centered labels
        ax.text(angle, 0.9, label, horizontalalignment='center', verticalalignment='center', fontsize=16, color='black')
    else:  # Left-aligned for indices 3, 4, 5
        ax.text(angle, 0.85, label, horizontalalignment='right', verticalalignment='center', fontsize=16, color='black')

yticks_values = [0.2,0.4,0.6,0.8]
for idx, value in enumerate(yticks_values):
    # Adjust the angle of the label based on the index and position it at a 90-degree (top) position
    fig.text(0.60+idx*0.09,0.53, value, fontsize=18, ha='center', va='center', color='black',zorder=0)
plt.suptitle('(b): LLaMA-2 as an evaluator', y=0.06,fontsize=20)  # y=-0.1 表示将标题放置在下方
plt.tight_layout(pad=0.1)
plt.savefig("LLaMA-2_evaluator.png")
