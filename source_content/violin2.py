# necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Modified data for better distinction
ad_strategy_1 = [0.05, 0.07, 0.06, 0.05, 0.04, 0.07, 0.06, 0.08, 0.07, 0.05]
ad_strategy_2 = [0.10, 0.12, 0.11, 0.12, 0.10, 0.09, 0.11, 0.12, 0.11, 0.10]
ad_strategy_3 = [0.02, 0.03, 0.02, 0.03, 0.01, 0.04, 0.02, 0.01, 0.02, 0.03]
ad_strategy_4 = [0.06, 0.05, 0.07, 0.06, 0.05, 0.06, 0.07, 0.05, 0.08, 0.06]

# list of strategies and list of conversions
strategies = ['Strategy 1']*10 + ['Strategy 2']*10 + ['Strategy 3']*10 + ['Strategy 4']*10
conversions = ad_strategy_1 + ad_strategy_2 + ad_strategy_3 + ad_strategy_4

# dataframe
df = pd.DataFrame({'Strategy': strategies, 'Conversion': conversions})

# plot
plt.figure(figsize=(9,6))

# Using a more vibrant color palette
sns.violinplot(x='Strategy', y='Conversion', data=df, palette="coolwarm")

plt.xlabel('Advertising Strategy', fontsize=18)
plt.ylabel('Conversion Rate', fontsize=18)

# Set the font size for the x-ticks and y-ticks
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.ylim(-0.01, 0.15)
# Tight layout
plt.tight_layout()

# Save the plot
plt.savefig("violin2.png")