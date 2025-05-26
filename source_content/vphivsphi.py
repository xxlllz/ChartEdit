import matplotlib.pyplot as plt
import numpy as np



# 横坐标从 0.80 到 1.00，50 个点
x1 = np.linspace(0.80, 1.00, 50)

# 二次函数模拟斜率逐渐增大的效果：y1(x) = a*(x - 0.80)^2 + c，其中a > 0
# 我们希望 y1(0.80) = 0.002 和 y1(1.00) = 0.035
# 通过求解来得到合适的 a 和 c
a = (0.035 - 0.002) / (0.20 ** 2)  # 假设(x - 0.80)的平方项
c = 0.002  # 起始值

y1 = a * (x1 - 0.80) ** 2 + c  # 二次函数计算

# 横坐标从 0.86 到 1.00，50 个点
x2 = np.linspace(0.86, 1.00, 50)

# 二次函数模拟斜率逐渐增大的效果：y2(x) = a*(x - 0.86)^2 + c，其中a > 0
# 我们希望 y2(0.86) = 0.002 和 y2(1.00) = 0.0125
a2 = (0.0125 - 0.002) / (0.14 ** 2)  # 假设(x - 0.86)的平方项
c2 = 0.002  # 起始值

y2 = a2 * (x2 - 0.86) ** 2 + c2  # 二次函数计算


# Plot
plt.figure(figsize=(8, 6))

# Plot the first curve (black solid line)
plt.plot(x2, y2, 'k-', label=r'$q_0 = -1.08$')

# Plot the second curve (red dashed line)
plt.plot(x1, y1, 'r--', label=r'$q_0 = -0.59$')

# Add labels
plt.xlabel(r'$\phi$')
plt.ylabel(r'$V(\phi)$')

# Set the legend in the upper left corner
plt.legend(loc='upper left')

# Remove grid
plt.grid(False)

# Set x and y axis limits
plt.xlim(0.80, 1.00)
plt.ylim(0, 0.035)
# Customize x and y ticks


# Customize x and y ticks
plt.xticks(np.arange(0.80, 1.01, 0.04))  # x ticks from 0.80 to 1.00 with an interval of 0.04
plt.yticks(np.arange(0, 0.036, 0.005))   # y ticks from 0 to 0.035 with an interval of 0.005

# Save the figure
plt.tight_layout()
plt.savefig('vphivsphi.png')
