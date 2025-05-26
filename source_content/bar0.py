import matplotlib.pyplot as plt
import numpy as np

# Labels for the different weather conditions
# labels = ['Snow', 'Fog', 'Rain', 'Clean']
labels = ['Clean', 'Rain', 'Fog', 'Snow']
# Success values for the three models
success_values = {
    'DRCT': [49.36, 58.25, 51.22, 75.3][::-1],
    'Siamese': [47.08, 62.24, 48.28, 74.3][::-1],
    'MBPTrack': [47.48, 57.02, 48.71, 73.7][::-1],
}

# Precision values for the three models
precision_values = {
    'DRCT': [58.23, 68.29, 60.9, 86.33][::-1],
    'Siamese': [57.03, 73.4, 58.5, 85.8][::-1],
    'MBPTrack': [56.49, 67.4, 58.16, 85.22][::-1],
}

# X-axis positions
x = np.arange(len(labels))

# Bar width
width1 = 0.25  # Increase this value if you want wider bars

# Create the figure and axis
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting the success values (shifted to the left, using negative values for the left axis)
ax.barh(x + width1+0.06, -np.array(success_values['MBPTrack']), height=width1, label='MBPTrack', color='deepskyblue',edgecolor = 'deepskyblue',lw=3)
ax.barh(x, -np.array(success_values['Siamese']), height=width1, label='Siamese', color='lightgreen',edgecolor = 'lightgreen',lw=3)
ax.barh(x - width1-0.06, -np.array(success_values['DRCT']), height=width1, label='DRCT', color='peachpuff',edgecolor = 'peachpuff',lw=3)
# Plotting the precision values (shifted to the right, positive values)
ax.barh(x - width1 -0.06, precision_values['DRCT'], height=width1,  color='white', alpha=1,edgecolor = 'peachpuff',lw=3)
ax.barh(x, precision_values['Siamese'], height=width1, color='white', alpha=1,edgecolor = 'lightgreen',lw=3)
ax.barh(x + width1 +0.06, precision_values['MBPTrack'], height=width1, color='white', alpha=1,edgecolor = 'deepskyblue',lw=3)

# Set labels for the y-axis and x-ticks
# ax.set_ylabel('Weather Conditions')
ax.set_xticks(np.arange(-100, 101, 20))  # X-axis with negative and positive range
ax.set_xticklabels([])

# Set y-ticks and y-tick labels
ax.set_yticks(x)
ax.set_yticklabels(labels)

# Set title
ax.set_title('Success Precision ', fontsize=18)

# Adding annotations to the bars
for i, label in enumerate(labels):
    for j, (model, value) in enumerate(success_values.items()):
        ax.annotate(f'{value[i]:.2f}', xy=(-value[i]-3, i + (j - 1) * width1), xytext=(-3, 0), textcoords='offset points', ha='right', va='center')
    for j, (model, value) in enumerate(precision_values.items()):
        ax.annotate(f'{value[i]:.2f}', xy=(value[i]+3, i + (j - 1) * width1), xytext=(3, 0), textcoords='offset points', ha='left', va='center')


ax.spines['top'].set_visible(True)
ax.spines['top'].set_color('silver')
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.tick_params(axis='both', which='both', bottom=False, top=False, left=False, right=False, labelbottom=False, labelleft=True)

# Add legend
ax.legend(loc='upper center', ncol=3, bbox_to_anchor=(0.5, -0.1),edgecolor='none',fontsize=20,handlelength=0.5,handleheight=0.5)

ax.axvline(x=0, color='silver', linestyle='-', linewidth=2,)
# 添加多条横线
ax.axhline(y=0.5, color='silver', linestyle='-', linewidth=1)
ax.axhline(y=1.5, color='silver', linestyle='-', linewidth=1)
ax.axhline(y=2.5, color='silver', linestyle='-', linewidth=1)
# ax.axhline(y=3.5, color='silver', linestyle='-', linewidth=1)
# Show plot
plt.tight_layout()
plt.savefig('bar0.png')
