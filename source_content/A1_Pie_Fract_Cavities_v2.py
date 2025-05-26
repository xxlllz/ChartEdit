import matplotlib.pyplot as plt

# Data to plot
labels = ['1 cavity', '2 cavities', '3 cavities', '4 cavities']
sizes = [52.2, 28.7, 14.7, 4.4]

# Lighter colors by using more white in the RGB values
colors = ['lightcoral', 'lightpink', 'thistle', 'lightblue']  # Lighter shades of the original colors

# Plot pie chart
plt.figure(figsize=(8, 7))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=180,
        wedgeprops={'edgecolor': 'black', 'linewidth': 2},
        textprops={'fontsize': 18})  # Increase font size for labels

# Add title with larger font and move it up
plt.title('TNG-Cluster, 105 clusters with X-ray cavities\n233 X-ray cavities in total', fontsize=15, y=1.05)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Save the pie chart to file
plt.savefig('A1_Pie_Fract_Cavities_v2.png')
