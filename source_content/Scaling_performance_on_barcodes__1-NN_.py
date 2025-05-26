import matplotlib.pyplot as plt
import numpy as np

# Data
char_x = [0.8, 1.5, 3.4, 5.05]
char_k = [0.99, 1.92,4,5.7]
char_accuracy = [48, 54, 60.9, 61]
k_mer_accuracy = [49.5, 64, 68.5,70.3]

# Plot
plt.figure(figsize=(6, 3))
plt.plot(char_x, char_accuracy, label='Char', markersize=4, linewidth=2)
plt.plot(char_k, k_mer_accuracy, label='K-mer',  color='darkorange', markersize=4, linewidth=2)

# Labels and Legend
plt.xlabel('                       Params                             1e7',fontsize=16)
plt.ylabel('1-NN accuracy (%)',fontsize=16)
plt.xticks([1,2,3,4,5],fontsize=16)  # Adjust x-ticks
plt.yticks(np.arange(50, 71, 5),fontsize=16)  # Adjust y-ticks
plt.legend(loc='lower right',fontsize=16)
plt.grid(True,color='gray')
plt.tight_layout()

# Show the plot
plt.savefig('Scaling_performance_on_barcodes__1-NN_.png')