import matplotlib.pyplot as plt
import numpy as np

# Step values (x-axis) and corresponding y-values and errors for each line
steps1 = np.array([100000, 300000, 500000, 700000, 800000, 1000000, 1300000, 1600000, 1900000, 2200000, 2300000, 2500000, 2700000, 2800000, 3000000])  # From Scratch [CNN]
data1 = np.array([0, 0.1, 0.4, 0.65, 0.74, 0.85, 0.9, 0.88, 0.9, 0.906, 0.929, 0.913, 0.912, 0.922, 0.92])
error1 = np.array([0.0, 0.04, 0.11, 0.11, 0.12, 0.05, 0.01, 0.006, 0.01, 0.007, 0.009, 0.005, 0.006, 0.008, 0.002])

steps2 = np.array([100000, 400000, 600000, 800000, 1000000, 1200000, 1400000, 1600000, 1800000, 2000000, 2200000, 2400000, 2600000, 2800000, 3000000])  # VC-1 [Full ViT-L]
data2 = np.array([0.0, 0.3, 0.45, 0.60, 0.56, 0.64, 0.68, 0.70, 0.72, 0.66, 0.73, 0.72, 0.80, 0.83, 0.79])
error2 = np.array([0.0, 0.05, 0.06, 0.07, 0.06, 0.05, 0.04, 0.025, 0.05, 0.05, 0.08, 0.06, 0.05, 0.07, 0.04])

steps3 = np.array([100000, 300000, 500000, 600000, 700000, 800000, 900000, 1000000, 1100000, 1200000, 1300000, 1500000, 1600000, 1800000, 2000000, 2300000, 2500000,  2700000, 2900000, 3000000])  # VC-1 [⅔ ViT-L]
data3 = np.array([0.0, 0.2, 0.25, 0.4, 0.52, 0.58, 0.62, 0.71, 0.67, 0.72, 0.74, 0.75, 0.74, 0.78, 0.76, 0.76, 0.78, 0.78, 0.79, 0.76])
error3 = np.array([0, 0.05, 0.08, 0.09, 0.07, 0.08, 0.08, 0.06, 0.07, 0.07, 0.06, 0.07, 0.09, 0.05, 0.06, 0.04, 0.05, 0.03, 0.04, 0.05])

steps4 = np.array([100000, 200000, 300000, 400000, 500000, 700000, 800000, 1000000, 1200000, 1400000,  1600000, 1800000, 2000000, 2100000, 2300000, 2500000, 2700000, 2800000, 2900000, 3000000])  # VC-1 [⅓ ViT-L]
data4 = np.array([0, 0.015, 0.12, 0.10, 0.20, 0.32, 0.31, 0.30, 0.38, 0.35, 0.40, 0.42, 0.43, 0.44, 0.44, 0.45, 0.51, 0.50, 0.55, 0.47])
error4 = np.array([0, 0.01, 0.01, 0.03, 0.04, 0.04, 0.04, 0.035, 0.07, 0.06, 0.04, 0.05, 0.07, 0.06, 0.04, 0.06, 0.04, 0.06, 0.07, 0.12])


# Create figure and axis
fig, ax = plt.subplots(figsize=(15, 8))

# Plot each line with shaded error bars
ax.plot(steps1, data1, label='From Scratch [CNN]', color='slateblue', linewidth=3)
ax.fill_between(steps1, data1 - error1, data1 + error1, color='slateblue', alpha=0.2)

ax.plot(steps2, data2, label='VC-1 [Full ViT-L]', color='lime', linewidth=3)
ax.fill_between(steps2, data2 - error2, data2 + error2, color='lime', alpha=0.2)

ax.plot(steps3, data3, label='VC-1 [⅔ ViT-L]', color='deepskyblue', linewidth=3)
ax.fill_between(steps3, data3 - error3, data3 + error3, color='deepskyblue', alpha=0.2)

ax.plot(steps4, data4, label='VC-1 [⅓ ViT-L]', color='darkorange', linewidth=3)
ax.fill_between(steps4, data4 - error4, data4 + error4, color='darkorange', alpha=0.2)

# Set labels and title
ax.set_xlabel('Step', fontsize=25, labelpad=5)
ax.set_ylabel('Return (ID)', fontsize=25, labelpad=5)
ax.set_title('Walker Walk (DMC)', fontsize=28, pad=20)

# Set x-axis tick labels
ax.set_xticks([0, 600000, 1200000, 1800000, 2400000, 3000000])
ax.set_xticklabels(['0', '600K', '1.2M', '1.8M', '2.4M', '3M'], fontsize=22)

# Set y-axis ticks
ax.set_yticks(np.linspace(0, 1, 5))  # Y-axis ticks at 0.0, 0.25, 0.5, 0.75, 1.0
ax.tick_params(axis='y', labelsize=22)

# Add refined gray grid lines
ax.grid(axis='y', color='gray', linestyle='-', linewidth=1, alpha=0.5)
ax.grid(axis='x', color='lightgray', linestyle='-', linewidth=1, alpha=0.5)

# Set legend
ax.legend(
    loc='upper center',                 # Place legend above the plot
    bbox_to_anchor=(0.45, -0.12),        # Centered below the plot
    fontsize=20,                        # Adjust font size
    ncol=4,                             # 2-column layout
    frameon=False,                       # Add a border to legend
    framealpha=0.3,                     # Make legend background semi-transparent
    edgecolor='gray'                    # Border color for legend
)

# Add slight shadow effect to the plot
ax.patch.set_alpha(0.9)

# Adjust layout to make room for the legend
plt.tight_layout()

# Display the plot
plt.savefig('curves_vc1.png')
