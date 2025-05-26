import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['GCD', 'PromptCAL', 'ORCA', 'GraphVL']
values = [15, 0.4, 0.2, 0.4]
colors = ['blue', 'green', 'red', 'purple']

# Create bar plot
fig, ax = plt.subplots()
ax.bar(categories, values, color=colors)

# Set logarithmic scale
ax.set_yscale('log')
ax.set_ylim(0,20)

# Set labels and titles
# ax.set_title('Synthetic Scenario 3')  # Added title
ax.set_ylabel('Trainable Parameters (P) in M',fontsize=18)
ax.grid(True, linestyle='--', axis='y')
# Set tick label sizes
plt.xticks(fontsize=14)  # Change x-axis ticks font size
plt.yticks(fontsize=14)  # Change y-axis ticks font size


# Show plot
plt.tight_layout()
plt.savefig('parameters_bar_plot.png')