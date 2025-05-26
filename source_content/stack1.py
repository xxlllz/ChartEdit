import matplotlib.pyplot as plt
import numpy as np

# Make data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 2, 1.2, 3.1, 1.5]
cy = [2, 1.2, 2.1, 4, 2.3]
y = np.vstack([ay, by, cy])

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

# Define custom colors for the stacked areas
colors = ['royalblue', 'coral', 'gold']  # Blue, Orange, Yellow
ax.stackplot(x, y, colors=colors, zorder=2)

# Set x and y limits
ax.set(xlim=(0, 8), ylim=(0, 10))

# Set x and y ticks
ax.set_xticks(np.arange(0, 9, 1))  # x ticks from 0 to 8
ax.set_yticks(np.arange(0, 11, 1))  # y ticks from 0 to 10

# Optionally, set tick labels
ax.set_xticklabels([f'{i}' for i in np.arange(0, 9, 1)])  # x tick labels
ax.set_yticklabels([f'{i}' for i in np.arange(0, 11, 1)])  # y tick labels

# Increase tick size
ax.tick_params(axis='both', which='major', labelsize=15, length=6, width=1.5)

# Add dashed grid lines in the background
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, which='both', zorder=0)

# Save the figure
plt.savefig('stack1.png')