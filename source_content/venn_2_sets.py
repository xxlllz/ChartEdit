import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# Define the subsets sizes
subsets = (2452, 1639, 299)  # T-CVAE only, GAN only, T-CVAE and GAN

# Create the Venn diagram
venn = venn2(subsets=subsets, set_labels=('T-CVAE', 'GAN'))

# Set the colors with transparency for each section of the Venn diagram
venn.get_patch_by_id('10').set_color('limegreen')
venn.get_patch_by_id('10').set_alpha(1.0)

venn.get_patch_by_id('01').set_color('royalblue')
venn.get_patch_by_id('01').set_alpha(0.85)

venn.get_patch_by_id('11').set_color('c')  # T-CVAE and GAN (PaleTurquoise)
venn.get_patch_by_id('11').set_alpha(0.8)

# Add borders (edgecolor) to the circles
venn.get_patch_by_id('10').set_edgecolor('lightGreen')
venn.get_patch_by_id('10').set_linewidth(2)  # Set border width

venn.get_patch_by_id('01').set_edgecolor('steelBlue')
venn.get_patch_by_id('01').set_linewidth(2)  # Set border width

venn.get_patch_by_id('11').set_edgecolor('paleturquoise') 
venn.get_patch_by_id('11').set_linewidth(2)  # Set border width

# Get the text labels and set their properties
venn.get_label_by_id('10').set_fontsize(20)
venn.get_label_by_id('01').set_fontsize(20)
venn.get_label_by_id('11').set_fontsize(20)

# Draw the plot
plt.title('T-CVAE vs GAN', fontsize=20)
plt.savefig('venn_2_sets.png')