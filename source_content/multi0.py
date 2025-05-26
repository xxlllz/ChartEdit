import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D


# Data setup
models = ['GPT2', 'Llama-1', 'Llama-2']
model_sizes = {
    'GPT2': ['0.8B', '1.5B'],
    'Llama-1': ['7B', '13B', '30B'],
    'Llama-2': ['7B', '13B', '70B']
}
methods = ['ICL', 'kNN-prompt', 'kNN-prompting', 'FADS-ICL']
colors = ['red', 'green', 'royalblue', 'purple']
hatches = ['//']*4

# Average accuracy data (approximation from the image)
data = {
    'GPT2': {
        '0.8B': [62, 67, 78, 85],
        '1.5B': [68, 74, 81, 87]
    },
    'Llama-1': {
        '7B': [84.5, 85.2, 88, 91],
        '13B': [84, 86, 88.5, 91.5],
        '30B': [87.5, 86, 89.5, 92.3]
    },
    'Llama-2': {
        '7B': [86.5, 85.7, 86, 90.5],
        '13B': [87.8, 87, 89.6, 92.5],
        '70B': [92, 88, 90.2, 93]
    }
}

# Reference accuracy line for each model group
reference_line = 82

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(24, 6), sharey=False)

# Plot for GPT2
sizes = model_sizes['GPT2']
x = np.arange(0,len(sizes)*2,2)  # X-axis positions
width = 0.35  # Width of bars
space =0.025

# ICL method
values_ICL = [data['GPT2']['0.8B'][0], data['GPT2']['1.5B'][0]]
axes[0].bar(x - 3*width/2 - 3* space, values_ICL, width, label='ICL', color=colors[0], hatch=hatches[0],edgecolor='black',alpha=0.5,zorder=6)

# kNN-prompt method
values_kNN_prompt = [data['GPT2']['0.8B'][1], data['GPT2']['1.5B'][1]]
axes[0].bar(x- width/2 - space, values_kNN_prompt, width, label='kNN-prompt', color=colors[1], hatch=hatches[1],edgecolor='black',alpha=0.5,zorder=6)

# kNN-prompting method
values_kNN_prompting = [data['GPT2']['0.8B'][2], data['GPT2']['1.5B'][2]]
axes[0].bar(x + width/2 + space, values_kNN_prompting, width, label='kNN-prompting', color=colors[2], hatch=hatches[2],edgecolor='black',alpha=0.5,zorder=6)

# FADS-ICL method
values_FADS_ICL = [data['GPT2']['0.8B'][3], data['GPT2']['1.5B'][3]]
axes[0].bar(x+3*width/2+ 3*space, values_FADS_ICL, width, label='FADS-ICL', color=colors[3], hatch=hatches[3],edgecolor='black',alpha=0.5,zorder=6)

# Plot reference line for GPT2
axes[0].axhline(reference_line, linestyle='--', color='black', linewidth=2, label='Reference',alpha=0.5)
axes[0].grid(True, linestyle='-', linewidth=0.5, alpha=0.7,zorder=0)

# Customize GPT2 subplot
axes[0].set_title('GPT2', fontsize=20, fontweight='bold')
axes[0].set_xticks(x)
axes[0].set_xticklabels(sizes, fontsize=18)
axes[0].set_ylim(50, 100)
axes[0].set_yticks([50,60,70,80,90])
axes[0].set_yticklabels([50,60,70,80,90], fontsize=18)
axes[0].set_ylabel('Avg. Acc', fontsize=18)
# axes[0].set_xlabel('Model Size', fontsize=12)
axes[0].tick_params(axis='both', which='major', length=0)

# Plot for Llama-1
sizes = model_sizes['Llama-1']
x = np.arange(0, len(sizes) * 2, 2)  # X-axis positions for Llama-1
width = 0.3
# ICL method for Llama-1
values_ICL = [data['Llama-1']['7B'][0], data['Llama-1']['13B'][0], data['Llama-1']['30B'][0]]
axes[1].bar(x - 3 * width / 2 - 3 * space, values_ICL, width, label='ICL', color=colors[0], hatch=hatches[0], edgecolor='black', alpha=0.5)

# kNN-prompt method for Llama-1
values_kNN_prompt = [data['Llama-1']['7B'][1], data['Llama-1']['13B'][1], data['Llama-1']['30B'][1]]
axes[1].bar(x - width / 2 - space, values_kNN_prompt, width, label='kNN-prompt', color=colors[1], hatch=hatches[1], edgecolor='black', alpha=0.5)

# kNN-prompting method for Llama-1
values_kNN_prompting = [data['Llama-1']['7B'][2], data['Llama-1']['13B'][2], data['Llama-1']['30B'][2]]
axes[1].bar(x + width / 2 + space, values_kNN_prompting, width, label='kNN-prompting', color=colors[2], hatch=hatches[2], edgecolor='black', alpha=0.5)

# FADS-ICL method for Llama-1
values_FADS_ICL = [data['Llama-1']['7B'][3], data['Llama-1']['13B'][3], data['Llama-1']['30B'][3]]
axes[1].bar(x + 3 * width / 2 + 3 * space, values_FADS_ICL, width, label='FADS-ICL', color=colors[3], hatch=hatches[3], edgecolor='black', alpha=0.5)

# Plot reference line for Llama-1
axes[1].axhline(reference_line, linestyle='--', color='black', linewidth=1, label='Reference')

# Customize Llama-1 subplot
axes[1].set_title('Llama-1', fontsize=20, fontweight='bold')
axes[1].set_xticks(x)
axes[1].set_xticklabels(sizes, fontsize=18)
axes[1].set_ylim(75, 100)
axes[1].set_yticks([75,80,85,90,95])
axes[1].set_yticklabels([75,80,85,90,95], fontsize=18)
axes[1].set_ylabel('Avg. Acc', fontsize=18)
# axes[1].set_xlabel('Model Size', fontsize=12)
axes[1].tick_params(axis='both', which='major', length=0)
axes[1].axhline(reference_line, linestyle='--', color='black', linewidth=2, label='Reference',alpha=0.5)
axes[1].grid(True, linestyle='-', linewidth=0.5, alpha=0.7,zorder=0)

# Plot for Llama-2
sizes = model_sizes['Llama-2']
x = np.arange(0, len(sizes) * 2, 2)  # X-axis positions for Llama-2

# ICL method for Llama-2
values_ICL = [data['Llama-2']['7B'][0], data['Llama-2']['13B'][0], data['Llama-2']['70B'][0]]
axes[2].bar(x - 3 * width / 2 - 3 * space, values_ICL, width, label='ICL', color=colors[0], hatch=hatches[0], edgecolor='black', alpha=0.5)

# kNN-prompt method for Llama-2
values_kNN_prompt = [data['Llama-2']['7B'][1], data['Llama-2']['13B'][1], data['Llama-2']['70B'][1]]
axes[2].bar(x - width / 2 - space, values_kNN_prompt, width, label='kNN-prompt', color=colors[1], hatch=hatches[1], edgecolor='black', alpha=0.5)

# kNN-prompting method for Llama-2
values_kNN_prompting = [data['Llama-2']['7B'][2], data['Llama-2']['13B'][2], data['Llama-2']['70B'][2]]
axes[2].bar(x + width / 2 + space, values_kNN_prompting, width, label='kNN-prompting', color=colors[2], hatch=hatches[2], edgecolor='black', alpha=0.5)

# FADS-ICL method for Llama-2
values_FADS_ICL = [data['Llama-2']['7B'][3], data['Llama-2']['13B'][3], data['Llama-2']['70B'][3]]
axes[2].bar(x + 3 * width / 2 + 3 * space, values_FADS_ICL, width, label='FADS-ICL', color=colors[3], hatch=hatches[3], edgecolor='black', alpha=0.5)

# Plot reference line for Llama-2
axes[2].axhline(reference_line, linestyle='--', color='black', linewidth=1, label='Reference')

# Customize Llama-1 subplot
axes[2].set_title('Llama-2', fontsize=20, fontweight='bold')
axes[2].set_xticks(x)
axes[2].set_xticklabels(sizes, fontsize=18)
axes[2].set_ylim(75, 100)
axes[2].set_yticks([75,80,85,90,95])
axes[2].set_yticklabels([75,80,85,90,95], fontsize=18)
axes[2].set_ylabel('Avg. Acc', fontsize=18)
# axes[1].set_xlabel('Model Size', fontsize=12)
axes[2].tick_params(axis='both', which='major', length=0)
axes[2].axhline(reference_line, linestyle='--', color='black', linewidth=2, label='Reference',alpha=0.5)
axes[2].grid(True, linestyle='-', linewidth=0.5, alpha=0.7,zorder=0)

legend_elements = [
    Line2D([0], [0], color='black', linestyle='--', linewidth=2, label='GPT2-large(0.8B)FT'),  # 虚线
    Patch(color='red', label='ICL'),  # ICL
    Patch(color='green', label='kNN-prompt'),  # kNN-prompt
    Patch(color='blue', label='kNN-prompting'),  # kNN-prompting
    Patch(color='purple', label='FADS-ICL')  # FADS-ICL
]

# 调整图像的边缘间距，适当减小间距
fig.subplots_adjust(left=0.03, right=0.99, top=0.9, bottom=0.2)

# 创建并显示 legend
fig.legend(handles=legend_elements, loc='lower center', fontsize=18,ncol=5,bbox_to_anchor=(0.5, 0),frameon=False)
plt.savefig('multi0.png')

