import matplotlib.pyplot as plt
import numpy as np

# Generate some data
np.random.seed(0)  # Set seed for reproducibility
data = np.random.normal(loc=1.81, scale=0.37, size=1000)

# Create the histogram
plt.figure(figsize=(12, 4))
plt.hist(data, bins=50, log=True)

# Add labels and title
plt.xlabel('Norm of coefficients')
plt.ylabel('Count')
plt.title('Norm: min=4.67e-01, mean=1.81e+00, max=2.73e+00')

# Set limits to match the source image
plt.xlim(0.4, 2.9)
plt.ylim(0.5, 1500)

# Display the plot
plt.tight_layout()
plt.savefig('fig_hist_NormOfCoeffs_TestSet_FTE_deg10_w1024_it500k_ICspectrum15_stat.png')