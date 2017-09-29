'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import pandas as pd
import numpy as np

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract





class WeightedMovingAverage(IndicatorAbstract):
    """Weighted Moving Average
        Also known as a Linerly Weighted Moving Average
        definition: https://en.wikipedia.org/wiki/Exponential_smoothing
                    https://www.oanda.com/forex-trading/learn/forex-indicators/weighted-moving-average
        e.g. 5 Day WMA is
            demonimator = sum 1 to 5 = 1 + 2 + 3 + 4 + 5 = 15
                        OR n(n+1)/2 = 5*6/2 = 15
            WMA = 83(5/15) + 81(4/15) + 79(3/15) + 79(2/15) + 77(1/15) = 80.7"""

    # Static Variables
    name = "Weighted Moving Average"
    version = 1.0

    def __init__(self,
                  p_wma_period,
                  p_wma_column
               ):
        """Constructor - validate and assign parameters"""

        # validate parameters and raise exceptionality
        if p_wma_period < 0:
            pass

        # Assign parameters
        self.wma_period = p_wma_period
        self.wma_column = p_wma_column

        # Standard members
        self.result = pd.DataFrame()
        self.error = []

    def initial(self, p_data):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''
        return p_data

    def calculate(self,
                   p_data        # pd dataframe series
                 ):
        '''  Calculations '''
        p_data = self.initial(p_data)
        # TODO: Convert next line from SMA to WMA
        # Simple Moving Average
        #p_data["WMA_"+str(self.wma_period)] = p_data[self.wma_column].rolling(window=self.wma_period, win_type='triang').mean().shift(1)

        # Option 1 Using Numpy Convolve
        # From https://stackoverflow.com/questions/12816011/weighted-moving-average-with-numpy-convolve
        #w = [1.0/self.wma_period]*self.wma_period
        #p_data["WMA_"+str(self.wma_period)] = np.convolve(p_data[self.wma_column],w,'valid')

        # Option 2 using Pandas Rolling
        # https://stackoverflow.com/questions/39742797/calculating-weighted-moving-average-using-pandas-rolling-method
        # construct thet weights array
        weights = np.arange(1,self.wma_period+1)

        # construct the fucntion to calcualte wma for each point
        def wma(w):
            def g(x):
                return (w*x).mean()
            return g

        # apply the wma function to each pont in the series
        p_data["WMA_"+str(self.wma_period)] = p_data[self.wma_column].rolling(window=self.wma_period).apply(wma(weights))

        return p_data

    def getResult (self):
        ''' Getter '''
        return self.result

    @classmethod
    def getName(self):
        ''' Getter '''
        return self.name
