import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
gc_separation1 = np.array([0.2, 0.6, 1.1, 1.6, 2.05, 2.5, 2.9, 3.4, 3.8, 4.2, 4.8, 5.2, 5.7])
gc_separation2 = np.array([0.22, 0.62, 1.12, 1.62, 2.07, 2.52, 2.92, 3.42, 3.82, 4.22, 4.82, 5.22, 5.72])
rrm_full = np.array([6.8, 1.1, 1.8, 1.75, 2.3, 1.9, 2, 1.8, 2, 1.8, 1.6, 1.85, 1.9])
rrm_grmth14 = np.array([5.3, 0.9, 1.1, 1.4, 2.0, 1.2, 1.65, 1.4, 1.7, 1.0, 1.5, 1.4, 1.6])
errors_full = np.array([1.5, 0.2, 0.2, 0.2, 0.3, 0.2, 0.2, 0.2, 0.2, 0.3, 0.2, 0.3, 0.3])
errors_grmth14 = np.array([2.8, 0.15, 0.1, 0.15, 0.25, 0.2, 0.2, 0.2, 0.2, 0.15, 0.2, 0.22, 0.2])

fig, ax = plt.subplots()

ax.errorbar(gc_separation1, rrm_full, yerr=errors_full, fmt='o', label='full')
ax.errorbar(gc_separation2, rrm_grmth14, yerr=errors_grmth14, fmt='o', color='orange', label='GRM$_{th}$=14 rad m$^{-2}$')

ax.set_xlabel('separation from GC [$R_{100}$]', fontsize=14)
ax.set_ylabel('RRM rms [rad m$^{-2}$]', fontsize=14)
ax.set_title('$M_{GC} > 1 × 10^{14} M_{\odot}$', fontsize=14)
ax.legend()

plt.savefig('rrm_R_grm.png')