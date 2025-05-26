import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Define the data
x = np.array([0.4, 0.7, 1, 1.5, 2.2, 3])

# Multiple sets of y-values corresponding to different lines
y_values = [
    np.array([500, 467, 433, 400, 367, 333]),  # Purple line
    np.array([420, 397, 363, 320, 287, 253]),  # Red line
    np.array([350, 327, 300, 270, 240, 220]),  # Green line
    np.array([300, 280, 253, 223, 197, 167]),  # Orange line
    np.array([220, 197, 173, 150, 127, 110])   # Blue line
]

# Line labels
labels = [
    r'$M = M_{\text{fid}}$',  # Purple line
    r'$M = 1.7M_{\text{fid}}$',  # Red line
    r'$M = 2.3M_{\text{fid}}$',  # Green line
    r'$M = 3.3M_{\text{fid}}$',  # Orange line
    r'$M = 5M_{\text{fid}}$'   # Blue line
]

# Line colors
colors = ['purple', 'red', 'green', 'orange', 'tab:blue']

# Plot each line
for y, label, color in zip(y_values, labels, colors):
    ax.plot(x, y, '-o', label=label, color=color)

# Add the $\\rho_g$ small line segment
small_line_x = [1.4, 1.7]
small_line_y = [120, 110]
ax.plot(small_line_x, small_line_y, 'k--', label='$\\rho_g$ segment')

# Set the x-axis and y-axis to log scale
ax.set_xscale('log')
ax.set_yscale('log')

# Set custom x-ticks
x_ticks = [0.6, 1, 2, 3]
ax.set_xticks(x_ticks)
ax.set_xticklabels([str(tick) for tick in x_ticks], fontsize=20)

# Set custom y-ticks
y_ticks = [50, 100, 500]
ax.set_yticks(y_ticks)
ax.set_yticklabels([str(tick) for tick in y_ticks], fontsize=20)


# Add annotations and labels
ax.set_xlabel(r'$\rho_g/\rho_{\text{fid}}$', fontsize=20)
ax.set_ylabel(r'$T_f - T_0 (K)$', fontsize=20)

# Add the $\rho_g$ annotation next to the short dashed line
ax.text(1.55, 95, r'$\rho_g^{-0.5}$', fontsize=20, color='black', verticalalignment='bottom', horizontalalignment='center')

# Legend
ax.legend(fontsize=16, loc='lower left')

# Adjust subplot spacing
fig.tight_layout()

# Show the plot
plt.tight_layout()
plt.savefig('resume_rhog.png')
