
import pandas as pd
from matplotlib import pyplot as plt

# plt.gcf() # Get current figure
# plt.gca() # Get current axis

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

## Plotting: Regular method, All Plots in One Figure
# plt.plot(ages, py_salaries, label = 'Python')
# plt.plot(ages, js_salaries, label = 'JavaScript')

# plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

# plt.legend()

# plt.title('Median Salary (USD) by Age')
# plt.xlabel('Ages')
# plt.ylabel('Median Salary (USD)')



## Plotting Using Subplots
# fig = figure
# ax = axes
# ax is set to (1 by 1) by default if no arguments are given
# fig, ax = plt.subplots() # 1x1 subplot
# fig, ax = plt.subplots(nrows = 2, ncols = 1) # 2x1 subplot
# fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1) # 2x1 subplot axes labeled separately
# fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True) # 2x1 subplot axes share X

fig1, ax1 = plt.subplots() # 2 figures with one axis only
fig2, ax2 = plt.subplots() # 2 figures with one axis only

# Print Current Axes
# print(ax)
# print(ax1)
# print(ax2)

ax1.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

ax2.plot(ages, py_salaries, label = 'Python')
ax2.plot(ages, js_salaries, label = 'JavaScript')


ax1.legend()
# set_*, where * - title, xlabel, or ylabel is used for subplots in syntax
ax1.set_title('Median Salary (USD) by Age')
# ax1.set_xlabel('Ages')
ax1.set_ylabel('Median Salary (USD)')


ax2.legend()
# set_*, where * - title, xlabel, or ylabel is used for subplots in syntax
# ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

fig1.savefig('fig1.png')
fig2.savefig('fig2.png')