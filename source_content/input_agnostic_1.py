import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Data
categories = ['Human', 'Art', 'Landscape', 'OCR']

mir_news_text = [3.2, 3.2, 3.15, 3.25]
mir_mail_text = [3.15, 3.15, 3.10, 3.25]

# Error values
error_news_text = [0.03, 0.05, 0.04, 0.05]
error_mail_text = [0.02, 0.05, 0.03, 0.06]

x = np.arange(len(categories))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, mir_news_text, width, label='News Text', color='#7F7CFC', yerr=error_news_text, capsize=5)
rects2 = ax.bar(x + width/2, mir_mail_text, width, label='Mail Text', color='#FF7C7C', yerr=error_mail_text, capsize=5)

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylim(2,3.7)
ax.set_yticks([2.00,2.25,2.50,2.75,3.00,3.25,3.50])
ax.set_ylabel('MIR',fontsize=18)
ax.tick_params(axis='y', labelsize=18)  # Increase y-tick label size

# ax.set_xlabel('Categories')
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=18)
ax.legend(loc='lower right', frameon=True, fontsize=18)

plt.tight_layout()
plt.savefig('input_agnostic_1.png')