import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['O0', 'O1', 'O2', 'O3']
gcc_means = [58, 55, 62, 65]
clang_means = [54, 47, 56, 59]
gcc_errors = [3, 4, 2, 2]
clang_errors = [3, 4, 3, 3]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(7, 4))
rects1 = ax.bar(x - width/2, gcc_means, width, label='gcc', yerr=gcc_errors, color='gray', capsize=4, error_kw={'ecolor': 'brown'})
rects2 = ax.bar(x + width/2, clang_means, width, label='clang', yerr=clang_errors, color='silver', capsize=4, error_kw={'ecolor': 'brown'})

# Labels, title, and custom x-axis tick labels
ax.set_ylabel('Ratio', fontsize=20)  # Increase y-axis label size
ax.set_yticks(np.arange(40, 90, 10))
ax.set_yticklabels([f'{i}%' for i in range(40, 90, 10)], fontsize=15)  # Adjust y-tick font size
ax.set_ylim(40, 80)
ax.set_xlabel('Optimization level', fontsize=20)  # Increase x-axis label size
ax.set_xticks(x)
ax.set_xticklabels(labels, fontsize=15)  # Adjust x-tick font size
ax.legend(ncol=2, fontsize=16)  # Adjust legend to two columns with larger font

# Enable grid
ax.yaxis.grid(True, linestyle='--', color='lightcoral', linewidth=0.5)

fig.tight_layout()

plt.savefig('fig_x32_f.png')