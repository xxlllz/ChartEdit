import matplotlib.pyplot as plt
import numpy as np

# Define data for resource usage
# Each resource is a sequence of (start, duration) tuples
cpu_1 = [(0, 2.5), (3, 1.5), (5.5, 2)]  # CPU 1 usage
cpu_2 = [(0.5, 1), (2, 2), (5, 1.5), (7, 1)]  # CPU 2 usage
cpu_3 = [(1, 0.8), (3, 1.2), (6, 0.5), (8, 1)]  # CPU 3 usage
cpu_4 = [(0.2, 1.8), (4, 1.2), (7.5, 1.5)]  # CPU 4 usage
disk = [(1.5, 1.2), (4.5, 0.8), (8, 1)]  # Disk usage
network = [(0.8, 0.5), (2.5, 0.7), (5.2, 0.3), (7, 0.6)]  # Network usage
gpu = [(0, 1.5), (3.5, 1), (6, 2)]  # GPU usage
memory = [(1, 0.8), (4, 1.5), (7, 1)]  # Memory usage

# Plot
fig, ax = plt.subplots(figsize=(8, 6))

# Define uncommon colors
colors = {
    'CPU 1': '#7F00FF',  # Purple
    'CPU 2': '#FF007F',  # Pink
    'CPU 3': '#00FF7F',  # Green
    'CPU 4': '#FF7F00',  # Orange
    'Disk': '#00FFFF',   # Cyan
    'Network': '#FF00FF',# Magenta
    'GPU': '#FFFF00',    # Yellow
    'Memory': '#8A2BE2'  # Blue Violet
}

# Plot each resource with uncommon colors
ax.broken_barh(cpu_1, (7.8, 0.4), color=colors['CPU 1'], label='CPU 1', zorder=2)
ax.broken_barh(cpu_2, (6.8, 0.4), color=colors['CPU 2'], label='CPU 2', zorder=2)
ax.broken_barh(cpu_3, (5.8, 0.4), color=colors['CPU 3'], label='CPU 3', zorder=2)
ax.broken_barh(cpu_4, (4.8, 0.4), color=colors['CPU 4'], label='CPU 4', zorder=2)
ax.broken_barh(disk, (3.8, 0.4), color=colors['Disk'], label='Disk', zorder=2)
ax.broken_barh(network, (2.8, 0.4), color=colors['Network'], label='Network', zorder=2)
ax.broken_barh(gpu, (1.8, 0.4), color=colors['GPU'], label='GPU', zorder=2)
ax.broken_barh(memory, (0.8, 0.4), color=colors['Memory'], label='Memory', zorder=2)

# Set x and y limits
ax.set_xlim(0, 9)
ax.set_ylim(0, 9)

# Set y ticks and labels
ax.set_yticks([8, 7, 6, 5, 4, 3, 2, 1],
              labels=["CPU 1", "CPU 2", "CPU 3", "CPU 4", "Disk", "Network", "GPU", "Memory"])

# Increase x and y ticks size
ax.tick_params(axis='both', which='major', labelsize=15, length=8, width=1.5)

# Add grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, zorder=0)

# Add title and labels
ax.set_xlabel("Time (s)", fontsize=18, labelpad=10)
ax.set_ylabel("Resource", fontsize=18, labelpad=10)

plt.tight_layout()
# Save the figure
plt.savefig('sepbar.png')