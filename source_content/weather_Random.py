import matplotlib.pyplot as plt
import numpy as np

# Sample data
epochs = np.array([100, 200, 300, 500, 800])
mae_values = np.array([0.85, 0.8, 0.78, 0.7, 0.65])
mse_values = np.array([1.31, 1.30, 1.29, 1.28, 1.25])

# Create a plot
plt.figure(figsize=(5, 4))
plt.plot(epochs, mae_values, label='MAE', color='orange', marker='*', linewidth=3)
plt.plot(epochs, mse_values, label='MSE', color='navy', marker='v', linewidth=3)

# Add labels and legend
plt.ylabel('Loss')
# Add a legend with two columns (horizontal)
plt.legend(ncol=2, loc='best')

# Set specific y-ticks
plt.yticks([0.5, 0.9, 1.3, 1.7])


# Set specific x-ticks with equal spacing


# Set y-limits to match the figure
plt.ylim(0.5, 1.7)
# Use np.linspace to create equal spaced positions in the range
# Set log scale for the x-axis
plt.xticks([100, 200, 300, 500, 800])
# Display the plot
plt.tight_layout()
plt.savefig('weather_Random.png')