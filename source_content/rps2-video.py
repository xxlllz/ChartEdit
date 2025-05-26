import matplotlib.pyplot as plt
import numpy as np

# Sample data
x1 = [5, 10, 15, 20, 25, 30]
y1 = [5, 9, 13, 16, 20, 23]  # blue
y3 = [5, 9.5, 14.5, 19, 23.5, 28]  # purple

x2 = [5, 10, 15, 20, 25]
y2 = [5, 9.5, 14.5, 19, 23.5]  # green


# Create figure and set size (narrower image)
plt.figure(figsize=(7.2, 4))  # Adjusted width and height for a narrower image

# Plot Knative-con (blue, lower brightness)
y1_style = {'color': '#1f3aC9', 'linestyle': '--', 'linewidth': 4, 'marker': 'o', 'markersize': 9}
plt.plot(x1, y1, label='Knative-con', **y1_style)

# Plot Knative-rts (green)
y2_style = {'color': 'green', 'linestyle': '-.', 'linewidth': 4, 'marker': 'D', 'markersize': 9}
plt.plot(x2, y2, label='Knative-rts', **y2_style)

# Plot Oprc (purple)
y3_style = {'color': 'purple', 'linestyle': ':', 'linewidth': 4, 'marker': 's', 'markersize': 9}
plt.plot(x1, y3, label='Oprc', **y3_style)

# Add legend
plt.legend(loc='upper left', fontsize=18)
# Set tick parameters for better readability
plt.tick_params(axis='both', labelsize=16)
# Labels
plt.xlabel('target throughput (rps)', fontsize=22)
plt.ylabel('actual throughput (rps)', fontsize=22)

# Grid
plt.grid(True)

# Show plot
plt.tight_layout()
plt.savefig('rps2-video.png')

