import matplotlib.pyplot as plt
from matplotlib.patches import Patch

# Data setup
categories = [
    'Agents', 'Pastness', 'Perception', 'Abstraction', 'Concreteness', 'Emotionality',
    'Dialogue', 'Event.Sequences', 'Eventfulness', 'Presentness', 'Conflict', 'Temporal.Specificity',
    'Symbolism', 'Location', 'Anachrony'
]

# Corresponding values for each category
weights = [33, 26, 11, -10, 7, 6, 5, 4, 4, -3, 2, 2, -2, 1, -0.5]

# Group colors for POV, Setting, and Time (as per the chart)
colors = ['dodgerblue', 'orangered', 'dodgerblue', 'limegreen', 'limegreen',  'dodgerblue', 'dodgerblue', 'orangered',
          'orangered', 'orangered', 'orangered', 'orangered', 'limegreen', 'limegreen', 'orangered']

# Create the plot
plt.figure(figsize=(8, 6))
bars = plt.barh(categories, weights, color=colors)

# Title and labels
plt.xlabel('Weight', fontsize=18)

# Increase the size of the x-axis ticks
plt.xticks(fontsize=18)
plt.yticks(fontsize=14)

# Remove the right and top spines (the boxes around the plot)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)

# Reverse the y-axis
plt.gca().invert_yaxis()

# Add legend for color categories
from matplotlib.lines import Line2D
legend_elements = [
    Patch(color='dodgerblue', label='POV'),
    Patch(color='limegreen', label='SETTING'),
    Patch(color='orangered', label='TIME')
]
# Adjust legend position and move it down
plt.legend(handles=legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.25), ncol=3, frameon=False, handlelength=1, handleheight=1, labelspacing=1.5, fontsize=16)
# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig('narrative_passage.png')