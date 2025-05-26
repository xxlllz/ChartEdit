import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# 使用 Arial 字体
song_bold_font = font_manager.FontProperties(family='SimSun', weight='bold', size=14)
y1 = np.array([2.8, 2.52, 2.25, 1.99, 1.74, 1.55, 1.4, 1.25, 1.15, 1.0,
             0.9, 0.8, 0.7, 0.58, 0.5, 0.4, 0.35, 0.3, 0.26, 0.24,
             0.22, 0.20, 0.18, 0.16, 0.14, 0.12, 0.10, 0.095, 0.09, 0.085, 0.1, 0.23])
y2 = np.array([3.38, 3.4, 3.37, 3.35, 3.33, 3.31, 3.29, 3.27, 3.25, 3.23,
             3.21, 3.19, 3.18, 3.16, 3.14, 3.15, 3.2, 3.26, 3.32, 3.38,
             3.44, 3.5, 3.54, 3.6, 3.66, 3.71, 3.77, 3.83, 3.89, 3.94, 4, 3.93])
x = np.arange(len(y1))

# Plotting the data
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='w/ $\\alpha$', marker='o', markersize=6, linestyle='-', color='b', alpha=0.3)
plt.plot(x, y2, label='w/o $\\alpha$', marker='^', markersize=6, linestyle='-', color='r', alpha=0.3)

# Adding labels and legend
plt.xlabel('Layer idx', fontsize=18, fontproperties=song_bold_font)
plt.ylabel('Per-Layer MIR', fontsize=18, fontproperties=song_bold_font)
# Set the legend in the lower-left corner with a specific font size
plt.legend(loc='lower left', fontsize=18)  # 图例字体大小设置为 12
plt.grid(True)


# Modify x and y axis tick font sizes
plt.tick_params(axis='x', labelsize=18)  # 修改 x 轴刻度字体大小
plt.tick_params(axis='y', labelsize=18)  # 修改 y 轴刻度字体大小
# Display the plot
plt.savefig('supp_1.png')