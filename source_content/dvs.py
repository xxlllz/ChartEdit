import matplotlib.pyplot as plt

# Data
x1 = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
y_skip_snn = [0.86, 0.87, 0.86, 0.855, 0.851, 0.845, 0.844, 0.844, 0.82, 0.81]
y_skip_rnn_plus_snn = [0.86, 0.852, 0.849, 0.846, 0.843, 0.842, 0.84, 0.836, 0.803, 0.79]
x2 = [100, 90, 70, 50, 30, 10]
y_random_snn = [0.86, 0.82, 0.808, 0.747, 0.655, 0.64]
y_fixed_snn = [0.86, 0.81, 0.75, 0.74, 0.67, 0.65]

plt.figure(figsize=(10, 6))

# Plotting each line with specified marker sizes to match the source image
plt.plot(x1, y_skip_snn, 'r-s', markersize=10, label='SkipSNN')
plt.plot(x1, y_skip_rnn_plus_snn, 'b-*', markersize=10, label='SkipRNN+SNN')
plt.plot(x2, y_fixed_snn, 'g-^', markersize=10, label='Fixed SNN')
plt.plot(x2, y_random_snn, 'y-v', markersize=10, label='Random SNN')

# Customize the labels and title
plt.xlabel('Percentage of awake state', fontsize=22)  # Larger font size for x-axis label
plt.ylabel('Test Accuracy', fontsize=22)             # Larger font size for y-axis label
plt.xticks(x1, [f'{i}%' for i in x1], fontsize=20)   # Larger font size for x-axis ticks
plt.yticks(fontsize=20)                              # Larger font size for y-axis ticks

plt.ylim(0.6, 0.9)
plt.xlim(10, 100)
# Reverse x-axis
plt.gca().invert_xaxis()

# Add legend with adjusted location
plt.legend(loc='lower left', fontsize=12, framealpha=1, fancybox=True)


# Show the plot
plt.tight_layout()
plt.savefig('dvs.png')
