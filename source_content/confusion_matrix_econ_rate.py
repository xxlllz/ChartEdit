import matplotlib.pyplot as plt
import numpy as np

# Data for the confusion matrix
confusion_matrix = [
    [35, 22, 6],
    [30, 108, 14],
    [6, 4, 9]
]

fig, ax = plt.subplots()
cax = ax.matshow(confusion_matrix, cmap='Blues')

# Add colorbar
fig.colorbar(cax)

# Annotate each cell with the numeric value
for (i, j), val in np.ndenumerate(confusion_matrix):
    ax.text(j, i, f'{val}', ha='center', va='center', color='black')

# Set axis labels
ax.set_xticklabels([''] + ['good', 'poor', 'none'],rotation=45)
ax.set_yticklabels([''] + ['good', 'poor', 'none'])
ax.tick_params(axis='x', direction='out', length=3, width=1, labelsize=10, top=False, labeltop=False, bottom=True,labelbottom=True)

# Set axis titles
plt.xlabel('Annotator A')
plt.ylabel('Annotator B')

# Annotate each cell with the numerical value
for (i, j), val in np.ndenumerate(confusion_matrix):
    ax.text(j, i, f'{val}', ha='center', va='center', color='white' if confusion_matrix[i][j] > 100 else 'black')

# Set the title of the plot
plt.title('Economic Conditions Agreement Confusion Matrix')
plt.tight_layout()
plt.savefig("confusion_matrix_econ_rate.png")
