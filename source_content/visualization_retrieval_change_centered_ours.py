import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Dinov2-Giant', 'CLIP (ViT-B32)', 'BIT-50', 'CLIPSeg (Rd64)', 'SAM (ViT-B)']
cosine = [0.81, 0.78, 0.74, 0.28, 0.61]
pi_cosine = [0.85, 0.83, 0.84, 0.83, 0.80]
linear = [0.81, 0.78, 0.72, 0.28, 0.61]
pi_linear = [0.85, 0.826, 0.81, 0.62, 0.78]
rbf = [0.803, 0.67, 0.68, 0.26, 0.46]
pi_rbf = [0.85, 0.82, 0.83, 0.83, 0.78]

# Bar width
bar_width = 0.1

# Positions of bars
r1 = np.arange(len(categories))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]
r6 = [x + bar_width for x in r5]

# Create the figure with specified size (width, height)
plt.figure(figsize=(10, 4))  # Example: 10 inches wide by 6 inches high

# Create bar plot
plt.bar(r1, cosine, color='tab:blue', width=bar_width, edgecolor='grey', hatch='/', label='Cosine Kernel')
plt.bar(r2, pi_cosine, color='tab:blue', width=bar_width, edgecolor='grey', label='(ours) PI Cosine Kernel')
plt.bar(r3, linear, color='tab:orange', width=bar_width, edgecolor='grey', hatch='/', label='Linear Kernel')
plt.bar(r4, pi_linear, color='tab:orange', width=bar_width, edgecolor='grey', label='(ours) PI Linear Kernel')
plt.bar(r5, rbf, color='tab:green', width=bar_width, edgecolor='grey', hatch='/', label='RBF Kernel')
plt.bar(r6, pi_rbf, color='tab:green', width=bar_width, edgecolor='grey', label='(ours) PI RBF Kernel')

# Labels and legend
plt.xlabel('Architecture')
plt.xticks([r + bar_width*2.5 for r in range(len(categories))], categories)
plt.ylabel('Retrieval F1@1')
# Move the legend outside of the plot
# Move the legend to the right middle part of the plot
plt.legend(title='Similarity Metric', bbox_to_anchor=(1.05, 0.5), loc='center left')

# Adjust layout to make space for the legend without changing the figure size
plt.tight_layout()  # Automatically adjusts the layout
plt.grid(axis='y', linestyle='--', color='gray', alpha=0.7)  # Adjust the line style, color, and transparency
plt.yticks(np.arange(0.0, 1.0, 0.2))  # Set y-ticks from 0.0 to 1.0 with step size 0.2

# Show plot
plt.tight_layout()
plt.savefig('visualization_retrieval_change_centered_ours.png')