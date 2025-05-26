import matplotlib.pyplot as plt

# Sample data
x = [50, 100, 150, 200, 250, 300, 350, 400]
xred = [48, 55, 71, 77]
xgreen = [20, 40, 55 , 90, 155]
xblue = [140, 150, 220, 390]

ours_psnr = [33.1, 33.9, 34.2, 34.4]
TetriRF_psnr = [31.7, 32.1, 32.3, 32.5, 32.7]
ReRF_psnr = [27.8, 29.9, 32.2, 33.5]

ours_ssim = [0.956, 0.961, 0.964, 0.9655]
TetriRF_ssim = [0.9501, 0.952, 0.9521, 0.953, 0.9531]
ReRF_ssim = [0.926, 0.937, 0.95, 0.958]

ours_lpips = [0.117, 0.107, 0.1, 0.095]
TetriRF_lpips = [0.121, 0.119, 0.118, 0.114, 0.113]
ReRF_lpips = [0.168, 0.148, 0.126, 0.118]

# Plotting
fig, axes = plt.subplots(1, 3, figsize=(12, 4))  # Adjust height to make plots flatter

# PSNR Plot
axes[0].plot(xred, ours_psnr, 'o-', color='red', label='Ours',linewidth=2)
axes[0].plot(xgreen, TetriRF_psnr, 'o-', color='green', label='TeTriRF',linewidth=2)
axes[0].plot(xblue, ReRF_psnr, 'o-', color='tab:blue', label='ReRF',linewidth=2)
axes[0].set_ylabel('PSNR', fontsize=20)
axes[0].set_xlabel('Per Frame Size (KB)', fontsize=20)
axes[0].set_xlim(0, 450)
axes[0].set_ylim(27, 35)
axes[0].grid(True, linestyle='--')  # Change to dashed grid

# SSIM Plot
axes[1].plot(xred, ours_ssim, 'o-', color='red', label='Ours',linewidth=2)
axes[1].plot(xgreen, TetriRF_ssim, 'o-', color='green', label='TeTriRF',linewidth=2)
axes[1].plot(xblue, ReRF_ssim, 'o-', color='tab:blue', label='ReRF',linewidth=2)
axes[1].set_ylabel('SSIM', fontsize=20)
axes[1].set_xlabel('Per Frame Size (KB)', fontsize=20)
axes[1].set_xlim(0, 450)
axes[1].set_ylim(0.92, 0.97)
axes[1].grid(True, linestyle='--')  # Change to dashed grid

# LPIPS Plot
axes[2].plot(xred, ours_lpips, 'o-', color='red', label='Ours',linewidth=2)
axes[2].plot(xgreen, TetriRF_lpips, 'o-', color='green', label='TeTriRF',linewidth=2)
axes[2].plot(xblue, ReRF_lpips, 'o-', color='tab:blue', label='ReRF',linewidth=2)
axes[2].set_ylabel('LPIPS', fontsize=20)
axes[2].set_xlabel('Per Frame Size (KB)', fontsize=20)
axes[2].set_xlim(0, 450)
axes[2].set_ylim(0.07, 0.18)
axes[2].grid(True, linestyle='--')  # Change to dashed grid

# Adjust Legend
fig.legend(['Ours (red)', 'TeTriRF (green)', 'ReRF (blue)'], loc='upper center', ncol=3, bbox_to_anchor=(0.5, 1), fontsize=16, markerscale=1)

plt.tight_layout(rect=[0, 0, 1, 0.88])
plt.savefig('HumanRF_test_fig.png')
