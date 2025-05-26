import matplotlib.pyplot as plt
import numpy as np

# 设置数据
models = ['GPT-4o', 'InternVL2-76B', 'InternVL2-8B', 'Qwen2-VL-7B', 'TinyChart(3B)', 'ChartCoder(7B)']
chartqa = [85.7, 88.4, 83.3, 83.0, 83.6, 0]  # ChartQA 数据
chartmimic = [83.3, 62.2, 40.5, 35.0, 25.9, 74.0]  # ChartMimic 数据

bar_width = 0.35  # 每个柱子的宽度
index = np.arange(len(models))  # 模型的索引
# 创建图形
fig, ax = plt.subplots(figsize=(11, 6))

# 绘制柱状图
bar1 = ax.bar(index - bar_width / 2, chartqa, bar_width, label='ChartQA', color="#f9c3bf", linewidth=1.2)
bar2 = ax.bar(index + bar_width / 2, chartmimic, bar_width, label='ChartMimic', color="#bfe4ee", linewidth=1.2)

# 计算并绘制 Delta 差异
for i in range(len(models)):
    if chartqa[i] > 0 and chartmimic[i] > 0:  # 过滤无效数据
        delta = chartqa[i] - chartmimic[i]
        delta_percentage = (delta / chartqa[i]) * 100

        # 添加差异文本
        ax.text(
            index[i], 
            max(chartqa[i], chartmimic[i]) + 3, 
            f"Δ=-{abs(delta_percentage):.1f}%", 
            color='darkred' if delta > 0 else 'blue',
            ha='center', 
            fontsize=16
        )
ax.plot(index+bar_width/2, chartmimic, color="#79add6", marker='o', linestyle='-', linewidth=2)

# 添加数据标签
def add_data_labels(bars, color, offset=1):
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, height + offset,  f'{height:.1f}', color=color, ha='center', va='bottom', fontsize=15)


# 设置X轴标签
ax.set_xticks([0,1,2,3,4, 5+0.35/2])
ax.set_xticklabels(models, fontsize=15)

# 添加标题和标签
ax.set_ylabel('Performance', fontsize=20)
ax.set_ylim(20, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels([20, 40, 60, 80, 100], fontsize=15)

# 添加图例
ax.legend(loc='upper right', bbox_to_anchor=(1.01, 0.95), fontsize=15)

# 美化图形
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# 调整布局
plt.tight_layout()

# 保存并显示图表
plt.savefig('delta_chart_comparison.png')