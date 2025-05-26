import matplotlib.pyplot as plt
import numpy as np

# Data for Gemma-2B
x_gemma = np.array([0, 25, 50, 75, 100])
y1_gemma = np.array([500, 200, 50, -100, -400])  # CHES Score
y2_gemma = np.array([50, 40, 30, 20, 10])  # Edit Distance Similarity
y3_gemma = np.array([20, 25, 20, 15, 5])  # Hidden Embedding Similarity

# Error data for Gemma-2B
y1_err_gemma = np.array([200, 35, 30, 25, 500])
y2_err_gemma = np.array([5, 4, 3, 2, 1])
y3_err_gemma = np.array([3, 2, 1, 2, 3])

# Data for Llama-3-8B
x_llama = np.array([0, 25, 50, 75, 100])
y1_llama = np.array([18, 10, 6, -6, -9])  # CHES Score
y2_llama = np.array([3, 8, 9, 7, 2])  # Edit Distance Similarity
y3_llama = np.array([10, 4, 8, 4, 2])  # Hidden Embedding Similarity

# Error data for Llama-3-8B
y1_err_llama = np.array([2, 3, 4, 10, 2])
y2_err_llama = np.array([1, 2, 3, 4, 5])
y3_err_llama = np.array([2, 2, 2, 2, 2])

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(12, 4), sharey=False)

# Plot for Gemma-2B
axs[0].errorbar(
    x_gemma, y1_gemma, yerr=y1_err_gemma, fmt='-o', color='blue', alpha=0.7, markersize=8, linewidth=1, label='CHES Score'
)
axs[0].errorbar(
    x_gemma, y2_gemma, yerr=y2_err_gemma, fmt='-s', color='darkorange', alpha=0.7, markersize=6, linewidth=1, label='Edit Distance Similarity'
)
axs[0].errorbar(
    x_gemma, y3_gemma, yerr=y3_err_gemma, fmt='-D', color='green', alpha=0.7, markersize=6, linewidth=1, label='Hidden Embedding Similarity'
)
axs[0].fill_between([-10, 110], -2000, 0, color='salmon', alpha=0.1)
axs[0].text(5, -800, 'Likelihood Displacement', color='brown', fontsize=10)
axs[0].set_title('Gemma-2B', fontsize=14)
axs[0].set_xlabel('Preference Similarity (Percentile)', fontsize=12)
axs[0].set_xlim([-10, 110]) 
axs[0].set_ylabel('Change in Preferred Response Log Probability', fontsize=12)
axs[0].set_yticks([-1000, -500, 0, 500])  # Adjusted y-axis ticks
axs[0].set_ylim([-2000, 1000])  # Adjusted y-axis ticks
# Plot for Llama-3-8B
axs[1].errorbar(
    x_llama, y1_llama, yerr=y1_err_llama, fmt='-o', color='blue', alpha=0.7, markersize=8, linewidth=1, label='CHES Score'
)
axs[1].errorbar(
    x_llama, y2_llama, yerr=y2_err_llama, fmt='-s', color='darkorange', alpha=0.7, markersize=6, linewidth=1, label='Edit Distance Similarity'
)
axs[1].errorbar(
    x_llama, y3_llama, yerr=y3_err_llama, fmt='-D', color='green', alpha=0.7, markersize=6, linewidth=1, label='Hidden Embedding Similarity'
)
axs[1].fill_between([-10, 110], -20, 0, color='salmon', alpha=0.1)
axs[1].text(5, -8, 'Likelihood Displacement', color='brown', fontsize=10)
axs[1].set_title('Llama-3-8B', fontsize=14)
axs[1].set_xlabel('Preference Similarity (Percentile)', fontsize=12)
axs[1].set_xlim([-10, 110]) 
axs[1].set_yticks([-10, 0, 10, 20])  # Adjusted y-axis ticks
axs[1].set_ylim([-20, 22])  

# Legend
axs[1].legend(loc='upper left', fontsize=10, bbox_to_anchor=(1, 1))

# Layout and save
plt.tight_layout()
plt.savefig('alpacafarm_dpo_gemma_llama_line_plots.png', dpi=300)
