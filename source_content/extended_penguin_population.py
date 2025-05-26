import matplotlib.pyplot as plt
import numpy as np

# Extended species and counts data
species = ('Adelie', 'Chinstrap', 'Gentoo', 'Macaroni', 'King', 'Rockhopper')  # Added new species
sex_counts = {
    'Male': np.array([80, 50, 90, 110, 150, 120]),  # Extended counts with new species
    'Female': np.array([75, 45, 70, 100, 140, 110]),  # Extended counts with new species
    'Unknown': np.array([23, 12, 31, 42, 63, 42])  # Added 'Unknown' category for new species
}

# Custom colors for each sex
colors = {
    'Male': 'royalblue',
    'Female': 'deepskyblue',
    'Unknown': 'navy',
}

width = 0.6  # Slightly wider bars to accommodate more data

# Create figure and axis
fig, ax = plt.subplots()

# Initialize bottom for stacked bars
bottom = np.zeros(len(species))

# Loop through the sex_counts to create stacked bars
for sex, sex_count in sex_counts.items():
    p = ax.bar(species, sex_count, width, label=sex, bottom=bottom, color=colors[sex])  # Use defined colors
    bottom += sex_count  # Update bottom for the stacked bars

# Customize the plot
ax.set_xlabel('Species', fontsize=14, fontweight='bold')
ax.set_ylabel('Population Count', fontsize=14, fontweight='bold')

# Increase tick font sizes
ax.tick_params(axis='x', labelsize=12)  # Increase font size for x-axis ticks
ax.tick_params(axis='y', labelsize=12)  # Increase font size for y-axis ticks

# Add a legend with a larger font size
ax.legend(title='Penguin Sex', fontsize=12, title_fontsize=14)

# Show the plot
plt.tight_layout()

# Save the figure
plt.savefig('extended_penguin_population.png')