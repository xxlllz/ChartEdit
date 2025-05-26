import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.array([400, 425, 450, 475, 500, 525, 550, 575, 600])
y1 = np.array([1275, 1500, 1600,  1720,1760,1700,1650,1550,1470])
y2 = np.array([1150, 1350, 1420,  1550,1580,1535,1490,1420,1340])
y3 = np.array([1050, 1250, 1300, 1410,1430,1390,1350,1260,1180])

plt.figure(figsize=(8, 4))

# Plotting the lines with different styles and markers
plt.plot(x, y1, 'g-p', label='$|S^C| = 5$', linewidth=3, markersize=10)
plt.plot(x, y2, 'b-.', marker='s', label='$|S^C| = 10$', linewidth=3, markersize=10)
plt.plot(x, y3,  color='orange', linestyle='--', label='$|S^C| = 15$', linewidth=3, markersize=10, marker='>')

plt.xlabel('DAS delay $\delta$ (ms)')
plt.ylabel('Throughput (CTx/sec)')
plt.legend(loc='lower center')
plt.grid(True, linestyle=':', color='k', alpha=0.6)
plt.xlim(350, 650)
plt.ylim(900, 1800)
plt.yticks([900,1200,1500,1800])
plt.xticks([350,400,450,500,550,600,650])

plt.savefig('TPSvsDelay1-n.png')