import matplotlib.pyplot as plt

# Data
labels = ['Below 2000 ft', '2000-4000 ft', '4000-6000 ft', '6000-8000 ft', 'Above 8000 ft']
sizes = [15, 30, 25, 20, 10]
explode = (0, 0.1, 0, 0, 0)

colors = ['#ff7f7f', '#ffb6c1', '#90ee90', '#f4a460', '#4682b4']

plt.figure(figsize=(8, 6))
# Plot
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140, colors=colors)

# Equal aspect ratio ensures that pie is drawn as a circle
plt.axis('equal')

# Title with larger font size
plt.title('Mountain Landscape Elevation Distribution', fontsize=18)

# Increase the font size of the labels
plt.setp(plt.gca().texts, fontsize=14)

# Layout adjustment
plt.tight_layout()
plt.savefig("pie_1.png")