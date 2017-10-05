"""Created on 06/09/2017

@author: michaelnew

From https://pythonprogramming.net/candlestick-ohlc-graph-matplotlib-tutorial/

end"""


import pandas as pd
import numpy as np
import datetime as datetime

from matplotlib.finance import candlestick2_ohlc
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# fix the no backend issue
import matplotlib as mpl

from Market import Market


class GraphCandlestick3(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def graphData(self, quotes):
        """Works in
        http://localhost:8888/notebooks/Jupyter/OHLC%20Graphs.ipynb
        end"""

        # Fix the no graphics backend issue
        mpl.use('TkAgg')

        fig, ax = plt.subplots()
        candlestick2_ohlc(
            ax, quotes['Open'], quotes['High'], quotes['Low'], quotes['Close'], width=0.6)

        xdate = [datetime.datetime.fromtimestamp(i) for i in quotes['Date']]

        ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

        def mydate(x, pos):
            try:
                return xdate[int(x)]
            except IndexError:
                return ''

        ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))

        fig.autofmt_xdate()
        fig.tight_layout()

        plt.show()

        return

    def testGraph(self):
        data = [1, 1, 2, 3, 5, 8, 13, 21, 34]

#         plt.figure
#         plt.title('mike', size = 'xx-large')
#         plt.plot(data)
#         plt.show()
#         %matplotlib inline
        plt.ion()
        plt.plot(data)
        pylab.show()


if __name__ == "__main__":

    mkt_name = "Bitcoin_Test"
    mkt = Market.fromTesting(mkt_name)
    mkt_data = mkt.readMarketDataCSV(p_testing=True)

    mkt_data = quotes.head(50)

    graph = GraphCandlestick3()
    print("mkt_data")
    print(mkt_data.head(5))
    # graph.graph_data(quotes)
    graph.testGraph()
    graph.graphData(quotes)
    # plt.switch_backend("macosx")
    print("plotted")

#     Backend    Description
# GTKAgg    Agg rendering to a GTK 2.x canvas (requires PyGTK and pycairo or cairocffi; Python2 only)
# GTK3Agg    Agg rendering to a GTK 3.x canvas (requires PyGObject and pycairo or cairocffi)
# GTK    GDK rendering to a GTK 2.x canvas (not recommended and d eprecated in 2.0) (requires PyGTK and pycairo or cairocffi; Python2 only)
# GTKCairo    Cairo rendering to a GTK 2.x canvas (requires PyGTK and pycairo or cairocffi; Python2 only)
# GTK3Cairo    Cairo rendering to a GTK 3.x canvas (requires PyGObject and pycairo or cairocffi)
# WXAgg    Agg rendering to to a wxWidgets canvas (requires wxPython)
# WX    Native wxWidgets drawing to a wxWidgets Canvas (not recommended and deprecated in 2.0) (requires wxPython)
# TkAgg    Agg rendering to a Tk canvas (requires TkInter)
# Qt4Agg    Agg rendering to a Qt4 canvas (requires PyQt4 or pyside)
# Qt5Agg    Agg rendering in a Qt5 canvas (requires PyQt5)
# macosx    Cocoa rendering in OSX windows (presently lacks blocking show() behavior when matplotlib is in non-interactive mode)


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
