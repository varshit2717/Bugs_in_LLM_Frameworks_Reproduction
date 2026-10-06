# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

# # Data
# categories = [
#     "R1", 
#     "R2",
#     "R3",
#     "R4",
#     "R5",
#     "R6",
#     "R7",
#     "R8",
#     "R9"
# ]

# frameworks = ["LC", "LI", "HS", "Total"]

# # Raw data for each framework
# raw_data = np.array([
#     [139, 112, 3, 254],  # API Misuse
#     [36, 15, 5, 56],     # Incompatibility
#     [22, 19, 0, 41],     # Assignment Issue
#     [96, 59, 5, 160],    # Parameter/Argument Issue
#     [163, 182, 45, 390], # Code Logic Issue
#     [19, 13, 4, 36],     # Import Error
#     [27, 19, 2, 48],     # Typo
#     [14, 14, 3, 31],     # Incorrect Exception Handling
#     [5, 3, 2, 10]        # Incorrect Numerical Computation
# ])

# # Calculate column sums for normalization
# column_sums = np.sum(raw_data, axis=0)

# # Create normalized data
# normalized_data = np.zeros_like(raw_data, dtype=float)
# for j in range(len(frameworks)):
#     normalized_data[:, j] = raw_data[:, j] / column_sums[j] * 100

# # Create the figure and set its size
# plt.figure(figsize=(14, 10))

# # Create a blank heatmap without annotations first
# ax = sns.heatmap(normalized_data, annot=False, fmt=".1f", cmap="Blues", 
#                  xticklabels=frameworks, 
#                  yticklabels=categories,
#                  vmin=0, vmax=35,  # Set fixed range for better contrast 
#                  cbar_kws={'label': 'Percentage within Framework (%)'})

# # Add custom annotations with both percentage and raw count
# for i in range(len(categories)):
#     for j in range(len(frameworks)):
#         # Determine text color based on cell intensity for better readability
#         cell_value = normalized_data[i, j]
#         if cell_value > 18:  # Threshold for switching text color
#             text_color = 'white'
#         else:
#             text_color = 'black'
            
#         text = f"{cell_value:.1f}% ({raw_data[i, j]})"
#         plt.text(j + 0.5, i + 0.5, text, 
#                 ha='center', va='center', color=text_color, 
#                 fontsize=21, fontweight='normal')

# # Remove title and axis labels
# plt.title('')
# plt.xlabel('')
# plt.ylabel('')

# # Make tick labels bold and larger
# plt.xticks(rotation=0, ha='center', fontweight='normal', fontsize=25)
# plt.yticks(rotation=0, fontweight='normal', fontsize=25)

# # Make colorbar label and ticks bold and larger
# cbar = ax.collections[0].colorbar
# cbar.ax.set_ylabel('Percentage within Framework (%)', fontweight='normal', fontsize=21)
# cbar.ax.tick_params(labelsize=14)
# for l in cbar.ax.yaxis.get_ticklabels():
#     l.set_weight('normal')
#     l.set_fontsize(18)

# # Add a border around each cell for better delineation
# for _, spine in ax.spines.items():
#     spine.set_visible(True)
#     spine.set_linewidth(1.5)

# # Adjust layout to make sure everything fits
# plt.tight_layout()

# # Save and show the plot
# plt.savefig('normalized_root_cause_framework_distribution.png', dpi=300, bbox_inches='tight')
# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.colors as mcolors

# Data
categories = [
    "S1", 
    "S2",
    "S3",
    "S4",
    "S5",
    "S6"
]

frameworks = ["LC", "LI", "HS", "Total"]

# Raw data for each framework
raw_data = np.array([
    [185, 114, 27, 326],  # Crash
    [120, 175, 20, 315],  # Incorrect Functionality
    [82, 77, 10, 169],    # Unexpected Output
    [15, 11, 3, 29],      # Hang
    [76, 24, 3, 103],     # External Connection Failure
    [43, 35, 6, 84]       # Unidentified
])

# Calculate column sums for normalization
column_sums = np.sum(raw_data, axis=0)

# Create normalized data
normalized_data = np.zeros_like(raw_data, dtype=float)
for j in range(len(frameworks)):
    normalized_data[:, j] = raw_data[:, j] / column_sums[j] * 100

# Create the figure and set its size
plt.figure(figsize=(14, 10))

# Create a custom colormap with stronger contrast
cmap = sns.color_palette("Blues", as_cmap=True)
# Alternative with more contrast: cmap = plt.cm.Blues_r

# Create a blank heatmap without annotations first
ax = sns.heatmap(normalized_data, annot=False, fmt=".1f", cmap=cmap, 
                 xticklabels=frameworks, 
                 yticklabels=categories,
                 vmin=0, vmax=45,  # Set fixed range for better contrast
                 cbar_kws={'label': 'Percentage within Framework (%)'})

# Add custom annotations with both percentage and raw count
for i in range(len(categories)):
    for j in range(len(frameworks)):
        # Determine text color based on cell intensity for better readability
        cell_value = normalized_data[i, j]
        if cell_value > 25:  # Threshold for switching text color
            text_color = 'white'
        else:
            text_color = 'black'
            
        text = f"{cell_value:.1f}% ({raw_data[i, j]})"
        plt.text(j + 0.5, i + 0.5, text, 
                ha='center', va='center', color=text_color, 
                fontsize=21, fontweight='normal')

# Remove title and axis labels
plt.title('')
plt.xlabel('')
plt.ylabel('')

# Make tick labels bold and larger
plt.xticks(rotation=0, ha='center', fontweight='normal', fontsize=25)
plt.yticks(rotation=0, fontweight='normal', fontsize=25)

# Make colorbar label and ticks bold and larger
cbar = ax.collections[0].colorbar
cbar.ax.set_ylabel('Percentage within Framework (%)', fontweight='normal', fontsize=23)
cbar.ax.tick_params(labelsize=14)
for l in cbar.ax.yaxis.get_ticklabels():
    l.set_weight('normal')
    l.set_fontsize(18)

# Add a border around each cell for better delineation
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1.5)

# Adjust layout to make sure everything fits
plt.tight_layout()

# Save and show the plot
plt.savefig('normalized_symptoms_framework_distribution.png', dpi=300, bbox_inches='tight')
plt.show()