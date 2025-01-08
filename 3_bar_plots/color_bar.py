import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


plt.rcParams['font.family'] = 'Arial'
plt.rcParams['font.size'] = 9



# Create a custom colormap
colors = ['#000af0', '#3CB043', 'red']  # Sky blue, parrot green, red
cmap = mcolors.LinearSegmentedColormap.from_list('aromaticity_colormap', colors)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(0.7, 5))
fig.subplots_adjust(left=0.3)

# Create the colorbar with reduced width
norm = mcolors.Normalize(vmin=0, vmax=1)
cb = plt.colorbar(
    plt.cm.ScalarMappable(norm=norm, cmap=cmap),
    cax=ax,
    orientation='vertical',
    shrink=0.25,
    aspect=10    # Adjust aspect ratio for a slimmer bar
)

# Add labels
#cb.set_label('', labelpad=5)
cb.ax.set_yticks([0, 0.5, 1])
cb.ax.set_yticklabels(['A', 'WA', 'NA'])

# Add y-axis title

# Save and display the figure
fig.tight_layout()
plt.savefig('aromaticity_colormap.pdf',dpi=600)
plt.savefig('aromaticity_colormap.png',dpi=300)
plt.show()

