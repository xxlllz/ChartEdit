import matplotlib.pyplot as plt
import numpy as np

# Sample data
epochs = np.array([1, 2, 3, 4, 5])
mae_values = np.array([0.64, 0.60, 0.56, 0.50, 0.46])
mse_values = np.array([0.69, 0.65, 0.60, 0.55, 0.50])

# Create a plot
plt.figure(figsize=(7, 5.5))
plt.plot(epochs, mae_values, label='MAE', color='orange', marker='*', linewidth=3.5, markersize=10)
plt.plot(epochs, mse_values, label='MSE', color='navy', marker='v', linewidth=3.5, markersize=10)

# Add labels and legend
plt.ylabel('Loss', fontsize=14)
plt.xlim(0.7,5.3)
xticks = [1, 2, 3, 4, 5]  # 实际 x 坐标的位置
xticklabels = [100,200,300,500,800]  # 显示的标签
plt.xticks(xticks,xticklabels,fontsize=16)  # 设置刻度位置

plt.yticks([0.4,0.6,0.8,1.0],fontsize=16)
plt.legend(loc='upper right', fontsize=16,ncol=2,edgecolor='none')
# plt.xlim(100, 800)
plt.ylim(0.4, 1.0)
plt.xticks(epochs)

# Show plot
plt.tight_layout()
plt.savefig('traffic_herding.png')
