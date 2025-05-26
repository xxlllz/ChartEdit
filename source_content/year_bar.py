import matplotlib.pyplot as plt
import numpy as np

years = ['2010', '2011', '2012', '2013', '2014']
birth_rates = [19, 18, 17, 16, 15]

# 引入一个数据系列：假设是全球各国的平均出生率，作参考线
global_avg_rates = [19.5, 18.7, 17.5, 16.3, 15.2]  # 假设的全球平均出生率

# 设置条形图的宽度
bar_width = 0.3

# 计算X轴的位置
index = np.arange(len(years))

# 创建图表
fig, ax = plt.subplots(figsize=(10, 6))

# 绘制条形图：出生率数据
rects1 = ax.bar(index, birth_rates, bar_width, label='Birth Rate', color='darkseagreen', alpha=0.8, zorder=2)

# 绘制参考线：全球平均出生率
rects2 = ax.plot(index, global_avg_rates, label='Global Average', color='coral', marker='o', linestyle='--', linewidth=2, markersize=8, zorder=2)

# 添加网格
ax.yaxis.grid(True, linestyle='--', alpha=0.6, zorder=0)

# 设置标签和标题
ax.set_xlabel('Years', fontsize=18)
ax.set_ylabel('Birthrate per 1000 Population', fontsize=18)

# 调整X轴标签
ax.set_xticks(index)
ax.set_xticklabels(years, fontsize=15)

# 设置Y轴的刻度范围
ax.set_yticks(np.arange(10, 21, 2))
ax.set_ylim(10, 22)
ax.tick_params(axis='y', labelsize=15)

# 移除图表边框
for spine in ax.spines.values():
    spine.set_visible(False)

# 调整图例
ax.legend(loc='upper right', fontsize=12)

# 确保布局紧凑
fig.tight_layout()

# 保存图表
plt.savefig("year_bar.png")