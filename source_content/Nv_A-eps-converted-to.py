import matplotlib.pyplot as plt
import numpy as np

# Data
Nv = [20, 30, 40, 50]
mpdqn_data = [0.056, 0.0585, 0.063, 0.083]
ga_data = [0.078, 0.084, 0.090, 0.098]
random_data = [0.081, 0.083, 0.092, 0.104]

bar_width = 0.2
x = np.arange(len(Nv))

# Plotting
plt.bar(x - bar_width-0.05, mpdqn_data, width=bar_width, label='MPDQN-based policy', color='#0072BD',edgecolor='black',zorder=3)
plt.bar(x, ga_data, width=bar_width, label='GA-based policy', color='#D95319',edgecolor='black',zorder=2)
plt.bar(x + bar_width+0.05, random_data, width=bar_width, label='Random policy', color='#EDB120',edgecolor='black',zorder=1)

# Customizing the plot
plt.xlabel('$N_v$')
plt.ylabel('AoI in Receiver / s')
plt.xticks(x, Nv)
plt.ylim(0,0.12)
plt.yticks([0,0.02,0.04,0.06,0.08,0.1,0.12],['0','0.02','0.04','0.06','0.08','0.1','0.12'])
plt.grid(True, linestyle='-',alpha=0.3,zorder=0)
plt.legend(loc='upper center',bbox_to_anchor=(0.65, 1),handlelength=3, handleheight=1)
plt.tight_layout()
plt.savefig('Nv_A-eps-converted-to.png')