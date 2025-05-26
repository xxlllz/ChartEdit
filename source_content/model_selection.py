import matplotlib.pyplot as plt
import numpy as np

categories = ['Indicator', 'Ideation', 'Behavior', 'Attempt', 'Macro', 'Micro']
bert_scores = [0.5, 0.63, 0.58, 0.0, 0.42, 0.57]
biomedbert_scores = [0.43, 0.60, 0.45, 0.21, 0.42, 0.51]
roberta_scores = [0.57, 0.70, 0.66, 0.44, 0.60, 0.63]

bert_errors = [0.05, 0.05, 0.05, 0.00, 0.05, 0.05]
biomedbert_errors = [0.08, 0.05, 0.05, 0.24, 0.07, 0.05]
roberta_errors = [0.09, 0.05, 0.09, 0.30, 0.10, 0.09]

x = np.arange(len(categories))  # the label locations
width = 0.15  # the width of the bars

fig, ax = plt.subplots(figsize=(8, 6))

# 绘制柱状图（不包括误差条）
bars1 = ax.bar(x - width-0.10, bert_scores, width, label='BERT', color='#8EB1FF', edgecolor ='#3367A2',linewidth=4,zorder=3)
bars2 = ax.bar(x, biomedbert_scores, width, label='BiomedBERT', color='#B49FDC', edgecolor ='#7557AB', linewidth=4,zorder=3)
bars3 = ax.bar(x + width+0.10, roberta_scores, width, label='RoBERTa', color='#EFABEF', edgecolor ='#A4329F', linewidth=4,zorder=3)

# 绘制误差条（不通过 yerr 参数，而是使用 errorbar）
ax.errorbar(x - width-0.10, bert_scores, yerr=bert_errors, fmt='none', color='#3367A2', capsize=4, zorder=2)
ax.errorbar(x, biomedbert_scores, yerr=biomedbert_errors, fmt='none', color='#7557AB', capsize=4, zorder=2)
ax.errorbar(x + width+0.10, roberta_scores, yerr=roberta_errors, fmt='none', color='#A4329F', capsize=4, zorder=2)

ax.set_ylabel('F1 Score',fontsize = 20,fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right', fontweight='bold',fontsize=16)  # Rotate and bold the category names
ax.set_yticks(np.arange(0, 1.1, 0.2))
ax.set_ylim(0, 1.0)
ax.set_yticklabels([0.0, 0.2, 0.4, 0.6, 0.8, 1.0], fontsize=16, fontweight='bold')
# ax.set_title('Comparison of F1 Scores')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_linewidth(2) # 下边框线宽
ax.spines['left'].set_linewidth(2)   # 左边框线宽
ax.legend(loc='lower center',ncol=3,fontsize=24,edgecolor='none',bbox_to_anchor=(0.5, -0.45),facecolor='none',labelspacing=0.1,columnspacing=0.15,borderaxespad=0.5)
ax.grid(True,linestyle='-',axis='y',zorder=0,color='black')
ax.tick_params(axis='both', length=8, width=2)  # x 和 y 轴刻度线的长度设置为10
plt.subplots_adjust(bottom=0.25)  # 0.2表示留出20%的空间
plt.tight_layout()
plt.savefig('model_selection.png')