import numpy as np
import matplotlib.pyplot as plt

# Data
models = ['ResNet', 'No $\mathbf{J}$', 'No $\mathbf{\Omega}$', 'Full']
accuracy = [12, 18, 38, 48]
colors = ['grey', '#52AE55', '#52AE55', '#52AE55']

# Create bar chart
plt.figure(figsize=(5, 4))
plt.bar(models, accuracy, color=colors)

# Adding labels and title
plt.ylim(0,50)
plt.yticks([0,10,20,30,40,50],fontsize=14)
plt.xticks(models,fontsize = 16)
plt.ylabel('Accuracy (%)', fontsize=16)
plt.xlabel('Model', fontsize=14)

# Display the plot
plt.tight_layout()
plt.savefig('noisy_acc.png')