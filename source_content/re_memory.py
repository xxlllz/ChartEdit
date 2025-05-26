import matplotlib.pyplot as plt
import numpy as np


plt.rcParams['font.family'] = 'serif'

# Data
categories = ['B', 'C', 'D', 'E', 'F']
activation = np.array([3.42, 1.84, 1.65, 0.8, 0.8])
optimizer = np.array([0.59, 0.55, 0.58, 0.54, 0.2])
parameters = np.array([0.58, 0.55, 0.55, 0.55, 0.18])

# Stacking
barWidth = 0.75
r = np.arange(len(categories))

# Plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(r, activation, color='#4682B4', edgecolor='black', width=barWidth, label='Activation',zorder=5)
ax.bar(r, optimizer, bottom=activation, color='#FFA500', edgecolor='black', width=barWidth, label='Optimizer',zorder=4)
ax.bar(r, parameters, bottom=activation+optimizer, color='#5F9BA0', edgecolor='black', width=barWidth, label='Parameters',zorder=3)

# Adding percentage text
percentages = ['64.9%', '62.1%', '43.1%', '25.0%']
# Correcting for loop to use i starting from 0
for i, perc in enumerate(percentages):
    ax.text(i + 1, 0.1 + activation[i + 1] + optimizer[i + 1] + parameters[i + 1], perc, ha='center', color='black', fontsize=17, fontweight='bold')

# Customizing the chart
ax.set_ylabel('Memory Usage (GB)', fontsize=24)
ax.set_ylim(0,4.82)
ax.set_yticks([0,1,2,3,4])
ax.set_yticklabels([0,1,2,3,4],fontsize=18)
ax.set_xticks(r)
ax.set_xticklabels(categories, fontsize=20)
ax.axhline(y=4.6, color='#FF7F7F', linewidth=5,zorder=2,xmin=0.03, xmax=0.97) 
ax.legend(loc='upper right', fontsize=24,edgecolor='none', bbox_to_anchor=(1, 0.95))
ax.grid(True,linestyle='--',axis='y',zorder=0)
plt.tight_layout()
plt.savefig('re_memory.png')