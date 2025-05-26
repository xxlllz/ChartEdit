from matplotlib import pyplot as plt
plt.rcParams['font.family'] = 'serif'
# Extracted data from the image
labels = ['Relationships', 'Attributes', 'Cultural\n Background', 'Temporal \nInformation','Location and \n Orientation', ]
sizes = [15, 21, 13, 27, 24]
colors = ['#ECFFDF', '#F6E1F1', '#DFEBF8', '#FFF3CC', '#FBE6D6']

# Create the pie chart
plt.figure(figsize=(6, 6))

# Customizing labels with both label and percentage
def label_with_pct(pct, allsizes, label):
    return f'{label}\n{pct:.0f}%'

# Create the pie chart with custom labels
plt.pie(sizes, labels=[label_with_pct(pct, sizes, label) for label, pct in zip(labels, sizes)], 
        colors=colors, startangle=90, wedgeprops={'edgecolor': 'black'}, 
        labeldistance=0.70, textprops={'fontsize': 12, 'ha': 'center', 'va': 'center'})

# Equal aspect ratio ensures that pie chart is drawn as a circle.
plt.axis('equal')

plt.tight_layout()
plt.savefig('pie0.png')