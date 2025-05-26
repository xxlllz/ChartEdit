import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = [0, 5, 10, 15, 20, 25, 30, 35]
y_vrdag = [1.2, 500, 2000, 4000, 6000, 10000, 20000, 25000]  # VRDAG data
y_tigger = [1.2, 1500, 5000, 11000, 20000, 25000, 40000, 45000]  # TIGGER data
y_taggen = [1.2, 1300, 8000, 20000, 30000, 40000, 50000, 80000]  # TagGen data

plt.figure(figsize=(10, 8))

# Plotting the lines with correct marker styles
plt.plot(x, y_vrdag, label='VRDAG', color='orangered', marker='D', markersize=14, linestyle='-', linewidth=2)
plt.plot(x, y_tigger, label='TIGGER', color='lightseagreen', marker='s', markersize=14, linestyle='-', linewidth=2)
plt.plot(x, y_taggen, label='TagGen', color='gold', marker='*', markersize=14, linestyle='-', linewidth=2)

# Set the y-scale to logarithmic


# Adding labels and title
plt.xlim(0,35) 
plt.ylim(1,100000)
plt.xlabel('Timestep', fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.ylabel('Running Time (sec)', fontsize=16)
plt.yscale('log')
# Adding legend
plt.legend(fontsize=18, loc='upper left')

# Show grid
plt.grid(True)

# Display the plot
plt.savefig('TrainTrend-v2.png')