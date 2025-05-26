import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# 创建DataFrame
data = {
    'Model': ['Starcoder', 'ChatGPT', 'Starcoder', 'ChatGPT'],
    'Type': ['All Dynamic', 'All Dynamic', 'Dynamic + Static', 'Dynamic + Static'],
    'Value': [50.41, 74.92, 51.87, 75.77]
}
df = pd.DataFrame(data)

# 创建 FontProperties 对象并设置字体
font = FontProperties(size=14)
# 创建一个小图形
plt.figure(figsize=(5, 3))

# 绘制柱状图
ax = sns.barplot(width=0.5, edgecolor='black', x='Model', y='Value', hue='Type', data=df, palette={'All Dynamic': '#81B8DF', 'Dynamic + Static': '#FA7F6F'})  # #81B8DF #82B0D2

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# 添加标题和标签
ax.set_xlabel('', x=0.5, fontdict={'size': 16})
plt.ylabel('Performance(%)', fontdict={'size': 16})
plt.xticks(size = 16)
plt.yticks(size = 14)

# 设置纵坐标数值范围
ax.set_ylim(45, 80)

ax.patches[0].set_x(ax.patches[0].get_x() - 0.03)
ax.patches[1].set_x(ax.patches[1].get_x() - 0.03)
ax.patches[2].set_x(ax.patches[2].get_x() + 0.03)
ax.patches[3].set_x(ax.patches[3].get_x() + 0.03)

# 在柱子上标上数值
for p in ax.patches:
    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontproperties=font)

# 删除默认的图例标题
ax.legend(title='', prop={'size': 12})

# 调整子图布局以使其适合更小的尺寸
plt.subplots_adjust(left=0.17, right=0.93, top=0.9, bottom=0.2, wspace=0.1)

plt.savefig("bart.png")