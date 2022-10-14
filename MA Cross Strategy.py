#!/usr/bin/env python
# coding: utf-8

# In[187]:


# import necessary libraries 

get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from tabulate import tabulate
import warnings
warnings.filterwarnings('ignore')
import pandas_datareader.data as web


# In[151]:


# import package
import pandas_datareader.data as web
# set start and end dates 
start = datetime.datetime(2018, 2, 1) 
end = datetime.datetime(2020, 2, 1) 
# extract the closing price data
aap_df = web.DataReader(['AAP'], 'yahoo', start = start, end = end)['Close']
aap_df.columns = {'Close Price'}
#aap_df.head(100)
aap_df.tail(100)


# In[155]:


aap_df['Close Price'].plot(figsize = (15, 8))
plt.grid()
plt.ylabel("Price in USD")
plt.show()


# In[173]:


# create 12 days simple moving average column

aap_df['12_SMA'] = aap_df['Close Price'].rolling(window = 12, min_periods = 1).mean()
# create 26 days simple moving average column
aap_df['26_SMA'] = aap_df['Close Price'].rolling(window = 26, min_periods = 1).mean()
# display first few rows
aap_df.head()


# In[170]:


aap_df['Signal'] = 0.0
aap_df['Signal'] = np.where(aap_df['12_SMA'] > aap_df['26_SMA'], 1.0, 0.0)


# In[172]:


aap_df['Position'] = aap_df['Signal'].diff()
# display first few rows
aap_df.head()


# In[174]:


plt.figure(figsize = (20,10))

#app_df[‘Close Price’].plot(color = ‘k’, label= ‘Close Price’)
aap_df['Close Price'].plot(color ='k', label='Close Price')
aap_df['12_SMA'].plot(color ='b', label='Close Price')
aap_df['26_SMA'].plot(color ='g', label='Close Price')
# plot close price, short-term and long-term moving averages 
#aap_df.head()
#aap_df['Close Price'].plot(color = ‘k’, label= ‘Close Price') 

# plot ‘buy’ signals
plt.plot(aap_df[aap_df['Position'] == 1].index, 
         aap_df['12_SMA'][aap_df['Position'] == 1], 
         '^', markersize = 15, color = 'g', label = 'buy')


# plot ‘sell’ signals
plt.plot(aap_df[aap_df['Position'] == -1].index, 
         aap_df['12_SMA'][aap_df['Position'] == -1], 
         'v', markersize = 15, color = 'r', label = 'sell')
plt.ylabel('Price in USD', fontsize = 15 )
plt.xlabel('Date', fontsize = 15 )
plt.title('ADVANCED AUTO PARTS', fontsize = 20)
plt.legend()
plt.grid()
plt.show()


# In[189]:


def MovingAverageCrossStrategy(stock_symbol = 'AAP', start_date = '2018-01-01', end_date = '2020-01-01', 
                               short_window = 12, long_window = 26, moving_avg = 'SMA', display_table = True):
    '''
    The function takes the stock symbol, time-duration of analysis, 
    look-back periods and the moving-average type(SMA or EMA) as input 
    and returns the respective MA Crossover chart along with the buy/sell signals for the given period.
    '''
    # stock_symbol - (str)stock ticker as on Yahoo finance. Eg: 'ULTRACEMCO.NS' 
    # start_date - (str)start analysis from this date (format: 'YYYY-MM-DD') Eg: '2018-01-01'
    # end_date - (str)end analysis on this date (format: 'YYYY-MM-DD') Eg: '2020-01-01'
    # short_window - (int)lookback period for short-term moving average. Eg: 5, 10, 20 
    # long_window - (int)lookback period for long-term moving average. Eg: 50, 100, 200
    # moving_avg - (str)the type of moving average to use ('SMA' or 'EMA')
    # display_table - (bool)whether to display the date and price table at buy/sell positions(True/False)


# In[190]:


MovingAverageCrossStrategy('HDFC.NS', '2016-08-31', '2020-08-31', 50, 200, 'SMA', display_table = True)

