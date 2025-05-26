import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
y_BBV = [0.36, 0.7, 0.87, 0.92]
y_NNCB_IBP = [0.23, 0.58, 0.82, 0.90]
y_Ours = [0.53, 0.82, 0.88, 0.92]
y_Upper_bound = [0.78, 0.88, 0.96, 0.98]
x = np.array([2*10**2, 8*10**2, 4*10**3, 2*10**4])

fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size for better visualization

# Plotting the lines
ax.plot(x, y_BBV, label='BBV', marker='o', color='blue', linewidth=2, markersize=8)
ax.plot(x, y_NNCB_IBP, label='NNCB-IBP', marker='^', color='orange', linewidth=2, markersize=8)
ax.plot(x, y_Ours, label='Ours', marker='s', color='green', linewidth=2, markersize=8)
ax.plot(x, y_Upper_bound, label='Upper bound', linestyle='--', color='gray', linewidth=2, marker='>')


# Decorations
ax.set_xscale('log')  # Logarithmic scale for x-axis
ax.set_xlabel('Num. of boundary hyper-rectangles', fontsize=20, labelpad=10)
ax.set_ylabel('Verified Rate', fontsize=20, labelpad=10)
ax.set_title(r'$\alpha = 1.0$, $\text{adversarial training}$', fontsize=22, pad=15)

# Set ticks for x-axis
ax.set_xticks([10**3, 10**4])
ax.get_xaxis().set_major_formatter(plt.ScalarFormatter())  # Prevent scientific notation
ax.set_xticklabels(['10$^3$', '10$^4$'], fontsize=14)

# Set ticks for y-axis
ax.set_yticks(np.arange(0.2, 1.1, 0.1))
ax.set_yticklabels([f'{i:.1f}' for i in np.arange(0.2, 1.1, 0.1)], fontsize=18)

# Add legend
ax.legend(fontsize=20, loc='lower right', frameon=True)

# Grid customization
ax.grid(axis='y', linestyle='-', linewidth=0.5, alpha=0.7)  # Horizontal grid only

# Customizing vertical grid lines at specific x-ticks
plt.grid(True, which='major', axis='x', linestyle='-', linewidth=1, alpha=0.7)  # Default vertical grid
plt.gca().set_xticks([10**3, 10**4], minor=False)  # Set major ticks to align grid only at 10^3 and 10^4

# Adjust layout and save
plt.tight_layout()
plt.savefig('adversarial_1.0.png')
