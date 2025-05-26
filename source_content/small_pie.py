import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
# Data for the pie charts
labels = ['Correct', 'Incorrect', 'Neither', 'Overlapped', 'Captioned']
sizes_distinct = [37, 23, 30, 3, 7]  # Example data for Distinct
sizes_disparate = [33, 13, 32, 9, 13]  # Example data for Disparate
colors = ['#300E4E','#354283','#246EAC', '#0092C8', '#0CC0DF']
colors1 = ['#0CC0DF','#0092C8','#0092C8','#354283','#300E4E',]
# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(7.5, 4.5))

# Plot the 'Distinct' pie chart in the first subplot
axs[0].pie(sizes_distinct, labels=None, colors=colors,startangle=90)
axs[0].set_title('Distinct', fontsize=28, pad=0)
axs[0].axis('equal')

# Plot the 'Disparate' pie chart in the second subplot
axs[1].pie(sizes_disparate, labels=None, colors=colors,startangle=90)
axs[1].set_title('Disparate', fontsize=28, pad=0)
axs[1].axis('equal')

# Set a common legend
# Create custom legend handles with circle markers
legend_handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=14) 
                  for color in colors1]
# Add a legend
plt.legend(legend_handles,labels, loc='lower center', bbox_to_anchor=(-0.1, -0.15), ncol=5,facecolor='none',edgecolor='none',fontsize=14,handlelength=0.5, handletextpad=0.5)

# Layout adjustment
plt.subplots_adjust()
plt.tight_layout(pad=20)
plt.savefig('small_pie.png')