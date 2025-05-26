import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([2*10**2, 8*10**2, 4*10**3, 2*10**4])
y1 = np.array([0.42, 0.73, 0.89, 0.94])  # Adjusted values
y2 = np.array([0.25, 0.60, 0.83, 0.90])  # Adjusted values
y3 = np.array([0.52, 0.74, 0.90, 0.94])  # Adjusted values
y4 = np.array([0.81, 0.90, 0.97, 0.98])  # Adjusted values

plt.figure(figsize=(8, 6))

# Plotting the lines with markers and colors
plt.plot(x, y1, 'o-', label='BBV', color='blue', markersize=8, linewidth=2)
plt.plot(x, y2, '^-', label='NNCB-IBP', color='orange', markersize=8, linewidth=2)
plt.plot(x, y3, 's-', label='Ours', color='green', markersize=8, linewidth=2)
plt.plot(x, y4, '*-', label='Upper bound', color='gray', linewidth=2)

# Adding labels and title
plt.xlabel('Num. of boundary hyper-rectangles', fontsize=16, labelpad=10)
plt.ylabel('Verified Rate', fontsize=16, labelpad=10)
plt.title(r'$\alpha = 0.5$, adversarial training', fontsize=18, pad=15)

# Logarithmic scale for x-axis
plt.xscale('log')
plt.xticks([10**3, 10**4], labels=['10$^3$', '10$^4$'], fontsize=14)
plt.yticks(np.arange(0.3, 1.1, 0.1), fontsize=14)

# Adding grid lines with vertical emphasis only at 10^3 and 10^4
plt.grid(True, which='both', axis='y', linestyle='-', linewidth=0.5, alpha=0.7)  # Horizontal grid lines

# Customizing vertical grid lines at specific x-ticks
plt.grid(True, which='major', axis='x', linestyle='-', linewidth=1, alpha=0.7)  # Default vertical grid
plt.gca().set_xticks([10**3, 10**4], minor=False)  # Set major ticks to align grid only at 10^3 and 10^4

# Adding legend
plt.legend(fontsize=14, loc='lower right', frameon=True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Save and show plot
plt.savefig('adversarial_0.5.png', dpi=300)
