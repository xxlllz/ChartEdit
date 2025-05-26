import matplotlib.pyplot as plt

categories = [
    'novel', 'contain rich info', 'no minor errors', 'no moderate errors', 
    'no severe errors', 'clarify intent', 'show empathetic', 'satisfy constraints', 
    'support stances', 'correct mistakes', 'lengthy'
]
human_data = [54, 59, 49.6, 58,  68, 50, 50.5,52, 51, 10, 65]
gpt4_data = [55.5, 67, 10, 67,  83, 53, 49.7,10, 50, 51.5, 62]
llama_data = [56.5, 66, 50.5, 62,  60,49.5 ,51, 51, 49, 51, 72]

fig, ax = plt.subplots(figsize=(18, 5))
x = range(len(categories))

ax.scatter(x, human_data, color='royalblue', s=350, label='Human', alpha=0.7)
ax.scatter(x, gpt4_data, color='orange', s=350, label='GPT-4-Turbo', alpha=0.7)
ax.scatter(x, llama_data, color='green', s=350, label='LLaMA-2-70B-Chat', alpha=0.7)

ax.axhline(y=50, color='red', linestyle='--', linewidth=2)

ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=20, ha='right', rotation_mode='anchor',fontsize=18)
ax.set_ylim(42, 88)# 修改纵坐标刻度
ax.set_yticks([50, 60, 70, 80])
ax.set_yticklabels([ 50, 60, 70, 80],fontsize=16)
ax.set_ylabel('Probability of Preferred (%)',fontsize=20)
ax.legend(loc='upper left',fontsize=18)
plt.grid(True)

plt.tight_layout()
plt.savefig('scatter7.png')