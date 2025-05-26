import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'serif'
# Data to plot
labels = ['Hypothetical', 'Causal', 'Comparative', 'Predictive', 'Factual', 'Explanatory', 'Methodological', 'Subjective']
sizes = [58, 39, 21, 41, 25, 27, 29, 40]
sizes = [i/100 for i in sizes]
colors = ['#339966', '#ff69b4', '#a7a4f2', '#ff9966', '#66cdaa', '#4fa3ff', '#ff6666', '#d2b48c']

# Custom function to display the actual number instead of percentage
def func(pct, allsizes):
    absolute = round(pct*sum(allsizes))  # calculate the actual number
    return f'{absolute}'  # return the actual number

# Create a pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, colors=colors, startangle=90, counterclock=False,
        textprops={'fontsize': 12}, autopct=lambda pct: func(pct, sizes),
        wedgeprops={'edgecolor': 'black', 'linewidth': 1})  # Custom autopct function

plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.tight_layout()
plt.savefig('questiontype_distribution.png')
plt.show()