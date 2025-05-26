import matplotlib.pyplot as plt

# Data
labels = ['ValueError (36)', 'IndexError (4)', 'NameError (3)', 'AttributeError (4)', 'RuntimeError (2)', 'KeyError (2)', 'TypeError (1)']
sizes = [36, 4, 3, 4, 2, 2, 1]
colors = ['#4682b4', '#add8e6', '#90ee90', '#f4a460', '#ff7f7f', '#ffb6c1', '#ffa07a']

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(sizes, labels=labels, colors=colors, autopct=None, startangle=150, textprops={'fontsize': 16})

# Equal aspect ratio ensures that pie is drawn as a circle
ax.axis('equal')  

plt.tight_layout()
plt.savefig('error_pie.png')