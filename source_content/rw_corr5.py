import matplotlib.pyplot as plt
import numpy as np

# Data for the first subplot
x1 = np.array([0, 280, 560])
x12 = np.array([5, 40, 280])
y1 = np.array([-0.075, 0.02, 0.115])
y2 = np.array([-0.0755, -0.056, 0.02])

# Data for the second subplot
x2 = np.array([-600, 300])
x22 = np.array([-420, 100, 120])
yn = np.array([0.28, 0.24])
yn2 = np.array([0.272, 0.248, 0.253])
ya = np.array([0.21, 0.135])
ya2 = np.array([0.2, 0.14, 0.17])
yf = np.array([0.1, 0.06])
yf2 = np.array([0.092, 0.068, 0.067])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7, 5.5))

# First subplot
ax1.plot(x1, y1, color='black')
ax1.scatter(x12, y2, color='black', s=100)
ax1.set_xlabel('Age (Myr)', fontsize=20)
ax1.set_ylabel('[Fe/H]', fontsize=20)
ax1.text(50, 0.02, 'r=1.00', fontsize=14)
# Set axis limits (range)
ax1.set_xlim(0, 350)  # Set x-axis range
ax1.set_ylim(-0.1, 0.05)  # Set y-axis range

# Set custom y-ticks (major and minor)
major_ticks = np.arange(-0.1, 0.05, 0.05)  # Major ticks
minor_ticks = np.arange(-0.1, 0.05, 0.01)  # Minor ticks

ax1.set_yticks(major_ticks)  # Set major ticks
ax1.set_yticks(minor_ticks, minor=True)  # Set minor ticks

# Display main and minor tick lines
ax1.tick_params(axis='y', which='both', length=6, direction='in', labelsize=12)  # Length of major and minor ticks
ax1.tick_params(axis='y', which='minor', length=4, direction='in', labelsize=12)  # Length of minor ticks
ax1.tick_params(axis='x', which='both', length=4, direction='in', labelsize=12)  # Length of minor ticks

# Second subplot
ax2.plot(x2, yn, color='red')
ax2.scatter(x22, yn2, color='red', s=60)
ax2.text(-400, 0.26, '[n/Fe],r=-0.97', color='red', fontsize=13, style='italic', rotation=-15)

ax2.plot(x2, ya, color='blue')
ax2.scatter(x22, ya2, color='blue', s=60)
ax2.text(-400, 0.17, r'[$\alpha$/Fe]+0.05,r=-0.87', color='blue', fontsize=13, style='italic', rotation=-20)

ax2.plot(x2, yf, color='green')
ax2.scatter(x22, yf2, color='green', s=60)
ax2.text(-400, 0.08, '[Fe-p/Fe],r=-1.00', color='green', fontsize=13, style='italic', rotation=-15)
# Set axis limits (range)
ax2.set_xlim(-600, 300)  # Set x-axis range
ax2.set_ylim(0.0, 0.35)  # Set y-axis range
ax2.set_xlabel('XY (pc)', fontsize=20)
ax2.set_ylabel('[X/Fe]', fontsize=20)
# Set custom y-ticks (major and minor)
major_ticks1 = [-500, -300, -100, 100]  # Major ticks
minor_ticks1 = [0.0, 0.1, 0.2, 0.3]  # Minor ticks

ax2.set_xticks(major_ticks1)  # Set major ticks
ax2.set_yticks(minor_ticks1)  # Set minor ticks

ax2.tick_params(axis='x', which='both', length=6, direction='in', labelsize=12)  # Length of major and minor ticks
ax2.tick_params(axis='y', which='both', length=6, direction='in', labelsize=12)  # Length of major and minor ticks

plt.tight_layout()
plt.savefig('rw_corr5.png')