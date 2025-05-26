import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Data
metrics = ['A$_0$', 'A$_1$', 'A$_2$']
Nz_values = [20, 30, 40, 50]
data = {
    20: [48, 70, 80],
    30: [80, 81, 95],
    40: [69, 71, 79],
    50: [43, 65, 80]
}
errors = {
    20: [10, 12, 12],
    30: [10, 10, 8],
    40: [10, 8, 6],
    50: [10, 12, 10]
}

# Bar plot
x = np.arange(len(metrics))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Manually plot each bar
ax.bar(x - width * 1.5-0.04, data[20], width, label='$N_z = 20$', yerr=errors[20], capsize=5,color='#5E9AD1')
ax.bar(x - width * 0.5-0.02, data[30], width, label='$N_z = 30$', yerr=errors[30], capsize=5,color='#EB7F3F')
ax.bar(x + width * 0.5+0.02, data[40], width, label='$N_z = 40$', yerr=errors[40], capsize=5,color='#A5A5A5')
ax.bar(x + width * 1.5+0.04, data[50], width, label='$N_z = 50$', yerr=errors[50], capsize=5,color='#FDC13A')
# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xlabel('Evaluation Metric', fontsize=24,labelpad=18)
ax.set_ylabel('Rate [%]', fontsize=18)
ax.set_ylim(0,105)
ax.set_yticks([0, 20, 40, 60, 80, 100])
ax.set_yticklabels([0, 20, 40, 60, 80, 100],fontsize=20)
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=20, style='italic')
ax.tick_params(axis='x', length=0)  # y轴的刻度方向（控制左边）
ax.legend(loc='lower center',fontsize=22,ncol=4,bbox_to_anchor=(0.5,-0.4),edgecolor='none',handlelength=0.5, handleheight=0.5)

# Show plot
plt.tight_layout()
plt.savefig('musashi-z.png')