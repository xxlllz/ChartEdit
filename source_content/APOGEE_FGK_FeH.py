import numpy as np
import matplotlib.pyplot as plt

# Generate random data
x1 = np.random.normal(-1, 0.5, 5000)
x2 = np.random.normal(1, 0.5, 5000)
x = np.concatenate([x1, x2])
y = x + np.random.normal(0, 0.3, 10000)

# Create the hexbin plot
plt.figure(figsize=(8, 6))
hb = plt.hexbin(x, y, gridsize=60, cmap='Oranges', bins='log', extent=(-3, 3, -3, 3))

# Add colorbar
cb = plt.colorbar(hb, label='log(N)')

# Modify colorbar tick parameters
cb.ax.tick_params(labelsize=14)  # Set colorbar tick label font size

# Add a diagonal line
plt.plot([-3, 3], [-3, 3], color='black', lw=1)

# Set labels
plt.xlabel('Pred ([Fe/H]) (dex)', fontsize=18)
plt.ylabel('APOGEE ([Fe/H]) (dex)', fontsize=18)

# Add text annotation
plt.text(-2.8, 2.8, '$\mu = -0.03, \sigma = 0.11$', fontsize=18,
         bbox=dict(facecolor='white', alpha=0.8, boxstyle='round,pad=0.2'))

# Modify tick parameters for axes
plt.tick_params(axis='both', which='major', labelsize=15)
plt.tick_params(axis='both', which='minor', labelsize=15)

# Save the figure
plt.savefig('APOGEE_FGK_FeH.png')