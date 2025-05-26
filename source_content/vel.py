import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 5, 100)
y = 0.25/np.sqrt(x)

plt.figure(figsize=(8, 8))
plt.plot(x, y, 'b-', linewidth=2)
plt.xlim(1, 5)
plt.ylim(0.08, 0.27)
plt.xticks([1, 2, 3, 4, 5])  # 横坐标刻度
plt.yticks([0.10, 0.15, 0.20, 0.25])  # 纵坐标刻度
plt.xlabel('$x$', fontsize=20)
plt.ylabel('$v/c$', fontsize=20)

plt.text(3.5, 0.22, '$g_s=0.5$', fontsize=20, bbox=dict(facecolor='none', edgecolor='none', boxstyle='round,pad=0.3'))

plt.tick_params(axis='both', which='major', labelsize=14)
plt.grid(False)
plt.legend(frameon=False)
plt.tight_layout()
plt.savefig('vel.png')
