import matplotlib.pyplot as plt
import numpy as np

categories = ['Regular', 'Upside-Down']
models = ['Gemini-1.5', 'GPT4-Omni', 'GPT4-Turbo', 'ResNet', 'ViT', 'Swin', 'Humans']
values = {
    'Gemini-1.5': [46, 46],
    'GPT4-Omni': [38, 31],
    'GPT4-Turbo': [51, 39],
    'ResNet': [66, 38],
    'ViT': [60, 40],
    'Swin': [67, 35],
    'Humans': [78, 79]
}
errors = {
    'Gemini-1.5': [6, 7],
    'GPT4-Omni': [6, 8],
    'GPT4-Turbo': [4, 7],
    'ResNet': [4, 6],
    'ViT': [5, 6],
    'Swin': [4, 5],
    'Humans': [4, 6]
}

colors = ['royalblue', 'lightsteelblue', 'deepskyblue', 'firebrick', 'chocolate', 'darkorange', 'lightgreen']

x = np.arange(len(categories))  # the label locations
width = 0.1  # the width of the bars
sep_width = 0.02
fig, ax = plt.subplots(figsize=(12, 6))

# Plotting bars with lightened colors and gray error bars
for i, model in enumerate(models):
    ax.bar(x + i * (width + sep_width), values[model], width, label=model, yerr=errors[model],
           capsize=8, color=colors[i], edgecolor='none', ecolor='gray', linestyle='-', 
           zorder=3, error_kw={'linewidth': 2})  # Increase error bar line thickness

# Adding a horizontal line for 'Random Guess'
ax.axhline(50, color='black', linestyle='--', linewidth=1, label='Random Guess', zorder=4)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Accuracy (%)', fontsize=20)
ax.set_xticks(x + (width + sep_width) * 3)
ax.set_xticklabels(categories, fontsize=20)
ax.legend(loc='upper left', bbox_to_anchor=(1.0, 0.8), fontsize=20)

# Increase the y-axis tick label size
plt.yticks(fontsize=20)
plt.ylim(0, 100)

fig.tight_layout()

# Save the plot
plt.savefig('camera_pose_acc_fixed.png')
