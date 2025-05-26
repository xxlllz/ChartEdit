import matplotlib.pyplot as plt
import numpy as np

# Sample data
missing_ratio = np.linspace(0, 1, 11)
wo_frf = [83, 82, 81, 79, 74, 72, 66, 63, 55, 50, 30]
wo_hmi = [84, 82, 81, 80, 76, 74, 72, 65, 60, 50, 30]
wo_hal = [81, 80, 79, 76, 73, 71, 71, 67, 63, 53, 32]
hrlf = [85, 83, 83, 82, 79, 77, 74, 69, 62, 53, 31]

# Plotting
plt.figure(figsize=(8, 5))
plt.plot(missing_ratio, wo_frf, color='green', marker='o', linestyle='-', label='w/o FRF', linewidth=1.5, markersize=8)
plt.plot(missing_ratio, wo_hmi, color='blue', marker='^', linestyle='-', label='w/o HMI', linewidth=1.5, markersize=8)
plt.plot(missing_ratio, wo_hal, color='orange', marker='s', linestyle='-', label='w/o HAL', linewidth=1.5, markersize=8)
plt.plot(missing_ratio, hrlf, color='red', marker='d', linestyle='-', label='HRLF', linewidth=2, markersize=8)

# Labels and limits
plt.xlabel('Missing Ratio', fontsize=14)
plt.ylabel('F1 Score', fontsize=14)
plt.ylim(20, 90)

# Legend
plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, fontsize=12, frameon=False)

# # Grid
# plt.grid(True, linestyle='--', linewidth=0.5)

# Tight layout for saving
plt.tight_layout()

# Save the figure
plt.savefig('abla_intra_mosi.png', dpi=300)
