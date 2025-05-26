import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0.36, 0.68, 50)
y1 = np.linspace(-29, 28, 50)
y2 = np.linspace(-11, 9, 50)

# Create the plot
plt.figure(figsize=(7, 4))

# Plotting the line
plt.plot(x, y1, 'b-')

# Plotting the scatter
plt.scatter(x, y2, color='red', s=20)
plt.plot(x, y2, color='red', linestyle='-', linewidth=1)
# Annotate with vertical dashed lines
plt.axvline(x=0.45, color='red', linestyle='--', label='Planet b full contact')
plt.axvline(x=0.625, color='red', linestyle='--')
plt.axvline(x=0.46, color='blue', linestyle='--')
plt.axvline(x=0.59, color='blue', linestyle='--', label='Planet c full contact')

plt.text(0.64, -39, '+2.460029e6', color='black', fontsize=10)
# Labeling the axes
plt.xlabel('Time [BJD]', fontsize=14)
plt.ylabel('RV [km/s]', fontsize=14)

# Adjust x-axis to better match the example
plt.xlim(0.35, 0.70)
plt.xticks(np.arange(0.35, 0.71, 0.05))

# Adding the legend
plt.legend(loc='lower center', fontsize=12, frameon=False)
# Display the plot
plt.tight_layout()
plt.savefig('rv_time.png')