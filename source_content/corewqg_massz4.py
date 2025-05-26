import matplotlib.pyplot as plt
import numpy as np

# 数据点 (x轴: log质量, y轴: CWQ比例) 和误差条
x = [11.6, 11.9, 12.25, 12.6, 12.8]  # 横轴 log(M_{z=4,halo}/M☉)
y = [0.011, 0.02, 0.016, 0.037, 0.048]  # 纵轴 Fraction of CWQs
yerr = [0.002, 0.003, 0.004, 0.006, 0.011]  # y轴误差条

# 绘制图形
fig, ax = plt.subplots(figsize=(6, 5))

# 绘制数据点和误差条，增大数据点大小
ax.errorbar(x, y, yerr=yerr, fmt='o', color='royalblue', capsize=4, markersize=8)  # 调整 markersize 增大原点

# 设置网格线 (竖线)
for xval in [11.75, 12.0, 12.25, 12.5, 12.75]:
    ax.axvline(x=xval, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)

# 设置坐标轴标签
ax.set_xlabel(r'$\log(M_{z=4, \mathrm{halo}} / M_\odot)$', fontsize=18)  # 调整标签字体大小
ax.set_ylabel('Fraction of CWQs', fontsize=18)  # 调整标签字体大小

# 调整轴刻度字体大小
ax.tick_params(axis='both', which='major', labelsize=15)  # 增大所有ticks的字体大小

# 设置x轴和y轴范围
ax.set_xlim(11.5, 13)
ax.set_ylim(0.005, 0.06)

# 调整布局
plt.tight_layout()

# 保存图形
plt.savefig('corewqg_massz4.png')
