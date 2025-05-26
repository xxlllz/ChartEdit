import matplotlib.pyplot as plt
import numpy as np

# New and modified data for penguin attributes
species = ("Adelie", "Chinstrap", "Gentoo", "Macaroni", "Emperor")  # Added Macaroni and Emperor
penguin_means = {
    'Bill Depth': (19.35, 19.43, 15.98, 17.22, 18.44),  # Modified values
    'Bill Length': (39.79, 49.83, 48.50, 51.23, 55.12),  # Modified values
    'Flipper Length': (190.95, 196.82, 218.19, 230.45, 250.75),  # Modified values
    'Body Mass': (3800, 3805, 3950, 4000, 5000)  # New attribute: Body Mass (grams)
}

# Adjust the bar positions and width
x = np.arange(len(species))  # the label locations
width = 0.15  # narrower bars
multiplier = 0

# Create figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Create a colormap for the bars
cmap = plt.get_cmap('viridis')  # Choose a perceptually uniform colormap
norm = plt.Normalize(vmin=0, vmax=len(penguin_means))  # Normalize the colormap based on the number of attributes

# Loop over the penguin attributes and plot each
for i, (attribute, measurement) in enumerate(penguin_means.items()):
    offset = width * multiplier
    color = cmap(norm(i))  # Get the color from the colormap
    rects = ax.bar(x + offset, measurement, width, label=attribute, color=color, zorder=2)
    multiplier += 1

# Add labels, title, and custom x-axis tick labels
ax.set_ylabel('Measurement Value (log scale)', fontsize=18, fontweight='bold', color='dimgray')

# Set custom x-axis labels and font size
ax.set_xticks(x + width * 1.5, species)
ax.set_xticklabels(species, fontsize=18, fontweight='bold')

# Increase the size of ticks on the x and y axes
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)

# Adjust the y-axis limits and set the scale to logarithmic (exponential)
ax.set_yscale('log')  # Set y-axis to log scale
ax.set_ylim(10, 5000)  # Adjust y-limits for log scale (min value > 0)

# Add horizontal grid lines (dashed lines)
ax.grid(True, which='major', axis='y', linestyle='--', color='gray', alpha=0.5, zorder=0)

# Add a horizontal dashed line at a specific value (e.g., 1000) for better reference
ax.axhline(y=1000, color='red', linestyle='--', linewidth=2)

# Set the legend with increased font size and placed below the plot
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), ncols=4, fontsize=18)

plt.tight_layout()
plt.savefig('bar_peg.png')