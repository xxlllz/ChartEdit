import matplotlib.pyplot as plt
import numpy as np


labels = ['en → de', 'en → ha\'', 'de\' → en', 'ha\' → en']
colors = ['peachpuff', 'coral', 'cornflowerblue', 'peachpuff', 'coral', 'cornflowerblue']
categories = ['sent. noise\n(32)', 'word noise\n(32)', 'clean\n(32)', 'sent. noise\n(1024)', 'word noise\n(1024)', 'clean\n(1024)']
hatches = [None, None, None, 'o', 'o', 'o']

data_1_values = np.array([
    [73, 75, 72, 74],
    [62, 68, 71.5, 74],
    [80, 77, 75, 72],
    [81, 75, 68, 73],
    [75, 72, 79, 74],
    [82, 81, 61, 72]
])

data_2_values = np.array([
    [78, 79, 81, 83],
    [72, 75, 80, 83],
    [81, 81, 82, 81],
    [77, 80, 83, 82],
    [64, 67, 81, 83],
    [78, 80, 83, 81]
])


# 创建图形和子图
fig, axs = plt.subplots(2, 1, figsize=(7, 4))  # 2行1列

# 设置柱子的宽度
bar_width = 0.15
index = np.arange(len(labels))  # X轴位置

# 绘制第一个子图
for i, (category, color, hatch) in enumerate(zip(categories, colors, hatches)):
    axs[0].bar(index + i * bar_width, data_1_values[i], bar_width, color=color, edgecolor='black', label=category, hatch=hatch)

axs[0].set_xlabel('Training direction', fontsize=12)
axs[0].set_ylabel('COMET\n$Avg_{en→X}$', fontsize=12)
axs[0].set_xticks(index + bar_width * 2.5)  # 将标签放在柱子的中间
axs[0].set_xticklabels(labels, fontsize=12)
axs[0].set_ylim([55, 85])
axs[0].legend(bbox_to_anchor=(0.5, 1.6), loc='upper center', ncol=6, fontsize=9)
axs[0].tick_params(axis='y', labelsize=12)

# 绘制第二个子图
for i, (category, color, hatch) in enumerate(zip(categories, colors, hatches)):
    axs[1].bar(index + i * bar_width, data_2_values[i], bar_width, color=color, edgecolor='black', label=category, hatch=hatch)

axs[1].set_xlabel('Training direction', fontsize=14)
axs[1].set_ylabel('COMET\n$Avg_{X→en}$', fontsize=14)
axs[1].set_xticks(index + bar_width * 2.5)  
axs[1].set_xticklabels(labels, fontsize=12)
axs[1].set_ylim([55, 85])
axs[1].tick_params(axis='y', labelsize=12)

plt.tight_layout()

# 保存图表
plt.savefig('comet.png', dpi=150)