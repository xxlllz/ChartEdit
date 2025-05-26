import matplotlib.pyplot as plt
import numpy as np

# Define the categories (axes of the radar chart)
labels = [
    'ChartX-Description', 'ChartX-Redrawing', 'ChartQA', 'Chart-to-Text', 
    'OpenCQA', 'Chart-to-Table', 'ChartX-QA', 'ChartX-Summary',
]

# Model data
data = {
    "Llava1.5-13B": [1.29, 0.73, 55.32, 7.16, 0, 0, 17.19, 1.45],
    "ChartInstruct-7B": [0, 0, 66.64, 12.92, 15.59, 0, 0, 0],
    "ChartInstruct-13B": [1.02, 0.94, 69.66, 14.23, 0, 90, 13.8, 1.04],
    "ChartAst-13B": [1.02, 0.73, 79.9, 15.5, 15.5, 91.6, 30.99, 0.33],
    "TinyChart-3B": [1.64, 1.89, 83.6, 17.18, 20.39, 93.78, 33.35, 1.58],
}

# Normalize the data for each axis
normalized_data = {}
for model, values in data.items():
    normalized_data[model] = [
        values[i] / max(data[other_model][i] for other_model in data) for i in range(len(values))
    ]
          
# Number of variables (axes)
num_vars = len(labels)

# Compute angle for each category
angles = np.linspace(- 2 * np.pi,0, num_vars, endpoint=False).tolist()

# Make the plot close to a circle
angles += angles[:1]

# Create the plot
fig, ax = plt.subplots(figsize=(12, 8), subplot_kw=dict(polar=True))

# Create colors for each model
colors = ['blue', 'green', 'orange', 'red', 'lightblue']

for model, values, color in zip(normalized_data.keys(), normalized_data.values(), colors):
    values += values[:1]  # To close the circle
    ax.plot(angles, values, label=model, color=color,linewidth=1)
    ax.fill(angles, values, color=color, alpha=0.25)  # Fill area under the curve
    # Add original data values around each point
    for i in range(len(values) - 1):  # Exclude the last point as it's a repeat of the first
        if data[model][i]!=0:
            ax.text(angles[i], values[i] + 0.05, f'{data[model][i]}', ha='center', fontsize=10, color='black')


# Set the labels and title
ax.set_yticklabels([])  # Hide radial ticks

# Adjusting the labels with custom horizontal alignment
label_alignments = ['left', 'left', 'center', 'right', 'right', 'right', 'center', 'left']

# Dynamically adjust the alignment (ha and va) based on the angle
for i, label in enumerate(labels):
    angle = angles[i]  # Angle for the label
    ha = label_alignments[i]  # Get the horizontal 
    va = 'center'
    ax.text(angle, 1.1, label, ha=ha, va=va, fontsize=16)

ax.set_xticks(angles[:-1])  # This creates the 8 axes for the octagon shape
ax.set_xticklabels([])
ax.tick_params(axis='x', pad=10)  # Label distance from 
ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray')  # Enable grid lines with custom style
# Add a legend
plt.legend(loc='lower right', bbox_to_anchor=(1.4, -0.13), fontsize=12,handlelength=1.5,handleheight=1, handletextpad=-10.8,facecolor='none',edgecolor='none')
ax.spines['polar'].set_visible(False)

# Show the plot
plt.tight_layout()
# Save the figure before showing it
plt.savefig('Radar_Chart2.png')
