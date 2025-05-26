import matplotlib.pyplot as plt
import numpy as np


# New example data with more participants and modified values
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim', 'Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Lily')
y_pos = np.arange(len(people))

# Manually specifying performance values and error values for a wider range
performance = [22, 12, 18, 25, 30, 10, 17, 35, 28, 40, 23]
error = [2, 1.5, 3, 1, 4, 0.8, 2.5, 3, 2, 1.2, 3.5]

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# Use custom colors for the bars (less common colors)
bar_colors = ['#d84315', '#5e35b1', '#fbc02d', '#039be5', '#8bc34a', '#f06292', '#0288d1', '#c2185b', '#8e24aa', '#43a047', '#3949ab']

# Create horizontal bar chart with error bars
hbars = ax.barh(y_pos, performance, xerr=error, align='center', color=bar_colors,  capsize=5, zorder=2)
ax.set_yticks(y_pos, labels=people)
ax.invert_yaxis()  # Invert y axis to display labels top to bottom
ax.set_xlabel('Performance', fontsize=16)


# Adjust xlim to fit larger performance values
ax.set_xlim(right=45)  # Adjust xlim to fit larger performance numbers

# Increase tick font size for x and y axes
ax.tick_params(axis='x', labelsize=14)
ax.tick_params(axis='y', labelsize=14)

ax.grid(True, which='both', linestyle='--', color='gray', linewidth=1.5, zorder=0)
# Show the plot
plt.tight_layout()

# Save the figure (optional)
plt.savefig('new_perform.png')