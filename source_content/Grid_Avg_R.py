import matplotlib.pyplot as plt
import numpy as np

# 数据
methods = ['PPO_Lag', 'CPPO_PID', 'FOCOPS']
avg_r_cp = [2.7, 2.01, 1.52]  # CP(our) 的平均值
avg_r_gc = [2.71, 2.0, 1.53]  # GC 的平均值
error_cp = [0.1, 0.1, 0.1]  # CP(our) 的误差
error_gc = [0.1, 0.25, 0.25]  # GC 的误差
baseline = 2.55  # PPO 的基准值


x = np.arange(len(methods))  # 横坐标
width = 0.35  # 柱状图宽度

# 图表
fig, ax = plt.subplots(figsize=(6, 4.5))

# 绘制柱状图
bars1 = ax.bar(x - width/2, avg_r_cp, width, yerr=error_cp, label='CP(our)', color='#A5B7D7', capsize=5)
bars2 = ax.bar(x + width/2, avg_r_gc, width, yerr=error_gc, label='GC', color='#ECC1A8', capsize=5)

# 添加基准线
ax.axhline(baseline, color='black', linestyle='--', linewidth=1.5)
ax.text(len(methods) - 0.5, baseline - 0.1, f'{baseline}', color='black', fontsize=14, ha='center')  # 标注基准线值往下移动


for i, bar in enumerate(bars1):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f"{avg_r_cp[i]:.2f}",
            ha='center', va='bottom', fontsize=16, color='saddlebrown', weight='bold')

for i, bar in enumerate(bars2):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, f"{avg_r_gc[i]:.2f}",
            ha='center', va='bottom', fontsize=16, color='royalblue', weight='bold')

# 坐标轴标签和标题
ax.set_ylabel('Avg. R', fontsize=29)  # 增大纵坐标标签字体
ax.set_xticks(x)
ax.set_xticklabels(methods, fontsize=22)  # 增大横坐标标签字体
ax.set_ylim(0, 2.999)  # 不显示 3.0
ax.tick_params(axis='y', labelsize=14)

# 图例
fig.legend(['PPO','CP(our)','GC'], loc='lower center', ncol=1, bbox_to_anchor=(0.55, 0.12), fontsize=18)

# 调整布局
plt.tight_layout()  # 留出图例的空间
plt.savefig('Grid_Avg_R.png')  # 保存图片