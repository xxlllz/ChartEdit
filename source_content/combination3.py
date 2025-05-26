import matplotlib.pyplot as plt
import numpy as np

# Data for the visualization
x=[1,4,7,10,12.5,16,19,22,25,27.5,31,34,37,40]
y=[44.3,41.56,39.3,36.8,35,32.5,30.5,29,27.5,26.5,25,24,23,22]
def polynomial(x):
    return 0.00963 * x**2 - 0.9507 * x + 45.1

x_fit = np.linspace(0, 39, 100)
y_fit = polynomial(x_fit) 

plt.figure(figsize=(8, 4))  # 可根据需要修改宽度和高度，这里设置为宽 8 高 6
# Plot the 'real value' line
plt.plot(x_fit, y_fit, label='real value', color='black', linewidth=5)

# Plot the 'predicted value' markers
plt.plot(x, y, label='predicted value', color='none', marker='^', markersize=13,markeredgecolor='orange', markeredgewidth=4,zorder=10,clip_on=False)

# Adding labels for axes
plt.xlabel('Time slot', fontsize=16)
plt.ylabel('Angle(deg)', fontsize=16)

# Customizing the legend
plt.legend(fontsize=16, loc='best', borderpad=1.2, handlelength=3)

# Setting y-axis and x-axis limits
plt.ylim(20, 45)
plt.xlim(0, 40)
plt.xticks(fontsize=18)

plt.yticks(fontsize=18)
# Improving layout
# Customize tick appearance
plt.tick_params(axis='both', which='both', direction='in', length=6, width=0.5,)
plt.tick_params(axis='x',  pad=15,)
ax = plt.gca()

# 设置 x 轴和 y 轴的刻度位置为 'both'
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')

# Display the plot
plt.tight_layout()
plt.savefig('combination3.png')