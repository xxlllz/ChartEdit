import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.patches as mpatches

# Modified Data (Slightly changed values)
age_groups = ["Children", "Teenagers", "Young Adults", "Adults", "Older Adults"]
reading_hours = {
    "Children": [1, 2, 2, 2, 3, 1, 2, 3, 1, 3],
    "Teenagers": [4, 5, 3, 6, 4, 5, 3, 6, 5, 4],
    "Young Adults": [8, 5, 8, 7, 5, 6, 6, 7, 10, 5],
    "Adults": [12, 10, 5, 8, 6, 7, 12, 8, 7, 9],
    "Older Adults": [4, 5, 3, 6, 4, 5, 3, 6, 5, 4],
}

# Preprocess data
data = []
for group in age_groups:
    data.append(reading_hours[group])

# Create violin plot with light colors
plt.figure(figsize=(10, 6))
sns.violinplot(data=data, palette='pastel')  # 'pastel' palette gives light colors

# Adding title, labels
plt.xlabel('Age Groups', fontsize=18)
plt.ylabel('Hours Spent Reading per Week', fontsize=18)

# Set x-ticks to the age groups
plt.xticks(range(len(age_groups)), age_groups, fontsize=15)

# Increase y-axis tick font size
plt.yticks(fontsize=15)

# Create custom legend handles
handles = [mpatches.Patch(color=sns.color_palette('pastel')[i], label=age_groups[i]) for i in range(len(age_groups))]
plt.legend(handles=handles, loc="upper left", bbox_to_anchor=(1, 1), fontsize=14)

# Layout adjustments
plt.tight_layout()

# Save the figure
plt.savefig("violin1.png")