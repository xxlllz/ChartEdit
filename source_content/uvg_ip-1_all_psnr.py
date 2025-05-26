import matplotlib.pyplot as plt

# Data
bit_rate1 = [0.018, 0.027, 0.041, 0.073]
psnr_ecvc = [36.1, 36.95, 37.8, 38.7]

bit_rate2 = [0.009, 0.018, 0.032, 0.054]
psnr_dcvc_fm = [34.6, 35.8, 36.95, 37.8]

bit_rate3 = [0.016, 0.024, 0.0395, 0.064]
psnr_dcvc_dc = [34.8, 36.0, 37.1, 38.09]

# Create figure and axis
fig, ax = plt.subplots()

# Plot the lines with different styles
ax.plot(bit_rate1, psnr_ecvc, '-o', color='brown', label='ECVC (Ours)')
ax.plot(bit_rate2, psnr_dcvc_fm, '-s', color='rosybrown', label='DCVC-FM (CVPR\'24)')
ax.plot(bit_rate3, psnr_dcvc_dc, '-*', color='deepskyblue', label='DCVC-DC (CVPR\'23)')

# Set title and labels
ax.set_title('UVG')
ax.set_xlabel('Bit-rate[bpp]')
ax.set_ylabel('PSNR[dB]')
ax.set_ylim((34.4,39))
ax.set_yticks([35,36,37,38,39])
ax.set_xticks([0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08])


# Show legend
ax.legend(loc='lower right')

# Set grid
ax.grid(True)

# Show plot
plt.tight_layout()
plt.savefig('uvg_ip-1_all_psnr.png')