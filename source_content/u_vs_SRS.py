import matplotlib.pyplot as plt

# Data
x = [5, 10, 15, 20, 25, 30]
ddpg_no_sc = [0.725, 0.724, 0.723, 0.722, 0.721, 0.720]
ddpg = [0.743, 0.871, 0.919, 0.937, 0.952, 0.960]
td3 = [0.741, 0.869, 0.917, 0.935, 0.950, 0.958]
samaddpg = [0.79, 0.90, 0.938, 0.953, 0.963, 0.973]

# Main plot
fig, ax = plt.subplots(figsize=(7, 5))
ax.plot(x, ddpg_no_sc, 'bo-', label='DDPG_NO_SC')
ax.plot(x, ddpg, 'o-', color='orange', label='DDPG')
ax.plot(x, td3, 'go-', label='TD3')
ax.plot(x, samaddpg, 'ro-', label='SAMADDPG')

ax.set_ylabel('SRS', fontsize=15)
ax.set_xlabel('Intra-platoon Gap (m)', fontsize=15)
plt.tick_params(axis='x', labelsize=12) 
plt.tick_params(axis='y', labelsize=12) 
ax.legend(loc='upper left',fontsize=9)

# Inset plot
ax_inset = ax.inset_axes([0.45, 0.2, 0.5, 0.4])
ax_inset.plot(x, ddpg, 'o-', color='orange', label='DDPG')
ax_inset.plot(x, td3, 'go-', label='TD3')
ax_inset.plot(x, samaddpg, 'ro-', label='SAMADDPG')
ax_inset.set_xlim(23.5, 30)
ax_inset.set_ylim(0.94, 0.98)
ax_inset.set_xticks([25,30])
ax_inset.set_yticks([0.94,0.95,0.96,0.97])
ax_inset.set_xlabel('u (bits/word)', fontsize=10)
ax_inset.set_ylabel('SRS', fontsize=10)

# Adding legends for the inset
ax_inset.legend(loc='lower right', fontsize=8)
plt.tight_layout()
plt.savefig('u_vs_SRS.png', dpi=300)