import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Sample data
data = np.array([[ 82, 6, 16, 1, 6],
                 [ 1, 21, 20, 3, 4],
                 [11, 19, 156, 4, 10],
                 [ 2, 6, 6, 9, 0],
                 [ 5, 4, 9, 2, 44]])

fig, ax = plt.subplots(figsize=(5, 4))

# Create heatmap
sns.heatmap(data, annot=False, fmt='d', cmap='plasma', ax=ax)  

# Annotate the heatmap
for i in range(data.shape[0]):
    for j in range(data.shape[1]):
        # Check if the value is 156, set deep blue color
        if data[i, j] > 80:
            ax.text(j + 0.5, i + 0.5, str(data[i, j]), 
                    color='blue', weight='bold', fontsize=18, ha='center', va='center')
        else:
            # Use yellow for other values
            ax.text(j + 0.5, i + 0.5, str(data[i, j]), 
                    color='yellow', weight='bold', fontsize=18, ha='center', va='center')

# Set labels with bold font
ax.set_xticklabels([0, 1, 2, 3, 4], rotation=0, fontsize=14, weight='bold')
ax.set_yticklabels([0, 1, 2, 3, 4], rotation=0, fontsize=14, weight='bold')
ax.set_xlabel('Predicted label', fontsize=16, weight='bold')
ax.set_ylabel('True label', fontsize=16, weight='bold')

# Customize colorbar label font size and make it bold
cbar = ax.collections[0].colorbar
cbar.ax.tick_params(labelsize=16, labelrotation=0, width=1.5)
cbar.set_ticks([0, 50, 100, 150])


plt.tight_layout()
plt.savefig('ar_ar_full_xlmt_classification_confusion_matrix.png')
plt.show()
