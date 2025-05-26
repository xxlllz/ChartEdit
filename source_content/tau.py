import matplotlib.pyplot as plt
import numpy as np


# Sample data
x = [1.0, 1.2, 1.4, 1.6, 1.8, 2.0]
acc1 = [0.158, 0.164, 0.162, 0.161, 0.162, 0.1625]
mrr = [0.25, 0.259, 0.257, 0.255, 0.256, 0.258]

# Create line plot
plt.figure(figsize=(6,6))
plt.plot(x, acc1, marker='o', markersize=16, color='steelblue', label='Acc@1')
plt.plot(x, mrr, marker='s', markersize=16, color='darkorange', label='MRR')

# Add legend
plt.legend(loc='center right', fontsize=28)

# Add labels
plt.xlabel(r'Parameter  $\tau$', fontsize=26)
plt.ylabel('Performance', fontsize=28)

# Set tick parameters
plt.xticks(np.arange(1.0, 2.1, 0.2),fontsize=26)
plt.yticks([0.16,0.18,0.20,0.22,0.24,0.26],fontsize=26)

# Show plot
plt.tight_layout()
plt.savefig('tau.png')