import matplotlib.pyplot as plt
import numpy as np

# Sample data (10 points each line)
x = np.array([50., 75., 100., 150., 200., 250., 300., 350., 400., 450.])  # Labeled Segments per Class

# Data and errors for each method
primus = np.array([0.66, 0.65, 0.66, 0.68, 0.69, 0.70, 0.695, 0.7, 0.706, 0.703])
primus_err = np.array([0.01, 0.012, 0.008, 0.01, 0.012, 0.013, 0.015, 0.005, 0.011, 0.01])

imu2clip = np.array([0.53, 0.53, 0.54, 0.55, 0.57, 0.59, 0.6, 0.61, 0.62, 0.63])
imu2clip_err = np.array([0.01, 0.01, 0.01, 0.01, 0.015, 0.02, 0.02, 0.01, 0.02, 0.02])

simclr = np.array([0.45, 0.47, 0.51, 0.54, 0.57, 0.58, 0.58, 0.582, 0.583, 0.58])
simclr_err = np.array([0.01, 0.01, 0.008, 0.01, 0.006, 0.007, 0.01, 0.005, 0.005, 0.005])

multitaskssl = np.array([0.09, 0.11, 0.13, 0.2, 0.3, 0.39, 0.44, 0.47, 0.5, 0.49])
multitaskssl_err = np.array([0, 0.01, 0.015, 0.018, 0.02, 0.02, 0.02, 0.015, 0.005, 0.025])

standard_training = np.array([0.23, 0.24, 0.32, 0.4, 0.46, 0.5, 0.51, 0.52, 0.51, 0.52])
standard_training_err = np.array([0.025, 0.03, 0.045, 0.04, 0.045, 0.03, 0.02, 0.015, 0.015, 0.02])

# Plotting
plt.figure(figsize=(8, 6))

# PRIMUS (ours)
plt.plot(x, primus, label='PRIMUS (ours)', color='blue', linestyle='-', linewidth=3)
plt.fill_between(x, primus - primus_err, primus + primus_err, color='blue', alpha=0.3)

# IMU2CLIP
plt.plot(x, imu2clip, label='IMU2CLIP', color='red', linestyle='--', linewidth=3)
plt.fill_between(x, imu2clip - imu2clip_err, imu2clip + imu2clip_err, color='red', alpha=0.3)

# SimCLR
plt.plot(x, simclr, label='SimCLR', color='orange', linestyle='--', linewidth=3)
plt.fill_between(x, simclr - simclr_err, simclr + simclr_err, color='orange', alpha=0.3)

# MultitaskSSL
plt.plot(x, multitaskssl, label='MultitaskSSL', color='green', linestyle='--', linewidth=3)
plt.fill_between(x, multitaskssl - multitaskssl_err, multitaskssl + multitaskssl_err, color='green', alpha=0.3)

# Standard Training
plt.plot(x, standard_training, label='Standard Training', color='gray', linestyle='--', linewidth=3)
plt.fill_between(x, standard_training - standard_training_err, standard_training + standard_training_err, color='gray', alpha=0.3)

# Labels, legend, and grid
plt.xlabel('Labeled Segments per Class', fontsize=18)
plt.ylabel('Test Accuracy', fontsize=18)
plt.xticks([100, 200, 300, 400], fontsize=14)
plt.yticks(fontsize=14)
plt.legend(loc='lower right', fontsize=14)
plt.grid(True, linestyle='-', alpha=0.7)

# Save and show
plt.tight_layout()
plt.savefig('egoexo4d.png', dpi=300)
