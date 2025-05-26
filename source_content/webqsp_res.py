import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
def percent(x, pos):
    return f'{int(x)}%'
# Sample data
x = np.array([10, 20, 50, 100])
y_joint = np.array([0.71, 0.77, 0.82, 0.851])
y_index_retrieval = np.array([0.715, 0.772, 0.816, 0.838])
y_index_joint = np.array([0.70, 0.774, 0.815, 0.843])
y_retrieval = np.array([0.64, 0.74, 0.81, 0.83])

fig, ax = plt.subplots(figsize=(8, 4))

ax.plot(x, y_joint, '^-', label='joint', color='blue')
ax.plot(x, y_index_retrieval, '^-', label='index => retrieval', color='orange')
ax.plot(x, y_index_joint, '^-', label='index => joint', color='green')
ax.plot(x, y_retrieval, 'x-', color='red', label='retrieval')

# Customize plot
ticks = ax.get_xticks()
# Set x-ticks to be exactly the values you want
ax.set_xlim(5, 105)
ax.set_xticks([10, 20, 50, 100])
ax.xaxis.set_major_formatter(FuncFormatter(percent))
# Set x-axis limits to leave space at both ends and match the ticks


ax.set_yticks(np.arange(0.65, 0.95, 0.05))
ax.set_ylim(0.60, 0.88)
ax.set_xlabel('Data Proportion')
ax.set_ylabel('Recall (%)')
ax.legend(loc='lower right')
ax.grid(True, linestyle='--', alpha=0.5, axis='y')

plt.tight_layout()
plt.savefig('webqsp_res.png')