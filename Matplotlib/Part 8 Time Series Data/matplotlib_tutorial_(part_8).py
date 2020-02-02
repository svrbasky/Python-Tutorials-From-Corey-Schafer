import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# # Sample Data
# dates = [
# 	datetime(2019, 5, 24),
# 	datetime(2019, 5, 25),
# 	datetime(2019, 5, 26),
# 	datetime(2019, 5, 27),
# 	datetime(2019, 5, 28),
# 	datetime(2019, 5, 29),
# 	datetime(2019, 5, 30),
# 	]

# y = [0, 1, 3, 4, 6, 5, 7]

# # Plot Sample Data
# # plt.plot_date(dates, y) # just plot
# # plt.plot_date(dates, y, linestyle = 'solid') # plot lines and not just dots

# # Auto-Format Method
# # plt.gcf() = get current figure
# # autofmt_xdate() = auto format the x-axis dates
# # plt.gcf().autofmt_xdate()

# # Change Date Format
# date_format = mpl_dates.DateFormatter('%b, %d %Y') 
# # %b = abbreviated name of the month
# # %d = day
# # %Y = 4 digit year

# # Add Changed Format to Figure
# # plt.gca() = get current axis
# # set_major_formatter() = Set major format of the the axis
# plt.gca().xaxis.set_major_formatter(date_format)


# Load Data
data = pd.read_csv('data.csv')

# Convert Dates into Datetime Format
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values('Date', inplace = True) 

price_date = data['Date'] # Dates are loaded as string if loaded straight from the file
price_close = data['Close']

# Plot Loaded Data
plt.plot_date(price_date, price_close, linestyle = 'solid') # plot lines and not just dots

# Auto-Format Method
plt.gcf().autofmt_xdate()


plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()