import matplotlib.pyplot as plt
import numpy as np

# Sample data

y1_a = [9, 5, 5, 2, 1.5]
x1_a = [0.1, 0.2, 0.3, 0.4, 0.5]

y2_a = [5, 2, 1.5, 1]
x2_a = [0.1, 0.3, 0.55, 1]

y1_b = [3.8, 2.5, 1]
x1_b = [0.05, 0.07, 0.09]

y2_b = [3.5, 2.5, 1.4, 1.2, 1.1, 1]
x2_b = [0, 0.05, 0.2, 0.5, 0.75, 1]

fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Plot for (a)
ax[0].plot(x1_a, y1_a, 'o-', color='C0', label='Tiled fused-layer')
ax[0].plot(x2_a, y2_a, 'o-', color='C1', label='Baseline (best of layer-by-layer or untiled fused-layer)')
ax[0].set_title('(a) conv+conv\nWidth: 56, Channel: 64', fontsize=16)  # Adjust title font size
ax[0].set_xlabel('Norm. capacity', fontsize=14)  # Adjust x-label font size
ax[0].set_ylabel('Norm. off-chip transfers', fontsize=14)  # Adjust y-label font size

# Set y-axis ticks and limits for (a)
ax[0].set_yticks([2, 4, 6, 8])
ax[0].set_ylim(0, 10)

# Adjust x and y tick size for (a)
ax[0].tick_params(axis='x', labelsize=16)  # Adjust x-axis tick font size
ax[0].tick_params(axis='y', labelsize=16)  # Adjust y-axis tick font size

# Plot for (b)
ax[1].plot(x1_b, y1_b, 'o-', color='C0', label='Tiled fused-layer')
ax[1].plot(x2_b, y2_b, 'o-', color='C1', label='Baseline (best of layer-by-layer or untiled fused-layer)')
ax[1].set_title('(b) conv+conv\nWidth: 112, Channel: 32', fontsize=16)  # Adjust title font size
ax[1].set_xlabel('Norm. capacity', fontsize=14)  # Adjust x-label font size

# Set y-axis ticks and limits for (b)
ax[1].set_yticks([1, 2, 3])
ax[1].set_ylim(0.9, 4.1)  # Slightly extend the range to add padding

# Adjust x and y tick size for (b)
ax[1].tick_params(axis='x', labelsize=16)  # Adjust x-axis tick font size
ax[1].tick_params(axis='y', labelsize=16)  # Adjust y-axis tick font size

# Add a single legend for the entire figure
fig.legend(
    handles=[ax[0].get_lines()[0], ax[0].get_lines()[1]],  # Only use the lines from the first plot
    labels=['Tiled fused-layer', 'Baseline (best of layer-by-layer or untiled fused-layer)'],
    loc='lower center',
    fontsize=14,  # Adjust legend font size
    ncol=2,  # Ensure the labels are in one row
    bbox_to_anchor=(0.5, 0)  # Adjust the position of the legend
)

plt.tight_layout(rect=[0, 0.1, 1, 1])
plt.savefig('conv+conv.lbl+pq.png')
plt.show()
