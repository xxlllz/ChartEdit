import matplotlib.pyplot as plt

# New and modified data
data = {'apple': 12, 'orange': 18, 'lemon': 8, 'lime': 22, 'grape': 25, 'banana': 30, 'kiwi': 16}
names = list(data.keys())
values = list(data.values())

# Create the figure with 3 subplots
fig, axs = plt.subplots(1, 3, figsize=(15, 6))

# Set a less common color palette for the plots
colors = ['#440154', '#3e4a89', '#31688e', '#26828e', '#1f9e89', '#35b779', '#aefc8f']

# Bar chart
axs[0].bar(names, values, color=colors, edgecolor='black')
axs[0].set_title('Bar Chart', fontsize=16)
axs[0].tick_params(axis='x', labelsize=14)  # Increase tick size for x-axis
axs[0].tick_params(axis='y', labelsize=14)  # Increase tick size for y-axis
axs[0].set_xticklabels(names, rotation=15, ha="center")  # Rotate x-axis ticks

# Scatter plot
axs[1].scatter(names, values, color=colors, s=100, edgecolors='black', alpha=0.7)
axs[1].set_title('Scatter Plot', fontsize=16)
axs[1].tick_params(axis='x', labelsize=14)  # Increase tick size for x-axis
axs[1].tick_params(axis='y', labelsize=14)  # Increase tick size for y-axis
axs[1].set_xticklabels(names, rotation=15, ha="center")  # Rotate x-axis ticks

# Line plot
axs[2].plot(names, values, marker='o', color=colors[0], markersize=8, linestyle='-', linewidth=2)
axs[2].set_title('Line Plot', fontsize=16)
axs[2].tick_params(axis='x', labelsize=14)  # Increase tick size for x-axis
axs[2].tick_params(axis='y', labelsize=14)  # Increase tick size for y-axis
axs[2].set_xticklabels(names, rotation=15, ha="center")  # Rotate x-axis ticks

# Set overall title and axis labels
fig.supxlabel('Fruit Types', fontsize=20)
fig.supylabel('Fruit Values', fontsize=20)

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])  # Adjust layout to avoid overlap with suptitle

# Show the plot
plt.savefig('multi3.png')