import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
revfilter_hr = np.array([0.91, 0.93, 0.95, 0.96, 0.97, 0.98, 0.97, 0.98, 0.98, 0.99])
ngcf_hr = np.array([0.50, 0.50, 0.57, 0.62, 0.61, 0.62, 0.63, 0.65, 0.66, 0.67])
lightgcn_hr = np.array([0.48, 0.55, 0.58, 0.61, 0.62, 0.63, 0.64, 0.66, 0.68, 0.679])
mlp_hr = np.array([0.00, 0.03, 0.04, 0.05, 0.07, 0.10, 0.14, 0.16, 0.20, 0.25])

revfilter_ndcg = np.array([0.57, 0.49, 0.45, 0.44, 0.43, 0.41, 0.39, 0.38, 0.37, 0.36])
ngcf_ndcg = np.array([0.42, 0.40, 0.44, 0.45, 0.45, 0.44, 0.45, 0.44, 0.45, 0.47])
lightgcn_ndcg = np.array([0.26, 0.28, 0.29, 0.28, 0.29, 0.28, 0.29, 0.28, 0.279, 0.281])+0.05
mlp_ndcg = np.array([0.01, 0.02, 0.023, 0.025, 0.03, 0.033, 0.036, 0.04, 0.045, 0.05])

fig, ax = plt.subplots(1, 2, figsize=(14, 6))

# Plotting HR
ax[0].plot(x, revfilter_hr, 'bo-', linewidth=3, label='RevFilter', markersize=10)
ax[0].plot(x, ngcf_hr, 'rs--', linewidth=3, label='NGCF', markersize=10)
ax[0].plot(x, lightgcn_hr, '^-.', color = 'green',linewidth=3, label='LightGCN', markersize=10)
ax[0].plot(x, mlp_hr, 'mD:', linewidth=3, label='MLP', markersize=10)
ax[0].set_xlabel('top-k', fontsize=18)
ax[0].set_ylim(-0.05, 1.05)
ax[0].set_yticks([0.00,0.25,0.50,0.75,1.00])
ax[0].set_yticks(np.concatenate([np.linspace(0.00, 0.25, 6), np.linspace(0.25, 0.50, 6), 
                              np.linspace(0.50, 0.75, 6), np.linspace(0.75, 1.00, 6)]), minor=True)

ax[0].set_yticklabels([], minor=True) 
# 设置X轴刻度和细化刻度（不显示数字）
ax[0].set_xticks([20, 40, 60, 80, 100])  # 只显示20, 40, 60, 80, 100
ax[0].set_xticks(np.concatenate([np.linspace(20, 40, 4), np.linspace(40, 60, 4), np.linspace(60, 80, 4), np.linspace(80, 100, 4)]), minor=True)  # 细化刻度
ax[0].set_xticklabels([], minor=True)  # 不显示细化刻度的数字标签
ax[0].tick_params(axis='x', direction='in', which='both',labelsize=18)  # X轴的刻度线指向图内
ax[0].tick_params(axis='y', direction='in', which='both',labelsize=18)


ax[0].set_ylabel('HR', fontsize=18)
ax[0].grid(True, which='major', linestyle='--')


# Plotting NDCG
ax[1].plot(x, revfilter_ndcg, 'bo-', linewidth=2, markersize=10 )
ax[1].plot(x, ngcf_ndcg, 'rs--', linewidth=2, markersize=10 )
ax[1].plot(x, lightgcn_ndcg, 'g^-.', linewidth=2, markersize=10 )
ax[1].plot(x, mlp_ndcg, 'mD:', linewidth=3, markersize=10 )
ax[1].set_xlabel('top-k', fontsize=18)
ax[1].set_ylabel('NDCG', fontsize=18)
ax[1].set_ylim(-0.05, 1.05)
ax[1].set_yticks([0.00,0.25,0.50,0.75,1.00])
ax[1].set_yticks(np.concatenate([np.linspace(0.00, 0.25, 6), np.linspace(0.25, 0.50, 6), 
                              np.linspace(0.50, 0.75, 6), np.linspace(0.75, 1.00, 6)]), minor=True)

ax[1].set_yticklabels([], minor=True) 
# 设置X轴刻度和细化刻度（不显示数字）
ax[1].set_xticks([20, 40, 60, 80, 100])  # 只显示20, 40, 60, 80, 100
ax[1].set_xticks(np.concatenate([np.linspace(20, 40, 4), np.linspace(40, 60, 4), np.linspace(60, 80, 4), np.linspace(80, 100, 4)]), minor=True)  # 细化刻度
ax[1].set_xticklabels([], minor=True)  # 不显示细化刻度的数字标签
ax[1].tick_params(axis='x', direction='in', which='both',labelsize=18)  # X轴的刻度线指向图内
ax[1].tick_params(axis='y', direction='in', which='both',labelsize=18)
ax[1].grid(True, which='major', linestyle='--')
# Adding legend
fig.legend(loc='upper center', ncol=4, fontsize=18, frameon=True)
# 增加上方的空间

plt.tight_layout(rect=[0, 0, 1, 0.9])
# plt.subplots_adjust(top=0.6)  # 调整上边缘位置，默认是1，减小数值会给上方留出更多空间

plt.savefig('rec_plot_k.png')