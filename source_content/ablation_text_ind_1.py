import matplotlib.pyplot as plt
import numpy as np

# Data for each subplot
categories = ['Texas', 'Cornell', 'Wis']

data_1 = {
    'MLDGG-ind w/o SL': [57, 47, 54],
    'MLDGG-ind w/o MAML': [56, 46, 52],
    'MLDGG-ind w/o SV': [58, 48, 53],
    'MLDGG-ind': [61, 49, 60]
}
errors_1 = {
    'MLDGG-ind w/o SL': [1, 2, 1],
    'MLDGG-ind w/o MAML': [1, 1, 1],
    'MLDGG-ind w/o SV': [2, 1, 2],
    'MLDGG-ind': [1, 2, 1]
}

data_2 = {
    'MLDGG-ind w/o SL': [55, 45, 52],
    'MLDGG-ind w/o MAML': [54, 44, 50],
    'MLDGG-ind w/o SV': [56, 46, 51],
    'MLDGG-ind': [60, 48, 58]
}
errors_2 = {
    'MLDGG-ind w/o SL': [1, 1, 2],
    'MLDGG-ind w/o MAML': [2, 1, 1],
    'MLDGG-ind w/o SV': [1, 2, 1],
    'MLDGG-ind': [2, 2, 1]
}

data_3 = {
    'MLDGG-ind w/o SL': [56, 46, 53],
    'MLDGG-ind w/o MAML': [55, 45, 51],
    'MLDGG-ind w/o SV': [57, 47, 52],
    'MLDGG-ind': [59, 47, 59]
}
errors_3 = {
    'MLDGG-ind w/o SL': [1, 1, 2],
    'MLDGG-ind w/o MAML': [2, 2, 1],
    'MLDGG-ind w/o SV': [1, 2, 1],
    'MLDGG-ind': [1, 1, 1]
}

colors = ['#5cb85c', '#428bca', '#5bc0de', '#f0ad4e']  # Colors for each group

# Create figure and subplots
fig, axs = plt.subplots(1, 3, figsize=(12, 4), sharey=True)

# Subplot 1: Data for S12T3
indices = np.arange(len(categories))
ax = axs[0]
for j, (label, values) in enumerate(data_1.items()):
    ax.bar(
        indices + j * 0.2,  # Position for each group
        values,
        0.2,  # Width of each bar
        label=label,
        yerr=errors_1[label],
        color=colors[j],
        capsize=4,
        linewidth=0.8
    )
ax.set_title('S12T3 (Twitch+FB-100 → WebKB)', fontsize=14, fontweight='bold', pad=10)
ax.set_xticks(indices + 0.3)
ax.set_xticklabels(categories, fontsize=15)
ax.set_yticks(np.arange(40, 70, 5))  # Set y ticks for this subplot
ax.set_ylim(40, 65)
ax.set_ylabel('Accuracy (%)', fontsize=15, fontweight='bold')
ax.tick_params(axis='y', labelsize=12)  # Set y tick label size for this subplot

# Subplot 2: Data for S1T2
indices = np.arange(len(categories))
ax = axs[1]
for j, (label, values) in enumerate(data_2.items()):
    ax.bar(
        indices + j * 0.2,  # Position for each group
        values,
        0.2,  # Width of each bar
        label=label,
        yerr=errors_2[label],
        color=colors[j],
        capsize=4,
        linewidth=0.8
    )
ax.set_title('S1T2 (Twitch → WebKB)', fontsize=14, fontweight='bold', pad=10)
ax.set_xticks(indices + 0.3)
ax.set_xticklabels(categories, fontsize=15)
ax.set_yticks(np.arange(40, 70, 5))  # Set y ticks for this subplot
ax.set_ylim(40, 65)
ax.tick_params(axis='y', labelsize=12)  # Set y tick label size for this subplot

# Subplot 3: Data for S1T1
indices = np.arange(len(categories))
ax = axs[2]
for j, (label, values) in enumerate(data_3.items()):
    ax.bar(
        indices + j * 0.2,  # Position for each group
        values,
        0.2,  # Width of each bar
        label=label,
        yerr=errors_3[label],
        color=colors[j],
        capsize=4,
        linewidth=0.8
    )
ax.set_title('S1T1 (WebKB → WebKB)', fontsize=14, fontweight='bold', pad=10)
ax.set_xticks(indices + 0.3)
ax.set_xticklabels(categories, fontsize=15)
ax.set_yticks(np.arange(40, 70, 5))  # Set y ticks for this subplot
ax.set_ylim(40, 65)
ax.tick_params(axis='y', labelsize=12)  # Set y tick label size for this subplot

# Global legend with border
fig.legend(
    data_1.keys(),
    loc='upper center',
    bbox_to_anchor=(0.5, 1.02),  # Adjusted to move legend inside the figure
    ncol=4,
    fontsize=15,
    frameon=True,  # Enable border
)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.9])  # Adjust space to prevent legend from overlapping
plt.savefig('ablation_text_ind_1.png')
