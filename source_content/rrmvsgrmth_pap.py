import matplotlib.pyplot as plt
import numpy as np

# Data
grms = np.array([4.5, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 28, 40, 55, 82, 110])
rrms = np.array([1.95, 1.77, 1.55, 1.45, 1.42, 1.5, 1.55, 1.48, 1.56, 1.55, 1.56, 1.56, 1.57,
                 1.58, 1.55, 1.58, 1.6, 1.6, 1.71, 1.73, 1.75, 1.8, 1.82])
errors = np.array([0.2, 0.18, 0.1, 0.08, 0.06, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05,
                   0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05])

# Highlight color for a specific point
highlighted_point = 11
plt.figure(figsize=(8, 6))
# Plot
plt.plot(grms, rrms, 'o', color='royalblue', markersize=6)
for i, (x, y, err) in enumerate(zip(grms, rrms, errors)):
    color = 'orange' if i == highlighted_point else 'royalblue'
    plt.vlines(x, y - err, y + err, color=color, linewidth=1.5)

plt.scatter(grms[highlighted_point], rrms[highlighted_point], color='orange', edgecolor='orange', zorder=5, s=40)

# Log scale for x-axis
plt.xscale('log')

# Set x and y axis limits
plt.xlim(4, 120)  # Set x-axis range
plt.ylim(0.00, 2.2)  # Set y-axis range

# Labels
plt.xlabel('GRM$_{th}$ [rad m$^{-2}$]', fontsize = 16)
plt.ylabel('RRM$_{rms}$ [rad m$^{-2}$]', fontsize = 16)

# Show plot
plt.savefig('rrmvsgrmth_pap.png')
