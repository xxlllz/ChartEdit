import matplotlib.pyplot as plt
import numpy as np

# Data for the bubble chart
labels = ['Siam R-CNN', 'LTMU', 'GlobalTrack', 'KYS', 'Ocean', 'PrDiMP', 'ATOM',  'DiMP', 'SiamAttn', 'MAML-FCOS', 'Ours-ST101', 'Ours-ST50']
speed = [5, 12.5, 6, 20, 25, 30, 30, 43, 45, 42.5, 32.5, 42]  # x-axis
success = [64.9, 57.4, 52, 55.5, 56.00, 59.8, 51.5, 57, 56, 52.3, 67.3, 66]  # y-axis
area = [6000, 1200, 200, 900, 1800, 6000, 2500, 5600, 5600, 4500, 8000, 8000]  # Size of the bubbles
colors = ['olive', 'gold', 'blue', 'magenta', 'seagreen', 'orange', 'grey',  'purple', 'orange', 'green', 'red', 'red']

plt.figure(figsize=(10, 6))

# Creating bubble chart
for i in range(len(speed)):
    plt.scatter(speed[i], success[i], s=area[i], color=colors[i], alpha=0.3, edgecolor=colors[i], linewidth=1)
    plt.scatter(speed[i], success[i],  color=colors[i],s=10)
    plt.text(speed[i], success[i] + 1 , labels[i], fontsize=14, ha='center')

# Customizing the plot
title_font = {'size':'18'}
label_font = {'size':'16'}
grid_font = {'size':'14'}


# 添加竖线 (vertical line)
plt.axvline(speed[0], color='grey', linestyle='-', linewidth=0.5,alpha=0.5)
plt.xlabel('Speed (FPS)', **label_font)
plt.ylabel('Success', **label_font)
plt.xlim(0, 50)
plt.ylim(50, 70)
plt.grid(True, linestyle='--', linewidth=0.5)

plt.xticks( fontsize=16)
plt.yticks( fontsize=16)

ax = plt.gca()
# 设置每个边框的粗细
for spine in ax.spines.values():
    spine.set_linewidth(2)  # 设置边框粗细为2点
    
plt.tight_layout()
plt.savefig('scatter5.png')