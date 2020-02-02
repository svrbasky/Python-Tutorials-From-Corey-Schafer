
import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1] # Sample Data (X-axis)
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1] # Sample Data (y-axis)

# Plotting
# plt.scatter(x, y) # plain
# plt.scatter(x, y, s = 100) # custom size of dots
# plt.scatter(x, y, s = 100, c = 'green') # custom marker color
# plt.scatter(x, y, s = 100, c = 'green', marker = 'X') # custom marker shape
# plt.scatter(x, y, s = 100, c = 'green', edgecolor = 'black', linewidth = 1, alpha = 0.7) # add edgecolor, linewidth and transparency (alpha) to the markers

# Colors
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5] # colors correspond to dataset

# plt.scatter(x, y, s = 100, c = colors, edgecolor = 'black', linewidth = 1, alpha = 0.7) # custom colors for each marker (grayscale)
# plt.scatter(x, y, s = 100, c = colors, cmap = 'Greens', edgecolor = 'black', linewidth = 1, alpha = 0.7) # custom colors for each marker (color map)


# Sizes
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539] # sizes correspond to dataset

# plt.scatter(x, y, s = sizes, c = colors, cmap = 'Greens', edgecolor = 'black', linewidth = 1, alpha = 0.7) # custom sizes and colors for each marker (color map)

# Color Bar
# cbar = plt.colorbar()
# cbar.set_label('Satisfaction')

# Real-World Data
data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

# plt.scatter(view_count, likes, edgecolor = 'black', linewidth = 1, alpha = 0.75) # plot real-world data with mostly defaults
plt.scatter(view_count, likes, c = ratio, cmap = 'summer', edgecolor = 'black', linewidth = 1, alpha = 0.75) # plot real-world data with color according to ratio

cbar = plt.colorbar()
cbar.set_label('Like/Dislike Ratio')

# Set axes scales to logarithmic to better view outliers
plt.xscale('log')
plt.yscale('log')



plt.title('Trending Youtube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
