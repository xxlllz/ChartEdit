import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [4, 6,8,12, 16, 32, 48]
quark = [10, 15,20, 25,40, 80, 120]
quark_plus = [60,70,80,110,130,280,430]

# Create a figure and axis
fig, ax = plt.subplots()

# Plotting the data
ax.plot(x, quark, 'o-', color='green', label='Quark')
ax.plot(x, quark_plus, 's-', color='orange', label='Quark+')

# Highlight a specific point with a vertical line and circle
highlight_x = 8
highlight_y_quark = 20
highlight_y_quark_plus = 100
ax.plot([highlight_x, highlight_x], [0, highlight_y_quark_plus], 'k--', lw=0.75)
# ax.plot(highlight_x, highlight_y_quark, 'o', color='green', markersize=8)
# ax.plot(highlight_x, highlight_y_quark_plus, 's', color='orange', markersize=8)

# Adding labels and title
ax.set_xlabel('Number of input views')
ax.set_ylabel('Inference time in milliseconds')
ax.set_title('Quark runtime when varying the number of input views')
ax.set_xticks(x)

# Adding legend
ax.legend()

plt.tight_layout()
# Show plot
plt.savefig('vary_num_input_views.png')