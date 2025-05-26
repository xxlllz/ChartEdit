import matplotlib.pyplot as plt
import numpy as np

# Data for the charts
categories1 = ['{4, 5}', '{4, 6}', '{5, 5}', '{5, 6}']
categories2 = ['{4, 6}', '{4, 8}', '{4, 10}', '{5, 8}']
theoretical_min1 = [1.05, 1.07, 1.05, 1.1]
theoretical_max1 = [1.2, 1.21, 1.21, 1.23]
mean_latency1 = [1.2, 1.2, 1.19, 1.2]
theoretical_min2 = [1.2, 1.2, 1.25, 1.25]
theoretical_max2 = [1.5, 1.5, 1.48, 1.7]
mean_latency2 = [1.3, 1.45, 1.4, 1.45]

x1 = np.arange(len(categories1))
width = 0.3

# Create subplots
fig, ax = plt.subplots(2, 1, figsize=(10, 8), sharey=True)

# Plot for the first subplot
ax[0].bar(x1 - width, theoretical_min1, width, label='Theoretical Min', color='#7f1d1d')
ax[0].bar(x1, theoretical_max1, width, label='Theoretical Max', color='#f5e0a1')
ax[0].bar(x1 + width, mean_latency1, width, label='Mean Latency', color='#b22222')
ax[0].set_ylabel('Latency ($\mu$s)', fontsize=20)  # Correctly display mu with LaTeX
ax[0].set_xticks(x1)
ax[0].set_xticklabels(categories1, fontsize=20)  # Adjust xticks size
ax[0].set_yticks(np.arange(0, 2, 0.5))  # Reduce the number of yticks
ax[0].set_yticklabels([f'{i:.1f}' for i in np.arange(0, 2, 0.5)], fontsize=20)  # Adjust yticks size
ax[0].set_ylim(0, 1.5)  # Set y-axis limits to be consistent
ax[0].set_title('H. Surface Code Subfamily', fontsize=20)

# Move legend to the right
ax[0].legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=18)

# Plot for the second subplot
x2 = np.arange(len(categories2))
ax[1].bar(x2 - width, theoretical_min2, width, color='#7f1d1d', label='Theoretical Min')
ax[1].bar(x2, theoretical_max2, width, color='#f5e0a1', label='Theoretical Max')
ax[1].bar(x2 + width, mean_latency2, width, color='#b22222', label='Mean Latency')
ax[1].set_ylabel('Latency ($\mu$s)', fontsize=20)  # Correctly display mu with LaTeX
ax[1].set_xticks(x2)
ax[1].set_xticklabels(categories2, fontsize=20)  # Adjust xticks size
ax[1].set_yticks(np.arange(0, 2, 0.5))  # Reduce the number of yticks
ax[1].set_yticklabels([f'{i:.1f}' for i in np.arange(0, 2, 0.5)], fontsize=20)  # Adjust yticks size
ax[1].set_ylim(0, 1.75)  # Set y-axis limits to be consistent
ax[1].set_title('H. Color Code Subfamily', fontsize=20)

# Move legend to the right
ax[1].legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=18)

# Adjust layout with specified padding
plt.tight_layout()
plt.savefig('figure_14.png')