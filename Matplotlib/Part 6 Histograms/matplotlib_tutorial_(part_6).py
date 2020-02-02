import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]


## Load data from csv
# Data from 2019 stackoverflow developer survey
data = pd.read_csv('data.csv')
ids = data['Responder_id']
ages = data['Age']


## bins
# bins = [10, 20, 30, 40, 50, 60]
# bins = [20, 30, 40, 50, 60] # Omit certain bins by omiting that bin limits.
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # expanded bins to plot loaded data.

## Plotting
# plt.hist(ages, bins = 5) # 5 bins
# plt.hist(ages, bins = 5, edgecolor = 'black') # with edge colors
# plt.hist(ages, bins = bins, edgecolor = 'black') # with edge colors bins = bins
plt.hist(ages, bins = bins, edgecolor = 'black', log = True) # logarithmic histogram


## Threshold line
median_age = 29
color = '#fc4f30'

# Plot median
# plt.axvline(median_age, color = color, label = 'Age Median')
plt.axvline(median_age, color = color, label = 'Age Median', linewidth = 2) # Thin median line

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()
