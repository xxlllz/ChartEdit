import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 11)

# Sample data for each line
ours = [49, 91.5, 96, 98, 98, 99.8, 99.7, 100, 100, 100]
bge_reranker_v2_m3 = [47, 81, 89.5, 93, 95, 96, 98, 99, 99.5, 100]
bge_m3 = [42.7, 70.7, 82, 88, 94, 95, 96, 98, 99, 100]
e5_mistral = [42.6, 70.6, 80, 85, 88, 92, 94, 95, 98, 100]
bge_llmembedder = [42.5, 70.5, 80.1, 84.9, 90, 94, 94.9, 97.9, 99.4, 100]
sentence_bert = [40, 63, 73, 80, 86, 90, 93.9, 96, 97.8, 100]
bm25 = [38, 60, 74.5, 81, 87, 90, 93, 94, 96, 100]

plt.figure(figsize=(8, 6))
plt.plot(x, ours, 'o-', label='ours', linewidth=3, markerfacecolor='royalblue',markersize=4, markeredgecolor='white')
plt.plot(x, bge_reranker_v2_m3, 's-', label='bge_reranker_v2_m3', linewidth=3,color='green', markerfacecolor='green',markersize=4, markeredgecolor='white')
plt.plot(x, bge_m3, '^-', label='bge_m3', linewidth=3,color='orange', markerfacecolor='orange',markersize=4, markeredgecolor='white')
plt.plot(x, e5_mistral, 'd-', label='e5_mistral', linewidth=3,color='orangered', markerfacecolor='orangered',markersize=5, markeredgecolor='white')
plt.plot(x, bge_llmembedder, 'P-', label='bge_llmembedder', linewidth=3,color='skyblue', markerfacecolor='skyblue',markersize=5, markeredgecolor='white')
plt.plot(x, sentence_bert, 'x-', label='sentence_bert', linewidth=3,color='lightgreen', markerfacecolor='lightgreen',markersize=5, markeredgecolor='white')
plt.plot(x, bm25, 'p-', label='bm25', linewidth=3,color='orchid', markerfacecolor='orchid',markersize=5, markeredgecolor='white')

plt.ylim(36,102)
plt.xticks(fontsize = 18)
plt.yticks(fontsize = 18)
plt.title('HQA',fontsize = 18)
plt.xlabel('Number of retrieved documents',fontsize = 18)
plt.ylabel('Recall(%)',fontsize = 18)
plt.grid(True)
plt.legend(fontsize = 14)

plt.savefig('recall_HQA.png')