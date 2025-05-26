import matplotlib.pyplot as plt
import numpy as np

# Prompt length data (x-axis)
prompt_lengths = np.array([1,2,3,4,5,6,7,8,9])
# Improved ACC data (primary y-axis)
improved_acc = np.array([6.4, 6.6, 9.9, 9.8, 7.7, 7.9, 7.2, 7.4, 6.2])
# Parameter utilization rate data (secondary y-axis)
param_utilization = np.array([0.84, 0.65, 0.61, 0.48, 0.32, 0.27, 0.23, 0.19, 0.14])

fig, ax1 = plt.subplots(figsize=(8, 6))

# Bar plot for Improved ACC
ax1.bar(prompt_lengths, improved_acc, color='#a1c2e6', edgecolor='#3b72b6',lw=4.5, width=0.4, label='Improved ACC', zorder=3)

ax1.set_xlabel('Prompt Length $\\ell_p$', fontsize=20)
ax1.set_ylabel('Improved accuracy over baseline', color='black', fontsize=18)
ax1.set_xlim(0.5,9.5)
ax1.set_xticks([1,2,3,4,5,6,7,8,9])
ax1.set_xticklabels([8,10,16,20,24,30,32,40,48],fontsize=16)
ax1.set_ylim(0, 12)
ax1.tick_params(axis='y', labelcolor='black', zorder=1,labelsize=16,pad=15,length=0)
ax1.tick_params(axis='x', length=0,pad=15)
ax1.grid(axis = 'y',linestyle='-', color='silver',alpha=0.5, lw=3,zorder=0)
for spine in ax1.spines.values():
    spine.set_linewidth(2)  # 设置框线宽度为 2

# Line plot for Parameter utilization rate
ax2 = ax1.twinx()
ax2.plot(prompt_lengths, param_utilization, color='#f1b383', marker='o', linestyle='-', markerfacecolor='#c25d15',markeredgecolor='#f1b383',markeredgewidth=3,label='Parameter utilization rate', linewidth=7, markersize=14, zorder=2)
ax2.set_ylabel('Parameter utilization rate', color='black', fontsize=16)
ax2.set_ylim(0, 0.9)
ax2.set_yticks([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
ax2.set_yticklabels([0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])
ax2.tick_params(axis='y', labelcolor='black', zorder=2,length=0,labelsize=16,pad=15)

# Legend
legend1 = fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1), ncol=2,edgecolor='none',facecolor='none',fontsize=16,handlelength=3)

# Adjust subplot margins
plt.subplots_adjust(top=0.85,bottom=0.15)
plt.savefig('multi2.png')