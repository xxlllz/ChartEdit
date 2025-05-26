import matplotlib.pyplot as plt

# Data
x = [57, 62, 59, 62, 67, 68.5, 68]
y = [12.5, 12, 12, 11.6, 11, 10.2, 10]
labels = ['MAE-L', 'MoCov3-L', 'DINO-B', 'JEPA-H', 'CLIP-L', 'SigLIP-L', 'DINov2-L']
colors = ['black', 'orange', 'royalblue', 'purple', 'green', 'grey', 'red']

# Create plot
fig, ax = plt.subplots(figsize=(6, 6))  # Slightly larger figure

# Add diagonal dashed line (zorder=0 for bottom layer)
plt.plot([50, 75], [14, 9], ls='--', color='grey', alpha=0.5, linewidth=3, zorder=0)

# Scatter plot (zorder=3 to keep above the line)
ax.scatter(x, y, c=colors, s=400, edgecolor='white', linewidth=1, zorder=3)

# Add labels with customized positions
for i, label in enumerate(labels):
    if i in [2, 3, 4, 6]:  # Adjust position for 3rd, 4th, and 7th labels
        ax.annotate(label, (x[i], y[i]), xytext=(0, -18), textcoords='offset points', fontsize=14, weight='bold', ha='center', va='center')
    else:  # Keep the rest on top
        ax.annotate(label, (x[i], y[i]), xytext=(0, 18), textcoords='offset points', fontsize=14, weight='bold', ha='center', va='center')

# Set axis labels
ax.set_xlabel('Validation Acc. (%)', fontsize=20, weight='bold')
ax.set_ylabel('FID-50K', fontsize=20, weight='bold')

# Set x and y limits
plt.xlim(50, 80)
plt.ylim(9, 14)

# Customize ticks
ax.tick_params(axis='x', labelsize=18)
ax.tick_params(axis='y', labelsize=18)

# Save and display
plt.tight_layout()
plt.savefig('encoder_type.png')
