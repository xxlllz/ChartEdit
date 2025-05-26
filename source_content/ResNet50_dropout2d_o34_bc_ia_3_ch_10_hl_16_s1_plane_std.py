import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y = np.array([0.05, 0.22, 0.07, 0.03, 0.06, 0.12, 0.1, 0.04, 0.2, 0.09])
error = np.array([0.06, 0.1, 0.05, 0.02, 0.03, 0.04, 0.03, 0.02, 0.08, 0.03])

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, color='b', label='Activation')

# Add error area with deeper color and blue border
plt.fill_between(x, y - error, y + error, color='#4FC0FF', alpha=0.7, edgecolor='b', label='± Error')

# Titles and labels
plt.title('Class-Dependent Activation\nacross FCN Memory Blocks', fontsize=18)
plt.xlabel('Memory Block Index', fontsize=18)
plt.ylabel('Average Softmax Activation (± SD)', fontsize=18)

# Set y-axis limits and customize ticks
plt.ylim(0, 0.65)
plt.yticks(np.arange(0, 0.65, 0.1),fontsize=18)  # Hide 0.65 by omitting it from ticks



# Adjust layout and save plot
plt.tight_layout()
plt.savefig('ResNet50_dropout2d_o34_bc_ia_3_ch_10_hl_16_s1_plane_std.png')
