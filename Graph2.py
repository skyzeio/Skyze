'''
Created on 06/09/2017

@author: michaelnew

From https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/

'''


import pandas as pd
import numpy as np

# Possible fix
# import matplotlib
# matplotlib.use("gtk")

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

import pylab



import datetime as dt

from Market import Market

class GraphCandlestick2(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    

    def graph_data(self,p_df_ohlc):
#         print("DF_OHLC .. before reset index"); print(p_df_ohlc.head(5))
        #Reset the index to remove Date column from index
        #df_ohlc = p_df_ohlc.reset_index()
        df_ohlc = p_df_ohlc
#         print("DF_OHLC .. after reset index"); print(df_ohlc.head(5))
        
        #Naming columns
        df_ohlc.columns = ["Date","Open","High",'Low',"Close"]
        
        #Converting dates column to float values
        df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)
        
        #Making plot
        fig = plt.figure()
        ax1 = plt.subplot2grid((6,1), (0,0), rowspan=6, colspan=1)
        
        #Converts raw mdate numbers to dates
        ax1.xaxis_date()
        plt.xlabel("Date")
        print("DF_OHLC .. after date2num in graph_data"); print(df_ohlc.head(5))
        
        #Making candlestick plot
        candlestick_ohlc(ax1,df_ohlc.values,width=1, colorup='g', colordown='k',alpha=0.75)
        # Parameters:    
#             ax : Axes... an Axes instance to plot to
#             quotes :    sequence of (time, open, high, low, close, ...) sequences
#                         As long as the first 5 elements are these values, the record can be as long as you want (e.g., it may store volume).
#                         time must be in float days format - see date2num
#             width : float...fraction of a day for the rectangle width
#             colorup : color ... the color of the rectangle where close >= open
#             colordown : color ...the color of the rectangle where close < open
#             alpha : float ... the rectangle alpha level
        plt.ylabel("Price")
        plt.legend()
        
#         fig.autofmt_xdate() #??
        plt.close('all')
        print("Mike - about to plt.show")
        plt.show()
        
    def testGraph(self):
        data = [1,1,2,3,5,8,13,21,34]

#         plt.figure
#         plt.title('mike', size = 'xx-large')
#         plt.plot(data)
#         plt.show()
#         %matplotlib inline
        plt.ion()
        plt.plot(data)
        pylab.show()




if __name__ == "__main__":
    
    mkt_name = "Bitcoin"
    mkt = Market(mkt_name)
    mkt_data = mkt.readMarketDataCSV()
    
    graph = GraphCandlestick2()
    quotes = mkt_data.loc[:20,"Date":"Close"]
    print("quotes"); print(quotes.head(5))
    #graph.graph_data(quotes)
    graph.testGraph()
    print("plotted")
        
        
        
# matplotlib.finance.candlestick_ohlc(ax, quotes, width=0.2, colorup='k', colordown='r', alpha=1.0)
# 
# Parameters:    
#             ax : Axes... an Axes instance to plot to
#             quotes :    sequence of (time, open, high, low, close, ...) sequences
#                         As long as the first 5 elements are these values, the record can be as long as you want (e.g., it may store volume).
#                         time must be in float days format - see date2num
#             width : float...fraction of a day for the rectangle width
#             colorup : color ... the color of the rectangle where close >= open
#             colordown : color ...the color of the rectangle where close < open
#             alpha : float ... the rectangle alpha level
#              
# Returns:    ret : tuple
#                 returns (lines, patches) where lines is a list of lines added and patches is a list of the rectangle patches added