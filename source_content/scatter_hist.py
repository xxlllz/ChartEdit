import matplotlib.pyplot as plt
import numpy as np

# Modify the data (not random anymore)
x = np.random.randn(1000)
y = np.random.randn(1000)

# Create a Figure, which doesn't have to be square
fig = plt.figure(figsize=(5, 5))

# Create the main Axes, leaving 25% of the figure space at the top and on the right to position marginals.
ax = fig.add_gridspec(top=0.75, right=0.75).subplots()

# Set aspect ratio of the main plot
ax.set(aspect=1)

# Create marginal Axes, which have 25% of the size of the main Axes.
ax_histx = ax.inset_axes([0, 1.05, 1, 0.25], sharex=ax)
ax_histy = ax.inset_axes([1.05, 0, 0.25, 1], sharey=ax)

# Scatter plot with custom color and markers
ax.scatter(x, y, c=x, cmap='twilight', edgecolors='black', alpha=0.7, s=50)

# Remove all ticks from the main plot and histograms
ax_histx.set_xticks([])  # Remove x-axis ticks on histogram
ax_histy.set_yticks([])  # Remove y-axis ticks on histogram

# Add marginal histograms
ax_histx.hist(x, bins=30, color='green', edgecolor='black', alpha=0.6)
ax_histy.hist(y, bins=30, color='blue', edgecolor='black', alpha=0.6, orientation='horizontal')

# Set limits for histograms for better appearance
ax_histx.set_xlim(-5, 5)
ax_histy.set_ylim(-5, 5)

# Show the plot
plt.savefig('scatter_hist.png')