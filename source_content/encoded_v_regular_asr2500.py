import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Poisoned', '10 % Data', '20 % Data', '30 % Data', '40 % Data', '50 % Data']
encoded_trigger = [0.57, 0.41, 0.4, 0.34, 0.46, 0.47]
constant_trigger = [0.63, 0.24, 0.27, 0.21, 0.23, 0.2]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Add grid lines
ax.grid(axis='both', linestyle='-', linewidth=0.8, alpha=0.7, color='gray', zorder=0)

# Plot bars with zorder to make sure they are above grid lines
rects1 = ax.bar(x - width/2, encoded_trigger, width, label='Encoded Trigger (ours)', color='royalblue', zorder=3)
rects2 = ax.bar(x + width/2, constant_trigger, width, label='Constant Trigger', color='tomato', zorder=3)

# Add labels, ticks, and title
ax.set_ylabel('ASR', fontsize=20)
ax.set_xlabel('Percentage of clean data used', fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=330, ha='left', fontsize=14)
ax.set_yticks(np.arange(0, 0.8, 0.1))  # Add y-axis ticks from 0 to 0.7
ax.set_ylim([0, 0.7])  # Extend y-axis to 0.8 for better visualization
ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='x', labelsize=16)

# Add legend and place it at the top center
ax.legend(
    fontsize=18,
    loc='upper center',
    bbox_to_anchor=(0.5, 1.15),
    ncol=2,
    frameon=False,
    handletextpad=0.4
)

# Adjust layout and save the figure
fig.tight_layout()
plt.savefig('encoded_v_regular_asr2500.png', dpi=300)
