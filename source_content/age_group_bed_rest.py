import matplotlib.pyplot as plt
import numpy as np

# Age groups and their average bed rest time
categories = [
    "12-",
    "12-23",
    "24-35",
    "36-45",
    "46-60",
    "60+",
]

# Average bed rest time (hours per week)
means = [9.2, 8.1, 7.8, 7.3, 8.2, 9.3]
errors = [0.7, 0.8, 1.1, 1.2, 0.7, 0.8]
downerrors = [0.7, 0.6, 0.3, 0.5, 0.8, 1.0]

# Texts and labels
legendtitles = ["Average Rest Time", "Overall Mean"]
texttitle = "Overall Mean Rest Time"
ylabel = "Bed Rest Time (Hours)"
xlabel = "Age Group"
dataset_mean = np.mean(means)  # Calculated dataset mean

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 7))

# Custom color scheme
marker_color = "navy"
error_color = "royalblue"

ax.errorbar(
    categories,
    means,
    yerr=[errors, downerrors],
    fmt="s",
    color=marker_color,
    ecolor=error_color,
    capsize=12,
    markersize=22,
    markerfacecolor="aliceblue",
    markeredgewidth=2,
    markeredgecolor=marker_color,
)

# Adding a legend with both "Average" and "Dataset mean"
mean_line = ax.errorbar(
    [], [], yerr=[], fmt="s", color="black", ecolor=error_color, capsize=6
)
dataset_mean_line = ax.axhline(
    y=dataset_mean, color="black", linestyle="-.", linewidth=2
)
ax.legend(
    [dataset_mean_line, mean_line],
    legendtitles,
    loc="upper center",
    fontsize=20,
    fancybox=True,
    framealpha=1,
    shadow=True,
    borderpad=1.2,
)

# Setting labels and a title
ax.set_xlabel(xlabel, fontsize=20)
ax.set_ylabel(ylabel, fontsize=20)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.grid(True, which="both", axis="y", linestyle="-", linewidth=1.5)

plt.tight_layout()
plt.savefig("age_group_bed_rest.png", bbox_inches="tight")
