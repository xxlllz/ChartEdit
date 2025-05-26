import matplotlib.pyplot as plt

# Data for each pie chart
labels = ['Close Book', 'Parameter', 'Wikipedia', 'SERP']
colors = ['#99CCFF', '#FFCC80', '#99CC99', '#FF9999']

hotpotqa = [22.1, 22.4, 26.3, 29.2]
musiQue = [24.0, 12.2, 25.1, 38.6]
wikiMQA = [13.6, 19.2, 34.0, 33.3]
bamboogle = [27.4, 32.7, 11.4, 28.6]

datasets = [hotpotqa, musiQue, wikiMQA, bamboogle]
titles = ['HotpotQA', 'MuSiQue', '2WikiMQA', 'Bamboogle']

fig, axes = plt.subplots(ncols=4, figsize=(12, 4))  # Create a figure with 4 subplots

for ax, data, title in zip(axes, datasets, titles):
    wedges, texts, autotexts = ax.pie(
        data,  autopct='%1.1f%%', startangle=90, colors=colors,wedgeprops={'edgecolor': 'white', 'linewidth': 2,},radius=1.2
    )
    ax.set_title(title, fontsize=24, fontweight='bold')
    # Customize the annotation appearance
    for autotext in autotexts:
        autotext.set_color('black')
        autotext.set_fontsize(18)
        autotext.set_alpha(0.7)

fig.legend(labels,  loc='lower center',fontsize=19, ncol=4)
plt.tight_layout()
plt.savefig('pie0.png')
