import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 数据，用于生成热图，对角线为 1
matrix_data = np.array([
    [1, 0, 0, 0, 0, 0, 0],
    [0.3, 1, 0, 0, 0, 0, 0],
    [0.22, 0.4, 1, 0, 0, 0, 0],
    [0.2, 0.28, 0.53, 1, 0, 0, 0],
    [0.3, 0.48, 0.51, 0.45, 1, 0, 0],
    [0.29, 0.5, 0.55, 0.37, 0.82, 1, 0],
    [0.15, 0.33, 0.46, 0.32, 0.43, 0.43, 1]
])

# 绘制热图
plt.figure(figsize=(8, 6))
sns.heatmap(
    matrix_data, 
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
plt.tight_layout()
plt.savefig('Heatmap0.png')
