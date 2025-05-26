import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data for demonstration
accuracy = np.array([
    [100.0, 100.0, 99.87, 99.87, 99.87, 100.0, 100.0, 99.47, 99.87, 99.87, 99.87, 97.85],
    [100.0, 99.87, 99.73, 99.87, 99.87, 99.87, 99.87, 99.6, 100.0, 99.6, 99.87, 97.85],
    [99.87, 99.87, 100.0, 99.87, 99.87, 99.87, 99.87, 99.33, 99.59, 99.46, 99.73, 97.31],
    [99.87, 99.73, 99.87, 99.87, 99.87, 99.6, 99.87, 99.46, 99.87, 99.46, 99.46, 97.58],
    [99.87, 99.87, 99.60, 99.87, 99.87, 100.0, 99.87, 99.19, 99.87, 99.73, 99.87, 97.98],
    [100.0, 99.73, 99.73, 99.60, 100.00, 99.73, 99.87, 99.19, 99.86, 99.87, 99.73, 98.12],
    [100.0, 99.73, 99.87, 99.87, 99.87, 99.87, 100.0, 99.6, 99.87, 99.6, 99.87, 97.85],
    [99.47, 99.46, 99.33, 99.19, 99.87, 99.46, 99.73, 99.6, 99.73, 99.19, 99.06, 96.90],
    [99.87, 99.6, 99.6, 99.32, 99.73, 100.0, 99.73, 99.06, 99.73, 99.46, 99.33, 97.17],
    [99.87, 99.33, 99.46, 99.73, 99.6, 99.46, 99.6, 99.19, 99.46, 100.0, 99.73, 97.31],
    [99.87, 99.6, 99.73, 99.6, 99.6, 99.6, 99.73, 98.79, 99.87, 99.6, 99.73, 97.44],
    [97.85, 96.1, 97.04, 96.77, 96.37, 96.5, 96.5, 94.48, 97.31, 96.77, 97.58, 99.87]
])

langs = ['EN', 'CS', 'DE', 'NL', 'ES', 'FR', 'PT', 'RU', 'TH', 'TR', 'VI', 'ZH']

# Plotting the heatmap
plt.figure(figsize=(12, 9))
heatmap = sns.heatmap(accuracy, annot=True, fmt='.2f', cmap='Reds', xticklabels=langs, yticklabels=langs,
                      vmin=90, annot_kws={"size": 12, "weight": "bold"}, vmax=100)

# Modify colorbar
colorbar = heatmap.collections[0].colorbar
colorbar.set_ticks([90, 92, 94, 96, 98, 100])  # Set colorbar ticks

# Increase font size for colorbar ticks
colorbar.ax.tick_params(labelsize=18, labelcolor='black')  # Increase font size of colorbar ticks

# Aesthetic improvements
plt.title('Multilingual Retriever Accuracy', fontsize=18, fontweight='bold')
plt.xlabel('Test Languages', fontsize=18, fontweight='bold')
plt.ylabel('Edit Languages', fontsize=18, fontweight='bold')
plt.xticks(fontsize=16, fontweight='bold')
plt.yticks(fontsize=16, fontweight='bold', rotation=360)
plt.tight_layout()
plt.savefig("retriever-acc.png")