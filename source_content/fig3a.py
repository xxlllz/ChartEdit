import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define the data
categories = [ 'CSV', 'JSON', 'Markdown', 'YAML','XML']
labels = categories

# Data
data_1 = [0.08, 0.25, 0.185, 0.5, 0.52,]
data_2 = [0.085, 0.43, 0.57, 0.44, 0.4]
data_1 += data_1[:1]  # complete the loop
data_2 += data_2[:1]  # complete the loop

# Number of variables
N = len(categories)

# What will be the angle of each axis in the plot?
angle_temp =  0.1 * pi
# We divide the plot / number of variables in full circle (2*pi)
angles = [n / float(N) * 2 * pi + angle_temp for n in range(N)]  # One more value to close the circle
angles += angles[:1]
angles.insert(0,0)

# Initialise the radar chart
fig, ax = plt.subplots(figsize=(8, 6), subplot_kw=dict(polar=True))

# Plot each individual = each line of the data
ax.plot(angles[1:], data_1, color='orange', linewidth=1.5, linestyle='-', marker='o',markersize=4)

ax.plot(angles[1:], data_2, color='teal', linewidth=1.5, linestyle='-', marker='o',markersize=4)

# Add labels for each point
plt.xticks(angles[1:], [], color='Black', size=15)
plt.yticks([0,0.1,0.2,0.3,0.4,0.5],[])

for i, label in enumerate(categories):
    angle = angles[1:][i]
    if i in [0,4]:  # Left-aligned labels
        ax.text(angle, 0.61, label, horizontalalignment='left', verticalalignment='center', fontsize=18, color='black')
    elif i in [1]:  # Centered labels
        ax.text(angle, 0.61, label, horizontalalignment='center', verticalalignment='center', fontsize=18, color='black')
    else:  # Left-aligned for indices 3, 4, 5
        ax.text(angle,0.61, label, horizontalalignment='right', verticalalignment='center', fontsize=18, color='black')
        
        
# One more point to close the chart (already in data)
# ax.set_rlabel_position(0)
ax.set_facecolor('#E5ECF6') 
ax.grid(color='white', linestyle='-', linewidth=1)
ax.spines['polar'].set_visible(False)
plt.ylim(0, 0.58)
ax.plot([0, 0], [0, 0.6], color='white', linestyle='-')
yticks_values = [0,0.1,0.2,0.3,0.4,0.5]
for idx, value in enumerate(yticks_values):
    # Adjust the angle of the label based on the index and position it at a 90-degree (top) position
    
    fig.text(0.525+idx*0.06, 0.45, value, fontsize=18, ha='center', va='center', color='black')

# Add a title
# plt.title("Radar Chart Example", size=16, color='navy', pad=20)
plt.subplots_adjust(top=0.85,bottom=0.1)
plt.tight_layout()
plt.savefig('fig3a.png')
