import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11, 1)
y1 = [1, 0.8, 0.64, 0.56, 0.5, 0.42, 0.3, 0.25, 0.2, 0.13]
y2 = [0.7, 0.2, 0.12, 0.1, 0.07, 0.04, 0.03, 0.009, 0.003, 0.002]


plt.figure(figsize=(7, 5))
plt.plot(x, y1, 'o-', color='black', label='full block approx.', markerfacecolor='white', markersize=10, linewidth=2)
plt.plot(x, y2, 's--', color='black', label='per sub-block approx.', markerfacecolor='white', markersize=10, linewidth=2)
plt.yscale('log')
plt.xlabel('approx. order', fontsize=18)
plt.ylabel('relative approx. loss $\kappa$', fontsize=18)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlim(1, 10)
plt.ylim(10**-3, 1)
plt.grid(True, which='both', linestyle='--', linewidth=0.4)
plt.legend(fontsize=16, loc='lower left', frameon=True)
plt.tight_layout()
plt.savefig('approx-loss.png')