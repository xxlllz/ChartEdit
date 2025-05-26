import matplotlib.pyplot as plt
import numpy as np

# Data
models = ['GritLM', 'Mistral', 'Mixtral', 'GPT-3.5', 'Gemini', 'GPT-4']
graph_level_performance = [0.2, 0.3, 0.5, 0.6, 0.7, 0.6]
node_level_performance = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
graph_level_error = [0.05, 0.05, 0.04, 0.05, 0.04, 0.03]
node_level_error = [0.04, 0.05, 0.03, 0.02, 0.03, 0.02]

# Plot
x = np.arange(len(models))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(6, 4))  # Adjust figure size if needed
rects1 = ax.bar(x - width/2, graph_level_performance, width, yerr=graph_level_error, label='Graph-level', color='skyblue', capsize=3)
rects2 = ax.bar(x + width/2, node_level_performance, width, yerr=node_level_error, label='Node-level', color='darkblue', capsize=3)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Performance', fontsize=14)
plt.ylim([0,1])
ax.set_xticks(x)
ax.set_xticklabels(models, rotation=45, ha='right', fontsize=14)
ax.legend(fontsize=15)

# Increase tick size
ax.tick_params(axis='both', labelsize=14)

fig.tight_layout()

plt.savefig('binvsdesc.png')
