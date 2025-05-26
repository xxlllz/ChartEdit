import matplotlib.pyplot as plt
import numpy as np
# 数据
ratios = [1.0, 0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0.05, 0.0]
accuracies = [25.81, 25.72, 25.56, 25.4, 24.43, 24.84, 23.93, 23.32, 21.51, 19.72, 19.72, 17.96]

# 绘图
plt.figure(figsize=(7, 5))
plt.plot(ratios, accuracies, 'o-', color='brown', markersize=8)

# 标注数据点
for i, txt in enumerate(accuracies):
    if i % 2 == 1: 
        plt.annotate(f'{txt}', (ratios[i], accuracies[i]), textcoords="offset points", xytext=(0,5), ha='center', fontsize=12)

# 标签和标题
plt.xlabel('Ratio of visual token kept', fontsize=18)
plt.ylabel('Accuracy', fontsize=18)
plt.title('Accuracy on ChartQA', fontsize=22)

for x, y in zip(ratios, accuracies):
    plt.axvline(x=x, color='gray', linestyle='--', linewidth=1)  # 垂直于横轴的虚线
    plt.axhline(y=y, color='gray', linestyle='--', linewidth=1)  # 垂直于纵轴的虚线

# 垂直线和阴影区域
plt.plot([ratios[3], ratios[3]], [0, accuracies[3]], color='brown', linestyle='--')  # 第一条竖线
plt.plot([ratios[5], ratios[5]], [0, accuracies[5]], color='brown', linestyle='--') 
plt.text(0.8, 18, '90%', color='brown', ha='center', fontsize=15)
plt.text(0.6, 18, '80%', color='brown', ha='center', fontsize=15)
plt.fill_between(ratios, accuracies, 17.5, where=(np.array(ratios) >= 0.5) & (np.array(ratios) <= 0.7), color='brown', alpha=0.1)
plt.fill_between(ratios, accuracies, 17.5, where=(np.array(ratios) >= 0.7) & (np.array(ratios) <= 1.0), color='brown', alpha=0.2)
plt.ylim(17.5, 26.5)

plt.margins(x=0)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

ax = plt.gca()
ax.invert_xaxis()

plt.tight_layout()
plt.savefig('chartqa_acc.png')
