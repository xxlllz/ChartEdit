import matplotlib.pyplot as plt
import numpy as np

# Data for HV-E dataset (a)
x_hve = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
lightgc2n_hve = np.array([25, 35, 49, 70, 90])
lightwos_hve = np.array([20, 30, 47, 67, 88])
lightwoc_hve = np.array([12, 20, 28, 40, 50])
lightwoa_hve = np.array([10, 14, 26, 30, 38])

# Data for HV-V dataset (b)
x_hvv = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
lightgc2n_hvv = np.array([20, 35, 55, 80, 96])
lightwos_hvv = np.array([18, 26, 54, 70, 80])
lightwoc_hvv = np.array([13, 23, 30, 40, 50])
lightwoa_hvv = np.array([12, 15, 27, 30, 45])

# Model volume data
model_volume_hve = [8.75, 8.32, 7.55, 6.97]
model_volume_hvv = [11.20, 10.35, 9.22, 8.21]
methods = ['LightGC$^2$N', 'Light$_{w/o}$S', 'Light$_{w/o}$C', 'Light$_{w/o}$A']

# Plot
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Line plot for HV-E dataset (a)
a1 = axs[0, 0]
a1.plot(x_hve, lightgc2n_hve, linestyle='--', marker='^', color='mediumseagreen', label='LightGC$^2$N')
a1.plot(x_hve, lightwos_hve, linestyle='--', marker='s', color='royalblue', label='Light$_{w/o}$S')
a1.plot(x_hve, lightwoc_hve, linestyle='--', marker='o', color='gold', label='Light$_{w/o}$C')
a1.plot(x_hve, lightwoa_hve, linestyle='--', marker='*', color='indianred', label='Light$_{w/o}$A')
a1.set_xlabel('Ratio of training data (%)\n on HV-E dataset (a)', fontsize=15, fontweight='bold')
a1.set_ylabel('Time Consumption (s)', fontsize=15, fontweight='bold')
a1.set_xticks(x_hve)
a1.tick_params(axis='both', labelsize=14)  # Adjust tick size
a1.set_ylim(0, 110)
a1.legend(loc='upper left', fontsize=12)

# Line plot for HV-V dataset (b)
a2 = axs[0, 1]
a2.plot(x_hvv, lightgc2n_hvv, linestyle='--', marker='^', color='mediumseagreen', label='LightGC$^2$N')
a2.plot(x_hvv, lightwos_hvv, linestyle='--', marker='s', color='royalblue', label='Light$_{w/o}$S')
a2.plot(x_hvv, lightwoc_hvv, linestyle='--', marker='o', color='gold', label='Light$_{w/o}$C')
a2.plot(x_hvv, lightwoa_hvv, linestyle='--', marker='*', color='indianred', label='Light$_{w/o}$A')
a2.set_xlabel('Ratio of training data (%)\n on HV-V dataset (b)', fontsize=15, fontweight='bold')
a2.set_ylabel('Time Consumption (s)', fontsize=15, fontweight='bold')
a2.set_xticks(x_hvv)
a2.tick_params(axis='both', labelsize=14)  # Adjust tick size
a2.set_ylim(0, 110)
a2.legend(loc='upper left', fontsize=12)

# Bar plot for HV-E dataset (c)
bar_width = 0.6  # Adjusted bar width
b1 = axs[1, 0]
bar1 = b1.bar(methods, model_volume_hve, width=bar_width, color=['mediumseagreen', 'royalblue', 'gold', 'indianred'])
b1.set_ylabel('Model volume (MB)', fontsize=15, fontweight='bold')
b1.set_xlabel('Compared variant methods\n on HV-E dataset (c)', fontsize=15, fontweight='bold')
b1.set_ylim([0, 12])
b1.tick_params(axis='both', labelsize=14)  # Adjust tick size
for bar in bar1:
    yval = bar.get_height()
    b1.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

# Bar plot for HV-V dataset (d)
b2 = axs[1, 1]
bar2 = b2.bar(methods, model_volume_hvv, width=bar_width, color=['mediumseagreen', 'royalblue', 'gold', 'indianred'])
b2.set_ylabel('Model volume (MB)', fontsize=15, fontweight='bold')
b2.set_xlabel('Compared variant methods\n on HV-V dataset (d)', fontsize=15, fontweight='bold')
b2.set_ylim([0, 14])
b2.tick_params(axis='both', labelsize=14)  # Adjust tick size
for bar in bar2:
    yval = bar.get_height()
    b2.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig('apfig5_efficiency.png', dpi=300)