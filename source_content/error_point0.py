import matplotlib.pyplot as plt
import numpy as np

# Data
balance_factor = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
classification_means = np.array([0.858, 0.867, 0.8643, 0.8615, 0.8645])
classification_errors = np.array([0.0021, 0.002, 0.003, 0.0022, 0.002])
generation_means = np.array([0.839, 0.848, 0.8475, 0.845, 0.841])
generation_errors = np.array([0.002, 0.001, 0.0022, 0.004, 0.0031])
# Plot
# plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()

# Classification line
ax.errorbar(balance_factor, classification_means, yerr=classification_errors, fmt='o-',
            color='#9CAECF', label='Classification', alpha=0.7, markersize=8,capsize=5,lw=3,elinewidth=3,capthick=3)

# Generation line
ax.errorbar(balance_factor, generation_means, yerr=generation_errors, fmt='o-', color='#E2B8A4', label='Generation', alpha=0.7, markersize=8,capsize=5,lw=3,elinewidth=3,capthick=3)

# Labels and Legend
ax.set_xlabel('Balance Factor',fontsize=16)
ax.set_ylabel('Micro F1',fontsize=16)
ax.set_ylim([0.835, 0.870])
ax.set_yticks([0.840,0.845,0.850,0.855,0.860,0.865,0.870])
ax.set_xlim([-0.05, 0.45])
ax.set_xticks([0.0,0.1,0.2,0.3,0.4])
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_visible(False)
ax.tick_params(length=0)
ax.grid(True,axis='y',color='white')

ax.set_facecolor('#EAEAF1')
ax.tick_params(pad=10)

ax.legend(title='Model')

# Create custom legend handles
from matplotlib.lines import Line2D

# Create custom legend handles
handle1 = Line2D([], [], marker='o', color='#9CAECF', markersize=8, linestyle='-', label='Classification',alpha=0.7,lw=3)
handle2 = Line2D([], [], marker='o', color='#E2B8A4', markersize=8, linestyle='-', label='Generation',alpha=0.7,lw=3)

# Add the legend
legend=ax.legend(handles=[handle1, handle2], title='Model',fontsize=14,facecolor='#EAEAF1',loc='center right',bbox_to_anchor=(1, 0.55))
legend.get_title().set_fontsize(14)

plt.tight_layout()
plt.savefig('error_point0.png')