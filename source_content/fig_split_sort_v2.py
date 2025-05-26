import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 数据
languages = ['Python', 'C++', 'Java', 'JavaScript', 'R']
models = ['Starcoder', 'Code Llama', 'Deepseek Coder', 'ChatGPT']
R_values = {
    'Deepseek Coder': [65.00, 62.31, 63.26, 64.21, 64.90],
    'Starcoder': [44.68, 43.23, 45.93, 46.59, 46.82],
    'Code Llama': [61.52, 58.90, 59.64, 60.68, 64.28],
    'ChatGPT': [70.40, 69.13, 69.82, 70.69, 71.02]
}
G_values = {
    'Deepseek Coder': [None, 56.1, 55.3, 51.9, 58.4],
    'Starcoder': [None, 31.1, 31.7, 28.5, 29.8],
    'Code Llama': [None, 44.7, 42.2, 48.2, 44.9],
    'ChatGPT': [None, 63.4, 69.2, 76.2, 67.1]
}
percentage_values = {
    'Deepseek Coder': [0.11, 15.12, 6.75, 18.63, 11.39],
    'Starcoder': [0.04, 6.38, 7.88, 11.34, 8.44],
    'Code Llama': [None, None, None, None, None],  # 该模型没有百分比数据
    'ChatGPT': [None, None, None, None, None]  # 该模型没有百分比数据
}

# 绘制折线图
fig, axs = plt.subplots(2, 2, figsize=(8, 6), gridspec_kw={'wspace': 0.35, "hspace": 0.35, "left": 0.12, "right": 0.88})
font = FontProperties(family='Times New Roman', size=11)

colors = ['#81B8DF', '#32B897', '#FA7F6F']  # R, G, %  blue green red
shapes = ['o', 's', '^', 'D', 'x', '*']

i = 0
model = 'Starcoder'
tmp_lans = ['R', 'C++', 'Python', 'Java', 'JS']
ax = axs[0, i]
ax.spines['top'].set_visible(False)

ax.set_xticks(range((len(languages))))
ax.set_xticklabels([lan for lan in (tmp_lans)], fontdict={'size': 14})

ax.set_xlabel("(a) Starcoder", fontdict={'size': 18})
ax.plot([k for k in range(len(languages))], R_values[model], linestyle='--', color=colors[0], marker=shapes[0], label='Reasoning')
ax.plot([k for k in range(len(languages))], G_values[model], linestyle='--', color=colors[1], marker=shapes[1], label='Generation')

ax2 = ax.twinx()
ax2.spines['top'].set_visible(False)
ax2.set_ylim(0, 20)
ax2.plot([k for k in range(len(languages))], percentage_values[model], linestyle='-', color=colors[2], marker=shapes[2], label=f'Percentage' if i == 0 else "") # marker = 'o'

ax.set_yticklabels(['{:.0f}'.format(x) for x in ax.get_yticks()], fontdict={'size': 14})
ax2.set_yticklabels(['{:.0f}'.format(x) for x in ax2.get_yticks()], fontdict={'size': 14})
ax.set_ylabel('Accuracy(%)', fontdict={'size': 14})

i = 1
model = 'Deepseek Coder'
tmp_lans = ['R', 'Python', 'JS', 'Java', 'C++']
ax = axs[0, i]
ax.spines['top'].set_visible(False)
ax.set_xticks(range((len(languages) + 1)))
ax.set_xticklabels([lan for lan in (tmp_lans + [""])], fontdict={'size': 14})
ax.set_xlabel("(b) Deepseek Coder", fontdict={'size': 18})
for j, value_type in enumerate(['R', 'G']):
    values = R_values[model] if value_type == 'R' else G_values[model]
    color = colors[j]
    ax.plot([k for k in range(len(languages))], values, linestyle='--', color=color, marker=shapes[j], label=f'{value_type}-{model}')
ax2 = ax.twinx()
ax2.spines['top'].set_visible(False)
# ax2.set_ylabel('%')
ax2.set_ylim(0, 20)
ax2.plot([k for k in range(len(languages))], percentage_values[model], linestyle='-', color=colors[2], marker=shapes[2], label=f'Data Amount')

ax.set_yticklabels(['{:.0f}'.format(x) for x in ax.get_yticks()], fontdict={'size': 14})
ax2.set_yticklabels(['{:.0f}'.format(x) for x in ax2.get_yticks()], fontdict={'size': 14})
ax2.set_ylabel('Data Amount(%)', fontdict={'size': 14})

i = 0
model = 'Code Llama'
tmp_lans = ['R', 'C++', 'JS', 'Python', 'Java']
ax = axs[1, i]
ax.set_xlabel("(c) Code Llama", fontdict={'size': 18})
ax.set_xticks(range((len(languages) + 1)))
ax.set_xticklabels([lan for lan in (tmp_lans + [""])], fontdict={'size': 14})
for j, value_type in enumerate(['R', 'G']):
    values = R_values[model] if value_type == 'R' else G_values[model]
    color = colors[j]
    ax.plot([k for k in range(len(languages))], values, linestyle='--', color=color, marker=shapes[j], label=f'{value_type}')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.set_yticklabels(['{:.0f}'.format(x) for x in ax.get_yticks()], fontdict={'size': 14})
ax.set_ylabel('Accuracy(%)', fontdict={'size': 14})

i = 1
model = 'ChatGPT'
tmp_lans = ['R', 'C++', 'Java', 'Python', 'JS']
ax = axs[1, i]
ax.set_xlabel("(d) ChatGPT", fontdict={'size': 18})
ax.set_xticks(range((len(languages) + 1)))
ax.set_xticklabels([lan for lan in (tmp_lans + [""])], fontdict={'size': 14})
ax.spines['top'].set_visible(False)   
ax.spines['right'].set_visible(False)
for j, value_type in enumerate(['R', 'G']):
    values = R_values[model] if value_type == 'R' else G_values[model]
    color = colors[j]
    ax.plot([k for k in range(len(languages))], values, linestyle='--', color=color, marker=shapes[j], label=f'{value_type}')

ax.set_yticklabels(['{:.0f}'.format(x) for x in ax.get_yticks()], fontdict={'size': 14})


# 显示图例
handles, labels = axs[0, 0].get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
axs[0, 0].legend(handles + h2, labels + l2, loc='center', bbox_to_anchor=(0.5, 0.95), bbox_transform=fig.transFigure, ncol=3, prop={'size': 16})

plt.savefig("fig_split_sort_v2.png")