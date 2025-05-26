import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Data for the plots
gx_fr = ['0.001', '0.003', '0.005', '0.006', '0.007', '0.008', '0.01', '0.1']
frame_level_auc_fr = [75.73, 75.81, 75.62, 75.44, 76.39, 75.44, 74.58, 75.09]
video_level_auc_fr = [81.68, 81.38, 81.67, 80.85, 82.31, 80.97, 80.42, 81.02]

gx_cl = ['0.05', '0.08', '0.1', '0.12', '0.14', '0.2', '1.0']
frame_level_auc_cl = [75.33, 75.45, 76.39, 75.84, 76.21, 75.52, 75.98]
video_level_auc_cl = [80.98, 81.59, 82.31, 81.87, 82.26, 81.25, 82.10]

n_groups_fr = len(gx_fr)
index_fr = np.arange(n_groups_fr)
bar_width = 0.35

n_groups_cl = len(gx_cl)
index_cl = np.arange(n_groups_cl)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(12, 6))

# Plot for Î»fr
bars1_fr = ax1.bar(index_fr, frame_level_auc_fr, bar_width, label='Frame-level AUC', color='lightblue')
bars2_fr = ax1.bar(index_fr + bar_width, video_level_auc_fr, bar_width, label='Video-level AUC', color='plum')

ax1.set_xticks(index_fr + bar_width / 2)
ax1.set_xticklabels(gx_fr)
ax1.set_ylabel('AUC (%)',fontsize=18,fontweight='bold')
ax1.set_ylim([70, 90])
ax1.set_yticks([70.0,72.5,75.0,77.5,80.0,82.5,85.0,87.5,90.0])

ax1.legend(fontsize=12,edgecolor='none', loc='upper right')
ax1.set_xlabel('$\lambda_{fr}$',fontsize=22,fontweight='bold')
ax1.axhline(80, color='grey', linestyle='--', linewidth=1)

# Label bars - Î»fr
for bar in bars1_fr:
    fontsize = 9
    if bar.get_x() == index_fr[np.argmax(frame_level_auc_fr)]:  # Boldface the highest value
        fontsize = 'x-large'
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() , f'{bar.get_height():.2f}', 
             ha='center', va='bottom', color='black', fontsize=fontsize)
for bar in bars2_fr:
    fontsize = 9
    if bar.get_x() == index_fr[np.argmax(video_level_auc_fr)]:  # Boldface the highest value
        fontsize = 'x-large'
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f'{bar.get_height():.2f}', 
             ha='center', va='bottom', color='black', fontsize=fontsize)

# Plot for Î»cl
bars1_cl = ax2.bar(index_cl, frame_level_auc_cl, bar_width, label='Frame-level AUC', color='lightblue')
bars2_cl = ax2.bar(index_cl + bar_width, video_level_auc_cl, bar_width, label='Video-level AUC', color='plum')

ax2.set_xticks(index_cl + bar_width / 2)
ax2.set_xticklabels(gx_cl)
ax2.set_ylabel('AUC (%)',fontsize=18,fontweight='bold')
ax2.set_ylim([70, 90])
ax2.set_yticks([70.0,72.5,75.0,77.5,80.0,82.5,85.0,87.5,90.0])
ax2.legend(fontsize=12,edgecolor='none', loc='upper right')
ax2.set_xlabel('$\lambda_{cl}$',fontsize=22,fontweight='bold')
ax2.axhline(80, color='grey', linestyle='--', linewidth=1)

# Label bars - Î»cl
for bar in bars1_cl:
    fontsize = 9
    if bar.get_x() == index_cl[np.argmax(frame_level_auc_cl)]:  # Boldface the highest value 
        fontsize = 'x-large'
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() , f'{bar.get_height():.2f}', 
             ha='center', va='bottom', color='black', fontsize=fontsize)
for bar in bars2_cl:
    fontsize = 9
    if bar.get_x() == index_cl[np.argmax(video_level_auc_cl)]:  # Boldface the highest value
        fontsize = 'x-large'
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() , f'{bar.get_height():.2f}', 
             ha='center', va='bottom', color='black', fontsize=fontsize)

# 加粗第一张图的横坐标 0.07
for label in ax1.get_xticklabels():
    if label.get_text() == '0.007':  # 注意匹配的字符串
        label.set_fontweight('bold')

# 加粗第二张图的横坐标 0.1
for label in ax2.get_xticklabels():
    if label.get_text() == '0.1':  # 注意匹配的字符串
        label.set_fontweight('bold')

plt.tight_layout()
plt.savefig('loss_weight.png')