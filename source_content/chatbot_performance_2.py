import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Define data
categories = ['Reasoning', 'Roleplay','Writing',  'Humanities','STEM', 'Extraction',   'Coding','Math', ]
n = len(categories)

# QLoRA-70B, QST-70B, LLaMA-2-70B data
values_1 = [4.2, 7.3, 8.3, 9.3, 7.5, 7.5, 3.8, 4]
values_2 = [5.1, 8.3, 9, 9.6, 9.1, 7.9, 4, 3.5]
values_3 = [5.9, 7.4, 9.2, 9.4, 8.8, 7.3, 3, 3.2]

# Completing the loop
values_1 += values_1[:1]
values_2 += values_2[:1]
values_3 += values_3[:1]

# The angle for each category
angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Draw one track one per track
ax.plot(angles, values_1, linewidth=2, linestyle='solid', label='QLoRA-70B', marker='o', color='#65C5CC',markersize=4)
# ax.fill(angles, values_1, alpha=0.25, color='C0')

ax.plot(angles, values_2, linewidth=2, linestyle='solid', label='QST-70B', marker='o', color='#F6CF72',markersize=4)
# ax.fill(angles, values_2, alpha=0.25, color='C1')

ax.plot(angles, values_3, linewidth=2, linestyle='solid', label='LLaMA-2-70B', marker='o', color='#F89C74',markersize=4)
# ax.fill(angles, values_3, alpha=0.25, color='C2')

# Add the labels for each angle
ax.set_ylim(0,10)
ax.set_yticks([0,1,2,3,4,5,6,7,8,9])
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])

# Adjusting the tick labels with size and color
ax.set_xticklabels([])

# Now manually adjust the alignment for specific labels
for i, label in enumerate(categories):
    angle = angles[i]
    if i == 0 or i == 1 or i == 7:  # Left-aligned labels
        ax.text(angle, 11, label, horizontalalignment='left', verticalalignment='center', fontsize=16, color='black')
    elif i == 2 or i == 6:  # Centered labels
        ax.text(angle, 11, label, horizontalalignment='center', verticalalignment='center', fontsize=16, color='black')
    else:  # Left-aligned for indices 3, 4, 5
        ax.text(angle, 11, label, horizontalalignment='right', verticalalignment='center', fontsize=16, color='black')
# To adjust the padding between labels and the axis, you can use:
ax.tick_params(axis='x', pad=20)  # Adjusts the padding of x-axis labels
# Add custom y-tick labels manually (text at different angles)
yticks_values = np.arange(0, 10, 1)  # Create a list of values from 0 to 9
# Add custom y-tick labels manually (text at different angles)
for idx, value in enumerate(yticks_values):
    # Adjust the angle of the label based on the index and position it at a 90-degree (top) position
    
    fig.text(0.46+idx*0.031,0.38, idx, fontsize=16, ha='center', va='center', color='black')


ax.set_facecolor('#E5ECF6') 
ax.grid(color='white', linestyle='-', linewidth=1)
# Add a title
ax.set_rlabel_position(30)
ax.spines['polar'].set_visible(False)
plt.subplots_adjust(top=0.86, right=0.7, bottom=0.21, left=0.0)

# Add a legend
plt.legend(loc='upper right', 
           bbox_to_anchor=(1.4, 1.4),
           fontsize=18,facecolor='none',edgecolor='none')
plt.tight_layout()
plt.savefig("chatbot_performance_2.png")
