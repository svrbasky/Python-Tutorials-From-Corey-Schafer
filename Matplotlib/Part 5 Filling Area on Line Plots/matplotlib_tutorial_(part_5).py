import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color = '#444444', linestyle = '--', label = 'All Devs')

plt.plot(ages, py_salaries, label = 'Python')

overall_median = 57287 # median of salaries

# plt.fill_between(ages, py_salaries) # fill between
# plt.fill_between(ages, py_salaries, alpha = 0.25) # fill between with alpha at 25% which means 25% opacity.
# plt.fill_between(ages, py_salaries, overall_median, alpha = 0.25) # fill between python salaries and overall median.

# plt.fill_between(ages, py_salaries, overall_median, 
# 				 where = (py_salaries > overall_median), 
# 				 interpolate = True, alpha = 0.25) # conditional fill-between python salaries and overall median. only fill above median.

# plt.fill_between(ages, py_salaries, overall_median, 
# 				 where = (py_salaries > overall_median), 
# 				 interpolate = True, color = 'green', alpha = 0.25) # conditional fill-between python salaries and overall median. only fill above median. color = green

# plt.fill_between(ages, py_salaries, overall_median, 
# 				 where = (py_salaries <= overall_median), 
# 				 interpolate = True, alpha = 0.25) # conditional fill-between python salaries and overall median. only fill below median.

# plt.fill_between(ages, py_salaries, overall_median, 
# 				 where = (py_salaries <= overall_median), 
# 				 interpolate = True, color =  'red', alpha = 0.25) # conditional fill-between python salaries and overall median. only fill below median. color = red



# ## Fill between Python salaries and Developer Salaries
# plt.fill_between(ages, py_salaries, dev_salaries, 
# 				 where = (py_salaries > dev_salaries), 
# 				 interpolate = True, color = 'green', alpha = 0.25) # conditional fill-between python salaries and developer salaries. 
# # only fill above with color = green

# plt.fill_between(ages, py_salaries, dev_salaries, 
# 				 where = (py_salaries <= dev_salaries), 
# 				 interpolate = True, color =  'red', alpha = 0.25) # conditional fill-between python salaries and developer salaries. 
# # only fill below with color = red

## Fill between Python salaries and Developer Salaries with labels for fills
plt.fill_between(ages, py_salaries, dev_salaries, 
				 where = (py_salaries > dev_salaries), 
				 interpolate = True, color = 'green', alpha = 0.25, label = 'Above Avg') # conditional fill-between python salaries and developer salaries. 
# only fill above with color = green. Labels added.

plt.fill_between(ages, py_salaries, dev_salaries, 
				 where = (py_salaries <= dev_salaries), 
				 interpolate = True, color =  'red', alpha = 0.25, label = 'Below Avg') # conditional fill-between python salaries and developer salaries. 
# only fill below with color = red. Labels added.


plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()
