import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

plt.style.use('_mpl-gallery')

# Make data
n = 100
xs = np.linspace(-2, 0, n)
ys = np.sin(xs * np.pi)
zs = np.cos(xs * np.pi)

# Create a colormap for the gradient
colors = np.linspace(0, 1, n)
cmap = LinearSegmentedColormap.from_list("gradient", ["blue", "red"])

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(6, 5))
for i in range(n - 1):
    ax.plot(xs[i:i + 2], ys[i:i + 2], zs[i:i + 2], color=cmap(colors[i]), linewidth=2)

# Set ticks for x, y, z axes
ax.set_xticks(np.linspace(-2, 0, 5))  # 5 ticks from -2 to 0
ax.set_yticks(np.linspace(-1, 1, 5))  # 5 ticks from -1 to 1
ax.set_zticks(np.linspace(-1, 1, 5))  # 5 ticks from -1 to 1

# Optionally, set tick labels
ax.set_xticklabels([f'{x:.1f}' for x in np.linspace(-2, 0, 5)])
ax.set_yticklabels([f'{y:.1f}' for y in np.linspace(-1, 1, 5)])
ax.set_zticklabels([f'{z:.1f}' for z in np.linspace(-1, 1, 5)])

plt.tight_layout()
# Save the figure
plt.savefig('3d_line.png')