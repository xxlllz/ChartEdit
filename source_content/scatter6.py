import matplotlib.pyplot as plt
import numpy as np

# Data
categories = ['harmless', 'grammarly correct', 
              'friendly', 'polite', 'interactive',
              'authoritative', 'funny', 'use rhetorical devices', 'complex word & sentence',
              'use supporting materials', 
              ]

x = np.arange(len(categories))

# Mock Data
human = [49, 51.5, 59.2, 49, 51, 49.8, 51.2, 10, 50.2, 51.2]
gpt4 = [10, 53, 52.5, 10, 53, 10, 50.5, 50.8, 51.0, 51.5]
llama = [51, 52.5, 67, 50.8, 54, 55, 49.8, 52, 51.5, 51]

# Plot
fig, ax = plt.subplots(figsize=(14, 6))
ax.scatter(x, human, color='skyblue', alpha=0.8, s=200, label='Human')
ax.scatter(x, gpt4, color='orange', alpha=0.7, s=200, label='GPT-4-Turbo')
ax.scatter(x, llama, color='green', alpha=0.7, s=200, label='LLaMA-2-70B-Chat')

# Horizontal Line
ax.axhline(50, color='red', linestyle='--', linewidth=2)

# X-axis
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=60, ha='right', fontsize=16, fontstyle='italic')
# Y-axis
ax.set_ylim(40, 80)# 修改纵坐标刻度
ax.set_yticks([40, 50, 60, 70, 80])
ax.set_yticklabels([40, 50, 60, 70, 80],fontsize=16)

# 开启网格，设置网格为实线、灰色、细线
ax.grid(True, linestyle='-', color='grey', linewidth=0.5)
ax.set_ylabel('Probability of Preferred (%)', fontsize=18)

# Legend
ax.legend(loc='upper right', fontsize=18, framealpha=0.5)

plt.tight_layout()
plt.savefig('scatter6.png')