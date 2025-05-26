import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['10', '15', '20', '25', '30']
hcbp = [4.05, 5.05, 5.9, 7.2, 7.4]
tpk_means = [3.8, 4.5, 4.7, 5.8, 5.8]
bk_means = [4, 4.6, 5.2, 6.3, 6.4]
tgbp = [3.8, 4.5, 4.9, 5.5, 5.6]

x = np.arange(len(categories))
width = 0.15

# Plotting
fig, ax = plt.subplots()

ax.bar(x - width*1.5-0.06, hcbp, width, label='HCBP', color='#995319',edgecolor='black')
ax.bar(x - width/2-0.03, tpk_means, width, label='TPK-Means', color='#EDB120',edgecolor='black')
ax.bar(x + width/2+0.03, bk_means, width, label='BK-Means', color='#0072BD',edgecolor='black')
ax.bar(x + width*1.5+0.06, tgbp, width, label='TGBP', color='#D95319',edgecolor='black')

ax.set_xlabel('Number of users',fontsize=14)
ax.set_ylabel('Average number of active beams',fontsize=14)
ax.set_xticks(x)
ax.set_xticklabels(categories,fontsize=10)
ax.set_yticks([0,1,2,3,4,5,6,7,8])
ax.set_ylim(0,8)

ax.tick_params(axis='x', labelsize=10, pad=10)  # `pad` 控制坐标轴刻度标签与坐标轴的距离
# Adjusting legend placement to avoid overlap
ax.legend(loc='upper left', ncol=1,fontsize=12,handlelength=2.5, handleheight=1.5)

#设置上边和右边刻度方向
ax.tick_params(axis='x', direction='in')  # x轴的刻度方向（控制下边）
ax.tick_params(axis='y', direction='in')  # y轴的刻度方向（控制左边）

# 控制上边和右边的刻度方向
ax.tick_params(axis='x', which='both', top='in')  # 控制上边的刻度
ax.tick_params(axis='y', which='both', right='in')  # 控制右边的刻度
plt.tight_layout()
plt.savefig('number_of_beams_small.png')