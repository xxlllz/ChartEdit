import matplotlib.pyplot as plt
import numpy as np

# Data
beta_values = np.array([1, 2, 4, 5, 10, 15])
near_ood = np.array([76.5, 76.58, 76.70, 76.68, 76.85, 76.88])
far_ood = np.array([96.60, 96.50, 96.40, 96.36, 96.34, 96.30])

# Create the plot
fig, ax1 = plt.subplots()

# Create a secondary y-axis
ax2 = ax1.twinx()

# Plot data on both y-axes
ax1.plot(beta_values, near_ood, color='firebrick', marker='*', linestyle='-', label='Near-OOD', linewidth=2, markersize=12)
ax2.plot(beta_values, far_ood, color='mediumblue', marker='^', linestyle='-', label='Far-OOD', linewidth=2, markersize=12)

# Set labels
ax1.set_xlabel(r'$\beta$ values', fontsize=16)  # Use r-string for LaTeX
ax1.set_ylabel('Near-OOD AUROC', color='firebrick', fontsize=16)
ax2.set_ylabel('Far-OOD AUROC', color='mediumblue', fontsize=16)

# Set axis limits
ax1.set_ylim(75, 77)
ax2.set_ylim(95, 97)

# Set tick parameters and increase tick label size
ax1.tick_params(axis='y', labelcolor='firebrick', labelsize=16)
ax2.tick_params(axis='y', labelcolor='mediumblue', labelsize=16)
ax1.tick_params(axis='x', labelsize=14)

# Set x-axis ticks
ax1.set_xticks([0, 5, 10, 15])  # Specify the ticks to display

# Combine legends from both axes
line1, label1 = ax1.get_legend_handles_labels()
line2, label2 = ax2.get_legend_handles_labels()
ax1.legend(line1 + line2, label1 + label2, fontsize=15)

# Adjust layout and save the figure
plt.tight_layout()
plt.savefig('beta_adaneg.png')
