import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(42)

# New treatment data with modified distributions and more data
inc = 0.1
e1 = np.random.normal(0, 1, size=100)  # Normal distribution
e2 = np.random.normal(0, 1, size=100)  # Normal distribution
e3 = np.random.normal(0, 1 + inc, size=100)  # Wider distribution (inc)
e4 = np.random.normal(0, 1 + 2*inc, size=100)  # Even wider distribution
e5 = np.random.normal(0, 1 - inc, size=100)  # Narrower distribution
e6 = np.random.normal(0, 1.5, size=100)  # Larger variance

treatments = [e1, e2, e3, e4, e5, e6]

# Directly compute medians and confidence intervals (2.5th and 97.5th percentiles)
def compute_median_and_ci(data, confidence_level=0.95):
    median = np.median(data)
    lower_ci = np.percentile(data, (1 - confidence_level) / 2 * 100)
    upper_ci = np.percentile(data, (1 + confidence_level) / 2 * 100)
    return median, (lower_ci, upper_ci)

# Compute medians and confidence intervals for all treatments
medians = []
conf_intervals = []

for treatment in treatments:
    median, ci = compute_median_and_ci(treatment)
    medians.append(median)
    conf_intervals.append(ci)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define colors for boxplots
box_colors = ['#9b59b6', '#1f77b4', '#f39c12', '#e74c3c', '#2ecc71', '#34495e']  # Uncommon colors

# Create the boxplot with custom colors
bp = ax.boxplot(treatments, sym='k+', positions=np.arange(1, len(treatments) + 1),
                notch=True, bootstrap=5000)

# Customize the boxplot appearance
# Update box colors
for patch, color in zip(bp['boxes'], box_colors):
    patch.set_linewidth(1.5)

# Add custom medians and confidence intervals manually
for i, median in enumerate(medians):
    ax.plot([i+1, i+1], [conf_intervals[i][0], conf_intervals[i][1]], color='black', lw=2)
    ax.plot(i+1, median, marker='o', color='white', markeredgecolor='black', markersize=10)

# Set axis labels and title with larger font sizes
ax.set_xlabel('Treatment', fontsize=16, fontweight='bold')
ax.set_ylabel('Response', fontsize=16, fontweight='bold')

# Increase tick size
ax.tick_params(axis='x', labelsize=16)  # Increase font size for x-axis ticks
ax.tick_params(axis='y', labelsize=16)  # Increase font size for y-axis ticks

# Set whisker and fliers style
plt.setp(bp['whiskers'], color='k', linestyle='-', linewidth=1.5)
plt.setp(bp['fliers'], markersize=6.0, marker='o', color='darkred')

# Show the plot
plt.tight_layout()
plt.savefig('boxwhite.png')