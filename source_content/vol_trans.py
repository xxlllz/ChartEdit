import matplotlib.pyplot as plt
import numpy as np

# Data
categories_a = ['100%', '10%']
values_a = np.array([[22.53, 20.46], [19.24, 15.24]])

categories_b = ['100%', '10%']
values_b = np.array([[21.45, 18.02], [18.45, 14.35]])

categories_c = ['SUNRGBD->ScanNet', 'ScanNe->SUNRGBD']
values_c = np.array([[19.40, 12.30], [20.39, 12.57]])

x = np.arange(len(categories_a))
width = 0.35

# Subplot (a)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

ax1.bar(x - width/2, values_a[:, 0], width, label='ImOV3D(Ours)', color='purple')
ax1.bar(x + width/2, values_a[:, 1], width, label='OV-3DET', color='yellow')
ax1.set_ylabel('mAP@0.25', fontsize=15)
ax1.set_title('SUNRGBD', fontsize=15)
ax1.set_xticks(x)
ax1.set_xticklabels(categories_a, fontsize=14)
ax1.set_xlabel('Data Volume', fontsize=15)
ax1.legend(fontsize=8)
ax1.set_ylim(0, 25)
ax1.tick_params(axis='y', labelsize=14)

for i, v in enumerate(values_a):
    ax1.text(i - width/2, v[0] + 0.5, str(v[0]), ha='center', va='bottom', fontsize=12)
    ax1.text(i + width/2, v[1] + 0.5, str(v[1]), ha='center', va='bottom', fontsize=12)

ax1.text(0.5, -0.2, '(a)', transform=ax1.transAxes, fontsize=14, va='top', ha='center')

# Subplot (b)
ax2.bar(x - width/2, values_b[:, 0], width, label='ImOV3D(Ours)', color='orange')
ax2.bar(x + width/2, values_b[:, 1], width, label='OV-3DET', color='blue')
ax2.set_title('ScanNet', fontsize=15)
ax2.set_xticks(x)
ax2.set_xticklabels(categories_b, fontsize=14)
ax2.set_xlabel('Data Volume', fontsize=15)
ax2.set_ylabel('mAP@0.25', fontsize=15)
ax2.legend(fontsize=8)
ax2.set_ylim(0, 25)
ax2.tick_params(axis='y', labelsize=14)

for i, v in enumerate(values_b):
    ax2.text(i - width/2, v[0] + 0.5, str(v[0]), ha='center', va='bottom', fontsize=12)
    ax2.text(i + width/2, v[1] + 0.5, str(v[1]), ha='center', va='bottom', fontsize=12)

ax2.text(0.5, -0.2, '(b)', transform=ax2.transAxes, fontsize=14, va='top', ha='center')

# Subplot (c)
ax3.bar(x - width/2, values_c[:, 0], width, label='ImOV3D(Ours)', color='green')
ax3.bar(x + width/2, values_c[:, 1], width, label='OV-3DET', color='navy')
ax3.set_title('ScanNet               SUNRGBD', fontsize=15)
ax3.set_xticks(x)
ax3.set_xticklabels(categories_c, fontsize=14)
ax3.set_xlabel('Transfer Direction', fontsize=15)
ax3.set_ylabel('mAP@0.25', fontsize=15)
ax3.legend(fontsize=8)
ax3.set_ylim(0, 25)
ax3.tick_params(axis='y', labelsize=14)

for i, v in enumerate(values_c):
    ax3.text(i - width/2, v[0] + 0.5, str(v[0]), ha='center', va='bottom', fontsize=12)
    ax3.text(i + width/2, v[1] + 0.5, str(v[1]), ha='center', va='bottom', fontsize=12)

ax3.text(0.5, -0.2, '(c)', transform=ax3.transAxes, fontsize=14, va='top', ha='center')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('vol_trans.png')
