import matplotlib.pyplot as plt
import numpy as np

# Parameters
N_points = 10_000

# Generate three normal distributions with different means and standard deviations
dataset1 = np.random.normal(0, 1, size=N_points)  # Mean = 0, Std = 1
dataset2 = np.random.normal(2, 1.5, size=N_points)  # Mean = 2, Std = 1.5
dataset3 = np.random.normal(-2, 2, size=N_points)  # Mean = -2, Std = 2

# Use a constant bin width to make the histograms easier to compare visually
bin_width = 0.25
bins = np.arange(np.min([dataset1, dataset2, dataset3]),
                 np.max([dataset1, dataset2, dataset3]) + bin_width, bin_width)

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the first histogram with an uncommon color
ax.hist(dataset1, bins=bins, label="(μ=0, σ=1)", color='#7F00FF', alpha=0.7, edgecolor='black')

# Plot the second histogram with an uncommon color (flipped upside down)
ax.hist(dataset2, weights=-np.ones_like(dataset2), bins=bins, label="(μ=2, σ=1.5)", color='#FF007F', alpha=0.7, edgecolor='black')

# Plot the third histogram with an uncommon color
ax.hist(dataset3, bins=bins, label="(μ=-2, σ=2)", color='#00FF7F', alpha=0.7, edgecolor='black')

# Add a horizontal line at y=0
ax.axhline(0, color="k", linewidth=1)

# Customize ticks
ax.tick_params(axis='both', which='major', labelsize=14, length=8, width=1.5)

# Customize legend
ax.legend(loc='upper right', fontsize=12, framealpha=0.9, title="Datasets", title_fontsize=14)

# Add grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add title and labels
ax.set_xlabel("Value", fontsize=18, labelpad=10)
ax.set_ylabel("Frequency", fontsize=18, labelpad=10)

plt.tight_layout()
# Save the figure
plt.savefig('hist3.png')
