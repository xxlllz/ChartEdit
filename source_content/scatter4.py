
import matplotlib.pyplot as plt

# Data
x = [0.48, 0.3, 0.3, 0.35, 2.1]
y = [77, 77.9, 80.4, 84.3, 89.7]
labels = ["BundleSDF-lite*", "BundleTrack*","BundleSDF-async*","6DOPE-GS", "BundleSDF*",  ]
colors = ['#878cc5', '#ed906e', '#8eae7d', '#ce9ec7', '#f6cc81']

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, c=colors, s=120) 

# Adding labels
for i, txt in enumerate(labels):
    plt.annotate(txt, (x[i], y[i]), fontsize=12,
                 ha='left',va='center', weight='bold', 
                 textcoords="offset points", xytext=(10,10))

# Labeling the axes
plt.xlabel("Average Time Per Frame (s)\n(Lower is Better)", fontsize=14, weight='bold')
plt.ylabel("ADD (%)\n(Higher is Better)", fontsize=14, weight='bold')

# Setting limits
plt.xlim(0, 3)
plt.ylim(76.3, 90.4)

plt.tight_layout()
plt.savefig('scatter4.png')