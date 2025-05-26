import matplotlib.pyplot as plt

# Sample data
x = [6, 10, 14, 18, 22, 26]
y1 = [35.7, 36.2, 36.5, 36.8, 36.9, 37.0]
y2 = [35.1, 35.8, 36.45, 36.81, 36.9, 37.0]
y3 = [34.1, 34.8, 35.4, 36.0, 36.4, 36.75]
y4 = [34.7, 34.8, 34.85, 34.9, 34.95, 35.00]

plt.figure()

# 绘制曲线
plt.plot(x, y1, 'o-', color='red', label='Ours')
plt.plot(x, y2, 'o-', color='teal', label='W/O div ISO')  # 使用更暗的 cyan 颜色
plt.plot(x, y3, 'o-', color='blue', label='W/O shuffle')
plt.plot(x, y4, 'o-', color='magenta', label='Fine-tuning')

# 设置标题和轴标签
plt.title('Sony', fontsize=16)
plt.xlabel('Size of Target Domain Data', fontsize=14, fontweight='bold')
plt.ylabel('PSNR(dB)', fontsize=14, fontweight='bold')

# 设置刻度字体大小
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# 设置 y 轴范围
plt.ylim(34.0, 37.0)

# 调整图例的位置到 magenta 线的上方
plt.legend(fontsize=12, loc='upper center', bbox_to_anchor=(0.8, 0.66))  # 图例放置在图形上方


# 保存图像
plt.tight_layout()
plt.savefig('Sony.png')
