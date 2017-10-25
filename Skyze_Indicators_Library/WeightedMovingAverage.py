"""Created on 04/09/2017
    @author: michaelnew"""

# 3rd parties
import pandas as pd
import numpy as np

# Skyze Library
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract


class WeightedMovingAverage(IndicatorAbstract):
    """Weighted Moving Average
        Also known as a Linerly Weighted Moving Average
        definition: https://en.wikipedia.org/wiki/Exponential_smoothing
                    https://www.oanda.com/forex-trading/learn/forex-indicators/weighted-moving-average
        e.g. 5 Day WMA is
            series = [83,81,79,79,77,...]
            demonimator = sum 1 to 5 = 1 + 2 + 3 + 4 + 5 = 15
                          OR n(n+1)/2 = 5*6/2 = 15
            WMA = 83(5/15) + 81(4/15) + 79(3/15) + 79(2/15) + 77(1/15) = 80.7"""

    # Static Variables
    _name = "Weighted Moving Average"
    _version = 1.0

    def __init__(self,
                 p_wma_period,
                 p_wma_column
                 ):
        """Constructor - validate and assign parameters"""

        # validate parameters and raise exceptionality
        if p_wma_period < 0:
            pass

        # Assign parameters
        self._wma_period = p_wma_period
        self._wma_column = p_wma_column

        # Standard members
        self._result = pd.DataFrame()
        self._error = []

    def _initial(self, p_data):
        """Calculate the first value if the calc is different to the subsequent calculations"""
        return p_data

    def calculate(self, p_data):
        """ Calculations"""
        wma_result_column = "WMA_" + str(self._wma_period)
        p_data = self._initial(p_data)

        # http://pbpython.com/weighted-average.html
        # https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.average.html
        # https://en.wikipedia.org/wiki/Convolution
        # Note: that convolve reverses the second (weights) array before sliding
        # them over each other
        # weights_vector = pd.Series(range(0, self._wma_period, 1))  # NOT CORRECT
        # Weight array is in descending order
        weights_vector = pd.Series(range(self._wma_period, 0, -1))
        weights_vector /= weights_vector.sum()
        print("\nWeights Vector: \n" + str(weights_vector))
        p_data[wma_result_column] = np.convolve(p_data[self._wma_column],
                                                weights_vector, 'same')
        # Mode ‘same’ returns output of length
        #    max(p_data[self._wma_column], weights_vector).
        #    Boundary effects are still visible

        # Remove boundary effects
        # Shift the series forward
        p_data[wma_result_column] \
            = p_data[wma_result_column].shift(int(self._wma_period / 2))
        # Remove the values less than the period
        p_data.loc[0:self._wma_period - 1, wma_result_column] = np.nan

        # p_data[wma_result_column] = np.average(p_data[self._wma_column],
        #                                       weights=weights_vector)

        # Option 1 Using Numpy Convolve
        # From https://stackoverflow.com/questions/12816011/weighted-moving-average-with-numpy-convolve
        # w = [1.0/self._wma_period]*self._wma_period
        # p_data["WMA_"+str(self._wma_period)] = np.convolve(p_data[self._wma_column],w,'valid')

        # Option 2 using Pandas Rolling
        # https://stackoverflow.com/questions/39742797/calculating-weighted-moving-average-using-pandas-rolling-method
        # construct thet weights array
        weights = np.arange(1, self._wma_period + 1)

        # construct the fucntion to calcualte wma for each point
        def wma(w):
            def g(x):
                return (w / x)
            return g

        # apply the wma function to each pont in the series
        # p_data["WMA_"+str(self._wma_period)] = \
        #    p_data[self._wma_column].rolling(window=self._wma_period) \
        #    .apply(wma(weights))#.sum()/self._wma_period

        return p_data

    def getResult(self):
        """Getter"""
        return self._result

    @classmethod
    def getName(self):
        """Getter"""
        return self._name

    @classmethod
    def getVersion(self):
        """Getter"""
        return self._version
