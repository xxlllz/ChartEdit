import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# 矩阵数据（例如 Bartlett 窗函数结果）
data = np.array([
    [1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00],
    [0.31, 1.00, 0.00, 0.00, 0.00, 0.00, 0.00],
    [0.28, 0.37, 1.00, 0.00, 0.00, 0.00, 0.00],
    [0.27, 0.29, 0.62, 1.00, 0.00, 0.00, 0.00],
    [0.41, 0.46, 0.56, 0.48, 1.00, 0.00, 0.00],
    [0.32, 0.45, 0.67, 0.40, 0.74, 1.00, 0.00],
    [0.23, 0.32, 0.52, 0.35, 0.44, 0.46, 1.00],
])
# 绘制热图
plt.figure(figsize=(8, 6))
sns.heatmap(
    data, 
    annot=True, 
    cmap="rocket", 
    cbar=True, 
    square=True, 
    xticklabels=range(7), 
    yticklabels=range(7), 
    vmin=0, 
    vmax=1,
    annot_kws={"size": 14},
)
# plt.title("Heatmap with Diagonal as 1")
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout(pad=0)
plt.savefig('Heatmap1.png')

