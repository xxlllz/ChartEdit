import matplotlib.pyplot as plt
import numpy as np

# Data setup
labels = ['Common', 'Controversial']
bm25 = [0.482, 0.451]
bert = [0.578, 0.438]
sailer = [0.64, 0.52]
keller = [0.678, 0.645]

# Set positions for bars
x = np.arange(len(labels))  # label positions

# Create the plot
fig, axes = plt.subplots(figsize=(6, 5))

# Bar widths and positioning
bar_width = 0.2
index = np.arange(len(labels))

# Create bars with pattern and color for each dataset
axes.bar(index, bm25, bar_width, color='yellow', label='BM25', hatch='//')
axes.bar(index + bar_width, bert, bar_width, color='red', label='BERT', hatch='..')
axes.bar(index + 2 * bar_width, sailer, bar_width, color='brown', label='SAILER', hatch='-')
axes.bar(index + 3 * bar_width, keller, bar_width, color='purple', label='KELLER', hatch='\\')

# Add the values on top of bars
for i in range(len(labels)):
    axes.text(index[i], bm25[i] + 0.005, f'{bm25[i]:.3f}', ha='center', va='bottom', fontsize=12)
    axes.text(index[i] + bar_width, bert[i] + 0.005, f'{bert[i]:.3f}', ha='center', va='bottom', fontsize=12)
    axes.text(index[i] + 2 * bar_width, sailer[i] + 0.005, f'{sailer[i]:.3f}', ha='center', va='bottom', fontsize=12)
    axes.text(index[i] + 3 * bar_width, keller[i] + 0.005, f'{keller[i]:.3f}', ha='center', va='bottom', fontsize=12)

# Add labels, title, and legend
axes.set_xlabel('Query Category', fontsize=18)
axes.set_ylabel('MAP', fontsize=18)
axes.set_ylim([0.4, 0.7])
axes.set_xticks(index + bar_width * 1.5)
axes.tick_params(axis='y', labelsize=14)
axes.set_xticklabels(['Common', 'Controversial'], fontsize=14)
axes.legend(fontsize=11)

# Adjust layout
plt.tight_layout()
plt.savefig('query_types.png')
plt.show()