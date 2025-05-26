import matplotlib.pyplot as plt
import numpy as np

# Generate random data for histogram
data = np.random.normal(0, 1, 10000)

# Create histogram
plt.hist(data, bins=50, color='white', edgecolor='blue', histtype='stepfilled', linewidth=1.5, label=r'All S$_{3 \mathrm{GHz}}$')

# Add vertical line
plt.axvline(x=-0.7, color='black', linestyle='--', linewidth=1, label=r'$\alpha = -0.7$')

# Add labels and legend
plt.xlabel(r'$\alpha$', fontsize=15)
plt.ylabel(r'$n$', fontsize=15)
plt.legend(loc='upper right')

# Save and show plot
plt.tight_layout()
plt.savefig('alpha_hist.png')
