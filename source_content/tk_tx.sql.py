import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = ['S1', 'S2', 'S3', 'S4']
y_true = [3600, 14200, 10400, 8100]
y_est = [3600, 13800, 10600, 8000]

y_true = np.array(y_true)
errors_true = np.array([50, 30, 40, 20])
errors_est = np.array([100, 80, 60, 50])

# Plot
plt.plot(x, y_true, 'o-', color='blue', label='True Card.', linewidth=0.8,markersize=4 )
plt.errorbar(x, y_est, yerr=errors_est, fmt='-+', color='orange', label='Refreshed Est.',markersize=12,  # 调整标记大小
    linewidth=0.8 ) # 调整线条粗细)

# 直接定义要注释的数字列表
annotations = [1.005, 1.033, 1.018, 1.012]  # 按顺序提供注释值

# Annotate data points
for i, value in enumerate(annotations):
    plt.annotate(f'{value:.3f}',  # 格式化为三位小数
                 (i, (y_true[i] + y_est[i]) / 2),  # 注释位置
                 color='orange', fontsize=19, 
                 ha='center', va='bottom')


plt.xticks(rotation=0,fontsize=16)  # Ensure x-tick labels are horizontal
plt.yticks(fontsize=16)
plt.ylabel('Cardinality',fontsize=20)
plt.legend(loc='lower right',fontsize=18)
plt.tight_layout()
plt.savefig('tk_tx.sql.png')