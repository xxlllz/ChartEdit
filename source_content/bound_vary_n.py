import matplotlib.pyplot as plt
import numpy as np

# 数据准备
gamma = np.linspace(0.1, 1.0, 10)  # 采样率 gamma (x轴)

# y轴数据
y1 = np.array([140, 140, 140, 140, 140, 140, 140, 140, 140, 140])  # Approx+Shuffling [EFM+19]
y2 = np.array([6, 15, 26, 38, 50, 66, 82, 101, 120, 140])         # Approx+Shuffling+Sampling [GDD+21]
y3 = np.array([4, 10, 17, 25, 33, 42, 51, 62, 71, 82])           # Camel

# 绘图
plt.figure(figsize=(8, 6))

# 绘制曲线
plt.plot(gamma, y1, 'm-o', label='Approx+Shuffling [EFM+19]', linewidth=2, markersize=10)  # 紫色线，圆点
plt.plot(gamma, y2, 'c-^', label='Approx+Shuffling+Sampling [GDD+21]', linewidth=2, markersize=10)  # 蓝绿色线，三角
plt.plot(gamma, y3, 'r-*', label='Camel', linewidth=2, markersize=10)  # 红色线，星号

# 设置坐标轴
plt.xscale('linear')  # x轴为线性刻度
plt.yscale('log')     # y轴为对数刻度

# 设置坐标轴标签
plt.xlabel(r'Sampling Rate $\gamma$', fontsize=20)
plt.ylabel(r'Approximate DP $\epsilon$', fontsize=20)

# 设置标题
plt.title(r'$N = 10^4, \delta = 10^{-5}, \epsilon_0 = 1.9, T = 500$', fontsize=20)

# 设置刻度字体大小
plt.xticks(np.linspace(0.1, 1.0, 10), fontsize=20)
plt.yticks(fontsize=20)

# 设置网格
plt.grid(True, which='major', linestyle='-', linewidth=0.5)  # 仅主网格线

# 添加图例并设置字体大小
plt.legend(fontsize=16, loc='lower right')

# 布局调整
plt.tight_layout()

# 保存图像
plt.savefig('bound_vary_n.png')