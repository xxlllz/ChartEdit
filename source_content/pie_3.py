import matplotlib.pyplot as plt

# Labels for the sections of our pie chart
labels = ["Good", "Fair", "Poor"]

# The values of each section of the pie chart for urban teenagers
sizes_urban_low = [40, 30, 30]
sizes_urban_moderate = [20, 50, 30]
sizes_urban_high = [10, 40, 50]

# The values of each section of the pie chart for rural teenagers
sizes_rural_low = [50, 25, 25]
sizes_rural_moderate = [30, 35, 35]
sizes_rural_high = [15, 20, 65]

colors = ["#ffcccc", "#d3d3d3", "#add8e6"]
# Creating explode data
explode = (0.1, 0, 0)

# Create pie charts
fig, axs = plt.subplots(2, 3, figsize=(12, 8))  # Adjusted size for clarity

# Pie chart for Urban - Low Usage
axs[0, 0].pie(sizes_urban_low, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
axs[0, 0].set_title('Urban - Low Usage', fontsize=16)

# Pie chart for Urban - Moderate Usage
axs[0, 1].pie(sizes_urban_moderate, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
axs[0, 1].set_title('Urban - Moderate Usage', fontsize=16)

# Pie chart for Urban - High Usage
axs[0, 2].pie(sizes_urban_high, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
axs[0, 2].set_title('Urban - High Usage', fontsize=16)

# Pie chart for Rural - Low Usage
axs[1, 0].pie(sizes_rural_low, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
axs[1, 0].set_title('Rural - Low Usage', fontsize=16)

# Pie chart for Rural - Moderate Usage
axs[1, 1].pie(sizes_rural_moderate, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
axs[1, 1].set_title('Rural - Moderate Usage', fontsize=16)

# Pie chart for Rural - High Usage
axs[1, 2].pie(sizes_rural_high, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'fontsize': 14})
axs[1, 2].set_title('Rural - High Usage', fontsize=16)

# Helps to keep the shape of pie as circle
plt.axis("equal")

# Adjust layout to make room for the table
plt.subplots_adjust(left=0.0, bottom=0.1, right=0.9)

# Make sure the layout is tight
plt.tight_layout()

# Save the figure
plt.savefig("pie_3.png")