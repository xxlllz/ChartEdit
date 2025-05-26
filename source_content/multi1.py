import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['BM25', 'Openai', 'Hybrid']
min_gap_4choice = [6.03, 6.02, 5.63]
ave_gap_4choice = [9.09, 8.62, 8.31]
min_gap_binary = [5.98, 6.10, 5.63]
ave_gap_binary = [9.00, 8.58, 8.21]
x = np.arange(len(categories))  # the label locations
width = 0.2  # the width of the bars
space = 0.03
fig, axes = plt.subplots(1, 2, figsize=(10, 3.8), sharey=False)

# Plot for Four Choice Setting
axes[0].bar(x - width/2 -space, min_gap_4choice, width, label='Min_Gap', color='#4461AD')
axes[0].bar(x + width/2 +space, ave_gap_4choice, width, label='Ave_Gap', color='#92A0D4')
axes[0].set_title('(1) Four Choice Setting', fontsize=22,y=-0.3)
ylabels=[0.00,2.00,4.00,6.00,8.00,10.00]
ylabels_str=['0.00','2.00','4.00','6.00','8.00','10.00']
axes[0].set_yticks(ylabels)
axes[0].set_yticklabels(ylabels_str,fontsize=18)
axes[0].set_xticks(x)
axes[0].set_xticklabels(categories,fontsize=16)
axes[0].tick_params(axis='x',pad=15)
axes[0].spines['top'].set_visible(False)
axes[0].spines['left'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['bottom'].set_color('silver')
axes[0].tick_params(length=0)
axes[0].spines['bottom'].set_alpha(0.5)
axes[0].spines['bottom'].set_linewidth(3)


# Adding labels above bars
for i in range(len(categories)):
    axes[0].text(i - width/2 -space, min_gap_4choice[i] + 0.3, str(min_gap_4choice[i]), ha='center', va='bottom',fontsize=14)
    axes[0].text(i + width/2 +space, ave_gap_4choice[i] + 0.3, str(ave_gap_4choice[i]), ha='center', va='bottom',fontsize=14)

# Plot for Binary Yes-No Setting
axes[1].bar(x - width/2 -space, min_gap_binary, width, label='Min_Gap', color='#4461AD')
axes[1].bar(x + width/2 +space, ave_gap_binary, width, label='Ave_Gap', color='#92A0D4')
axes[1].set_title('(2) Binary Yes-No Setting', fontsize=22,y=-0.3)
ylabels=[0.00,2.00,4.00,6.00,8.00,10.00]
ylabels_str=['0.00','2.00','4.00','6.00','8.00','10.00']
axes[1].set_yticks(ylabels)
axes[1].set_yticklabels(ylabels_str,fontsize=16)
axes[1].set_xticks(x)
axes[1].set_xticklabels(categories,fontsize=16)
axes[1].tick_params(axis='x',pad=15)
axes[1].spines['top'].set_visible(False)
axes[1].spines['left'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['bottom'].set_color('silver')
axes[1].tick_params(length=0)
axes[1].spines['bottom'].set_alpha(0.5)
axes[1].spines['bottom'].set_linewidth(3)
# Adding labels above bars
for i in range(len(categories)):
    axes[1].text(i - width/2 -space, min_gap_binary[i] + 0.3, f"{min_gap_binary[i]:.2f}", ha='center', va='bottom',fontsize=14)
    axes[1].text(i + width/2 +space, ave_gap_binary[i] + 0.3, f"{ave_gap_binary[i]:.2f}", ha='center', va='bottom',fontsize=14)


# Add overall legend with square markers (marker='s')
fig.legend(labels=['Min_Gap', 'Ave_Gap'], loc='upper left', fontsize=16, markerscale=2, markerfirst=True, frameon=False, handlelength=1, handleheight=1,ncol=2,bbox_to_anchor=(0.1, 1))

fig.subplots_adjust(left=0.1, right=0.99, top=0.85, bottom=0.19)
plt.savefig('multi1.png')