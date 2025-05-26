import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['RCT', 'SciCite', 'ChemProt', 'SciERC', 'News']
FT_means = [79.8, 80, 82.7, 85.8, 88.2]  # FT (蓝色条形图) 的平均值
TB_means = [80.3, 81.6, 83.6, 87.8, 93.5]  # TB (橙色条形图) 的平均值
FT_errors = [0.3, 2.0, 0.2, 1.5, 5.2]  # FT 的误差
TB_errors = [0.3, 1.7, 0.2, 1.0, 2.2]  # TB 的误差

# 设置图表参数
x = np.arange(len(categories))  # x 坐标
width = 0.3  # 条形图的宽度
spe_width = 0.05

# 创建图表
fig, ax = plt.subplots(figsize=(6, 4))

# 添加横竖网格线，置于条形图底层
ax.grid(axis='y', linestyle='--', linewidth=1.5, alpha=0.7, zorder=0)
ax.grid(axis='x', linestyle='--', linewidth=1.5, alpha=0.7, zorder=0)

# 绘制 FT 条形图 (蓝色)
bars1 = ax.bar(
    x - (width + spe_width) / 2, FT_means, width, yerr=FT_errors,
    label='FT', color='lightskyblue', edgecolor='black',
    error_kw=dict(ecolor='black', capsize=4, lw=1.5),
    hatch='.', zorder=3  # 设置 zorder 确保条形图在网格上方
)

# 绘制 TB 条形图 (橙色)
bars2 = ax.bar(
    x + (width + spe_width) / 2, TB_means, width, yerr=TB_errors,
    label='TB', color='coral', edgecolor='black',
    error_kw=dict(ecolor='black', capsize=4, lw=1.5),
    hatch='/', zorder=3  # 设置 zorder 确保条形图在网格上方
)

# 添加标签和标题
ax.set_ylabel('Test Accuracy', fontsize=16)
ax.set_xticks(x)  # 设置 x 轴刻度
ax.set_xticklabels(categories, fontsize=14)
ax.set_ylim(75, 100)  # 设置 y 轴范围

# 增大 y 轴刻度字体大小
ax.tick_params(axis='y', labelsize=14)

# 添加图例
ax.legend(loc='upper left', fontsize=15)

# 调整布局
plt.tight_layout()

# 保存图表
plt.savefig('domain_spec.png')