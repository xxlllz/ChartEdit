import matplotlib.pyplot as plt
import numpy as np

# Adjusted sample data based on observed distribution
np.random.seed(10)
data = [
    np.random.normal(1, 0.5, 100),  # For 5-days
    np.random.normal(0.5, 0.7, 100),  # For 3-days
    np.random.normal(-0.2, 0.8, 100),  # For 1-day
    np.random.normal(0, 0.6, 100)  # For 1-day (2)
]

fig, ax = plt.subplots(figsize=(8, 6))  # Adjusted figure size

# Ensure grid lines are below the plot elements
ax.set_axisbelow(True)

# Add grid lines for the background
ax.grid(which='major', linestyle='--', linewidth=0.8, alpha=0.7)  # Add dashed grid lines

# Create violin plot
parts = ax.violinplot(data, showmeans=False, showmedians=False, showextrema=False)

# Style the violins
for i, pc in enumerate(parts['bodies']):
    pc.set_facecolor('#87CEEB')  # Light blue
    pc.set_edgecolor('black')
    pc.set_alpha(0.6)  # Adjusted transparency for better visibility
    if i == 2:  # Add hatch to the third violin
        pc.set_hatch('\\')

# Overlay quartile information
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
means = np.mean(data, axis=1)
ax.errorbar(range(1, len(means) + 1), means, yerr=[means - quartile1, quartile3 - means],
            fmt='o', color='purple', lw=2, label='Mean ± IQR', markersize=10, capsize=6, elinewidth=2)

# Title, labels, and annotations
ax.set_xticks([1, 2, 3, 4])
ax.set_xticklabels(['5-days', '3-days', '1-day', '1-day (2)'], fontsize=12, weight='bold')
ax.set_xlabel('Cadence (C)', fontsize=14, weight='bold', labelpad=10)
ax.set_ylabel(r'$\tau_g \ \text{(days)}$', fontsize=14, labelpad=10)  # Corrected LaTeX expression
ax.set_yticks(np.arange(-2, 3, 1))
ax.set_yticklabels(range(-2, 3), fontsize=12)

# Add annotations and style
ax.text(0.5, 4.2, r'WFST-$gri$: $\mathcal{Y} = 1, \mathcal{M} = 6, \text{SNR}_\sigma = 3$',
         fontsize=12, ha='center', transform=ax.transAxes, style='italic')
ax.text(-0.15, 4.0, '(b)', fontsize=14, weight='bold', transform=ax.transAxes)

plt.savefig('agn_cadence.png', dpi=300)
