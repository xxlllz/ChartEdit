import matplotlib.pyplot as plt
import numpy as np

# Generate some data
np.random.seed(0)  # Ensures reproducibility
# Increased sample size to reflect source image characteristics
data = np.random.exponential(scale=1, size=1000)

# Create a histogram
plt.hist(data, bins=100, color='teal')

# Set the labels
plt.xlabel('Event Length (s)', fontsize=14)
plt.ylabel('Count', fontsize=14)

# Set tick label size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('all_event_lens.png')
