import matplotlib.pyplot as plt
import numpy as np
plt.rcParams['font.family'] = 'serif'
# Sample data
epochs = np.array([0, 20, 40, 60, 80])
epochs1 = np.array([0,10,20,30,40,50,60,70,80,90])
rank = np.array([1, 5, 15, 32,64])
natural = [50, 65, 75, 85]
specialized = [85, 90, 95]
structured = [40, 60, 80, 70]
mse_loss = {
    'Linear (LoRA)': [0.25, 0.22, 0.18, 0.13, 0.05],
    'Sigmoid': [0.238, 0.175, 0.12, 0.06, 0.01],
    'RBF': [0.245, 0.215, 0.153, 0.048, 0.004],
    'Piecewise Linear': [0.225, 0.165, 0.105, 0.036, 0.002]
}
training_loss = {
    'Linear (LoRA)': [4.6, 1.7, 0.1, 0.05,0.04,0.05,0.04,0.05,0.04,0.05],
    'Sigmoid': [4.6, 4.3, 3.5, 2.6,2,1.4,1.2,1.02,1.01,1],
    'RBF': [4.6, 4.4, 3.3, 2.2,1.4,0.8,0.6,0.5,0.42,0.41],
    'Piecewise Linear': [4.6, 1.7, 0.11, 0.05,0.04,0.05,0.04,0.05,0.04,0.05]
}
acc_data = {
    'RBF': [50, 83, 40],
    'Sigmoid': [60, 77, 50],
    'Linear (LoRA)': [80, 84, 60],
    'Piecewise Linear': [80, 85, 61]
}
categories = ['Natural', 'Specialized', 'Structured']

colors = ['#0B5CA4', '#00B844', '#FE9400', '#FE2B00'] 

plt.figure(figsize=(15, 5))

# Subplot 1: MSE Loss vs Rank
plt.subplot(1, 3, 1)
for i, (method, data) in enumerate(mse_loss.items()):
    plt.plot(rank, data, marker='o', label=method, color=colors[i])
plt.xlabel('Rank',fontsize=18)
plt.ylabel('MSE Loss',fontsize=18)
plt.yticks(fontsize=12)
plt.xticks([0,20,40,60],fontsize=12)
plt.legend(loc='upper right',edgecolor='none',facecolor='none',fontsize=14)
plt.title('(a)' ,y=-0.2,fontsize=18,fontweight='bold',pad=-10)
plt.tick_params(top=True, right=True,direction='in')
plt.grid(False)

# Subplot 2: Mean Acc. by category
plt.subplot(1, 3, 2)
x = np.arange(len(categories))
width = 0.2
# for i, (method, acc_values) in enumerate(acc_data.items()):
#     plt.bar(x + i*width, acc_values, width, label=method, color=colors[i])
plt.bar(x+2*width,[80, 84, 60],width,label='Linear (LoRA)',color='#0B5CA4')
plt.bar(x+1*width,[60, 77, 50],width,label='Sigmoid',color='#00B844')

plt.bar(x+0*width,[50, 83, 40],width,label='RBF',color='#FE9400')
plt.bar(x+3*width,[80, 85, 61],width,label='Piecewise Linear',color='#FE2B00')




plt.xlabel('(Rank=8)',fontsize=18)
plt.ylabel('Mean Acc. (%)',fontsize=18)
plt.ylim(38,100)
plt.yticks([40,60,80,100],fontsize=14)
plt.xticks(x + width*1.5, categories,fontsize=12)
plt.legend(loc='upper right',ncol=2,edgecolor='none',facecolor='none',fontsize=11.5)
plt.title('(b)',y=-0.2,fontsize=18,fontweight='bold',pad=-10)
plt.tick_params(top=True, right=True,direction='in')
plt.grid(False)

# Subplot 3: Training Loss vs Epoch
plt.subplot(1, 3, 3)
for i, (method, data) in enumerate(training_loss.items()):
    plt.plot(epochs1, data, marker='o', label=method, color=colors[i])
plt.ylim(-0.2,4.8)
plt.xlim(-5,95)
plt.xlabel('Epoch',fontsize=18)
plt.ylabel('Training Loss',fontsize=18)
plt.legend(loc='upper right',edgecolor='none',facecolor='none',fontsize=14)
plt.title('(c)',y=-0.2,fontsize=18,fontweight='bold',pad=-10)
plt.tick_params(top=True, right=True,direction='in')
plt.grid(False)

plt.tight_layout()
plt.savefig('kernel_func_abl.png')