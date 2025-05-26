import matplotlib.pyplot as plt
import numpy as np

# Generate some example data
np.random.seed(0)  # For reproducibility
x = overlap_percentage = np.linspace(0, 1, 100)
overlap_percentage = np.random.rand(20)
random_accuracy = 0.7 + 0.3 * np.random.rand(20)
adversarial_accuracy = 0.65 + 0.3 * np.random.rand(20)

# Create a scatter plot
plt.scatter(overlap_percentage, random_accuracy, color='blue', label='Random',s=10)


# Trend lines
z1 = np.polyfit(overlap_percentage, random_accuracy, 1)
p1 = np.poly1d(z1)
plt.plot(overlap_percentage, p1(overlap_percentage), color='blue', label='Random (Accuracy=0.89, p<=0.001)')



plt.scatter(overlap_percentage, adversarial_accuracy, color='orange', label='Adversarial',s=10)


z2 = np.polyfit(overlap_percentage, adversarial_accuracy, 1)
p2 = np.poly1d(z2)
plt.plot(overlap_percentage, p2(overlap_percentage), color='orange', label='Adversarial (Accuracy=0.86, p<=0.001)')

# Labels and title
plt.xlabel('Overlap Percentage')
plt.ylabel('Accuracy')
plt.title('Accuracy of Responses by Overlap Percentage')
plt.legend(title='Condition')
plt.grid(True)
plt.xticks(np.arange(0.0,1.1,0.1))
plt.ylim(0, 1)  # Adjust y-limit to match more closely

plt.tight_layout()
plt.savefig('view_overlap_analysis.png')