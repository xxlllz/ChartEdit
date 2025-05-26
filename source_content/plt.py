import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Data
categories = ['0.2', '0.6', '1.8', '3.0']
bevformer_values = [24.89, 24.83, 24.94, 24.58]
cvt_occ_values = [25.15, 25.80, 26.46, 27.37]

x = np.arange(len(categories))
width = 0.35

fig, ax = plt.subplots()

# Creating bar plots
ax.bar(x - width/2, bevformer_values, width, label='BEVFormer', color='tab:blue')
ax.bar(x + width/2, cvt_occ_values, width, label='CVT-Occ', color='tab:orange')

# Adding some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('mIoU', fontsize = 20, rotation=0,labelpad=40)
ax.set_xlabel('Time Span (s)', fontsize = 18)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=14)
ax.set_ylim(24.1, 28.2)  # Set limits to match the source image
ax.set_yticks([25,26,27,28])
ax.set_yticklabels([25,26,27,28], fontsize=14)
ax.legend(loc='upper right')

# Adding data labels
for i, v in enumerate(bevformer_values):
    ax.text(i - width/2, v + 0.1, f'{v:.2f}', ha='center',fontsize = 12)
for i, v in enumerate(cvt_occ_values):
    ax.text(i + width/2, v + 0.1, f'{v:.2f}', ha='center',fontsize = 12)

plt.tight_layout()
plt.savefig('plt.png')