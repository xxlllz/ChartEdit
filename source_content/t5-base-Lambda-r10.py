import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

# Sample data
x = np.array([0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0])
y1 = np.array([65.2, 66.8, 68.8, 70.2, 71.4, 72.2, 72.5, 72.7, 73, 73.7, 72.8, 72, 71.5])
y2 = np.array([71.2, 72.2, 73, 73.3, 73.5, 74.5, 74.7, 74.3, 73.2, 73.6, 72.2, 71.5, 70.7])

plt.figure(figsize=(20, 12))

# Plotting data
graph1, = plt.plot(x, y1, 'o-', color='blue', label='TIES-Merging', linewidth=6, markersize=28)
graph2, = plt.plot(x, y2, 's-', color='red', label='PCB-Merging (ours)', linewidth=6, markersize=28)

# Titles and labels
plt.title('T5-base', fontsize=60)
plt.xlabel('various λ at r=0.1', fontsize=60)
plt.ylabel('Avg. Performance', fontsize=60)
plt.minorticks_on()

# Axes limits and ticks
plt.ylim(63.4, 77)
plt.xlim(0.7, 2.1)

# Display x-axis and y-axis ticks
plt.xticks(np.arange(0.8, 2.2, 0.2), fontsize=60)  # x-axis ticks with step 0.2
plt.yticks(np.arange(64, 77, 3), fontsize=60)  # y-axis ticks with step 3

# Show tick marks only on the axes
plt.tick_params(axis='both', which='major', length=10, width=3, direction='out', grid_alpha=0.5)

# Display grid only for horizontal lines
plt.grid(axis='y')

# Hide the top spine (black line at the top of the plot)
plt.gca().spines['top'].set_visible(False)

# Custom legend with line color
legend_elements = [Line2D([0], [0], color='blue', lw=4, label='TIES-Merging'),
                   Line2D([0], [0], color='red', lw=4, label='PCB-Merging (ours)')]

plt.legend(handles=legend_elements, loc='lower right', fontsize=50)

# Adjust layout to ensure everything fits
plt.tight_layout()

# Save the figure
plt.savefig('t5-base-Lambda-r10.png', bbox_inches='tight')
