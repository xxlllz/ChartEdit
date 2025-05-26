import matplotlib.pyplot as plt

# Data
x = [0, 10, 20, 30, 40, 50, 60, 70]
y = [0.7, 0.5, 0.14, 0.17, 0.5, 0.0, 0.0, 0.0]

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, marker='o')

# Set title and labels
plt.title('Success Rate vs Action Length', fontsize=18)
plt.xlabel('Action Length', fontsize=18)
plt.ylabel('Success Rate', fontsize=18)

# Modify x and y axis tick font sizes
plt.tick_params(axis='x', labelsize=18)  # Modify x-axis tick font size
plt.tick_params(axis='y', labelsize=18)  # Modify y-axis tick font size
# Show plot
plt.tight_layout()
plt.savefig('Success_Rate_vs_Action_Length.png')