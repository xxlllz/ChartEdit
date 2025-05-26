import matplotlib.pyplot as plt
import numpy as np


# Generate data for 3x3 grid
x = np.tile(np.arange(1, 4), 3)  # Create 3 x's (1, 2, 3) repeated 3 times
y = np.repeat(np.arange(1, 4), 3)  # Create 3 y's (1, 2, 3) repeated 3 times
z = np.zeros_like(x)  # All bars start from z = 0
dx = np.ones_like(x) * 0.5  # Width of the bars
dy = np.ones_like(y) * 0.5  # Depth of the bars
dz = [27, 43, 65, 26, 38, 54, 31, 46, 67]  # Heights of the bars

# Define colors based on the dz values
colors = ['gold', 'gold','gold', 'limegreen', 'limegreen', 'limegreen', 'royalblue', 'royalblue', 'royalblue']

# Plotting the 3x3 grid of 3D bars
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(10, 8))  # Modify figsize here

# Plotting the bars with conditional colors
ax.bar3d(x, y, z, dx, dy, dz, color=colors)

# Set xticks and yticks to the middle of each group of bars
ax.set_xticks([1.5, 2.5, 3.5])  # Middle positions of x-axis ticks
ax.set_yticks([1.5, 2.5, 3.5])  # Middle positions of y-axis ticks

# Set labels for x and y ticks
ax.set_xticklabels(["CNN", "RNN", "LTC"], fontsize=15)
ax.set_yticklabels(["DDP", "ARD", "SDK"], fontsize=15)
ax.set_zticklabels([0, 10, 20, 30, 40, 50, 60, 70], fontsize=15)

# Set labels for axes
ax.set_xlabel('Models', fontsize=20, labelpad=10)
ax.set_ylabel('Tasks', fontsize=20, labelpad=10)
ax.set_zlabel('Performance', fontsize=20, labelpad=10)

# Display the plot
plt.savefig('3d_bar.png')