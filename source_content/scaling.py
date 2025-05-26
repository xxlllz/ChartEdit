import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

# 数据：移除40处的点，120附近只保留一个点
N_p = np.array([0, 5, 10, 15, 20, 35, 50, 90, 120, 170, 220, 270, 320])
T_ideal = N_p  # 理想线保持线性
T_actual = np.array([0, 4, 10, 14, 20, 34, 50, 90, 120, 160, 200, 230, 250])  # 修改后的对应值



# 调整200-320区间的弯曲程度
for i in range(len(N_p)):
    if N_p[i] > 200:
        T_actual[i] = 200 + (T_actual[i] - 200) * 0.7  # 减小200-320之间的弯曲程度

plt.figure(figsize=(10, 8))

# 绘制理想线（降低明度的蓝色线）
plt.plot(N_p, T_ideal, label='Ideal', color='#004080', linewidth=4)  # 加粗蓝色线条

# 绘制实际线并加上标记
plt.plot(N_p, T_actual, label='Actual', color='#FF8C00', linewidth=4, marker='o', markersize=12)  # 提高明度的橙色

# 添加标签和图例
plt.xlabel('$N_p$', fontsize=24, weight='bold')  # 加粗横坐标字体
plt.ylabel('$T_1 / T_{N_p}$', fontsize=24, weight='bold')  # 加粗纵坐标字体
plt.legend(
    loc='upper left',
    fontsize=24
)

# 去掉背景网格线
plt.grid(False)

# 加粗坐标轴线条
plt.gca().spines['top'].set_linewidth(3)
plt.gca().spines['right'].set_linewidth(3)
plt.gca().spines['left'].set_linewidth(3)
plt.gca().spines['bottom'].set_linewidth(3)

# 手动设置主刻度为整百数，只保留 0、100、200、300
plt.xticks([0, 100, 200, 300], fontsize=24, weight='bold')
plt.yticks([0, 100, 200, 300], fontsize=24, weight='bold')

# 设置主刻度和次刻度
plt.gca().xaxis.set_minor_locator(MultipleLocator(20))  # 横坐标每20一个次刻度
plt.gca().yaxis.set_minor_locator(MultipleLocator(20))  # 纵坐标每20一个次刻度
plt.minorticks_on()  # 打开次刻度
plt.tick_params(which='both', width=2)  # 所有刻度加粗
plt.tick_params(which='major', length=10)  # 主刻度线长度加长
plt.tick_params(which='minor', length=5)  # 次刻度线长度加长

# 设置坐标范围，从 -20 开始
plt.xlim(-20, 320)
plt.ylim(-20, 320)

# 保存图像
plt.tight_layout()
plt.savefig('scaling.png')
plt.show()
