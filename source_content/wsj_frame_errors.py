import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data for the confusion matrix
data = np.array([[ 0,  1,  0,  0,  0],
                 [ 0,  0,  1,  0,  0],
                 [ 0,  0, 14,  0,  0],
                 [ 0,  0,  1,  0,  0],
                 [ 0,  0,  1,  0,  0]])

# Label names
labels = ['business', 'industry', 'macro', 'government', 'other']

# Create the confusion matrix plot
fig,ax = plt.subplots(figsize=(5, 4))
ax1=sns.heatmap(data, annot=True, fmt="d", cmap="Blues", cbar=True,
            xticklabels=labels, yticklabels=labels)

# Add labels and title
plt.xticks(rotation=45,ha='right')
plt.yticks(rotation=360)
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.tick_params(axis='both', which='both', direction='out', length=6)
# 确保底部和左侧边框可见
colorbar = ax1.collections[0].colorbar
colorbar.outline.set_edgecolor('black')  # 设置边框颜色为黑色
colorbar.outline.set_linewidth(1)  # 设置边框宽度为 2
ax.spines['bottom'].set_visible(True)  # 显示底部边框
ax.spines['left'].set_visible(True)    # 显示左侧边框

# 如果需要，可以设置其他边框为不可见
ax.spines['top'].set_visible(True)
ax.spines['right'].set_visible(True)
plt.subplots_adjust(bottom=0.2,left=0.2,top=0.8,right=0.8)

plt.title('WSJ Article-Level Type Prediction Errors',fontsize=10)
plt.tight_layout()
plt.savefig('wsj_frame_errors.png')

