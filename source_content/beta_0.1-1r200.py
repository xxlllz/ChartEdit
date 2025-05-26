import matplotlib.pyplot as plt
import numpy as np

# Sample data
x_tng300 = np.array([13, 13.2, 13.4, 13.6, 13.8, 14, 14.2, 14.4])
y_tng300 = np.array([0.03, 0.06, 0.09, 0.12, 0.13, 0.16, 0.22, 0.18])

x_tng100 = np.array([12.4, 12.7, 13, 13.2, 13.4, 13.6, 13.8, 14, 14.2])
y_tng100 = np.array([-0.11, -0.06, -0.02, 0, 0, 0.1, 0.12, 0.2, 0.15])

x_tng50 = np.array([11.5, 11.8, 12.1, 12.4, 12.7, 13, 13.3, 13.5])
y_tng50 = np.array([-0.17, -0.24, -0.17, -0.18, -0.1, 0.04, 0.07, 0.08])

# Error bars
error_tng300 = np.array([0.01, 0.01, 0.0, 0.01, 0.0, 0.01, 0.03, 0.08])
error_tng100 = np.array([0.02, 0.02, 0.03, 0.03, 0.03, 0.02, 0.07, 0.09, 0.06])
error_tng50 = np.array([0.02, 0.02, 0.03, 0.04, 0.05, 0.10, 0.07, 0.06])

# Plot data
plt.figure(figsize=(6, 4))
plt.errorbar(x_tng300, y_tng300, yerr=error_tng300, fmt='o-', color='blue', label='TNG300', markersize=8, linewidth=2)
plt.errorbar(x_tng100, y_tng100, yerr=error_tng100, fmt='*-', color='orange', label='TNG100', markersize=12, linewidth=2)
plt.errorbar(x_tng50, y_tng50, yerr=error_tng50, fmt='^-', color='green', label='TNG50', markersize=8, linewidth=2)

# Labels and grid
plt.xlabel(r'$\log_{10}(M_{200c}/M_\odot)$', fontsize=18)
plt.ylabel(r'$\beta$', fontsize=18)
plt.legend(fontsize=12, loc='upper left', frameon=True)
plt.grid(True, linestyle='--', alpha=0.6)

# Save the figure
plt.tight_layout()
plt.savefig('beta_0.1-1r200.png',dpi=300)
