import matplotlib.pyplot as plt

# Data
models = ['CoordTok-S', 'CoordTok-B', 'CoordTok-L']
rFVD = [460, 285, 195]
PSNR = [24, 25.2, 26.90]

fig, ax1 = plt.subplots()

# Plot rFVD
line1, = ax1.plot(models, rFVD, '-', color='royalblue', label='rFVD', linewidth=3, markersize=14)
ax1.scatter(models, rFVD, color='royalblue', s=150)
ax1.set_xlabel('Model size', fontsize=16, fontweight='bold')
ax1.set_ylabel('rFVD↓', fontsize=18, fontweight='bold')
ax1.tick_params(axis='y',labelsize=14)
ax1.tick_params(axis='x',labelsize=18)
ax1.set_ylim(150, 550)
ax1.set_yticks([200,300,400,500])


ax1.grid(visible=True, which='both', linestyle='--', linewidth=0.7)

# Create a second y-axis
ax2 = ax1.twinx()

# Plot PSNR
line2, = ax2.plot(models, PSNR, '-', color='red', label='PSNR', linewidth=3, markersize=14)
ax2.scatter(models, PSNR, color='red', s=150)
ax2.set_ylabel('PSNR↑', fontsize=18, fontweight='bold',rotation=270, labelpad=20)
ax2.tick_params(axis='y',labelsize=14)
ax2.set_ylim(23.5, 27.5)
ax2.set_yticks([24,25,26,27])
# Add legend
# Combine legends
lines = [line1, line2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper center',  ncol=2, fontsize=18)

plt.tight_layout()
plt.savefig('scalability_model_size.png')