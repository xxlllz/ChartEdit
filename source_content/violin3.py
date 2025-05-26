import pandas as pd
import matplotlib.pyplot as plt

# Data
region_a = [287, 302, 300, 332, 325, 330, 335, 281, 305, 311]
region_b = [281, 292, 295, 285, 301, 303, 292, 304, 311, 298]
region_c = [242, 288, 298, 232, 292, 281, 243, 281, 291, 283]

# Combining the data 
data = [region_a, region_b, region_c]

# Create a figure and an axis
fig, ax = plt.subplots(figsize=(6, 5))

# Creating the violinplot with the data and setting the labels
parts = ax.violinplot(data, showmedians=True)
ax.set_xticks([1, 2, 3])
ax.set_xticklabels(['A', 'B', 'C'])

# Setting colors for the violin parts
colors = ['skyblue', 'royalblue', 'lightsteelblue']
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')

# Customize edges
parts['cmins'].set_edgecolor('darkblue')
parts['cmaxes'].set_edgecolor('darkblue')
parts['cbars'].set_edgecolor('darkblue')
parts['cmedians'].set_edgecolor('darkblue')

# Adding title and labels with increased font size
plt.xlabel('Regions', fontsize=20)
plt.ylabel('Elevation', fontsize=20)

# Increase font size of ticks
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)


# Add legend
ax.legend(['Region A', 'Region B', 'Region C'], loc='upper right', fontsize=14)

# Tight layout for better spacing
plt.tight_layout()

# Save the plot as a PNG file
plt.savefig("violin3.png")