'''
Created on 06/09/2017

@author: michaelnew

From https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/

'''


import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc

import numpy as np
import datetime as dt

from Market import Market

class GraphCandlestick(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    

    def graph_data(self,stock,ohlc):
    
        fig = plt.figure()
        ax1 = plt.subplot2grid((1,1), (0,0))
        
        # commented code at the bottom was here to load teh data
            
        candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
    
        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.grid(True)
        
    
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title(stock)
        plt.legend()
        plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
        plt.show()







if __name__ == "__main__":
    
    mkt_name = "Bitcoin"
    mkt = Market(mkt_name)
    mkt_data = mkt.readMarketDataCSV(p_test=True)
    
    graph = GraphCandlestick()
    quotes = mkt_data.loc[:,"Date":"Close"]
    print(quotes.head(10))
    graph.graph_data(mkt_name, quotes)
#     run(config, testing, tickers, filename)
        


# === PREVIOUS LOAD DATA CODE ==================================
# def bytespdate2num(fmt, encoding='utf-8'):
#     strconverter = mdates.strpdate2num(fmt)
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#     return bytesconverter
# 
# 
# 
# 
# # 
#     # Unfortunately, Yahoo's API is no longer available
#     # feel free to adapt the code to another source, or use this drop-in replacement.
#     stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
#     source_code = urllib.request.urlopen(stock_price_url).read().decode()
#     stock_data = []
#     split_source = source_code.split('\n')
#     
#     for line in split_source:
#         split_line = line.split(',')
#         if len(split_line) == 7:
#             if 'values' not in line and 'labels' not in line:
#                 stock_data.append(line)
#     
#     print(len(source_code))
#     print(len(stock_data))
#   #  print(source_code)
#     print(stock_data[:30])
# 
#     
#     date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
#                                                           delimiter=',',
#                                                           unpack=True,
#                                                           converters={0: bytespdate2num('%Y-%m-%d')})
# 
#     print("HEREREREREE")
# 
# 
#     x = 0
#     y = len(date)
#     ohlc = []
# 
#     while x < y:
#         append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
#         ohlc.append(append_me)
#         x+=1