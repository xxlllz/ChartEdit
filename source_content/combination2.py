import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator

# Data for each slit
latitudes_slit7 = np.array([67, 67.8, 71, 71.5,75.1,75.121,76.1,77.5,80.2,80.35,81])
speeds_slit7 = np.array([0.51, 0.45, 0.395, 0.398,0.335,0.350,0.28,0.32,0.235,0.195,0.2 ])

latitudes_slit5 = np.array([68,70,73,76.5,77.2,80.3])
speeds_slit5 = np.array([0.43,0.36,0.35,0.33,0.332,0.20,])

latitudes_slit3 = np.array([80])
speeds_slit3 = np.array([0.23])

latitudes_slit5N = np.array([61.5,65,69,])
speeds_slit5N = np.array([0.565,0.485,0.43])

# Recreate plot
plt.figure(figsize=(6, 6))
# Linear fit/ line annotation
x_new = np.array([60, 90.1])
y_new = np.array([0.63, -0.002])

plt.plot(x_new, y_new, 'r--', label='v/1.86 =-(lat-90)/90',zorder=4)  # 'b-' means a solid blue line
# 第一个图例（slit 7, slit 5, slit 3）
plt.plot(90, 0.00221, 'o', color='white', markeredgecolor='black', markersize=6, markeredgewidth=1.5,label='',zorder=0)


# Plotting the slits data
plt.scatter(latitudes_slit7, speeds_slit7, color='red', label='slit 7',zorder=4)
plt.scatter(latitudes_slit5, speeds_slit5, color='blue', label='slit 5',zorder=4)
plt.scatter(latitudes_slit3, speeds_slit3, color='lightgreen', label='slit 3',zorder=4)
plt.scatter(latitudes_slit5N, speeds_slit5N, color='black', label='slit 5N',zorder=4)
# 第二个图例（slit 5N）

# Annotations and formatting
plt.title('speed vs. latitude', fontsize=16, fontweight='bold')
plt.xlabel('latitude (deg)', fontsize=14, fontweight='bold')
plt.ylabel('speed (km/s)', fontsize=14, fontweight='bold')
plt.xticks(fontsize=14, fontweight='bold')
plt.yticks(fontsize=14, fontweight='bold')
plt.xlim(59.5, 90.5)
plt.ylim(-0.02, 1.02)
plt.grid(False)

# 设置坐标轴加粗
ax = plt.gca()
ax.xaxis.set_ticks_position('both')
ax.yaxis.set_ticks_position('both')

# 在 x 轴添加 4 个次要刻度
ax.xaxis.set_minor_locator(AutoMinorLocator(4))

# 在 y 轴添加 3 个次要刻度
ax.yaxis.set_minor_locator(AutoMinorLocator(3))

for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(2)  # 设置坐标轴宽度为 2，可根据需要调整

# 设置 ticks 四个轴都有且朝向内部
ax.tick_params(direction='in', which='both',width=2)  # 'both' 表示主次刻度可根据需要调整为'major' 或'minor'

# 第一个图例（slit 7, slit 5, slit 3）
handles1, labels1 = ax.get_legend_handles_labels()
print(handles1, labels1 )
legend1 = plt.legend(handles1[0:1], labels1[0:1], loc='upper right', fontsize=14, bbox_to_anchor=(0.9, 0.95),edgecolor="none",prop={'weight': 'bold','size':13})
ax.text(72.5, 0.83, "rms dev = 0.0257",fontsize=13,fontweight='bold')

ax.add_artist(legend1)

legend2 = plt.legend(handles1[1:], labels1[1:], loc='upper right', fontsize=14, bbox_to_anchor=(1, 0.8),ncol=4,edgecolor="none",columnspacing=0.2,prop={'weight': 'bold','size':13})

# plt.legend(loc='upper right',ncol=4 ,fontsize=10)
plt.savefig("combination2.png")