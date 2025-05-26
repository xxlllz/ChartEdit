import matplotlib.pyplot as plt
import numpy as np

# 数据：x 轴是数据集大小，y 是 MIA F1 分数
dataset_size = [20, 40, 60, 80, 100, 120, 140, 160, 180, 200]
known_nms_values = {
    10: [0.93, 0.96, 0.99, 0.97, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    20: [0.98, 0.99, 0.98, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    30: [0.97, 0.98, 0.98, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    40: [0.96, 0.99, 0.98, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    50: [0.97, 0.99, 0.99, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
}

# 假设每条曲线的置信区间
ci_values = {
    10: [0.07, 0.04, 0.01, 0.03, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    20: [0.02, 0.01, 0.02, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    30: [0.03, 0.02, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    40: [0.04, 0.01, 0.02, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    50: [0.03, 0.01, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
}

# Sentence MIA F1 红色虚线
sentence_mia_f1 = 0.79

# 设置浅色颜色和标签
colors = ['#5DA5C4', '#6DBD76', '#E57373', '#F39C55', '#9E77B5']
labels = [f'Known NMs: {k}' for k in known_nms_values.keys()]

# 绘图
plt.figure(figsize=(8, 5))
for i, (k, v) in enumerate(known_nms_values.items()):
    ci = ci_values[k]
    # 绘制曲线和置信区间
    plt.plot(dataset_size, v, label=labels[i], marker='o', color=colors[i])
    plt.fill_between(dataset_size, np.array(v) - np.array(ci), np.array(v) + np.array(ci),
                     color=colors[i], alpha=0.2)

# 绘制红色虚线
plt.axhline(sentence_mia_f1, color='red', linestyle='--', label='Sentence MIA F1')

# 添加标签和标题
plt.xlabel('Dataset Size (# questions)', fontsize=16)
plt.ylabel('Dataset MIA F1', fontsize=16)

# 设置 X 轴的刻度
plt.xticks(dataset_size, fontsize=15)
plt.yticks(fontsize=15)
plt.ylim(0.75, 1.02)

# 添加网格线
plt.grid(True, linestyle='-', alpha=0.5)

# 图例设置
plt.legend(loc='upper left', fontsize=13, shadow=False, edgecolor='gray',
           bbox_to_anchor=(0.65, 0.8), facecolor='lightgray', framealpha=0.5)


# 保存并显示
plt.tight_layout()
plt.savefig('cot-v2.png')
plt.show()
