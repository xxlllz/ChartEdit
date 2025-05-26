
import matplotlib.pyplot as plt
import numpy as np

# Data
x = [10**-3, 6*10**-3, 10**-2, 6*10**-2, 10**-1]
y1 = [0.25, 0.26, 0.3, 0.65, 0.6]  # DOW30
y2 = [0.68, 0.71, 1.23, 1.85, 1.75]  # NAS100
y3 = [0.10, 0.07, 0.08, 0.07, 0.38]  # Crypto10

# Plot
plt.figure(figsize=(8, 5))

# DOW30
plt.plot(x, y1, '-s', color='#2ca02c', label='DOW30', linewidth=4, markersize=12)  # Changed to greenish color

# NAS100
plt.plot(x, y2, '--o', color='#ff7f0e', label='NAS100', linewidth=4, markersize=12)  # Changed to orange

# Crypto10
plt.plot(x, y3, ':d', color='#1f77b4', label='Crypto10', linewidth=4, markersize=12)  # Changed to blue

# Logarithmic scale for x-axis
plt.xscale('log')

xticks = [10**-3, 10**-2, 10**-1]
plt.xticks(xticks, labels=[r'$10^{-3}$', r'$10^{-2}$', r'$10^{-1}$'], fontsize=12)

# Labels and title
plt.xlabel(r'$\delta_d$', fontsize=14)
plt.ylabel('APR', fontsize=14)

# Legend
plt.legend(fontsize=20, loc='best', frameon=True)

# Modify spines (border color)
ax = plt.gca()  # Get current axes
for spine in ax.spines.values():
    spine.set_edgecolor('gray')
    spine.set_linewidth(1.5)  # Optional: Adjust border thickness

# Grid and layout
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

# Save the plot
plt.savefig('APR_vs_delta.png', dpi=300)