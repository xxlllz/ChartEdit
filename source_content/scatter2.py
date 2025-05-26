import matplotlib.pyplot as plt
import numpy as np

# Defining the values
x = np.arange(17)
methods = ['','','','','','','ToMP',"TransT", "OSTrack", "SBT", "SwinTrack", "ROMTrack",  "Mixformer", "SeqTrack","ARTrack", "SUTrack"]

y_values = [0.25, 0.37, 0.420, 0.440, 0.456,0.47, 0.511,0.512,0.518,0.522,0.524,0.540,0.549,0.568,0.570,0.633]

# Defining the marker styles and colors
markers = ['v', '*', 'x', 'o', 'h', '^', 's', '>', '*', '<', '+', 'd', 'v', 'o', 'x', 'o']
colors = [ 'orange', 'royalblue', 'lightblue', '#ef999b', 'green', '#cad01e', 'green', 'orange', '#4668b2', '#7cc7f1', '#ee9a9c', 'grey', '#cad01e', 'green', 'orange', '#4668b2']

# Plot
plt.figure(figsize=(10, 4))

# 17 individual scatter commands
plt.scatter(0, y_values[0], color='none', marker=markers[0], edgecolor=colors[0],linewidths=3,s=200,clip_on=False)
plt.scatter(1, y_values[1], color='none', marker=markers[1], edgecolor=colors[1],linewidths=3,s=200,clip_on=False)
plt.scatter(2, y_values[2], color='lightblue', marker=markers[2], edgecolor=colors[2], linewidths=3, s=200, clip_on=False)
plt.scatter(3, y_values[3], color='none', marker=markers[3], edgecolor=colors[3], linewidths=5, s=200, clip_on=False)
plt.scatter(4, y_values[4], color='none', marker=markers[4], edgecolor=colors[4], linewidths=3, s=200, clip_on=False)
plt.scatter(5, y_values[5], color='none', marker=markers[5], edgecolor=colors[5], linewidths=3, s=200, clip_on=False)
plt.scatter(6, y_values[6], color='none', marker=markers[6], edgecolor=colors[6], linewidths=3, s=200, clip_on=False,label=f"{methods[6]} [{y_values[6]:.3f}]")
plt.scatter(7, y_values[7], color='none', marker=markers[7], edgecolor=colors[7], linewidths=3, s=200, clip_on=False, label=f"{methods[7]} [{y_values[7]:.3f}]")
plt.scatter(8, y_values[8], color='none', marker=markers[8], edgecolor=colors[8], linewidths=3, s=200, clip_on=False, label=f"{methods[8]} [{y_values[8]:.3f}]")
plt.scatter(9, y_values[9], color='none', marker=markers[9], edgecolor=colors[9], linewidths=3, s=200, clip_on=False, label=f"{methods[9]} [{y_values[9]:.3f}]")
plt.scatter(10, y_values[10], color='#ee9a9c', marker=markers[10], edgecolor=colors[10], linewidths=3, s=200, clip_on=False, label=f"{methods[10]} [{y_values[10]:.3f}]")
plt.scatter(11, y_values[11], color='none', marker=markers[11], edgecolor=colors[11], linewidths=3, s=200, clip_on=False, label=f"{methods[11]} [{y_values[11]:.3f}]")
plt.scatter(12, y_values[12], color='none', marker=markers[12], edgecolor=colors[12], linewidths=3, s=200, clip_on=False, label=f"{methods[12]} [{y_values[12]:.3f}]")
plt.scatter(13, y_values[13], color='green', marker=markers[13], edgecolor=colors[13], linewidths=3, s=200, clip_on=False, label=f"{methods[13]} [{y_values[13]:.3f}]")
plt.scatter(14, y_values[14], color='orange', marker=markers[14], edgecolor=colors[14], linewidths=3, s=200, clip_on=False, label=f"{methods[14]} [{y_values[14]:.3f}]")
plt.scatter(15, y_values[15], color='#4668b2', marker=markers[15], edgecolor=colors[15], linewidths=3, s=200, clip_on=False, label=f"{methods[15]} [{y_values[15]:.3f}]")



for i in range(16): 
    plt.vlines(i, 0, y_values[i], color='gray',alpha=0.3, linestyle='--', linewidth=1)  # Add dashed vertical lines to the x-axis

plt.ylim(0.25,0.65)
plt.yticks([0.25, 0.35, 0.45, 0.55], [0.25, 0.35, 0.45, 0.55], fontsize=18)

plt.tick_params(axis='both', which='major', length=7, width=3, direction='in', top=True, right=True)
# 设置每个脊柱（边框线）的宽度
for spine in plt.gca().spines.values():
    spine.set_linewidth(3)  # 将1.5替换为您想要的线条宽度

# plt.minorticks_on()

plt.xlim(0, 15)
# 设置主刻度和次刻度
plt.xticks(range(0, 15, 3),[])  # 主tick从0到15，间隔为1

plt.tick_params(axis='y', which='minor', length=0)
plt.tick_params(axis='x', which='minor', length=1)
plt.title('VOT2022 Bounding-box Evaluation', fontsize=18, weight='bold')
plt.grid(True, linestyle='-', alpha=0.3,lw=3)
legend = plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), frameon=True,fontsize=16,edgecolor='black')
legend.get_frame().set_linewidth(3)  # 设置边框线宽为3
plt.subplots_adjust(right=0.75)
plt.tight_layout()
plt.savefig('scatter2.png')
