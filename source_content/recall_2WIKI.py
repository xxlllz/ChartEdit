import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)

y_ours = [45, 90, 95, 100, 100, 100, 100, 100, 100, 100]
y_bge_reranker = [44.8, 75, 82.5, 88, 92, 96, 97, 98, 99, 100]
y_bge_m3 = [43, 73.5, 82, 89, 92, 95, 96, 98, 99, 100]
y_e5_mistral = [43, 73, 82, 88, 91.5, 95, 96, 98, 99, 100]
y_bge_llmembedder = [42, 72, 80, 85, 90, 94, 94.8, 97, 98, 100]
y_sentence_bert = [40, 63, 75.5, 83, 88, 92, 96, 97, 98, 100]
y_bm25 = [31, 52, 64, 71, 78, 83, 87, 93, 96, 100]

plt.figure(figsize=(8, 6))
plt.plot(x, y_ours, 'o-', label='ours', linewidth=3, markerfacecolor='royalblue',markersize=4, markeredgecolor='white')
plt.plot(x, y_bge_reranker, 's-', label='bge_reranker_v2_m3', linewidth=3,color='green', markerfacecolor='green',markersize=4, markeredgecolor='white')
plt.plot(x, y_bge_m3, '^-', label='bge_m3', linewidth=3,color='orange', markerfacecolor='orange',markersize=4, markeredgecolor='white')
plt.plot(x, y_e5_mistral, 'd-', label='e5_mistral', linewidth=3,color='orangered', markerfacecolor='orangered',markersize=5, markeredgecolor='white')
plt.plot(x, y_bge_llmembedder, 'P-', label='bge_llmembedder', linewidth=3,color='skyblue', markerfacecolor='skyblue',markersize=5, markeredgecolor='white')
plt.plot(x, y_sentence_bert, 'x-', label='sentence_bert', linewidth=3,color='lightgreen', markerfacecolor='lightgreen',markersize=5, markeredgecolor='white')
plt.plot(x, y_bm25, 'p-', label='bm25', linewidth=3,color='orchid', markerfacecolor='orchid',markersize=5, markeredgecolor='white')

plt.ylim(28,102)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.title('2WIKI',fontsize = 18)
plt.xlabel('Number of retrieved documents',fontsize = 18)
plt.ylabel('Recall(%)',fontsize = 18)
plt.grid(True)
plt.legend(fontsize = 14)

plt.savefig('recall_2WIKI.png')