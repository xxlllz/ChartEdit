import matplotlib.pyplot as plt
import numpy as np

# Sample data
x1 = np.array([35, 105, 175, 245, 325])
x2 = np.array([35, 105, 175, 245])
y1_gsm8k = np.array([50.5, 65.5, 69, 73, 74])
y2_gsm8k = np.array([57.5, 63.5, 65, 66])
y1_svamp = np.array([67.5, 73, 77, 78.5, 81.3])
y2_svamp = np.array([58, 62.5, 64, 62])
y1_asdiv = np.array([71, 77, 78.5, 79, 81])
y2_asdiv = np.array([69, 71.5, 71.3, 72.5])
y1_math = np.array([6, 6.8, 7.4, 8.2, 8.8])
y2_math = np.array([5, 5.5, 5.35, 5.8])

# Plot configuration
fig, axs = plt.subplots(1, 4, figsize=(11, 4))
subjects = ['GSM8k', 'SVAMP', 'ASDiv', 'MATH']
x_1 = [x1, x1, x1, x1]
x_2 = [x2, x2, x2, x2]
y_data1 = [y1_gsm8k, y1_svamp, y1_asdiv, y1_math]
y_data2 = [y2_gsm8k, y2_svamp, y2_asdiv, y2_math]

for i, ax in enumerate(axs):
    ax.plot(x2, y_data2[i], 'o-', label='MMQA', color='lightblue', markersize=6, linewidth=3)
    ax.plot(x1, y_data1[i], 'D-', label='Ours', color='salmon', markersize=6, linewidth=3)
    ax.set_title(subjects[i], fontsize=18)
    ax.set_xlim(0, 350)
    ax.set_xticks(np.arange(0, 400, 70))
    if i == 0 :
        ax.set_ylim(50, 76)
        ax.set_yticks(np.arange(50, 76, 5), )
    elif i == 1:
        ax.set_ylim(55, 82)
        ax.set_yticks(np.arange(55, 82, 5))
    elif i == 2:
        ax.set_ylim(67, 82)
        ax.set_yticks(np.arange(70, 81, 5))
    elif i == 3:
        ax.set_ylim(3, 9.5)
        ax.set_yticks(np.arange(3, 10, 1))
    ax.tick_params(axis='x',labelsize=12)  # Length of major and minor ticks
    ax.tick_params(axis='y',labelsize=12)  # Length of major and minor ticks
    ax.grid(False)

# Main axis
fig.text(0.5, 0, 'Size of Training Dataset (Thousands)', ha='center', fontsize=14)
fig.text(0, 0.5, 'Accuracy (%)', va='center', rotation='vertical', fontsize=14)

# Place the legend
handles, labels = axs[0].get_legend_handles_labels()
fig.legend(handles, labels, loc='lower center', bbox_to_anchor=(0.9, 0.1), ncol=1, fontsize=16)

plt.tight_layout()
plt.savefig('scability-old.png')