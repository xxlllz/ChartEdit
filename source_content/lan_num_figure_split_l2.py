import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# 数据
languages = ['Python', 'C++', 'Java', 'JS', 'R']
models = ['Starcoder', 'Code Llama', 'Deepseek Coder', 'ChatGPT']
values = {
    'star-low-high': [44.14, 46.01, 50.39, 51.71, 53.85],
    'star-high-low': [46.37, 49.19, 51.48, 52.77, 53.85],
    'deep-low-high': [65.00, 66.88, 68.70, 69.28, 70.27],
    'deep-high-low': [64.21, 66.96, 67.78, 68.73, 70.27]
}

# 绘制折线图
fig, axs = plt.subplots(1, 2, figsize=(6, 3.5), gridspec_kw={'wspace': 0.3, "left": 0.15, "right": 0.92, 'bottom': 0.25, 'top': 0.78}) # 
for ax in axs:
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
colors = ['#81B8DF', '#FA7F6F']  # R, G  blue green
shapes = ['o', 's', '^', 'D', 'x', '*']

model = 'Starcoder'
ax = axs[0]
ax.set_xticks(range(6))
ax.set_xticklabels([i + 1 for i in range(6)], fontdict={'size': 16})
ax.set_xlabel("(a) Starcoder", fontdict={'size': 16})
ax.set_ylabel('Performances(%)', fontdict={'size': 16})

ax.plot([k for k in range(5)], values['star-low-high'], linestyle='--', color=colors[0])
ax.plot([k for k in range(5)], values['star-high-low'], linestyle='-', color=colors[0])
ax.scatter([k for k in range(5)], values['star-low-high'], marker='o', color=colors[0]) # , label='Starcoder'
ax.scatter([k for k in range(5)], values['star-high-low'], marker='o', color=colors[0])
ax.set_yticklabels(['{:.0f}'.format(x) for x in ax.get_yticks()],fontdict={'size': 16})
h1, l1 = ax.get_legend_handles_labels()
ax = axs[1]
ax.set_xticks(range(6))
ax.set_xticklabels([i + 1 for i in range(6)], fontdict={'size': 16})
ax.set_xlabel("(b) Deepseek Coder", fontdict={'size': 16})

ax.plot([k for k in range(5)], values['deep-low-high'], linestyle='--', color=colors[1])
ax.plot([k for k in range(5)], values['deep-high-low'], linestyle='-', color=colors[1])
ax.scatter([k for k in range(5)], values['deep-low-high'], marker='o', color=colors[1])  # , label='Deepseek Coder'
ax.scatter([k for k in range(5)], values['deep-high-low'], marker='o', color=colors[1])
ax.set_yticklabels(['{:.0f}'.format(x) for x in ax.get_yticks()],fontdict={'size': 16})

h2, l2 = ax.get_legend_handles_labels()

custom_legend = [
    Line2D([0], [0], color='black', linestyle='--', label='Low -> High'),
    Line2D([0], [0], color='black', linestyle='-', label='High -> Low'),
]

# 显示图例
ax.legend(h1 + h2 + custom_legend, l1 + l2 + ['Data Amount Little -> Large', 'Data Amount Large -> Little'], loc='center', bbox_to_anchor=(0.5, 0.89), 
          bbox_transform=fig.transFigure, ncol=1, prop={'size': 15})

fig.text(0.5, 0.03, 'The Number of Languages', ha='center', fontdict={'size': 16})

plt.savefig("lan_num_figure_split_l2.png")