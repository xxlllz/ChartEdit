import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap

# Sample data that represents the correlation matrix
matrix = np.array([
    [1, 0.26, 0.41, 0.19, 0.22, 0.16, 0.07, 0.14, 0.22],
    [0.26, 1, 0.32, 0.33, 0.83, 0.41, 0.61, 0.56, 0.31],
    [0.41, 0.32, 1, 0.78, 0.35, 0.53, 0.71, 0.6, 0.85],
    [0.19, 0.33, 0.78, 1, 0.6, 0.76, 0.9, 0.88, 0.98],
    [0.22, 0.83, 0.35, 0.6, 1, 0.5, 0.79, 0.82, 0.56],
    [0.16, 0.41, 0.53, 0.76, 0.5, 1, 0.76, 0.59, 0.74],
    [0.07, 0.61, 0.71, 0.9, 0.79, 0.76, 1, 0.9, 0.9],
    [0.14, 0.56, 0.6, 0.88, 0.82, 0.59, 0.9, 1, 0.85],
    [0.22, 0.31, 0.85, 0.98, 0.56, 0.74, 0.9, 0.85, 1]
])

labels = ["1-1", "1-2", "2-1", "2-2", "3-1", "3-2", "4-1", "4-2", "5-1"]
colors = ['blue', 'blue', 'green', 'green', 'orange', 'orange', 'red', 'red', 'black']

colors_positions = [
    (-1, 'white'),  # 起点
    # (-0.25,'#E5E4F2'),
    (-0.5, '#EDECF5'), 
    (0, '#D8DAEE'),    
    # (0.25,'#CEC9E7'),
    (0.5, '#B3BFE0'),   
    # (0.75,"#95A7D0"),
    (0.96, '#48638C')   # 终点
]
color_black = 'black'  # 0.98 到 1 是黑色

# 定义自定义渐变 colormap
positions, colors1 = zip(*colors_positions)


gradient_cmap = LinearSegmentedColormap.from_list("custom_gradient", colors1)

# 手动扩展颜色以包括黑色
colors_list = [gradient_cmap(i) for i in np.linspace(0, 1, 256)]  # 渐变部分
colors_list.append(color_black)  # 添加黑色

# 定义边界：-1 到 0.98 连续变化，0.98 到 1 是黑色
bounds = np.linspace(-1, 0.96, 256).tolist() + [1.01]  # 添加额外的黑色区间

# 创建 colormap 和 norm
cmap = LinearSegmentedColormap.from_list("custom_cmap", colors_list)
norm = BoundaryNorm(bounds, len(colors_list))

def dynamic_text_color(value):
    """返回数字颜色：大于 0.75 为白色，否则为黑色"""
    return 'white' if value > 0.75 else 'black'

plt.figure(figsize=(10, 8))
heatmap=sns.heatmap(matrix, annot=True, cmap=cmap,norm=norm, cbar_kws={'ticks': [-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1],},
            linewidths=0, linecolor='black', square=True, annot_kws={"size": 15,},
            xticklabels=labels, yticklabels=labels,vmin=-1,vmax=1
)

for text in heatmap.texts:
    value = float(text.get_text())  # 获取文本对应的数值
    text.set_color(dynamic_text_color(value))  # 动态设置颜色
    
heatmap.figure.axes[-1].tick_params(size=0)  # 设置刻度线大小为 0
cbar = heatmap.figure.axes[-1]  # 获取颜色条的轴
cbar.tick_params(which='both', size=0,labelsize=12)  # 主刻度和次刻度线都隐藏

# Setting the color for each tick label
ax = plt.gca()
ax.set_xticklabels(labels, rotation=45, ha="center", fontsize=15)
ax.set_yticklabels(labels, rotation=45, fontsize=15)
for ticklabel, color in zip(ax.get_xticklabels(), colors):
    ticklabel.set_color(color)
for ticklabel, color in zip(ax.get_yticklabels(), colors):
    ticklabel.set_color(color)
ax.tick_params(which='both', size=0)  # 主刻度和次刻度线都隐藏  

# Adjust layout
plt.tight_layout()
plt.show()

plt.savefig('Heatmap2.png')
