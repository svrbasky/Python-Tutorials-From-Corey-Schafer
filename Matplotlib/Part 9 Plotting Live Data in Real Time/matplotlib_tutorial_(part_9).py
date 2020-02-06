
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt

# Import library for animated plot
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

## Sample Data (Static)
# x_vals = [0, 1, 2, 3, 4, 5]
# y_vals = [0, 1, 3, 2, 3, 5]

# plt.plot(x_vals, y_vals)


## Sample Data (Dynamic)
x_vals = []
y_vals = []

plt.plot(x_vals, y_vals)

## Dynamic counting
index = count() 
# count() from itertools library counts up one number at a time

# function to append x and y values 
# def animate(i):
# 	x_vals.append(next(index)) # count x_vals sequentially.
# 	y_vals.append(random.randint(0, 5)) # appends y_values randomly by a number between 0 and 5

# 	# Plotting
# 	# plt.plot(x_vals, y_vals) # this method plots multiple colored lines

# 	plt.cla() # Clear Axis: This rectifies the problem
# 	plt.plot(x_vals, y_vals) 


# ## Animated Plot
# # plt.gcf() = Get current figure
# # animate = function to pass the animation on (our custom defined function)
# # interval = 1000 ==> 1000 ms ==> 1 s
# ani = FuncAnimation(plt.gcf(), animate, interval = 1000)


# plt.tight_layout()
# plt.show()

## Real-Time Data
# data = pd.read_csv('data.csv')
# x = data['x_value']
# y1 = data['total_1']
# y2 = data['total_2']

def animate(i):
	## Real-Time Data
	data = pd.read_csv('data.csv') # Reading data from live data
	x = data['x_value'] # X_values
	y1 = data['total_1'] # Y_1
	y2 = data['total_2'] # Y_2

	plt.cla() # Clear Axis: This rectifies the problem

	plt.plot(x, y1, label = 'Channel 1') 
	plt.plot(x, y2, label = 'Channel 2') 

	plt.legend(loc = 'upper left')
	plt.tight_layout()



## Animated Plot
# plt.gcf() = Get current figure
# animate = function to pass the animation on (our custom defined function)
# interval = 1000 ==> 1000 ms ==> 1 s
ani = FuncAnimation(plt.gcf(), animate, interval = 1000)


plt.tight_layout()
plt.show()