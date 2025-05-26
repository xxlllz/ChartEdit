import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap

# Sample data (as appearing in the heatmap)
data = np.array([
    [31.49, 7.67, 11.31, 9.02, 8.61, 8.08, 9.83, 5.79, 0.67, 3.50, 5.25, 5.92],
    [17.50, 13.46, 12.11, 8.61, 9.02, 9.56, 9.15, 5.25, 0.67, 3.23, 6.73, 7.13],
    [21.53, 8.61, 19.38, 9.83, 9.02, 10.09, 11.04, 6.73, 0.81, 3.36, 6.86, 5.25],
    [19.92, 8.34, 11.98, 15.34, 9.42, 9.83, 10.77, 5.65, 0.40, 2.69, 7.13, 6.73],
    [18.71, 7.40, 11.31, 9.15, 13.86, 7.40, 8.88, 5.92, 0.54, 2.56, 5.92, 6.46],
    [19.11, 7.27, 13.06, 9.69, 7.94, 16.55, 9.29, 6.33, 0.94, 2.29, 6.46, 5.79],
    [19.25, 8.48, 12.52, 9.15, 9.15, 8.61, 16.02, 6.06, 0.40, 2.96, 6.33, 6.59],
    [13.19, 5.52, 6.81, 7.00, 6.33, 7.00, 6.86, 10.90, 0.54, 2.29, 4.98, 5.79],
    [13.06, 4.58, 6.86, 5.11, 5.52, 5.79, 6.59, 3.90, 1.48, 1.75, 2.29, 3.23],
    [17.77, 7.81, 11.71, 9.56, 8.34, 9.02, 9.29, 6.46, 0.67, 8.08, 6.86, 5.79],
    [19.65, 8.21, 12.25, 9.29, 9.69, 9.56, 10.63, 6.19, 0.27, 3.50, 9.02, 6.59],
    [16.15, 7.81, 9.83, 7.67, 8.88, 7.67, 8.08, 4.71, 0.00, 3.36, 4.71, 9.29]
])

blue_to_red_cmap = LinearSegmentedColormap.from_list(
    "blue_to_red", ['#073467',
'#C5DFEC',
'#FBE6DA',
'#D7634F',
'#6E0220',], N=256
)
# Labels for the heatmap
edit_langs = ['EN', 'CS', 'DE', 'NL', 'ES', 'FR', 'PT', 'RU', 'TH', 'TR', 'VI', 'ZH']
test_langs = ['EN', 'CS', 'DE', 'NL', 'ES', 'FR', 'PT', 'RU', 'TH', 'TR', 'VI', 'ZH']
cbar_ticks = [20, 40, 60, 80, 100]
# Create the heatmap
plt.figure(figsize=(12, 10))
heatmap=sns.heatmap(data, annot=True, fmt=".2f", cmap=blue_to_red_cmap, xticklabels=test_langs, yticklabels=edit_langs, vmin=10, vmax=100, annot_kws={"size": 16, "weight": "bold","color":'w'},)
# 获取颜色条对象并设置刻度
colorbar = heatmap.collections[0].colorbar
colorbar.ax.tick_params(labelsize=20)
colorbar.set_ticks([20, 40, 60, 80, 100])  # 设置颜色条的刻度

# Labels and title with increased font size
plt.xlabel('Test Language', fontsize=20,fontweight='bold')
plt.ylabel('Edit Language', fontsize=20,fontweight='bold')
plt.title('Portability score of ALL(edit) -> ALL(test)', fontsize=22, fontweight='bold')

# Increase font size of tick labels
plt.xticks(fontsize=16,fontweight='bold')
plt.yticks(fontsize=16,fontweight='bold',rotation=360)

# Adjust the plot to fit
plt.tight_layout()
plt.savefig("por-xx2yy.png")
