import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([250, 500, 750, 1000, 1250, 1500, 1750, 2000])
nsga_y = np.array([0.357, 0.342, 0.34, 0.338, 0.336, 0.334, 0.331, 0.33])
rs_y = np.array([0.34, 0.29, 0.275, 0.265, 0.26, 0.255, 0.253, 0.25])


nsga_error = np.array([0.05] + [0.04] +[0.03]* (len(nsga_y) - 2))


rs_error = np.array([0.025] + [0.02] + [0.009] * 2 + [0.007] + [0.005]*3)

# 绘制误差条图
line_nsga, = plt.plot(x, nsga_y, color='#8B008B', linestyle='-', label='NSGA-II')
line_rs, = plt.plot(x, rs_y, color='#004080', linestyle='-', label='RS')

# 绘制误差条图
plt.errorbar(x, nsga_y, yerr=nsga_error, label='NSGA-II', color='#8B008B', linestyle='-', marker='o', capsize=5, linewidth=2,markersize = 4, markerfacecolor='black')
plt.errorbar(x, rs_y, yerr=rs_error, label='RS', color='#004080', linestyle='-', marker='o',capsize=5,linewidth=2,markersize = 4, markerfacecolor='black')

# 设置横坐标从 0 开始
plt.xlim(0, 2250)

# 设置纵坐标刻度
plt.yticks([0.25, 0.30, 0.35, 0.40], fontsize=12, fontweight='bold')

plt.xlabel('Number of Evaluations', fontsize=18, fontweight='bold')
plt.ylabel('CID', fontsize=18, fontweight='bold')
plt.xticks(fontsize=14, fontweight='bold')

# 调整图例，仅显示蓝线和紫线
plt.legend(handles=[line_nsga, line_rs], prop={'size': 16, 'weight': 'bold'})


# 调整布局
plt.tight_layout()
plt.savefig('subplots_combined_ds.png')
