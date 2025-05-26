import matplotlib.pyplot as plt
import numpy as np

# Define new category names and results
category_names = ['Strongly disagree', 'Disagree',
                'Neither agree nor disagree', 'Agree', 'Strongly agree']
results = {
'1': [15, 20, 25, 30, 10],
'2': [10, 25, 30, 20, 15],
'3': [5, 15, 40, 25, 15],
'4': [20, 10, 15, 35, 20],
'5': [25, 30, 10, 15, 20],
'6': [10, 20, 30, 25, 15],
'7': [5, 10, 35, 30, 20],
'8': [15, 25, 20, 25, 15],
'9': [10, 15, 25, 30, 20],
'10': [20, 10, 15, 25, 30]
}

labels = list(results.keys())
data = np.array(list(results.values()))
data_cum = data.cumsum(axis=1)

# Define uncommon colors
category_colors = ['navy', 'blue', 'steelblue', 'royalblue', 'deepskyblue']  # Purple, Pink, Green, Orange, Cyan

fig, ax = plt.subplots(figsize=(12, 8))
ax.invert_yaxis()
ax.xaxis.set_visible(False)
ax.set_xlim(0, np.sum(data, axis=1).max())

for i, (colname, color) in enumerate(zip(category_names, category_colors)):
    widths = data[:, i]
    starts = data_cum[:, i] - widths
    rects = ax.barh(labels, widths, left=starts, height=0.5,
                    label=colname, color=color)

    text_color = 'white'
    ax.bar_label(rects, label_type='center', color=text_color, fontsize=15)

# Increase x and y ticks size
ax.tick_params(axis='y', which='major', labelsize=15, length=8, width=1.5)

# Add legend with larger font size
ax.legend(ncols=len(category_names), bbox_to_anchor=(0.5, -0.1), loc='lower center', fontsize=15)

# Add grid
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7, axis='x')

# Add title and labels
ax.set_title("Survey Results: Detailed Analysis", fontsize=25, fontweight='bold', pad=10)
ax.set_ylabel("Questions", fontsize=20, labelpad=10)

plt.tight_layout()
# Save the figure
plt.savefig('complex_survey_results.png', dpi=300, bbox_inches='tight')