import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

year = [1960, 1970, 1980, 1990, 2000, 2010, 2020]
population_by_continent = {
    'Oceania': [0.015, 0.02, 0.025, 0.03, 0.035, 0.04, 0.065],
    'the Americas': [0.4, 0.5, 0.6, 0.75, 0.85, 0.95, 1.2], 
    'Africa': [0.25, 0.35, 0.45, 0.6, 0.75, 1.1, 1.7], 
    'Europe': [0.25, 0.3, 0.35, 0.4, 0.4, 0.38, 0.34], 
    'Asia': [1.6, 2.0, 2.5, 3.0, 3.6, 4.1, 4.9], 
}

# Set less common colors using custom color palette
colors = ['#f28e2b', '#5e4fa2', '#3b9e1f', '#c4475c', '#57d1f5'] 

fig, ax = plt.subplots()

# Create the stackplot with custom colors
ax.stackplot(year, population_by_continent.values(),
             labels=population_by_continent.keys(), alpha=0.85, colors=colors, zorder=2)

# Add a legend and reverse the order to match the original style
ax.legend(loc='upper left', fontsize=15)

# Title and labels
ax.set_xlabel('Year', fontsize=18, fontweight='bold', color='dimgray')
ax.set_ylabel('Number of people (billions)', fontsize=18, fontweight='bold', color='dimgray')

# Customize ticks for better visibility
ax.set_xticks(year)
ax.set_xlim(1960, 2020)
ax.set_xticklabels(year, fontsize=15)

ax.set_yticks([0, 2, 4, 8])
ax.set_yticklabels([f'{x}' for x in [0, 2, 4, 8]], fontsize=15)

# Minor ticks at every 100 million people
ax.yaxis.set_minor_locator(mticker.MultipleLocator(0.1))

# Customize grid and background
ax.grid(True, which='major', linestyle='--', color='gray', alpha=0.5, zorder=0)

plt.tight_layout()

# Save the figure
plt.savefig('stack2.png')