import matplotlib.pyplot as plt
import numpy as np


plt.figure(figsize=(8, 6))
# Initialize model parameters (x-axis) and excess loss (y-axis) data
model_params = np.array([5*10**4, 1.5*10**5, 4*10**5, 4*10**6, 10**7, 2*10**7, 10**8])
excess_loss_cells = [
    [0.14, 0.088, 0.06, 0.05, 0.046, 0.043, 0.045],  # 52M cells
    [0.12, 0.09, 0.06, 0.04, 0.043, 0.03, 0.039], # 141M cells
    [0.11, 0.07, 0.05, 0.03, 0.024, 0.022, 0.019], # 269M cells
    [0.10, 0.058, 0.047, 0.028, 0.022, 0.019, 0.018],  # 598M cells
    [0.099, 0.055, 0.043, 0.023, 0.018, 0.016, 0.012] # 2B cells
]
synthetic_loss = [0.091, 0.05, 0.04, 0.028, 0.026, 0.022, 0.025]

# Define colors
colors = ['#FFCC66', '#FF6666', '#CC66FF', '#6633FF', '#333366']

# Plot each dataset
for i, (data, color) in enumerate(zip(excess_loss_cells, colors)):
    plt.plot(model_params, data, marker='o', markersize=12, linewidth=4, color=color, label=f'{[52, 141, 269, 598, 2000][i]}M cells')

# Plot synthetic data
plt.plot(model_params, synthetic_loss, 'g--o', markersize=12, linewidth=4, label='Synthetic')

# Set logarithmic scale
plt.xscale('log')
plt.yscale('log')

# Set limits for axes
plt.xlim(0.9*4*10**4, 1.1*10**8)
plt.ylim(1e-2, 2*1e-1)

# Add labels and legend
plt.xlabel('Model Parameters', fontsize=20)
plt.ylabel('Excess loss', fontsize=20)
plt.legend(loc='lower left', fontsize=15)

# Set tick parameters to increase the font size of ticks
plt.tick_params(axis='both', which='major', labelsize=20)  # Major ticks
plt.tick_params(axis='both', which='minor', labelsize=20)  # Minor ticks

# Enable grid and make it visible
plt.grid(True, which='both', linestyle='--', linewidth=1)

plt.tight_layout()
# Show plot
plt.savefig('cecor_scaling_law_poster.png')

