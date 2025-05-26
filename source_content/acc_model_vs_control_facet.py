import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Control', 'Model']
data = {
    'Group 1': [80, 70],
    'Group 2': [70, 60],
    'Group 3': [60, 65],
    'Group 4': [75, 68],
}
colors = ['#374B94', '#40336B', '#3E8775', '#71A2A6']  # Adjusted for four groups

x = np.arange(len(labels))  # the label locations
width = 0.2  # Narrower bar width to accommodate four groups

fig, ax = plt.subplots(figsize=(8, 4))  # Adjust size

# Plot each group
for idx, (group, values) in enumerate(data.items()):
    ax.bar(x + idx * width, values, width, label=group, color=colors[idx])

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Accuracy', fontsize=15, fontweight='bold')
ax.set_title('FACET', fontsize=20, fontweight='bold')
ax.set_xticks(x + (width * 1.5))  # Center the xticks for all groups
ax.set_xticklabels(labels, fontsize=15)


# Remove top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


# Adjust layout and save
plt.savefig('acc_model_vs_control_facet.png')
