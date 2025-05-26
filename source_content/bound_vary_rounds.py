import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
t = np.linspace(100, 2000, 20)

y1 = np.array([32, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600])
y2 = np.array([15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195, 205])
y3 = np.array([12, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98, 106, 113, 121, 130, 137, 145, 153, 162])

plt.figure(figsize=(8, 6))

# Plot each line with markers and styles
plt.plot(t, y1, 'm-o', label='Approx+Shuffling [EFM+19]', linewidth=2, markersize=12)  # 'o' is the marker
plt.plot(t, y2, 'c-^', label='Approx+Shuffling+Sampling [GDD+21]', linewidth=2, markersize=12)  # '^' is the marker
plt.plot(t, y3, 'r-*', label='Camel', linewidth=2, markersize=12)  # '*' is the marker

# Scale and limits
plt.xscale('linear')  # X-axis linear scale
plt.yscale('log')     # Y-axis log scale
plt.ylim(10, 1000)    # Y-axis limit

# Labels and title with increased font size
plt.xlabel('# of Iterations $T$', fontsize=20)
plt.ylabel('Approximate DP $\epsilon$', fontsize=20)
plt.title('$N = 10^4, \delta = 10^{-5}, \gamma = 0.5, \epsilon_0 = 1.9$', fontsize=20)

# Custom ticks
plt.xticks([0, 500, 1000, 1500, 2000], fontsize=20)
plt.yticks([10, 100, 1000], fontsize=20)  # Only show y-axis ticks at 10, 100, and 1000

# Grid and legend
plt.grid(True, which='major', linestyle='-', linewidth=0.5)
plt.legend(fontsize=16, loc='lower right')

# Tight layout and save the plot
plt.tight_layout()
plt.savefig('bound_vary_rounds.png')