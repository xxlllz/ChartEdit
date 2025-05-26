import matplotlib.pyplot as plt
import numpy as np

x = np.array([1e3, 1e4, 1e5, 1e6])  # x轴 (log scale)

y1 = np.array([1000, 180, 20, 6])  # Approx+Shuffling [EFM+19]
y2 = np.array([800, 60, 8, 1.5])    # Approx+Shuffling+Sampling [GDD+21]
y3 = np.array([700, 40, 6, 1.2])    # Camel

plt.figure(figsize=(8, 6))


plt.plot(x, y1, 'm-o', label='Approx+Shuffling [EFM+19]', linewidth=3, markersize=15)
plt.plot(x, y2, 'c-^', label='Approx+Shuffling+Sampling [GDD+21]', linewidth=3, markersize=15)
plt.plot(x, y3, 'r-*', label='Camel', linewidth=3, markersize=15)

plt.xscale('log')
plt.yscale('log') 

plt.xlabel(r'# of (Shuffled) Messages $N$', fontsize=20)
plt.ylabel(r'Approximate DP $\epsilon$', fontsize=20)


plt.title(r'$\gamma = 0.5, \delta = 10^{-5}, \epsilon_0 = 1.9, T = 500$', fontsize=20)

plt.xticks(fontsize=20)
plt.yticks(fontsize=20) 

plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.legend(fontsize=16, loc='upper right')


plt.tight_layout()
plt.savefig('bound_vary_gamma.png')