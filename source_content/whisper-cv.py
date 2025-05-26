import matplotlib.pyplot as plt
import numpy as np

# Data for boxplot, assuming similar to visual
np.random.seed(0)
# 定义均值和方差（标准差逐渐减小）
means = [0.69, 0.72, 0.76, 0.76, 0.77, 0.8]
std_devs = [0.03, 0.03, 0.025, 0.02, 0.02, 0.015]  # 方差逐渐减小

# 生成数据
data = [np.random.normal(mean, std_dev, 100) for mean, std_dev in zip(means, std_devs)]

# 添加离群点（位于最后一组数据的下方）
outliers = [0.74, 0.73]
data[-1] = np.concatenate((data[-1], outliers))

# Create box plot
plt.figure(figsize=(8, 6))

boxprops = dict(linewidth=1.5)
medianprops = dict(linestyle='-', linewidth=1, color='black')  # 更改中位线颜色为黑色
meanlineprops = dict(linestyle='-', linewidth=2, color='k')

# Create the boxplot
bplot = plt.boxplot(data, patch_artist=True, boxprops=boxprops, medianprops=medianprops, showmeans=False, meanprops=meanlineprops, widths=0.8)

# 设置每个箱子颜色
colors = ['lightblue', 'lightsalmon', 'lightgreen', 'lightcoral', 'thistle', 'lightgray']

# 填充每个箱子的颜色
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)

# 设置离群点的样式
bplot['fliers'][0].set(marker='o', color='red', alpha=0.7)  # 设置离群点样式（红色）
bplot['fliers'][0].set(markerfacecolor='red', markeredgecolor='red', markersize=7)

# Add horizontal line for transcription
plt.axhline(y=0.8, color='green', linestyle=':', linewidth=1.5, label='Manual transcription')

# 设置标签
plt.xticks([1, 2, 3, 4, 5, 6], ['≥ 50', '(50, 40]', '(40, 30]', '(30, 20]', '(20, 10]', '(10, 0]'], fontsize=10)
plt.ylabel('AD Detection Accuracy', fontsize=12)
plt.xlabel('Word Error Rate (%)', fontsize=12)
plt.yticks(np.arange(0.60, 0.90, 0.05), fontsize=10)

# Move the legend to the lower right corner
plt.legend(loc='lower right')

# 设置网格
plt.grid(axis='y', linestyle='-', linewidth=0.5)

# 自动调整布局
plt.tight_layout()

# 保存图片
plt.savefig('whisper-cv.png')
