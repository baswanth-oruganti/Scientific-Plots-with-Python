import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set up the figure and subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
x = np.linspace(-3, 3, 500)

# Plot for Unitary Transformation (More Skewed Gaussian)
# Original Gaussian
original_gaussian = norm.pdf(x, 0, 1)
# More Skewed Gaussian for Unitary Transformation
more_skewed_gaussian = norm.pdf(x, 1, 0.7)

# Plot Original and More Skewed Gaussian with Blue Shading
axes[0].plot(x, original_gaussian, label="Original Gaussian", color='blue', linestyle="--")
axes[0].fill_between(x, original_gaussian, color='blue', alpha=0.1)
axes[0].plot(x, more_skewed_gaussian, label="After Unitary Transformation", color='green')
axes[0].fill_between(x, more_skewed_gaussian, color='green', alpha=0.2)

# Bars below the curves for Unitary Transformation
axes[0].bar(x[::50], original_gaussian[::50], color='blue', width=0.25, alpha=0.2)
axes[0].bar(x[::50], more_skewed_gaussian[::50], color='green', width=0.25, alpha=0.2)

# Add arrow annotations to indicate recoverability
axes[0].annotate("Original\nrecoverable\nby inverse",
                 xy=(1.5, 0.35), xytext=(0.3, 0.4),
                 fontsize=10, ha="center")

# Set labels and legend
axes[0].set_title("Unitary Transformation (More Skewed Redistribution)")
axes[0].legend()
axes[0].set_xlabel("State")
axes[0].set_ylabel("Probability Density")
axes[0].text(-2.5, 0.35, "Area under curve = 1", fontsize=10, color="black")

# Plot for Non-Unitary Transformation (Collapse to Single Outcome)
# Collapsed state as a Dirac-like spike
collapsed = np.zeros_like(x)
collapsed[np.abs(x - 1).argmin()] = 1  # Set one point to a spike

# Plot Gaussian Before Collapse and Dirac Spike
axes[1].plot(x, original_gaussian, label="Original Gaussian", color='blue', linestyle="--")
axes[1].fill_between(x, original_gaussian, color='blue', alpha=0.1)
axes[1].plot(x, collapsed, label="After Non-Unitary (Collapse)", color='red')
axes[1].fill_between(x, collapsed, color='red', alpha=0.6)

# Bars below the curves for Non-Unitary Transformation
axes[1].bar(x[::50], original_gaussian[::50], color='blue', width=0.25, alpha=0.2)
axes[1].bar(x[::50], collapsed[::50], color='red', width=0.25, alpha=0.6)

# Set titles, labels, and legend
axes[1].set_title("Non-Unitary Transformation (Collapse)")
axes[1].legend()
axes[1].set_xlabel("State")
axes[1].set_ylabel("Probability Density")
axes[1].text(-2.5, 0.35, "Collapsed to one outcome", fontsize=10, color="black")




plt.tight_layout()
plt.show()

