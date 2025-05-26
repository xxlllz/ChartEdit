import matplotlib.pyplot as plt
import numpy as np

# Sample data
z = np.linspace(0, 3, 100)
linear_model = 0.39 - 0.12 * z**0.65
polytropic_model = 0.38 - 0.15 * z**0.63

# Create plot
plt.figure(figsize=(9, 6))
plt.plot(z, linear_model, 'r-', linewidth=3, label='Linear Model')
plt.plot(z, polytropic_model, 'b-', linewidth=3, label='Polytropic Model')

# Add labels with Times New Roman font
plt.xlabel(r'$z$', fontsize=24, fontname='Times New Roman')
plt.ylabel(r'$\Omega(z)$', fontsize=24, fontname='Times New Roman')

# Legend with Times New Roman font
plt.legend(
    fontsize=16,
    loc='lower left',
    framealpha=0,
    bbox_to_anchor=(0, 0.1),
    borderaxespad=1,
    handlelength=1,
    handleheight=1,
    labelspacing=1,
)

# Add grid
plt.grid(True, linestyle=':', linewidth=0.5)

# Set tick parameters
plt.ylim(0.05, 0.45)
plt.xlim(0.0, 3.0)

# Remove the first y-tick (0.05)
yticks = np.arange(0.1, 0.5, 0.05)
plt.yticks(yticks, fontsize=16)

plt.xticks(fontsize=16)

# Enable minor ticks and customize them
plt.minorticks_on()
plt.tick_params(which='minor', length=4, width=1, color='gray', direction='inout', grid_alpha=0.5)

# Disable minor ticks on top and right axis
plt.tick_params(axis='x', which='minor', bottom=True, top=True)
plt.tick_params(axis='y', which='minor', left=True, right=True)

# Adjust layout and save the figure
plt.tight_layout(pad=2.0)
plt.savefig('t_z.png', bbox_inches='tight')
