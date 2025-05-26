import matplotlib.pyplot as plt
import numpy as np

# Data from the confusion matrix
matrix = np.array([
    [58, 9, 6, 2],
    [9, 59, 21, 5],
    [2, 17, 12, 0],
    [13, 10, 2, 9]
])

fig, ax = plt.subplots(figsize=(8,6))
cax = ax.matshow(matrix, cmap='Blues')

# Adding color bar
plt.colorbar(cax)

# Set axes labels
ax.set_xticklabels([''] + ['better', 'worse', 'same', 'none'],rotation=45)
ax.set_yticklabels([''] + ['better', 'worse', 'same', 'none'])
ax.tick_params(axis='x', direction='out', length=3, width=1, labelsize=10, top=False, labeltop=False, bottom=True,labelbottom=True)
# Set title
plt.title('Economic Direction Agreement Confusion Matrix')

# Loop over data dimensions and create text annotations.
for (i, j), val in np.ndenumerate(matrix):
    ax.text(j, i, f'{val}', ha='center', va='center', color='white' if matrix[i][j] > 50 else 'black')

# Rotate x-tick labels
plt.xticks(rotation=45, ha='right')

# Set axes labels
plt.xlabel('Annotator A')
plt.ylabel('Annotator B')

plt.tight_layout()
plt.savefig("confusion_matrix_econ_change.png")