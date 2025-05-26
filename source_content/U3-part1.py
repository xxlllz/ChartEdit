import matplotlib.pyplot as plt
import numpy as np

# Data
categories = [ 'Naturalness','Appropriateness',]
values_remodiffuse = [39.3,41.1]
values_retrieval = [60.7,58.9]

# Bar width
bar_width = 0.4

# Positions of bars on y-axis
y_pos = np.arange(len(categories))*0.5

plt.figure(figsize=(6,2))
# Create bars
plt.barh(y_pos, values_remodiffuse, color='#cfebff', edgecolor='none', height=bar_width, label='ReMoDiffuse')
plt.barh(y_pos, values_retrieval, color='#f4c3c2', edgecolor='none', height=bar_width, left=values_remodiffuse, label='ReMoDiffuse + Our Retrieval')

# Add data labels
for i, (v1, v2) in enumerate(zip(values_remodiffuse, values_retrieval)):
    plt.text(v1 / 2, y_pos[i], f'{v1:.1f}%', ha='left', va='center', color='black', fontsize=12, fontweight='bold')
    if i == 1:
        plt.text(v1 + v2 / 2, y_pos[i], f'{v2:.1f}%', ha='left', va='center', color='black', fontsize=12, fontweight='bold')
    else:
        plt.text(v1 + v2 / 2, y_pos[i], f'{v2:.1f}%*', ha='left', va='center', color='black', fontsize=12, fontweight='bold')

# Y-axis labels
plt.yticks(y_pos, categories, fontsize=15)
plt.xticks([0, 20, 40, 60, 80, 100],["0%","20%","40%","60%","80%","100%"])

# Add legend
plt.legend(fontsize=10, loc='upper center', bbox_to_anchor=(0.3, 1.5), ncol=2,edgecolor='none')

# 调整布局，确保图例不被裁剪
plt.subplots_adjust(top=0.6)  # 为顶部的图例留出空间
# X-axis label
plt.xlabel('Percentage Preference (%)', fontsize=15, fontweight='bold')

# Adjust layout for better display
plt.xlim([0, 100])
plt.tight_layout()

# Show plot
plt.savefig('U3-part1.png')