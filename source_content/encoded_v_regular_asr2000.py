import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Poisoned', '10 % Data', '20 % Data', '30 % Data', '40 % Data', '50 % Data']
encoded_trigger = [0.57, 0.43, 0.44, 0.48, 0.44, 0.47]
constant_trigger = [0.62, 0.24, 0.27, 0.2, 0.23, 0.19]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars

# Create figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Add gray grid lines (zorder=0 for background)
ax.grid(axis='both', linestyle='-', linewidth=0.8, alpha=0.7, color='gray', zorder=0)

# Plot bars (zorder=3 to ensure bars are above grid lines)
rects1 = ax.bar(x - width/2, encoded_trigger, width, label='Encoded Trigger (ours)', color='royalblue', zorder=3)
rects2 = ax.bar(x + width/2, constant_trigger, width, label='Constant Trigger', color='tomato', zorder=3)

# Add labels, title, and custom ticks
ax.set_ylabel('ASR', fontsize=20)
ax.set_xlabel('Percentage of clean data used', fontsize=20)
ax.set_xticks(x)  # Set ticks
ax.set_xticklabels(categories, rotation=330, ha='left', fontsize=14)  # Shift rotation and alignment

ax.tick_params(axis='y', labelsize=16)
ax.tick_params(axis='x', labelsize=16)

# Move legend to the middle top of the chart
legend = ax.legend(
    fontsize=14, loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2, frameon=False, handletextpad=0.4
)

# Adjust layout and save the figure
fig.tight_layout()
plt.savefig('encoded_v_regular_asr2000.png')
