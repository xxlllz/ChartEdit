import matplotlib.pyplot as plt
import numpy as np

# 数据
categories = ['w/o MBTI', 'w/ Hard', 'w/ Soft']
accuracy = [71, 73.2, 74]  # Accuracy 数据
f1_score = [72, 72.3, 73.8]  # F1 Score 数据

x = np.arange(len(categories))  # x轴位置
width = 0.3  # 柱的宽度

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 添加网格线，放在底层
ax.grid(axis='y', linestyle='-', color='gray', linewidth=0.8, alpha=0.7, zorder=0)  # 设置zorder=0

# 绘制柱状图
bar1 = ax.bar(x - width/2, accuracy, width, label='Accuary (%)', color='forestgreen', edgecolor='black', linewidth=2, zorder=2)
bar2 = ax.bar(x + width/2, f1_score, width, label='F1 Score (%)', color='royalblue', edgecolor='black', linewidth=2, zorder=2)

# 设置标题和标签
ax.set_ylim(69, 75)  # y轴范围
ax.set_ylabel('', fontsize=18)  # 空的y轴标签
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=18)  # 增大x轴刻度字体
ax.set_yticks(np.arange(69, 76, 1))
ax.tick_params(axis='y', labelsize=18, direction='in', length=5, width=1.5)
ax.tick_params(axis='x', labelsize=18, direction='in', length=5, width=1.5)

# 设置图表框为灰色
for spine in ax.spines.values():
    spine.set_color('gray')  # 将框的颜色设置为灰色
    spine.set_linewidth(0.5)  # 设置框线的宽度

# 添加图例，放在图表正上方
ax.legend(
    fontsize=16,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.15),
    ncol=2,
    frameon=False
)

# 调整布局，显示和保存图像
plt.tight_layout()
plt.savefig('downstream_2.png')
