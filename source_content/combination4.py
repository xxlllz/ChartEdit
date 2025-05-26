import matplotlib.pyplot as plt
import numpy as np

# Generate synthetic data
x = np.arange(0, 41, 3)
real_value = 80 + x * 2
 # Let's assume predicted value close to real value for demonstration
x1 = np.array([1,4,7,10,13,16,19,22,25,28,31,34,37,40])
predicted_value = 80 + x1 * 2 
# Create the figure and axis
fig, ax = plt.subplots(figsize=(8,4))

# Plot real values
ax.plot(x, real_value, '-k', linewidth=4, label='real value')

# Plot predicted values
ax.plot(x1, predicted_value, 'D', markersize=14, color='none', markeredgecolor='orange', label='predicted value',markeredgewidth=5,zorder=10,clip_on=False)

# Set labels and title
ax.set_xlabel('Time slot', fontsize=16)
ax.set_ylabel('Distance(m)', fontsize=16)
plt.ylim(75,165)
plt.yticks([80,100,120,140,160])
plt.xlim(0, 40)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)

# Add a legend
ax.legend(fontsize=20)

plt.tight_layout()
plt.savefig('combination4.png')