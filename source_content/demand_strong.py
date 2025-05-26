import matplotlib.pyplot as plt
import numpy as np

# Data
x = np.arange(1, 10)
clean = [11, 11.5, 11.5,  11.5,  11.5,  11.5,  11.5,  11.5,  11.5]
adv = [2.5, 4, 8.5, 15, 19, 20, 16, 8, 4]

# Plot
bar_width = 0.3
fig, ax = plt.subplots(figsize=(9, 6))
ax.bar(x - bar_width/2, clean, bar_width, label='Clean', color='indigo', edgecolor='black')
ax.bar(x + bar_width/2, adv, bar_width, label='Adv', color='gold', edgecolor='black')

# Labels and Legend
ax.set_xlabel('Node Demand', fontsize=25)
ax.set_ylabel('Percentage Frequency (%)', fontsize=25)
ax.set_xticks(x)
ax.set_yticks(np.arange(0, 21, 2.5))
ax.legend(fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.tight_layout()
plt.savefig('demand_strong.png')