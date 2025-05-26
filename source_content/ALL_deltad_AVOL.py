import matplotlib.pyplot as plt
import numpy as np

# Data
x = [10**-3, 6*10**-3, 10**-2, 6*10**-2, 10**-1]
y1 = [0.11, 0.12, 0.13, 0.18, 0.17]  # DOW30
y2 = [0.45, 0.47, 0.58, 0.73, 0.78]  # NAS100
y3 = [0.6, 0.58, 0.58, 0.61, 0.75]  # Crypto10

# Plot
plt.figure(figsize=(8, 5))

# DOW30
plt.plot(
    x, y1, '-s', color='#3CB371',  # Darker green
    label='DOW30', linewidth=3, markersize=12,
    markeredgewidth=1.5, markeredgecolor='white'
)

# NAS100
plt.plot(
    x, y2, '--o', color='#FF8C00',  # Darker orange
    label='NAS100', linewidth=3, markersize=12,
    markeredgewidth=1.5, markeredgecolor='white'
)

# Crypto10
plt.plot(
    x, y3, ':d', color='#4682B4',  # Darker blue
    label='Crypto10', linewidth=3, markersize=12,
    markeredgewidth=1.5, markeredgecolor='white'
)

# Logarithmic scale for x-axis
plt.xscale('log')

# Customize x-ticks
xticks = [10**-3, 10**-2, 10**-1]
plt.xticks(xticks, labels=[r'$10^{-3}$', r'$10^{-2}$', r'$10^{-1}$'], fontsize=15)

# Customize y-ticks
plt.yticks(fontsize=15)  # Increase font size of y-axis ticks

# Labels and title
plt.xlabel(r'$\delta_d$', fontsize=14)
plt.ylabel('AVOL', fontsize=14)

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
plt.savefig('ALL_deltad_AVOL.png', dpi=300)
