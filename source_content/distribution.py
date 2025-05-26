import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D
# Data
labels = [
    'OPT-125M-C, 8849','OPT-350M-C, 8775', 'OPT-1.3B-C, 9202', 
    'OPT-13B-C, 8126', 'OPT-2.7B-C, 9161','OPT-6.7B-C, 8858',  
    'OPT-30B-C, 8971', 'OPT-iml-max-1.3B-C, 9157','OPT-mini-30B-C, 9330', 
    
    'BLOOM-7B-C, 8818','TO-11B-C, 8930', 'TO-38B-C, 9452',
    'gpt-3.5-trubo-C, 9530', 'gpt-3.5-trubo-T, 6547', 'gpt-3.5-trubo-S, 6602',
    'text-davinci-002-C, 9066', 'text-davinci-002-T, 6410', 'text-davinci-002-S, 6366', 
    'text-davinci-003-C, 9409', 'text-davinci-003-T, 6329', 'text-davinci-003-S, 6354',
    'LLaMA-7B-C, 9278', 'LLaMA-13B-C, 9290', 'LLaMA-30B-C, 9351', 'LLaMA-65B-C, 9335', 
    'GLM130B-C, 9182',
    'FLAN-T5-small-C, 9382', 'FLAN-T5-base-C, 9454',
    'FLAN-T5-large-C, 9394', 'FLAN-T5-xl-C, 9170', 'FLAN-T5-xxl-C, 9319',
    'GPT-J-6B-C, 7588', 'GPT-NeoX-20B-C, 6839',  
    
]

sizes = [int(label.split(',')[1].strip()) for label in labels]

colors = ["#CFBBFB"]*9 +  ["#DDBB9E"]*3+ ["#A2C9F1"]*9+ ["#FDB588"]*4+ ["#91E4A6"]*1 + ["#FDA19D"]*5+ ["#F8B1E1"]*2

# Plot
fig, ax = plt.subplots(figsize=(16, 16))

def func(pct, allvalues, labels):
    for i, size in enumerate(allvalues):
        if abs(size / sum(allvalues) - pct / 100) < 1e-6:  # Use a small tolerance for floating-point comparison
            return f"{labels[i]}"

patches, texts, autotexts = ax.pie(sizes, labels=['']*33, colors=colors, 
                                   startangle=181, pctdistance=0.73, 
                                   autopct=lambda pct: func(pct, sizes, labels))

# Ensure the aspect ratio is equal
# 调整文本角度
for i, text in enumerate(autotexts):
    # 获取每个文本的位置角度
    angle = (sum(sizes[:i]) + sizes[i] / 2) / sum(sizes) * 360 + 1.5
    # print(angle)
    # 旋转文本，使其对齐
    if i in np.arange(8,25,1):
        text.set_rotation(angle+180)
    else:
        text.set_rotation(angle)
    text.set_fontsize(18) 
# ax.axis('equal')


# Add legend
legend_labels = [
    "OpenAI GPT", "LLaMA", "GLM-130B", "FLAN-T5",  "OPT", "BigScience","EleutherAI"
]
legend_colors = [
    "#A2C9F1", "#FDB588", "#91E4A6", "#FDA19D", "#CFBBFB", "#DDBB9E", "#F8B1E1"
]
handles = [Line2D([0], [0],marker='o', color='w', markerfacecolor=color, markersize=20, markeredgecolor='w', label=label) for color, label in zip(legend_colors, legend_labels)]
plt.legend(handles, legend_labels, title="Model Sets", loc="center",fontsize=22,title_fontsize=20)
# plt.subplots_adjust(left=0.3, right=0.8, top=0.8, bottom=0.3)

plt.tight_layout()
plt.savefig("distribution.png")
