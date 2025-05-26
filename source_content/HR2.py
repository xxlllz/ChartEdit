import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 生成示例数据
np.random.seed(10)
L_data = np.concatenate([
    np.random.uniform(-1.6, -0.5, 3),
    np.random.normal(0.25, 0.25, 400),
    np.random.uniform(1, 2.3, 3)
])

# S 数据：顶部更宽，下部逐渐收窄
S_data = np.concatenate([
    np.random.uniform(-0.5, 1 , 40),
    np.random.normal(0.6, 0.6, 100), 
    np.random.uniform(0.5, 1.0, 200),
    np.random.uniform(1.0, 1.4, 300)
])


# 数据整理
data = {
    'Group': ['L'] * len(L_data) + ['S'] * len(S_data),
    'HR': np.concatenate([L_data, S_data])
}
df = pd.DataFrame(data)

# 自定义颜色
custom_palette = {'L': '#3174A1', 'S': '#E1812C'}

# 绘制小提琴图
plt.figure(figsize=(6, 4.5))

# 添加纵向点划线背景，每指定单位添加一条
y_ticks = [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
for y_position in y_ticks:
    plt.axhline(y=y_position, color='gray', linestyle='--', linewidth=0.8, zorder=1)  # 设置图层在下方

# 添加横坐标处的竖着的点划线
x_positions = range(len(df['Group'].unique()))
for x_position in x_positions:
    plt.axvline(x=x_position, color='gray', linestyle='--', linewidth=0.8, zorder=1)  # 设置图层在下方

sns.violinplot(x='Group', y='HR', data=df, hue='Group', palette=custom_palette, inner='box', dodge=False, legend=False, zorder=2)

# 设置纵轴范围和刻度
plt.ylim(-1.9, 2.6)
plt.yticks(y_ticks, fontsize=14)

# 设置标签
plt.xlabel('Group', fontsize=16)
plt.ylabel('HR', fontsize=16)
plt.xticks(fontsize=14)


# 调整布局
plt.tight_layout()
plt.savefig('HR2.png')  # 保存图像