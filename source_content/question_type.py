import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
# Data
labels = ['Purpose', 'Arg0', 'Time', 'Instrument', 'Location']
# labels1 = ['Location', 'Arg0', 'Time','Instrument','Purpose',]
sizes = [35,9,11,31,15]
colors = ['#7E1E1F','#AF6125','#F1C181','#646D43','#4E606E',]
colors1 = ['#4E606E','#646D43','#F1C181','#AF6125','#7E1E1F',]
# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(sizes, colors=colors, startangle=90, autopct='%1.0f%%',textprops={'fontsize': 12, 'color': 'white'})


# Create custom legend handles with circle markers
legend_handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=14) 
                  for color in colors1]
# Add a legend
plt.legend(legend_handles,labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=5,facecolor='none',edgecolor='none',fontsize=12)

plt.tight_layout()
plt.savefig('question_type.png')