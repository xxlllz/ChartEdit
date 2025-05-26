import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

rcParams['font.family'] = 'serif'

# Sample data
x = np.arange(1, 11)

y1 = [0.59, 0.57, 0.62, 0.65, 0.656, 0.68, 0.70, 0.705, 0.71, 0.715]
y1_err = [0.05]*10

y2 = [0.7, 0.77, 0.80, 0.85, 0.855, 0.88, 0.87, 0.88, 0.878, 0.878]
y2_err = [0.04]*10

plt.figure(figsize=(8, 5))

plt.plot(x, y1, 'g-', label='TNDP-RS', marker='^', linewidth=2,markersize=10)
plt.fill_between(x, np.array(y1) - np.array(y1_err), np.array(y1) + np.array(y1_err), color='green', alpha=0.2)

plt.plot(x, y2, 'orange', label='TNDP', marker='*', linewidth=2,markersize=14)
plt.fill_between(x, np.array(y2) - np.array(y2_err), np.array(y2) + np.array(y2_err), color='orange', alpha=0.2)

plt.xlabel('Design steps $t$', fontsize=14)
plt.ylabel('Proportion of correct decisions (%)', fontsize=16)
plt.ylim(0.5, 0.95)
plt.xlim(1,10)
plt.xticks([1,2,3,4,5,6,7,8,9,10],fontsize=14)
plt.yticks([0.5,0.6,0.7,0.8,0.9],fontsize=14)
plt.legend(loc='lower right',ncol=2, fontsize=12)
plt.grid(True,color='gray', alpha=0.3)
plt.tight_layout()
plt.savefig('tal_synth_ablation.png')