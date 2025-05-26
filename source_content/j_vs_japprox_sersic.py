import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Corrected sample data
x_well_described = np.array([2.1,2.12,2.2,2.0,2.2,2.16,3,3.8,4.4,4.5,5,5.9,6.1,6.7,5.9,5.6,4,4.5])
y_well_described = np.array([0.0,0.21,0.26,0.265,0.35,0.41,0.15,0.08,-0.01,-0.1,-0.07,-0.085,-0.105,-0.02,0.02,0.05,0.29,0.27])
x_poorly_described = np.array([3.7, 4, 4.3, 5.9, 6,6.5,8.3])
y_poorly_described = np.array([0.28, 0.32, -0.16, -0.23, -0.15,-0.05,-0.18])

plt.figure(figsize=(8, 6))

# Plot the well-described points
plt.scatter(x_well_described, y_well_described, label='Well described by S$e\u0301$rsic profile', color='cornflowerblue', s=100, edgecolor='black')

# Plot the poorly described points
plt.scatter(x_poorly_described, y_poorly_described, label='Poorly described by S$e\u0301$rsic profile', color='orange', s=100, edgecolor='black', marker='D')

# Add horizontal line at y=0
plt.axhline(0, color='gray', linestyle='--')

# Add labels, title, and legend
plt.xlim(1.2,8.8)
plt.xticks([2,4,6,8],fontsize=14)
plt.ylim(-0.25,0.43)
plt.yticks([-0.2,-0.1,0.0,0.1,0.2,0.3,0.4],fontsize=14)
plt.xlabel(r'$r_{eff}$ [kpc]', fontsize=18)
plt.ylabel(r'$\log_{10} (j_*/\tilde{j}_*)$', fontsize=18)
plt.tick_params(axis='both', which='major', labelsize=14,direction='inout',length=10)
plt.legend(fontsize=12, loc='upper right')

# Show plot
plt.tight_layout()
plt.savefig('j_vs_japprox_sersic.png')