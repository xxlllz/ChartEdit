import matplotlib.pyplot as plt

# Data
p_values = [100, 200, 800, 1600, 3000, 7000]
coin_values = [87, 88, 89, 88, 88, 88]
regmean_values = [75, 78, 78, 78, 78, 78]
ensemble_values = [76, 85, 92, 94, 95, 96]

plt.figure(figsize=(8, 6))

# Plot lines
plt.plot(p_values, coin_values, marker='o', color='blue', linewidth=2.5, markersize=10, label='COIN')
plt.plot(p_values, regmean_values, marker='o', color='orange', linewidth=2.5, markersize=10, label='RegMean')
plt.plot(p_values, ensemble_values, marker='o', color='green', linewidth=2.5, markersize=10, label='Ensemble')

# Labels and Legend
plt.xlabel('P', fontsize=20, labelpad=10)
plt.ylabel('Avg. Normalized Decoding Accuracy', fontsize=20, labelpad=10)

# Adjust legend position
plt.legend(
    loc='upper center',  # Place legend above the plot
    bbox_to_anchor=(0.5, 1.15),  # Fine-tune position (centered and above)
    ncols=3,
    fontsize=16,
    frameon=True,  # Enable frame
    framealpha=1,  # Solid frame
    edgecolor='black'  # Frame color
)

# Ticks - Reduce number of ticks
plt.xticks([0, 2000, 4000, 6000], fontsize=16)  # Reduced X-axis ticks
plt.yticks([75, 80, 85, 90, 95], fontsize=16)    # Reduced Y-axis ticks

# Adjust layout and save
plt.tight_layout()  # Adjust layout to give space for legend
plt.savefig('acc_vs_samples.png', dpi=300)