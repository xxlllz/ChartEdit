import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(0, 11, 1)
y = 40 / (x + 1)

# Create plot
plt.figure(figsize=(6, 4))
plt.plot(x, y, 'bo-', label='Data')

# Labels and legend
plt.xlabel('log(block size)')
plt.ylabel('Compression Ratio')
plt.legend(loc='lower right', fontsize='small', framealpha=1.0)


# Show plot
plt.tight_layout()
plt.savefig('yiip_equilibrium-901x111815_eb=1e-1_CR.png')