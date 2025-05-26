import matplotlib.pyplot as plt

# Pie chart labels
labels = ['18-24', '25-34', '35-44', '45-54', '55 and above']

# Sizes for each slice
sizes = [25, 20, 15, 10, 5]

# Screen time for each age group
screen_time = ['4-6 hours', '6-8 hours', '8-10 hours', '10-12 hours', '>12 hours']

# Colors for the pie chart slices
colors = ['#ff7f7f', '#90ee90', '#f4a460', '#4682b4', '#ffb6c1']

# Creating pie chart
fig1, ax1 = plt.subplots(figsize=(8, 6))
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors, textprops={'fontsize': 18})

# Equal aspect ratio ensures that pie is drawn as a circle
ax1.axis('equal')  

# Additional information in the form of screen time included using legend with modified font size and moved position
plt.legend(screen_time, title="Daily screen time", loc="upper left", bbox_to_anchor=(1, 1), fontsize=15)

# Increase the font size of the labels
plt.setp(ax1.texts, fontsize=16)

plt.tight_layout()
plt.savefig("pie_2.png")