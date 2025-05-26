import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.array([0, 1, 2, 3, 4, 5])
y1 = np.array([0.83, 0.89, 0.74, 1.0, 0.78, 0.86])
y2 = np.array([0.99, 0.92, 0.93, 1.0, 1.0, 0.94])

error1 = np.array([0.08, 0.02, 0.02, 0.0, 0.01, 0.07])
error2 = np.array([0.0, 0.05, 0.02, 0.0, 0.01, 0.06])

# Plot
fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted size for clarity

# Hard (dataset 1)
ax.errorbar(
    x, y1, yerr=error1, fmt='o', linestyle='--', 
    label='Hard', color='tab:blue', markersize=15, linewidth=2, capsize=4
)

# Hard w/ CoT (dataset 2)
ax.errorbar(
    x, y2, yerr=error2, fmt='o', linestyle='--', 
    label='Hard w/ CoT', color='tab:orange', markersize=15, linewidth=2, capsize=4
)

# Labels and title
ax.set_xlabel('Interpolated path index', fontsize=18)
ax.set_ylabel('Text similarity', fontsize=18)
ax.set_title('Animal pose dataset', fontsize=20)

# Set y-axis range
ax.set_ylim(0.6, 1.05)

# Increase tick label size
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

# Legend
ax.legend(fontsize=18, loc='lower left', frameon=True)

# Grid for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Save and show
plt.tight_layout()
plt.savefig('ANIMAL_POSE_text_sim_top1.png', dpi=300)
