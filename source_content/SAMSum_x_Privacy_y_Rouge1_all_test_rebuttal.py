import matplotlib.pyplot as plt
import numpy as np

# 设置全局字体大小
plt.rcParams.update({'font.size': 16})  # 设置全局字体大小为16

# Data
private_lora_x = [0.1, 0.3, 0.6, 1.1, 2,3,8]
private_lora = [39, 44.8, 46, 47.5, 48.5,49,49]

x_values = [0, 2, 4, 6, 8]
dp_icl_x = [1, 3, 8] 
dp_icl = [40, 40.9, 40.8] 
prompt_pategen = [39, 39.5, 40, 41, 41.5]
lora_x=[1, 3, 8]
lora = [38,37.8,40.9]
zero_shot = [25, 0, 0, 0, 0]

# Create a new figure and axis
fig, ax = plt.subplots()

# Plot lines
ax.plot(private_lora_x, private_lora, marker='o', linestyle='-', label='PrivateLoRA', color='royalblue', markersize = 8)
ax.plot(dp_icl_x, dp_icl, marker='x', linestyle='--', label='DP-ICL', color='darkorange', markersize = 8)
ax.plot(lora_x, lora, marker='s', linestyle=':', label='PromptPateGen', color='green', markersize = 8)

# Plot special points for 'LoRA' and 'Zero-Shot'
ax.scatter(9, 50.1, color='green', s=200, zorder=5, label='LoRA',edgecolor='black')
ax.scatter(0, 23, color='red', s=200, zorder=5, label='Zero-Shot',edgecolor='black')

# Labels and title
ax.set_xlabel('Privacy Cost ε', fontsize=18)  # 调整横坐标字体大小
ax.set_ylabel('Rouge-1 Score', fontsize=18)   # 调整纵坐标字体大小

# Legend
ax.legend(loc='lower right', fontsize=15)  # 调整图例字体大小

# Grid and aesthetics
ax.grid(True)
ax.set_xlim(-0.5,9.5)
ax.set_ylim(21,52)
ax.set_xticks([0,2,4,6,8])
ax.tick_params(axis='both', labelsize=14)  # 调整刻度字体大小

# Show plot
plt.tight_layout()  # 自动调整布局以防止重叠
plt.savefig('SAMSum_x_Privacy_y_Rouge1_all_test_rebuttal.png')
