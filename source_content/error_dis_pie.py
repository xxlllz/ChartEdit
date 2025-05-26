import matplotlib.pyplot as plt

# Data
labels = [
    'ValueError (61)', 
    'IndexError (9)', 
    'NameError (3)', 
    'AttributeError (4)', 
    'KeyError (5)', 
    'TypeError (14)', 
    'AssertionError (4)', 
    'SyntaxError (13)', 
    'RuntimeError (2)'
]
sizes = [61, 9, 3, 4, 5, 14, 4, 13, 2]
colors = [
    '#4682b4',  # Blue
    '#add8e6',  # Light Blue
    '#90ee90',  # Light Green
    '#f4a460',  # Sandy Brown
    '#ff6347',  # Tomato
    '#ffa07a',  # Light Salmon
    '#dda0dd',  # Plum
    '#dab3ff',  # Lavender
    '#b0c4de',  # Light Steel Blue
]

# Plot
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(
    sizes, 
    labels=labels, 
    colors=colors, 
    autopct=None, 
    startangle=150, 
    textprops={'fontsize': 12},
    wedgeprops={'edgecolor': 'white', 'linewidth': 1}  # Add white borders between segments
)

# Equal aspect ratio ensures the pie chart is a circle
ax.axis('equal')  

plt.tight_layout()
plt.savefig('error_dis_pie.png')
