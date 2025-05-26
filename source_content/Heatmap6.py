import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Data for the heatmap
labels = ['Yi', 'LLAMA-2', 'Vicuna', 'Tulu', 'Mistral', 'Zephyr', 'Qwen', 'WizardLM']
data = np.array([
    [0.83, 0.75, 0.75, 0.8, 0.83, 0.84, 0.81, 0.82],
    [0.75, 0.69, 0.77, 0.74, 0.73, 0.78, 0.74, 0.75],
    [0.83, 0.77, 0.87, 0.81, 0.83, 0.81, 0.82, 0.83],
    [0.8, 0.74, 0.81, 0.75, 0.81, 0.84, 0.79, 0.83],
    [0.83, 0.73, 0.83, 0.81, 0.81, 0.86, 0.82, 0.84],
    [0.84, 0.78, 0.86, 0.84, 0.86, 0.92, 0.83, 0.86],
    [0.81, 0.74, 0.81, 0.79, 0.82, 0.83, 0.79, 0.83],
    [0.82, 0.75, 0.82, 0.83, 0.84, 0.86, 0.83, 0.82]
])

fig, ax = plt.subplots(figsize=(8, 8))
cax = ax.matshow(data, cmap='viridis', vmin=0.68, vmax=0.92)

# 添加 colorbar
colorbar = plt.colorbar(cax, ax=ax, shrink=0.72)  # 调整 shrink 以控制高度

# 设置边框为 0
colorbar.outline.set_visible(False)

plt.xticks(ticks=np.arange(len(labels)), labels=labels, rotation=0, ha="center",fontsize=10)
plt.yticks(ticks=np.arange(len(labels)), labels=labels)

# Annotate each cell with the corresponding value
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        ax.text(j, i, f'{data[i, j]:.2f}', va='center', ha='center', size = 12, color='white' if data[i, j] < 0.86 else 'black')

ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.xaxis.set_ticks_position('bottom')
# Colorbar
plt.show()
plt.tight_layout(pad=0)

plt.savefig('Heatmap6.png')