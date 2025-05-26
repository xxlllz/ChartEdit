import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Fruits data with modified counts and colors
fruits = ['apple', 'blueberry', 'cherry', 'orange', 'kiwi']
counts = [45, 120, 35, 65, 80]  # Modified counts
bar_labels = ['red', 'blue', 'pink', 'orange', 'green']  # New labels with a more varied color scheme

# New, more harmonious color scheme
bar_colors = ['#FF6347', '#4682B4', '#FF69B4', '#FFA07A', '#32CD32']  # More complementary colors
bar_edge_colors = ['#B22222', '#5A5A5A', '#C71585', '#FF8C00', '#228B22']  # Border colors for the bars

# Create bar plot with edgecolors for the borders
bars = ax.bar(fruits, counts, color=bar_colors, edgecolor=bar_edge_colors, linewidth=2)

# Customize the labels and title
ax.set_ylabel('Fruit supply', fontsize=14)
ax.set_title('Fruit supply by kind and color', fontsize=16)

# Customize x and y ticks with larger font size
ax.tick_params(axis='x', labelsize=12)  # Increase font size for x-axis ticks
ax.tick_params(axis='y', labelsize=12)  # Increase font size for y-axis ticks

# Show the plot
plt.tight_layout()

# Save the figure
plt.savefig('fruitbar.png')