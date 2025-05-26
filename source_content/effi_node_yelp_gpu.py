import matplotlib.pyplot as plt
import numpy as np

# Sample data
node_scale = np.array([8000, 9000, 10000, 11000, 12000])
rdgsl_gpu_usage = np.array([10, 12, 15, 19, 24])
dgib_gpu_usage = np.array([9, 11, 14, 17, 21])
dg_mamba_gpu_usage = np.array([8, 10, 12, 14, 16])

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(node_scale, rdgsl_gpu_usage, label='RDGSL', linestyle='-', marker='s', color='cyan', linewidth=2)
plt.plot(node_scale, dgib_gpu_usage, label='DGIB', linestyle='-', marker='^', color='pink', linewidth=2)
plt.plot(node_scale, dg_mamba_gpu_usage, label='DG-Mamba (ours)', linestyle='-', marker='o', color='purple', linewidth=2)

# Labels and Title
plt.xlabel('Node Scale', fontsize=15)
plt.ylabel('GPU Usage (GB)', fontsize=15)
plt.ylim(0, 25)
plt.xlim(8000, 12000)
plt.xticks(node_scale, labels=['~ 8000', '9000', '10000', '11000', '12000'], fontsize=15)
plt.tick_params(axis='y', labelsize=15)
# Customizing the legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=3, fontsize=12, frameon=False)
plt.tight_layout()
# Show the plot
plt.savefig('effi_node_yelp_gpu.png')