import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# 给定的数据
satisfaction_scores = {
    "2016": [3.5, 3.7, 4.0, 3.9, 4.1, 3.8, 3.6, 3.9, 3.8, 4.2, 3.7, 3.9, 4.0, 3.6, 3.8, 4.1, 3.9, 4.0, 4.3, 3.7],
    "2017": [3.9, 4.1, 4.3, 4.6, 4.4, 4.2, 4.1, 4.3, 4.2, 4.5, 4.1, 4.3, 4.2, 4.4, 4.5, 4.7, 4.3, 4.2, 4.4, 4.6],
    "2018": [4.6, 4.7, 4.8, 4.5, 4.7, 4.9, 4.7, 4.8, 4.9, 5.0, 4.6, 4.8, 4.7, 4.9, 5.1, 5.0, 4.8, 4.7, 4.9, 5.1],
    "2019": [5.2, 5.3, 5.1, 5.5, 5.4, 5.7, 5.3, 5.6, 5.4, 5.2, 5.5, 5.3, 5.6, 5.8, 5.7, 5.4, 5.6, 5.3, 5.5, 5.7],
    "2020": [5.8, 6.1, 6.0, 6.2, 6.4, 6.1, 6.3, 6.0, 6.4, 6.2, 6.0, 6.3, 6.2, 6.5, 6.4, 6.7, 6.3, 6.5, 6.4, 6.6]
}

# 定义颜色
colors = ['deepskyblue', 'dodgerblue', 'royalblue', 'blue', 'navy']

# 准备数据
years = []
scores = []
for year, score in satisfaction_scores.items():
    years += [year] * len(score)
    scores += score

# 创建数据框
df = pd.DataFrame({"Year": years, "Satisfaction Score": scores})

# 创建小提琴图
sns.violinplot(x="Year", y="Satisfaction Score", data=df, palette=colors)

# 设置图表标题
plt.title('Employee Satisfaction Levels Over Time')

# 调整布局并保存图像
plt.tight_layout()
plt.savefig("year_violin.png")