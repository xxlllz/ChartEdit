import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['Rx$_{(1-1)}$', 'Rx$_{(14-7)}$', 'Rx$_{(8-8)}$', 'Rx$_{(7-7)}$', 'Rx$_{(1-19)}$']
same_sample_rate = [75, 77, 70, 75, 75]
different_sample_rate = [74.5, 75, 65, 78, 68]

x = np.arange(len(categories))
width = 0.25

fig, ax = plt.subplots()

# # Bar plot
# bars1 = ax.bar(x - width/2, same_sample_rate, width, label='same sample rate', color='royalblue')
# bars2 = ax.bar(x + width/2, different_sample_rate, width, label='different sample rate', color='gray')

# Labels and Titles
ax.set_ylabel('Recognition Accuracy(%)',fontsize=14)
ax.set_xlabel('Test Receiver',fontsize=14)
ax.set_ylim(0,80)
ax.set_xticks(x)
ax.set_xticklabels(categories,fontsize=12)
# Grid lines in the background
# Grid lines behind the bars
ax.grid(True, alpha=0.7, zorder=0)

# Bar plot with black edge color and spacing between bars
bars1 = ax.bar(x - width/2 - 0.03, same_sample_rate, width, label='same sample rate', color='steelblue', edgecolor='black', zorder=3)
bars2 = ax.bar(x + width/2 + 0.03, different_sample_rate, width, label='different sample rate', color='gray', edgecolor='black', zorder=3)

ax.legend(loc='lower right', bbox_to_anchor=(1,0.2), fontsize=10,edgecolor='black')

fig.tight_layout()
plt.savefig('sample-eps-converted-to.png')