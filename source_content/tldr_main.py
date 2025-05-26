import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.logspace(-2.3, 1.3, 12)
x1 = np.delete(x, [1, 5])
MLE_y = [20.9, 20.9,20.6, 20.8, 21, 22.5, 23, 22.8,15,2.5,0.43,0.42]
MLE_y1 = [20.9, 20.6, 20.8, 21,  23.3, 23.1,16,1,0.43,0.42]
IQLearn_y = [26, 26, 25.9, 26, 24.5, 24.8,24.4, 20,3,0.3,0.3,0.4]
IQLearn_y1 = [25.9, 26, 25.8, 26.1, 24.4, 24.9,24.6, 22,0.5,0.3,0.3,0.4]
plt.figure(figsize=(8, 4))

# Plot lines with markers
plt.scatter(x1, MLE_y1, color='blue', marker='o',  s=50)  # 散点图，蓝色圆形
plt.scatter(x, IQLearn_y1, color='orange', marker='x', s=50)  # 散点图，红色正方形
plt.plot(x, MLE_y, color='blue', label='MLE')
plt.plot(x, IQLearn_y, label='IQLearn($\lambda = 0.5$)', color='orange')

# Set scale to logarithmic
plt.xscale('log')

plt.xlabel('Temperature', fontsize=20)
plt.ylabel('Rouge Lsum', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.legend(fontsize=15, loc='lower left')
plt.grid(True)

plt.tight_layout()
plt.savefig('tldr_main.png')