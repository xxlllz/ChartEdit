import matplotlib.pyplot as plt
import numpy as np

# Data
tokens = ['3B', '6B', '9B']

sft_20k = [0, 180, 180]  # +0%, +100%, +200%
sft_30k = [420, 600, 820]  # +400%, +500%, +600%
sft_50k = [780, 800, 1000]  # +800%, +900%, +1000%

# Labels
x_labels = tokens
y_labels = ['+0%', '+200%', '+400%', '+600%', '+800%', '+1000%']

# Create plot
plt.figure(figsize=(8, 6))

# Plot SFT-20K
plt.plot(tokens, sft_20k, 'o-', color='blue', label='SFT-20K', linewidth=2.5, markersize=10)
plt.plot(tokens[0], sft_20k[0], 'ro', markersize=10)  # Highlight first point

# Plot SFT-30K
plt.plot(tokens, sft_30k, 'x--', color='orange', label='SFT-30K', linewidth=2.5, markersize=10)

# Plot SFT-50K
plt.plot(tokens, sft_50k, 's:', color='green', label='SFT-50K', linewidth=2.5, markersize=10)

# Customize Legend
plt.legend(
    loc='upper left',
    fontsize=14,
    frameon=True,  # Add border to legend
    framealpha=1,  # Border transparency (1 = no transparency)
    edgecolor='black'  # Border color
)

# Add Titles and Labels
plt.xlabel('Trained Alignment Data (tokens)', fontsize=16, fontweight='bold', labelpad=10)
plt.ylabel('Harmlessness', fontsize=16, fontweight='bold', labelpad=10)

# Customize Y-Ticks
plt.yticks(range(0, 1200, 200), y_labels, fontsize=14)

# Customize X-Ticks
plt.xticks(fontsize=14)

# Grid Settings
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust Layout
plt.tight_layout()

# Save Figure
plt.savefig('ablation3-harmlessness-highlight.png', dpi=300)