import matplotlib.pyplot as plt
import numpy as np

# Sample data
epochs_x = [1,2,3,4,5]
epochs_label= [100, 200, 300, 500, 800]
mae_values = [5.55, 4.8, 4.45, 4.2, 4.15]
mse_values = [5.65, 4.5, 4.35, 4.05, 4.00]

# Plot
plt.figure(figsize=(5, 4))

# Plot MAE and MSE
plt.plot(epochs_x, mae_values, color='orange', marker='*', linestyle='-', linewidth=3, markersize=8, label='MAE')
plt.plot(epochs_x, mse_values, color='darkblue', marker='v', linestyle='-', linewidth=3, markersize=6, label='MSE')

# Axis Labeling with increased font size
plt.ylabel('Loss', fontsize=16)

# Scientific notation for the y-axis
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))

# Axis limits
plt.ylim(3.8, 5.8)
plt.yticks([3.8,4.3,4.8,5.3,5.8], fontsize=16)
plt.xlim(0.8,5.2)
plt.xticks([1, 2, 3, 4, 5], [100, 200, 300, 500, 800], fontsize=16)

# Legend with increased font size
plt.legend(loc='upper right', fontsize=14,ncol = 2,edgecolor='none')
plt.text(0.03, 1.03, '1e—1', fontsize=12, ha='center', va='center', transform=plt.gca().transAxes)

# Show plot
plt.tight_layout()
plt.savefig('samples_etth1.png')

# Show plot
plt.show()
