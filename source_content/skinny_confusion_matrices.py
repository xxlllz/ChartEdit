import matplotlib.pyplot as plt
import numpy as np

data_1_0 = np.array([[16, 8], [16, 8]])
data_1_5 = np.array([[25, 12], [19, 13]])
data_2_0 = np.array([[29, 18], [24, 26]])

fig, axes = plt.subplots(1, 3, figsize=(12, 1.5), constrained_layout=True)
cmap = plt.cm.Purples

# Define a global vmin and vmax for the color scale
vmin, vmax = 0, 30

# Plot heatmaps
for iter,(ax, data, title) in enumerate(zip(axes, [data_1_0, data_1_5, data_2_0], ["Stable Diffusion 1.0", "Stable Diffusion 1.5", "Stable Diffusion 2.0"])):
    im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax,aspect=0.35)
    if iter == 0:
    # Annotate each cell
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                ax.text(j, i, f"{data[i, j]}", ha="center", va="center", color="black", fontsize=16)
    else:
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                ax.text(j, i, f"{data[i, j]}", ha="center", va="center", color="white", fontsize=16)
    
    ax.plot([-0.5,1.5],[0.5,0.5],color='white')
    ax.plot([0.5, 0.5], [-0.5, 1.5], color='white')
    ax.set_title(title, fontsize=14, weight="bold")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Entity 1", "Entity 2"])
    ax.set_yticks([0, 1])
    if iter == 0:
        ax.set_yticklabels(["1", "2"])
    else:
        ax.set_yticklabels([])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(axis='both', which='both', length=0)
    # ax.grid(True,color='white')

# Set shared labels
fig.text(0.03, 0.55, "True", va="center", ha="center", fontsize=14, weight="bold",)
fig.text(0.03, 0.35, "Label", va="center", ha="center", fontsize=14, weight="bold",)

# Add a single colorbar spanning all heatmaps
cbar = fig.colorbar(im, ax=axes, orientation='vertical', fraction=0.02, pad=0.03)
cbar.set_ticks([0, 15, 30])
cbar.set_label("", fontsize=12)
cbar.outline.set_visible(False)

plt.savefig('skinny_confusion_matrices.png')

