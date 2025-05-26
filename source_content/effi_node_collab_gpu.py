import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [13000, 15000, 17000, 19000, 21000]
rdgsl = [13, 19, 24, 32, 39]
dgib = [12, 16, 21, 28, 32]
dg_mamba = [11, 16, 20, 24, 29]

plt.figure(figsize=(6, 5))

# RDGSL line
plt.plot(x, rdgsl, 's-', color='c', label='RDGSL', linestyle='-', linewidth=2, markersize=12,
         markeredgecolor='white', markeredgewidth=2)

# DGIB line
plt.plot(x, dgib, 'v-', color='pink', label='DGIB', linestyle='-', linewidth=2, markersize=14,
         markeredgecolor='white', markeredgewidth=2)

# DG-Mamba line
plt.plot(x, dg_mamba, 'o-', color='purple', label='DG-Mamba (ours)', linestyle='-', linewidth=2, markersize=12,
         markeredgecolor='white', markeredgewidth=2)

plt.xticks(x, labels=['~ 13000', '15000', '17000', '19000', '21000'], fontsize=14)  # Using labels as per the image
plt.xlabel('Node Scale', fontsize=16)
plt.ylabel('GPU Usage (GB)', fontsize=16)
plt.yticks([20, 30, 40], fontsize=14)
plt.legend(loc='upper center', fontsize=13, bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=True)
plt.grid(True)
plt.tight_layout()

plt.savefig('effi_node_collab_gpu.png')