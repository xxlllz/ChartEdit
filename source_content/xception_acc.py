import matplotlib.pyplot as plt

# Sample Data
epochs = range(1, 21)
# Training accuracy (starts higher, then converges and crosses with validation accuracy)
training_accuracy = [
    0.92, 0.925, 0.93, 0.935, 0.94, 0.93, 0.925, 0.92, 0.915, 0.91,
    0.91, 0.915, 0.92, 0.93, 0.94, 0.95, 0.955, 0.96, 0.96, 0.96
]

# Validation accuracy (starts lower, then crosses and converges with training accuracy)
validation_accuracy = [
    0.85, 0.855, 0.86, 0.865, 0.87, 0.875, 0.88, 0.895, 0.91, 0.92,
    0.925, 0.93, 0.94, 0.945, 0.95, 0.955, 0.96, 0.96, 0.96, 0.96
]


# Plotting
plt.figure()
plt.plot(epochs, training_accuracy, label='Training Accuracy', color='C0')
plt.plot(epochs, validation_accuracy, label='Validation Accuracy', color='C1')

# Adding labels & title
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Model Accuracy')
plt.ylim(0.3, 1.0)  # Set y-axis range
plt.grid(False)  # Add grid
plt.legend(loc='lower right')
plt.savefig('xception_acc.png')