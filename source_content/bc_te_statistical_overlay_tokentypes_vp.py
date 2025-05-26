import matplotlib.pyplot as plt
import numpy as np

# Data generation
np.random.seed(42)
subjects_data = np.random.normal(0, 25, 300)
relations_data = np.random.normal(20, 50, 200)

# Combine data
data = [subjects_data, relations_data]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(5, 4))

# Create violin plot
parts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False)

# Customize the violins
colors = ['#1f97b4', '#ff9f0e']  # Blue and orange
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor(colors[i])
    pc.set_edgecolor('black')
    pc.set_alpha(0.8)

# Add boxplot overlay
boxprops = dict(color='black', linewidth=1)
medianprops = dict(color='gray', linewidth=1.5)
ax.boxplot(data, positions=[1, 2], widths=0.25, boxprops=boxprops, medianprops=medianprops, showmeans=False)

# Customize the axes
ax.set_xticks([1, 2])
ax.set_xticklabels(['subjects', 'relations'], fontsize=16)
ax.set_xlabel('Behavior', fontsize=18)
ax.set_ylabel('TE', fontsize=18)
ax.set_ylim(-100, 200)

# Tight layout and save the plot
fig.tight_layout()
plt.savefig('bc_te_statistical_overlay_tokentypes_vp.png')
