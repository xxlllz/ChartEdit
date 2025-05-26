import matplotlib.pyplot as plt
import numpy as np

# Data
labels_a = ['Harder', 'Easier', 'Equal']
sizes_a = [22.25, 47.25, 30.5]
colors_a = ['#A7A7FF', '#9AD2FF', '#C1C5FF']

labels_b = ['Generated', 'Original', 'Equal']
sizes_b = [53, 39, 8]
colors_b = ['#E2AD51', '#F83261', '#D76F46']

# Explode effect to make certain slices more prominent
explode_a = (0.05, 0.05, 0.05)  # Explode 'Harder' and 'Easier' in the first chart
explode_b = (0.05, 0.05, 0.05)    # Explode 'Generated' in the second chart

# Create figure and axes
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

# Plot the first donut chart (Manual Difficulty Comparison)
wedges_a, texts_a, autotexts_a = axs[0].pie(sizes_a, labels=labels_a, autopct='%1.2f%%', startangle=90, colors=colors_a,
                                            wedgeprops={'width': 0.4, 'edgecolor': 'white'}, explode=explode_a)

# Plot the second donut chart (Manual Image-text Matching Comparison)
wedges_b, texts_b, autotexts_b = axs[1].pie(sizes_b, labels=labels_b, autopct='%1.2f%%', startangle=150, colors=colors_b,
                                            wedgeprops={'width': 0.4, 'edgecolor': 'white'}, explode=explode_b)

# Adjust the position of text to avoid overlap and move them to a new location
# Position the percentage text for the first donut chart (Manual Difficulty Comparison)
for i, autotext in enumerate(autotexts_a):
    autotext.set_color(colors_a[i])  # Set the color of the percentage text to match the segment color
    autotext.set_fontsize(12)  # Make text larger
    autotext.set_fontweight('bold')  # Make the text bold
    # Move the text outward and adjust the X and Y position
    angle = (wedges_a[i].theta1 + wedges_a[i].theta2) / 2  # Get the midpoint angle of the slice
    x_offset = 0.4 * np.cos(np.radians(angle))  # Move outward based on the angle (X direction)
    y_offset = 0.4 * np.sin(np.radians(angle))  # Move outward based on the angle (Y direction)
    autotext.set_position((x_offset, y_offset))  # Apply the new position

# Position the percentage text for the second donut chart (Manual Image-text Matching Comparison)
for i, autotext in enumerate(autotexts_b):
    autotext.set_color(colors_b[i])  # Set the color of the percentage text to match the segment color
    autotext.set_fontsize(12)  # Make text larger
    autotext.set_fontweight('bold')  # Make the text bold
    # Move the text outward and adjust the X and Y position
    angle = (wedges_b[i].theta1 + wedges_b[i].theta2) / 2  # Get the midpoint angle of the slice
    x_offset = 0.4 * np.cos(np.radians(angle))  # Move outward based on the angle (X direction)
    y_offset = 0.4 * np.sin(np.radians(angle))  # Move outward based on the angle (Y direction)
    autotext.set_position((x_offset, y_offset))  # Apply the new position

# Adjust label text size and make them bold
for text in texts_a:
    text.set_fontsize(12)  # Increase font size for category labels
    text.set_fontweight('bold')  # Make the category labels bold

for text in texts_b:
    text.set_fontsize(12)  # Increase font size for category labels
    text.set_fontweight('bold')  # Make the category labels bold

# Adjust layout to avoid overlap of labels and text
plt.tight_layout()

# Save the plot
plt.savefig('manual_comparison.png')