import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Data (approximation based on the image)
data = np.array([
    [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    [99.8, 99.9, 99.6, 99.8, 99.6, 71.4, 76.6, 76.3, 70.7, 57.5, 76.3],
    [99.5, 99.5, 98.6, 99.6, 99.3, 76.5, 81.6, 76.8, 71.4, 58.3, 76.1],
    [94.9, 97.3, 96.7, 95.5, 97.6, 98.8, 98.8, 99.3, 96.8, 98.7, 98.3],
    [96.0, 95.8, 91.6, 94.8, 88.8, 98.2, 98.5, 98.6, 93.8, 99.8, 98.7],
    [90.9, 97.2, 97.0, 97.7, 98.3, 97.5, 97.7, 98.4, 97.3, 97.8, 97.6],
    [90.0, 96.6, 95.3, 90.8, 97.6, 98.8, 98.8, 99.6, 99.1, 98.8, 98.6]
])

# Labels
train_directions = ['all dir.', 'de → en', 'zh → en', 'en → de', 'en → zh', 'fr → de', 'de → fr']
test_directions = ['cs → en', 'de → en', 'ja → en', 'ru → en', 'zh → en', 'en → cs', 'en → de', 'en → hr', 'en → ja', 'en → ru', 'en → zh']

# Split data into two parts
data_part1 = data[:, :5]  # First 5 columns
data_part2 = data[:, 5:]  # Last 6 columns

# Set up the color map with reversed 'coolwarm' and adjusted range
cmap = sns.diverging_palette(0, 240, as_cmap=True, s=80, l=30)  # Saturation: 100%, Lightness: 30%

# Create subplots
fig, axes = plt.subplots(1, 2, figsize=(9, 4))

# Plot first heatmap (first 5 columns)
sns.heatmap(
    data_part1, 
    annot=True, 
    fmt=".1f", 
    cmap=cmap, 
    xticklabels=test_directions[:5], 
    yticklabels=train_directions,
    cbar=False,
    ax=axes[0],
    vmin=60, vmax=100  # Ensure color starts from 60
)
axes[0].set_xlabel("Test direction", fontsize=12, fontweight="bold")
axes[0].set_ylabel("Train direction", fontsize=12, fontweight="bold")
axes[0].tick_params(axis='x', rotation=30, labelsize=10)
axes[0].tick_params(axis='y', rotation=30, labelsize=10)

# Plot second heatmap (last 6 columns)
sns.heatmap(
    data_part2, 
    annot=True, 
    fmt=".1f", 
    cmap=cmap, 
    xticklabels=test_directions[5:], 
    yticklabels=False, 
    cbar_kws={"shrink": 0.8},
    ax=axes[1],
    vmin=60, vmax=100  # Ensure color starts from 60
)
axes[1].set_xlabel("Test direction", fontsize=12, fontweight="bold")
axes[1].tick_params(axis='x', rotation=30, labelsize=10)

# Adjust layout
plt.tight_layout()

# Save or show
plt.savefig("language_trans.png")