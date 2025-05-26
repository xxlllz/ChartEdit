import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
from matplotlib.lines import Line2D

star_marker = Line2D([0], [0], marker='*', color='w', markerfacecolor='yellow', markersize=15, label='Star Pattern', lw=0, markeredgewidth=2)

categories = ['MedCLIP', 'MM-Retinal', 'QuiltNet', 'MetaCLIP', 'BioMedCLIP', 'PMC CLIP', 'OpenM3Net']
performance = [33.07, 40.01, 43.79, 37.25, 49.02, 53.37, 61.63]
patterns = ['////', '////', '////', 'xxx', 'xxx', 'xxx', '*']
colors = ['#FFB703', '#FB8500', '#E66155', '#313695', '#91BFD9', '#4575B4', '#00B4D8']

fig, ax = plt.subplots()

# Bar plot
bars = ax.bar(categories, performance, color=colors, hatch=patterns,edgecolor='black')

# Add numerical labels on top of bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 2), ha='center', va='bottom', fontsize=12)

# Setting labels
ax.set_xlabel('Average over 21 datasets', fontsize=14,)
ax.set_ylabel('Performance (%)', fontsize=14)




# Create Patch objects for legend
legend_labels = ['MedCLIP', 'MM-Retinal', 'QuiltNet', 'MetaCLIP', 'BioMedCLIP', 'PMC CLIP', 'OpenM3Net']

# Create Patch objects for legend with hatch patterns
legend_markers_1 = [mpatches.Rectangle((0, 0),1,1, facecolor=col, hatch=patterns[i+3],edgecolor='black',label=label) 
                    for i, (col, label) in enumerate(zip(colors[3:], legend_labels[3:]))]  # First set of labels

legend_markers_2 = [mpatches.Rectangle((0, 0), 1, 1, facecolor=col, hatch=patterns[i],edgecolor='black', label=label) 
                    for i, (col, label) in enumerate(zip(colors[:3], legend_labels[:3]))]  # Second set of labels (from index 4)

# Create the legend
first_legend = plt.legend(handles=legend_markers_1, title='Generalistic Medical VLMs', loc='upper center', bbox_to_anchor=(0.18, 1.0), borderaxespad=0., ncol=1, handlelength=2.5, handleheight=1)
second_legend = plt.legend(handles=legend_markers_2, title='Specialized Medical VLMs', loc='upper center', bbox_to_anchor=(0.53, 1.00), borderaxespad=0., ncol=1,
                           handlelength=2.5, handleheight=1)

# Add legends to the plot
ax.add_artist(first_legend)
ax.add_artist(second_legend)


# Set limits and style
ax.set_ylim([25, 65])
ax.set_xlim([-0.5, len(categories)-0.5])
ax.set_xticklabels([])


ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
plt.xticks(rotation=0)
plt.yticks(np.arange(25, 70, 5))

# Title
title_font_props = {'weight': 'bold', 'size': 14}
# plt.title('Performance of Medical VLMs', fontdict=title_font_props

# Layout adjustment
plt.tight_layout()

# Show plot
plt.savefig('per21_barchart_samescheme.png')
