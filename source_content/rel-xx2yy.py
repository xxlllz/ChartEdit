import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

blue_to_red_cmap = LinearSegmentedColormap.from_list(
    "blue_to_red", ['#063264','#A0CCE2','#FAE7DC',"#DC6E57",'#67001F'], N=256
    )
# Data from the image
languages = ["EN", "CS", "DE", "NL", "ES", "FR", "PT", "RU", "TH", "TR", "VI", "ZH"]
data = np.array([
    [100.00, 75.10, 81.70, 72.68, 68.10, 73.35, 71.20, 62.58, 32.44, 70.79, 68.37, 54.78],
    [87.89, 99.87, 76.45, 69.04, 65.95, 66.35, 66.76, 62.05, 27.46, 63.53, 63.80, 49.13],
    [90.17, 68.64, 100.00, 72.01, 66.89, 68.51, 68.91, 60.03, 28.53, 64.20, 64.47, 51.41],
    [87.21, 68.64, 78.20, 99.87, 65.95, 69.18, 67.03, 59.62, 26.38, 62.05, 61.51, 49.39],
    [86.41, 69.45, 75.37, 69.72, 99.87, 71.74, 71.06, 60.97, 26.11, 63.12, 62.58, 51.14],
    [86.41, 69.31, 77.79, 69.85, 67.97, 99.73, 70.66, 62.31, 29.88, 63.53, 62.85, 50.07],
    [86.68, 68.78, 76.58, 68.78, 69.04, 69.45, 100.00, 60.83, 28.80, 62.31, 62.85, 53.03],
    [82.91, 62.58, 68.91, 61.10, 58.82, 62.45, 60.43, 99.60, 21.27, 55.45, 57.47, 45.63],
    [49.26, 23.69, 28.26, 24.63, 21.13, 23.28, 21.67, 17.77, 99.46, 19.92, 15.34, 9.96],
    [82.10, 60.97, 68.91, 61.64, 58.14, 58.82, 58.14, 53.97, 23.28, 99.73, 56.39, 42.66],
    [84.66, 67.16, 73.76, 67.29, 62.72, 63.26, 64.20, 58.55, 19.92, 62.05, 92.46, 48.86],
    [72.14, 51.95, 56.39, 48.99, 44.68, 47.51, 46.16, 41.86, 8.75, 40.38, 44.15, 93.27]
])

fig, ax = plt.subplots(figsize=(10, 10))
cax = ax.matshow(data, cmap=blue_to_red_cmap, vmin=10, vmax=100)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(languages)))
ax.set_yticks(np.arange(len(languages)))
ax.set_xticklabels(languages)
ax.set_yticklabels(languages)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=90, ha="center")

# Loop over data dimensions and create text annotations.
for i in range(len(languages)):
    for j in range(len(languages)):
        if data[i, j]<35 or data[i, j]>80 :
            ax.text(j, i, f'{data[i, j]:.2f}',
                    ha="center", va="center", color="w", fontsize=12,weight='bold')
        else:
            ax.text(j, i, f'{data[i, j]:.2f}',
                    ha="center", va="center", color="black", fontsize=12,weight='bold')

# Title and labels
plt.title("Reliability score of ALL(edit) -> ALL(test)", fontsize=22, fontweight='bold')
ax.set_xlabel('Test Language', fontsize=20,fontweight='bold')
ax.set_ylabel('Edit Language', fontsize=20,fontweight='bold')
ax.tick_params(axis='x', direction='out', length=3, width=1, labelsize=10, top=False, labeltop=False, bottom=True,labelbottom=True)
# Increase font size of tick labels
plt.xticks(fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold',rotation=360)

# Show the plot
plt.tight_layout()
plt.savefig('rel-xx2yy.png')
