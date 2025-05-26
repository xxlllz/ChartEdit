import matplotlib.pyplot as plt
import numpy as np

# 设置字体为 Serif
plt.rcParams['font.family'] = 'serif'
# Data
model_size = ['1B', '2B', '9B', '27B']
mean_score_text_only = [55, 64, 69, 74]
mean_score_mix_training = [46, 61, 66, 73]
x = np.arange(len(model_size))

# Plot
plt.figure(figsize=(5, 5))
plt.plot(x, mean_score_text_only, 's--', color='skyblue', label='text-only', markersize=10, linewidth=2)
plt.plot(x, mean_score_mix_training, 's--', color='red', label='mix-training', markersize=10, linewidth=2)

# Add details
plt.xticks(x, model_size, fontsize = 14,fontweight='bold')
plt.ylabel('Mean Score',fontsize = 16)
plt.xlabel('Model Size',fontsize = 16)
plt.ylim(40, 80)
plt.legend(loc='lower right',ncol=2,edgecolor='none',fontsize=12)

# Set the grid
plt.grid(True,  alpha=0.6,axis='y')
plt.tight_layout()
plt.savefig('tradeoff_law_mean_shadow.png')