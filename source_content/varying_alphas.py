import matplotlib.pyplot as plt
import numpy as np

# Data for plots
data = {
    'Simple Spring': {'x': [1,2,3,4,5], 'y_treat': [0.0076, 0.0072, 0.0065, 0.0079, 0.0087], 'y_lg_ode': [0.0095] * 5},
    'Damped Spring': {'x': [1,2,3,4,5], 'y_treat': [0.0140, 0.0123, 0.0117, 0.0130, 0.0143], 'y_lg_ode': [0.0167] * 5},
    'Forced Spring': {'x': [1,2,3,4,5], 'y_treat': [0.0167, 0.0164, 0.0143, 0.0146, 0.0190], 'y_lg_ode': [0.0187] * 5},
    'Pendulum': {'x': [1,2,3,4,5], 'y_treat': [0.0138, 0.0123, 0.0125, 0.0145, 0.01456], 'y_lg_ode': [0.0141] * 5}
}

fig, axes = plt.subplots(1, 4, figsize=(18, 3))

# Simple Spring
ax = axes[0]
values = data['Simple Spring']
ax.plot(values['x'], values['y_treat'], 'r-o', label='TREAT')
ax.plot(values['x'], values['y_lg_ode'], 'b--', label='LG-ODE')
ax.set_xlabel(r'$\alpha$ values', fontsize=12)
ax.set_ylabel('MSE', fontsize=12)
#设置横坐标刻度和对应的标签
xticks = [1, 2, 3, 4, 5]  # 实际 x 坐标的位置
xticklabels = [0.01, 0.02, 0.1, 2, 5]  # 显示的标签
ax.set_xticks(xticks)  # 设置刻度位置
ax.set_xticklabels(xticklabels)  # 设置刻度显示为标签字符串
ax.set_yticks([0.007,0.008,0.009])
ax.legend(loc='center')
fig.text(0.15,0.005, '(a) Simple Spring', ha='center', fontsize=14)  # 修改 y 坐标，让标题位于子图下方




# Damped Spring
ax = axes[1]
values = data['Damped Spring']
ax.plot(values['x'], values['y_treat'], 'r-o', label='TREAT')
ax.plot(values['x'], values['y_lg_ode'], 'b--', label='LG-ODE')
ax.set_xlabel(r'$\alpha$ values', fontsize=12)
ax.set_ylabel('MSE', fontsize=12)
xticks = [1, 2, 3, 4, 5]  # 实际 x 坐标的位置
xticklabels = [0.02, 0.1, 0.5, 5, 10]  # 显示的标签
ax.set_xticks(xticks)  # 设置刻度位置
ax.set_xticklabels(xticklabels)  # 设置刻度显示为标签字符串
ax.set_yticks([0.012,0.014,0.016])
ax.legend(loc='center')
fig.text(0.40,0.005, '(b) Damped Spring', ha='center', fontsize=14)  # 修改 y 坐标，让标题位于子图下方
# Forced Spring
ax = axes[2]
values = data['Forced Spring']
ax.plot(values['x'], values['y_treat'], 'r-o', label='TREAT')
ax.plot(values['x'], values['y_lg_ode'], 'b--', label='LG-ODE')
xticks = [1, 2, 3, 4, 5]  # 实际 x 坐标的位置
xticklabels = [0.02, 0.1, 0.5, 2, 5]  # 显示的标签
ax.set_xticks(xticks)  # 设置刻度位置
ax.set_xticklabels(xticklabels)  # 设置刻度显示为标签字符串
ax.set_yticks([0.014,0.016,0.018,0.020])
ax.set_xlabel(r'$\alpha$ values', fontsize=12)
ax.set_ylabel('MSE', fontsize=12)
ax.legend(loc='center')
fig.text(0.65,0.005, '(c) Forced Spring', ha='center', fontsize=14)  # 修改 y 坐标，让标题位于子图下方

# Pendulum
ax = axes[3]
values = data['Pendulum']
ax.plot(values['x'], values['y_treat'], 'r-o', label='TREAT')
ax.plot(values['x'], values['y_lg_ode'], 'b--', label='LG-ODE')
ax.set_xlabel(r'$\alpha$ values', fontsize=12)
ax.set_ylabel('MSE', fontsize=12)
xticks = [1, 2, 3, 4, 5]  # 实际 x 坐标的位置
xticklabels = [10, 50, 100, 500, 1000]  # 显示的标签
ax.set_xticks(xticks)  # 设置刻度位置
ax.set_xticklabels(xticklabels)  # 设置刻度显示为标签字符串
ax.set_yticks([0.012,0.013,0.014,0.015])
ax.legend(loc='center')
fig.text(0.89,0.005, '(d) Pendulum', ha='center', fontsize=14)  # 修改 y 坐标，让标题位于子图下方

plt.tight_layout()
plt.savefig('varying_alphas.png')
