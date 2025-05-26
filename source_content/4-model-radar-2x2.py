import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
# Data for the radar chart
categories = ["Appl.", "Math", "Date", "Tabular", "Spatial", "AVG"]
languages = ["Python", "R", "C++", "Java", "JavaScript", "MultiPoT"]
# starc
values = np.array([
    [47.04, 19.69, 34.96, 79.19, 70.00], # Python
    [44.21, 17.74, 37.13, 77.85, 65.90], # R
    [47.34, 16.74, 18.70, 82.55, 70.95], # C++
    [47.97, 16.76, 35.23, 78.52, 69.50], # Java
    [48.40, 19.15, 36.31, 80.54, 72.95], # Javascript
    [49.67, 20.41, 40.38, 87.25, 71.55]  # MultiPoT
])
# codel
values1 = np.array([
    [68.63, 27.95, 50.68, 92.62, 77.55],  # Python
    [66.80, 26.65, 58.27, 93.29, 79.05],  # R
    [71.33, 24.99, 43.36, 93.29, 80.45],  # C++
    [70.10, 27.93, 56.91, 93.96, 81.80],  # Java
    [68.97, 26.16, 50.41, 87.25, 80.35],  # Javascript
    [71.17, 27.97, 58.54, 93.96, 79.60]   # MultiPoT
])
# deepc
values2 = np.array([
    [70.65, 37.64, 44.72, 93.96, 89.80],
    [69.22, 33.59, 53.12, 93.29, 92.60],
    [72.32, 33.94, 39.57, 95.30, 93.40],
    [72.10, 35.35, 55.56, 93.96, 88.75],
    [71.89, 35.60, 52.57, 93.29, 86.10],
    [72.32, 37.55, 54.47, 95.30, 91.70]  # MultiPoT
])

# chatgpt
values3 = np.array([
    [82.31, 45.76, 47.70, 94.63, 93.60],
    [80.95, 40.61, 58.81, 93.29, 94.60],
    [81.40, 43.77, 49.05, 93.29, 88.45],
    [81.79, 45.33, 53.39, 92.62, 88.80],
    [82.58, 40.64, 56.10, 96.64, 93.30],
    [84.33, 49.92, 58.54, 98.66, 95.30]  # MultiPoT
])

# Number of variables (including AVG)
num_vars = len(categories)

# Compute angle for each category, ensuring AVG is at the bottom
angles = np.linspace(np.pi / 6, 2 * np.pi + np.pi / 6, num_vars, endpoint=False).tolist() 
angles = angles[-1::-1]
angles = angles[2:] + angles[:2]  # Adjusting so that AVG is at the bottom
angles += angles[:1]  # Complete the loop

# Colors for different languages
colors = ["#7093F4", "#63C45C", "#FA7F6F", "c", "#B081E3", "#3C6578"] # "b", "g", "r", "c", "m"

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20, 7), subplot_kw=dict(polar=True), 
                                         gridspec_kw={'wspace': 0.22, 'left': 0.05, 'right': 0.95, 'top': 0.85, 'bottom': 0.1})
# Add category labels
categories_pos = {"Appl.":7, "Math":7, "Date":6, "Tabular":10, "Spatial":10, "AVG":6}
tmp_angles = angles[:-1]
categories_angel = {"Appl.":tmp_angles[0] - np.pi/40, "Math":tmp_angles[1] + np.pi/40, "Date":tmp_angles[2], "Tabular":tmp_angles[3] - np.pi/50, 
                    "Spatial":tmp_angles[4] + np.pi/55, "AVG":tmp_angles[5]}
font_properties = {
        'size': 14,
    }

# Function to create a radar chart with lighter fill colors and title at the bottom
def create_radar_chart(ax, angles, data, title):
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([""]*num_vars, size=15, va="center")
    ax.grid(axis='x', color='black', alpha=0.3)
    # Calculate the average performance for each language
    avg_performance = data.mean(axis=1)
    # Append the average performance to the values
    values_with_avg = np.c_[data, avg_performance]
    # Calculate the maximum values for each category including the average
    max_values = np.max(values_with_avg, axis=0)
    ax.spines['polar'].set_color('black')  # 设置边框颜色
    ax.grid(color='black') 
    # Scale the values to the maximum of each category
    data = (values_with_avg / max_values) * 100
    for i, value in enumerate(data):
        value_with_loop = np.append(value, value[0])  # Completing the loop
        ax.plot(angles, value_with_loop, linewidth=2, linestyle='solid', marker='o', color=colors[i % len(colors)], alpha=0.8, zorder=5)
        ax.fill(angles, value_with_loop, color=colors[i % len(colors)], alpha=0.1)  # Lighter fill
    
    ax.set_ylim(50, 100.9)
    ax.set_yticklabels([])
    ax.yaxis.grid(False)

    ax:plt.Axes
    for angle, category in zip(angles[:-1], categories):
        # angle = angle - np.pi / num_vars  # 向左移动
        ax.text(categories_angel[category], ax.get_rmax() + categories_pos[category], category, 
                fontdict=font_properties, 
                horizontalalignment='center', 
                verticalalignment='center')
    
    title = ax.set_title(title, color='black', y=-0.15, fontdict={'size': 18})  # Title at the bottom
    title.set_position((0.5, -0.2))

# Creating the radar charts with the adjusted settings
create_radar_chart(ax1, angles, values, "(a) Starcoder")
create_radar_chart(ax2, angles, values1, "(b) Code Llama")
create_radar_chart(ax3, angles, values2, "(c) Deepseek Coder")
create_radar_chart(ax4, angles, values3, "(d) ChatGPT")

legend_lines = [plt.Line2D([0], [0], color=color, linewidth=2) for color in colors]

# Adding a legend for languages
fig.legend(legend_lines, languages, loc='upper center', bbox_to_anchor=(0.5, 0.9), ncol=6, prop={'size': 18})
plt.savefig("4-model-radar-2x2.png")