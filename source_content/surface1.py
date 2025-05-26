import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# 创建数据
X = np.arange(0, 5, 0.5)
Y = np.arange(-5, 0, 0.5)
X, Y = np.meshgrid(X, Y)
R = np.sqrt(X + Y**2)
Z = np.sin(R)

# 绘制三维曲面图
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

# 使用新的颜色映射，例如 'viridis'
ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.inferno)

# 保存图像
plt.savefig('surface1.png')
