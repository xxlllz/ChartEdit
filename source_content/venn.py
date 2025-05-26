import matplotlib.pyplot as plt
from matplotlib_venn import venn3

# Define the subsets sizes
subsets = {'100': 2452,  # T-CVAE only
           '010': 1639,  # GAN only
           '001': 1407,  # T-VAE only
           '110': 299,   # T-CVAE and GAN
           '101': 622,   # T-CVAE and T-VAE
           '011': 289,   # GAN and T-VAE
           '111': 202}   # T-CVAE, GAN, and T-VAE

# Create the Venn diagram
venn = venn3(subsets=subsets, set_labels=('T-CVAE', 'GAN', 'T-VAE'))

# Set the colors with transparency
venn.get_patch_by_id('100').set_color('#98fb98')  # LightGreen
venn.get_patch_by_id('100').set_alpha(1.0)
venn.get_patch_by_id('010').set_color('#4682b4')  # SteelBlue
venn.get_patch_by_id('010').set_alpha(0.85)
venn.get_patch_by_id('001').set_color('#6a5acd')  # SlateBlue
venn.get_patch_by_id('001').set_alpha(0.85)
venn.get_patch_by_id('110').set_color('#afeeee')  # PaleTurquoise
venn.get_patch_by_id('110').set_alpha(0.8)
venn.get_patch_by_id('101').set_color('#87ceeb')  # SkyBlue
venn.get_patch_by_id('101').set_alpha(0.75)
venn.get_patch_by_id('011').set_color('#4682b4')  # SteelBlue
venn.get_patch_by_id('011').set_alpha(0.7)
venn.get_patch_by_id('111').set_color('#afeeee')  # PaleTurquoise
venn.get_patch_by_id('111').set_alpha(0.65)

# Draw the plot
plt.savefig('venn.png')
