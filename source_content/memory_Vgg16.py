import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator
plt.rcParams['font.family'] = 'serif'

# Data
methods = ['Vanilla', 'FGC', 'FGA', 'FLP', 'SFT', 'SmartSplit']
values = [1400, 1100, 1120, 350, 200, 20]
percentages = ['', '0.80', '0.82', '0.25', '0.15', '0.01']
colors = ['#679da0', '#d6e3a1', '#f7a916', '#40e0d0', '#f0e2aa', '#fee08b']

# Create bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bar_width = 0.6
bars = ax.bar(methods, values, color=colors, edgecolor='black', width=bar_width,linewidth=3,zorder=3)

# Add labels above bars
for bar, percentage in zip(bars, percentages):
    if percentage:
        height = bar.get_height() + 20
        ax.text(bar.get_x() + bar.get_width() / 2.0, height, percentage, ha='center', va='bottom', fontsize=16, fontname='serif',fontweight='bold')

# Add title and labels

ax.set_title('Vgg16', fontsize=28, family='serif',pad=10)
ax.set_ylabel('Memory Usage (MB)', fontsize=24, family='serif')
ax.set_xticklabels(methods, fontsize=18, family='serif')
plt.ylim(0,1470)
plt.yticks([0,200,400,600,800,1000,1200,1400],fontsize=18, family='serif')
# ax.yaxis.set_major_locator(plt.MaxNLocator(integer=True))
ax.tick_params(axis='y', which='major',direction='in', width=2)  # x 和 y 轴刻度
ax.tick_params(axis='x', length=0)
ax.grid(axis='y',color='gray', linestyle='--', linewidth=1,zorder=0,alpha=0.5)
# ax.xaxis.set_major_locator(MultipleLocator(5))  # x 轴主刻度每隔 0.5

# Show plot
plt.savefig('memory_Vgg16.png')