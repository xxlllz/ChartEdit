import matplotlib.pyplot as plt
import numpy as np

mask_ratio = [0.001, 0.02, 0.04, 0.05, 0.06, 0.08, 0.1, 0.15]
asr_values = [25, 5, 5, 5, 5, 5, 5, 75]
der_values = [100, 100, 100, 100, 100, 100, 100, 50]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Mask Ratio')
ax1.set_ylabel('ASR (%)', color=color)
ax1.plot(mask_ratio, asr_values, color=color, marker='s', linestyle='-',
         markerfacecolor='white', label='ASR')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  
color = 'tab:blue'
ax2.set_ylabel('DER (%)', color=color)  
ax2.plot(mask_ratio, der_values, color=color, marker='^', linestyle='-',
         markerfacecolor='white', label='DER')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.1), ncol=2, markerscale=1)
plt.grid(True)
plt.savefig('change_mask_ratio.png')