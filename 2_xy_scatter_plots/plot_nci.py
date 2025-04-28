import sys
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import cm
from matplotlib.colors import LinearSegmentedColormap

# Load the data from your file into a DataFrame (replace 'your_data_file.dat' with the actual filename)
data = pd.read_csv(sys.argv[1], delim_whitespace=True, header=None)
# Assuming the first column is sign(λ2)ρ and the second column is RDG (s)
sign_lambda_rho = data[0]
rdg = data[1]

# Create the plot
fig, ax = plt.subplots(figsize=(3.25, 4))



# Set the colormap to a diverging one that goes from blue to green to red
#cmap = cm.get_cmap('turbo')
colors = [(0, 'blue'), (0.5, '#32CD32'), (1, 'red')] 
cmap = LinearSegmentedColormap.from_list("blue_parrot_green_red", colors)

# Define normalization for color scale with zero as a central value
norm = mcolors.TwoSlopeNorm(vmin=-0.07, vcenter=-0.0, vmax=0.07)





# Define the scatter plot with a diverging colormap and set the vmin, vmax directly in the scatter function
scatter = ax.scatter(sign_lambda_rho, rdg, c=sign_lambda_rho, cmap=cmap, norm=norm, s=5,  marker='o')

# Add color bar for reference
cbar = fig.colorbar(scatter, ax=ax)
cbar.set_label(r'sign($\lambda_{2}$)$\rho$ (a.u.)')

# Add labels and title
ax.set_xlabel(r'sign($\lambda_{2}$)$\rho$ (a.u.)')
ax.set_ylabel('RDG (a.u.)')

# Set axis limits if needed
ax.set_xlim([-0.06, 0.06])
ax.set_ylim([0, 1.0])

# Show grid for reference
ax.grid(True)

# Display the plot
plt.show()

