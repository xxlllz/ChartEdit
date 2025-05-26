import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap, BoundaryNorm, LinearSegmentedColormap

# Data preparation
correlation_matrix = np.array([
    [1.0, 0.83, 0.64, 0.65],
    [0.83, 1.0, 0.62, 0.62],
    [0.64, 0.62, 1.0, 0.59],
    [0.65, 0.62, 0.59, 1.0]
])

labels = ['GPT4', 'Human1', 'Human2', 'Human3']
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

# Create the heatmap
plt.figure(figsize=(8, 6))
ax = sns.heatmap(correlation_matrix, annot=True, cmap=cmap,norm=norm, cbar=True, 
                 vmin=-1, vmax=1,annot_kws={"size": 15,},
                 cbar_kws={"ticks":[-1, -0.75, -0.5, -0.25, 0, 0.25, 0.5, 0.75, 1]})

for text in ax.texts:
    value = float(text.get_text())  # 获取文本对应的数值
    text.set_color(dynamic_text_color(value))  # 动态设置颜色

cbar = ax.figure.axes[-1]  # 获取颜色条的轴
cbar.tick_params(which='both', size=0,labelsize=12)  # 主刻度和次刻度线都隐藏

colors=['blue', 'green', 'green', 'green']
# Custom axis labels
ax.set_xticklabels(labels, rotation=0, ha='center', fontsize=14)
ax.set_yticklabels(labels, rotation=0, fontsize=14, va='center')


for ticklabel, color in zip(ax.get_xticklabels(), colors):
    ticklabel.set_color(color)
for ticklabel, color in zip(ax.get_yticklabels(), colors):
    ticklabel.set_color(color)
ax.tick_params(which='both', size=2)  # 主刻度和次刻度线都隐藏  

# Show the plot
plt.tight_layout()
plt.savefig('Heatmap3.png')
