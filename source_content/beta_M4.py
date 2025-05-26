import matplotlib.pyplot as plt
import numpy as np

# Sample data
distance = np.array([0.1, 0.2, 0.3, 0.5, 1, 2, 4, 6, 12, 20])
all_values = np.array([0, -0.4, -0.7, -0.5, -0.2, -0.1, 0.1, 0.12, 0.18, 0.3])
prograde_values = np.array([0.12, 0.2, 0.1, 0.07, 0.15, 0.35, 0.4, 0.33, 0.35, 0.4])
retrograde_values = np.array([0.8, 0.25, -0.2, 0.2, 0.3, 0.35, 0.45, 0.5, 0.55, 0.612])

fig, ax = plt.subplots(figsize=(6, 6))

# Main plot
ax.plot(distance, all_values, 'o-', label='All')
ax.plot(distance, prograde_values, 'o-', color='orangered', label='Prograde')
ax.plot(distance, retrograde_values, 'o-', color='green', label='Retrograde')

ax.set_xlabel(r'$r$ [pc]', fontsize=18)
ax.set_ylabel(r'$\beta$', fontsize=18)
ax.set_title('M4: large-$d_i$', fontsize=16)
ax.set_xlim(0, 20)
ax.set_ylim(-1, 1)

# Increase tick label size and adjust tick direction for main plot
ax.tick_params(axis='both', labelsize=15, direction='in')

# Remove legend border
ax.legend(loc="upper right", fontsize=12, frameon=False)

# Inset plot
axins = ax.inset_axes([0.4, 0.15, 0.5, 0.35])
axins.plot(distance, all_values, 'o-')
axins.plot(distance, prograde_values, 'o-', color='orangered')
axins.plot(distance, retrograde_values, 'o-', color='green')

def zoom_in(axins):
    axins.set_xlim(0, 1)
    axins.set_ylim(-1, 1)
    axins.set_xticks([0, 0.5, 1.0])
    axins.set_yticks([-1.0, 0.0, 1.0])

    # Increase tick label size and adjust tick direction for inset plot
    axins.tick_params(axis='both', labelsize=12, direction='in')

zoom_in(axins)

plt.tight_layout()
plt.savefig('beta_M4.png', dpi=300)
