import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 15, 25, 30])
y1 = np.array([0.76, 0.783, 0.782, 0.788])
y2 = np.array([0.75, 0.772, 0.771, 0.781])
y3 = np.array([0.702, 0.761, 0.765, 0.775])

plt.figure(figsize=(8, 6))

plt.plot(x, y1, marker='^', linestyle='-', color='darkred', markersize=20, linewidth=6, label='w l2I prior', markerfacecolor='none', markeredgewidth=6)
plt.plot(x, y2, marker='o', linestyle='-', color='#006580', markersize=20, linewidth=6, label='w T2I prior', markerfacecolor='none', markeredgewidth=6)
plt.plot(x, y3, marker='s', linestyle='-', color='grey', markersize=20, linewidth=6, label='w/o prior', markerfacecolor='none', markeredgewidth=6)

plt.xlabel('Training Steps: /k steps', fontsize=20)
plt.ylabel('', fontsize=16)

xticks = np.array([5, 10, 15, 20, 25, 30])
plt.xticks(xticks, fontsize=20)

# 修改纵坐标
plt.yticks(np.arange(0.70, 0.81, 0.02), fontsize=20)

# 禁用纵坐标的黑色竖线，仅保留横坐标的黑色横线
plt.tick_params(axis='y', which='both', length=0)  # 移除 y 轴刻度线
plt.tick_params(axis='x', which='both', direction='out', length=5, width=1)  # 保留 x 轴刻度线

# 去掉背景里竖着的线，仅保留水平线
plt.grid(axis='y', linestyle=':')

# 去掉坐标轴边框
for spine in plt.gca().spines.values():
    spine.set_visible(False)

# 修改图例位置为右下角
plt.legend(fontsize=25, loc='lower right')

plt.tight_layout()
plt.savefig('SSIM.png')
