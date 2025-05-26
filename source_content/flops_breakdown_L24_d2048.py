import matplotlib.pyplot as plt
import numpy as np

# Data
x = ['128', '256', '512', '1K', '2K', '4K', '8K']
blue_ratios = [0.661, 0.656, 0.646, 0.627, 0.593, 0.533, 0.444]  # Blue (FFN) ratios
green_ratios = [0.339, 0.344, 0.354, 0.373, 0.407, 0.467, 0.556]  # Green (Attention) ratios

# Initialize data
blue_values = [0.11 * blue_ratios[0]]  # Blue part for 128
total_values = [0.11]  # Total value for 128

# Calculate blue and green values iteratively
for i in range(1, len(x)):
    blue_value = total_values[i - 1]  # Current blue part equals previous total
    total_value = blue_value / blue_ratios[i]  # Calculate total based on blue ratio
    green_value = total_value - blue_value  # Calculate green part

    blue_values.append(blue_value)
    total_values.append(total_value)

green_values = [total_values[i] - blue_values[i] for i in range(len(total_values))]  # Green part

# Plotting
indices = np.arange(len(x))
bar_width = 0.3

fig, ax = plt.subplots(figsize=(9, 5.5))  # Adjust figure size to make it narrower
plt.bar(indices, blue_values, width=bar_width, label='FFN FLOPs', color='cornflowerblue')
plt.bar(indices, green_values, width=bar_width, bottom=blue_values, label='Attention FLOPs', color='palegreen')

# Percentage annotations
for i in range(len(x)):
    plt.text(indices[i], total_values[i], f'{blue_ratios[i] * 100:.1f}%',
             ha='center', va='bottom', color='blue', fontsize=16)

# Labels and title
plt.xlabel('T (Context Length)', fontsize=20)
plt.ylabel('FLOPs', fontsize=20)
plt.xticks(indices, x, fontsize=20)
plt.yticks(np.arange(0, 3.5, 1), ['0', '1', '2', '3'], fontsize=20)

# Add scientific notation label
ax.text(-0.5, 3.2, '1e13', fontsize=12, ha='center', va='center')
plt.title(r'$L=24, d=2048$', fontsize=16)
plt.legend(loc='upper left',fontsize=18)

# Save plot
plt.tight_layout()
plt.savefig('flops_breakdown_L24_d2048.png')
