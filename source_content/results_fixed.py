import matplotlib.pyplot as plt
import numpy as np

# Sample data
x_blue = np.arange(0.18, 0.641, 0.025)
y_blue = np.linspace(30, 36, len(x_blue))  # 蓝色线数据

x_green = [0.16, 0.2, 0.31, 0.455, 0.625]
y_green = [30, 30.55, 32.45, 34.1, 36]

x_red = [0.2, 0.315, 0.44, 0.65]
y_red = [30.56, 32.25, 34.1, 35.9]

x_brown = [0.175, 0.27, 0.43, 0.59]
y_brown = [29.75, 31.3, 33.4, 35]

x_yellowgreen = [0.15, 0.265, 0.43, 0.64]
y_yellowgreen = [28.75, 30.9, 33, 35]

x_orange = [0.2, 0.315, 0.46, 0.655]
y_orange = [29.4, 31.1, 32.9, 35]
# 调整图的尺寸比例
plt.figure(figsize=(10, 7))  # 宽 10，高 5，让图更扁
# Plot
plt.plot(x_blue, y_blue, 'o-', label='Proposed', color='tab:blue', markersize=5, lw=3)  # 蓝色实线加点
plt.plot(x_orange, y_orange, 'o--', label='Ballé', color='orange', markersize=4, lw=1)  # 橙色均匀虚线加点
plt.plot(x_brown, y_brown, 'o--', label='Cheng', color='brown', markersize=4, lw=1)  # 棕色均匀虚线加点
plt.plot(x_red, y_red, 'o--', label='Zou', color='red', markersize=4, lw=1)  # 红色均匀虚线加点
plt.plot(x_green, y_green, 'o--', label='Liu', color='green', markersize=4, lw=1)  # 绿色均匀虚线加点
plt.plot(x_yellowgreen, y_yellowgreen, 'o--', label='Minnen', color='yellowgreen', markersize=4, lw=1)  # 黄绿色均匀虚线加点

# 设置标题和标签
plt.title('Kodak',fontsize=18)
plt.xlabel('bpps',fontsize=16, fontweight='bold')
plt.ylabel('PSNR (dB)',fontsize=16, fontweight='bold')

# 设置网格和坐标轴范围
plt.grid(True)
plt.gca().set_xticks(np.arange(0.15, 0.67, 0.05), minor=False)  # 背景网格横坐标每 0.05 一个
plt.gca().set_xticklabels(["", "0.2", "", "0.3", "", "0.4", "", "0.5", "", "0.6", ""],fontsize=14, fontweight='bold')  # 标签数量匹配
plt.gca().set_yticks(np.arange(29, 36.5, 0.5))  # 背景网格纵坐标每 0.5 一个
plt.gca().set_yticklabels([str(int(y)) if y.is_integer() else "" for y in np.arange(29, 36.5, 0.5)],fontsize=14, fontweight='bold')

plt.xlim(0.125, 0.65)
plt.ylim(29, 36)

# 调整图例位置到右侧中间
plt.legend(loc='center left', bbox_to_anchor=(0.9, 0.5))

# 调整布局和保存图像
plt.tight_layout()
plt.savefig('results_fixed.png')
