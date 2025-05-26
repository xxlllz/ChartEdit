import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# 自定义颜色列表（替换下面的颜色值）
custom_colors = [
    "#FCFBDB",  # 颜色1
    "#D6E7B3",  # 颜色2
    "#73C4BA",  # 颜色3
    "#2398C1",  # 颜色4
    "#234C9F",  # 颜色5
    "#17254C"   # 颜色6
]

# 创建自定义的颜色映射
custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", custom_colors)

# Data for the heatmap
values = np.array([
    [1.00, 0.83, 0.64, 0.65],
    [0.83, 1.00, 0.62, 0.62],
    [0.64, 0.62, 1.00, 0.59],
    [0.65, 0.62, 0.59, 1.00]
])

# Labels for rows and columns
labels = ['GPT4', 'Human1', 'Human2', 'Human3']

# Create the heatmap
plt.figure(figsize=(8, 6))
ax = sns.heatmap(values, annot=True, fmt=".2f", cmap=custom_cmap,  vmin=0, vmax=1,annot_kws={"size": 18,'color':'white'})


cbar = ax.figure.axes[-1]  # 获取颜色条的轴
cbar.tick_params(which='both', size=2,labelsize=16)  # 主刻度和次刻度线都隐藏

# Customize tick labels
ax.set_xticks(np.arange(len(labels)) + 0.5)
ax.set_yticks(np.arange(len(labels)) + 0.5)


colors=["blue", "red", "red", "red"]
ax.set_xticklabels(labels, fontsize=14, rotation=0)
ax.set_yticklabels(labels, fontsize=14, rotation=0)


for ticklabel, color in zip(ax.get_xticklabels(), colors):
    ticklabel.set_color(color)
for ticklabel, color in zip(ax.get_yticklabels(), colors):
    ticklabel.set_color(color)
ax.tick_params(which='both', size=2)  # 主刻度和次刻度线都隐藏  


# Set axis labels
ax.set_xlabel('')
ax.set_ylabel('')

# Adjusting the aspect
ax.set_aspect('equal', 'box')

# Display the plot
plt.tight_layout(pad=0)
plt.savefig('Heatmap5.png')
