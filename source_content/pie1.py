import matplotlib.pyplot as plt

# Labels, sizes, and colors for each category
labels = [
    'Object', 'Animal', 'Food', 'Plant', 'Vehicle', 'Clothing', 'Profession', 
    'Material', 'Instrument', 'Place', 'Bird', 'Sport', 'Building', 
    'Furniture', 'Celestial', 'Mythical', 'Other'
]
sizes = [20.2, 17.1, 16.7, 8.6, 3.7, 3.3, 3.1, 2.8, 2.7, 2.1,2.1,  2.0, 1.8, 1.8,  1.7, 1.6, 8.6]
colors = [
    '#3e7fbd', '#71acd6', '#a1c9e1', '#c8daef', '#e25a14', '#f9913e', '#fab16c',
    '#fad2a2', '#32a453', '#74c576', '#a0da9b', '#c7eac0', '#7868b1', 
    '#a099c8', '#bdbcdc', '#dbdaeb', '#636363'
]
# Create the pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes,labels=labels, colors=colors, 
        autopct='%1.1f%%', startangle=135, pctdistance=0.85)

# Equal aspect ratio ensures that pie is drawn as a circle.
plt.axis('equal')
plt.title('Category Distribution of Things dataset', fontsize = 18)
plt.tight_layout()
plt.savefig('pie1.png')



