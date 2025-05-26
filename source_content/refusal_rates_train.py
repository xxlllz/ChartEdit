import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Gemma-2B-IT', 'Llama-3-8B-Instruct']
groups = ['Initial', 'DPO', 'DPO + SFT', 'DPO (gold)', 'DPO (filtered)']
data = np.array([[80, 55, 85, 90, 95], [77, 30, 77, 78, 94]])
errors = np.array([[0, 5, 2, 3, 0], [1, 6, 3, 6, 0]])

# Colors
colors = ['#606060', '#d62828', '#38A3A5', '#FFD60A', '#57C4E5']

# Bar plot details
barWidth = 0.15

# Position each bar
r1 = np.arange(len(categories))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

# Adjust figure size
plt.figure(figsize=(12, 9))

plt.bar(r1, data[:, 0], color=colors[0], width=barWidth, label=groups[0], yerr=errors[:, 0], capsize=5)
plt.bar(r2, data[:, 1], color=colors[1], width=barWidth, label=groups[1], yerr=errors[:, 1], capsize=5)
plt.bar(r3, data[:, 2], color=colors[2], width=barWidth, label=groups[2], yerr=errors[:, 2], capsize=5)
plt.bar(r4, data[:, 3], color=colors[3], width=barWidth, label=groups[3], yerr=errors[:, 3], capsize=5)
plt.bar(r5, data[:, 4], color=colors[4], width=barWidth, label=groups[4], yerr=errors[:, 4], capsize=5)

# Add star markers for specific bars
plt.scatter([r5[0], r5[1]], [85, 85], color='black', marker='*', s=400, zorder=3)

# Add ticks on the middle of the groups
plt.ylabel('Refusal Rate (%)', fontsize=24)
plt.xticks([r + 2 * barWidth for r in range(len(categories))], categories, fontsize=24)  # Adjusted font size for x-axis

# Set y-axis ticks and font size
plt.yticks(np.arange(0, 111, 20), fontsize=24)  # Fixed y-axis ticks

# Remove background grid lines
plt.grid(False)


# Create legend with specified order
handles, labels = plt.gca().get_legend_handles_labels()
new_order = [0, 1, 2, 3, 4]  # Reorder handles and labels for the desired legend arrangement
handles = [handles[i] for i in new_order]
labels = [labels[i] for i in new_order]
plt.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=3, frameon=False, fontsize=30)

# Adjust layout to reduce overlap
plt.tight_layout()

# Save the figure
plt.savefig('refusal_rates_train.png')
