import matplotlib.pyplot as plt
import numpy as np

# Data for the confusion matrix
confusion_matrix = np.array([
    [165, 14, 65],
    [14, 243, 59],
    [37, 38, 163]
])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the heatmap
cax = ax.matshow(confusion_matrix, cmap='Blues')

# Add a colorbar
plt.colorbar(cax)

# Set axis labels
ax.set_xlabel('Annotator A')
ax.set_ylabel('Annotator B')

# Set axis ticks
ax.set_xticks([0, 1, 2])
ax.set_yticks([0, 1, 2])

# Set tick labels
ax.set_xticklabels(['pos', 'neg', 'neutral'] ,rotation=45, ha='center')
ax.set_yticklabels(['pos', 'neg', 'neutral'])
ax.tick_params(axis='x', direction='out', length=3, width=1, labelsize=10, top=False, labeltop=False, bottom=True,labelbottom=True)

# Set title
plt.title('+/- Agreement Confusion Matrix')

# Annotate each cell with the numerical value
for (i, j), val in np.ndenumerate(confusion_matrix):
    ax.text(j, i, f'{val}', ha='center', va='center', color='white' if confusion_matrix[i, j] > 120 else 'black')

plt.tight_layout()
plt.savefig("confusion_matrix_spin.png")