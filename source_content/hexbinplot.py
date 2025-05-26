import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19)

# Increase the number of points and modify the data distribution
n = 500_000 
x = np.random.standard_normal(n) * 3  # Larger spread of x
y = 2.0 + 3.0 * x + 4.0 * np.random.standard_normal(n) * 2  # Larger spread of y

xlim = x.min(), x.max()
ylim = y.min(), y.max()

fig, ax = plt.subplots(figsize=(6, 6))

hb = ax.hexbin(x, y, gridsize=50, bins='log', cmap='twilight')  # 'twilight' is a unique color map
ax.set(xlim=xlim, ylim=ylim)
cb = fig.colorbar(hb, ax=ax, label='Counts')
cb.ax.tick_params(labelsize=12) 
cb.set_label('Counts', fontsize=16)

# Customize ticks and legends
ax.tick_params(axis='both', labelsize=14)

plt.tight_layout()
plt.savefig('hexbinplot.png')