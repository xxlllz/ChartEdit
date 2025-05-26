import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 250, 100)
y1 = 4 * np.log(x + 1)**2

std = np.log(x**10)

plt.figure(figsize=(5, 4))  # Adjusted figure size
plt.plot(x, y1, label='Standard', color='tab:blue', linewidth=2)
plt.fill_between(x, y1 - 0.5 * std, y1 + 0.5 * std, color='tab:blue', alpha=0.3)

# Simulate another data set for comparison
y2 = 2 * np.log(np.sqrt(x))**2
plt.plot(x, y2, label='Invariant', color='tab:red', linewidth=2)
plt.fill_between(x, y2 - 0.2 * std, y2 + 0.2 * std, color='tab:red', alpha=0.3)

plt.title('CyclInv-3D', fontsize=14)

plt.xlim(0, 250)
plt.ylim(0, 150)
plt.xlabel('Number of evaluations', fontsize=15)
plt.ylabel('Cumulative regret', fontsize=15)

# Increase tick size
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)

plt.legend(loc='upper left', fontsize=15)
plt.tight_layout()
plt.savefig('cyclinv3d_ucb_regret.png')
