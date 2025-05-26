import matplotlib.pyplot as plt
import numpy as np

# Updated corrected data points
x_corrected = [0, 0.1, 0.2, 0.3, 0.4, 1, 2, 3, 5, 8, 14, 20]
y_corrected = [0, 300, 130, 90, 75, 65, 55, 50, 45, 39, 30, 24]

x_corrected1 = [0, 0.1, 0.2, 0.3, 0.4, 0.7, 1, 2, 3, 5, 8, 14, 20]
y_corrected1 = [80, 120, 90, 75, 52, 40, 43, 35, 32, 30, 25, 20, 18]

x_corrected2 = [0, 0.1, 0.2, 0.3, 0.45, 0.6, 0.8, 2, 3, 5, 8, 14, 20]
y_corrected2 = [0, 100, 90, 70, 50, 47, 41, 30, 23, 20, 15, 11, 8]

fig, ax = plt.subplots(figsize=(8, 6))

# Plotting the main plot with updated data and thicker lines
ax.plot(x_corrected, y_corrected, color='#004080', marker='o', label='All', linewidth=3)  # Blue line with reduced brightness
ax.plot(x_corrected1, y_corrected1, color='orange', marker='o', label='Prograde', linewidth=3)  # Orange line
ax.plot(x_corrected2, y_corrected2, color='green', marker='o', label='Retrograde', linewidth=3)  # Green line

ax.set_xlabel('r [pc]', fontsize=20)
ax.set_ylabel('$V_t$ [km/s]', fontsize=20)
ax.set_title('M1: small-q', fontsize=20)
ax.set_xlim(0, 20)  # Set x-axis range to 0-20
ax.set_ylim(0, 300)  # Set y-axis range to 0-300

# Adding ticks and minor ticks
ax.set_xticks(range(0, 21, 4))  # Major ticks every 4 units
ax.set_xticks(range(0, 21, 1), minor=True)  # Minor ticks every 1 unit
ax.set_yticks(range(0, 301, 50))  # Major ticks every 50 units
ax.set_yticks(range(0, 301, 10), minor=True)  # Minor ticks every 10 units

# Creating the inset
inset_position = [0.65, 0.35, 0.25, 0.3]  # Adjusted position
ax_inset = fig.add_axes(inset_position)

# Plotting inset with updated data and thicker lines
ax_inset.plot(x_corrected, y_corrected, color='#004080', marker='o', markersize=4, linewidth=3)  # Blue line
ax_inset.plot(x_corrected1, y_corrected1, color='orange', marker='o', markersize=4, linewidth=3)  # Orange line
ax_inset.plot(x_corrected2, y_corrected2, color='green', marker='o', markersize=4, linewidth=3)  # Green line
ax_inset.set_xlim(0, 1)  # x-axis starts from 0
ax_inset.set_ylim(0, 300)  # y-axis starts from 0

# Setting specific ticks for the inset
ax_inset.set_xticks([0.0, 0.5, 1.0])  # Set x-axis ticks for the inset
ax_inset.set_xticks(np.linspace(0, 1, 11), minor=True)  # Minor ticks every 0.1
ax_inset.set_yticks([0, 100, 200, 300])  # Set y-axis ticks for the inset
ax_inset.set_yticks(range(0, 301, 50), minor=True)  # Minor ticks every 50 units

# Adjusting tick parameters for inset
ax_inset.tick_params(labelsize=18)

# Adding legend to the main plot with larger font size
ax.legend(fontsize=20)

# Save the figure
plt.tight_layout()
plt.savefig('sigma_tan_M1.png')
