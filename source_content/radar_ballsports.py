import matplotlib.pyplot as plt
import numpy as np

# Define the new data for different sports
labels = np.array(
    [
        "Speed",
        "Endurance",
        "Strength",
        "Skill",
        "Teamwork",
    ]
)
stats = np.array(
    [
        [5, 4, 5, 3, 4],  # Basketball
        [3, 4, 5, 5, 3],  # Tennis
        [4, 5, 3, 4, 5],  # Soccer
    ]
)
titles = ["Basketball", "Tennis", "Soccer"]
colors = ["#FF4500", "#1E90FF", "#32CD32"]  # Orange, Dodger blue, Lime green
rticks = [1, 2, 3, 4, 5]
suptitle = "Comparison of Attributes Across Sports"


# Set the figure size
fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Define the number of variables
num_vars = len(labels)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
angles += angles[:1]

# The plot is made circular
stats = np.concatenate((stats, stats[:, [0]]), axis=1)

# Draw one radar chart with all sports
for idx, case_data in enumerate(stats):
    ax.fill(angles, case_data, color=colors[idx], alpha=0.3, label=titles[idx])
    ax.plot(angles, case_data, color=colors[idx], linestyle="--", linewidth=2.5, marker="o")

# Configure the radar chart
ax.set_rticks(rticks)
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=16, rotation=90, ha="center", va="center")
ax.xaxis.set_tick_params(pad=20) 
ax.grid(True)
ax.tick_params(axis='y', labelsize=15)
# Add legend
ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1), fontsize=20)

# Adjust layout for better fit
plt.tight_layout()
plt.savefig("radar_ballsports.png", bbox_inches="tight")
