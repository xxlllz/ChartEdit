import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Define the confusion matrix
data = np.array([
    [0.36, 0.19, 0.19, 0, 0.04, 0.2, 0.017],
    [0, 0.99, 0, 0.005, 0, 0, 0],
    [0.015, 0, 0.95, 0, 0, 0.025, 0.005],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0.005, 0, 0, 0.99, 0, 0],
    [0.01, 0, 0.005, 0.025, 0, 0.96, 0],
    [0.025, 0, 0, 0, 0, 0, 0.97]
])

# Class labels
labels = ['unknown', 'AM-DSB', 'QAM64', 'CPFSK', 'GFSK', '8PSK', 'PAM4']

plt.figure(figsize=(10, 8))

# Create a heatmap
sns.heatmap(data, annot=True,  cmap='Blues',
            xticklabels=labels, yticklabels=labels, cbar=True)

# Label titles
plt.title('Confusion Matrix (SNR=0)')
plt.xlabel('Predicted label')
plt.ylabel('True label')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)

plt.tight_layout()
plt.savefig('triplet.png')