"""Created on 04/09/2017
    @author: michaelnew"""

# 3rd parties
import pandas as pd
import numpy as np

# Skyze Library
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract


class ExponentialWeightedMovingAverage(IndicatorAbstract):
    """Exponential Weighted Moving Average
        Also known as a Linerly Weighted Moving Average
        definition: https://en.wikipedia.org/wiki/Exponential_smoothing
                    http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-windows
        e.g. 5 Day ewma is
            series = [83,81,79,79,77,...]
            alpha å  = 1 / period
            demonimator = sum 1 to n = 1 + (1-Å) + (1-Å)^2 + (1-Å)^3 + ... + (1-Å)^period
            numerator = x1 + (1-Å)x2 + (1-Å)^2x3l"""

    # Static Variables
    _name = "Exponential Weighted Moving Average"
    _version = 1.0

    def __init__(self,
                 p_ewma_period,
                 p_ewma_column
                 ):
        """Constructor - validate and assign parameters"""

        # validate parameters and raise exceptionality
        if p_ewma_period < 0:
            pass

        # Assign parameters
        self._ewma_period = p_ewma_period
        self._ewma_column = p_ewma_column

        # Standard members
        self._result = pd.DataFrame()
        self._error = []

    def _initial(self, p_data):
        """Calculate the first value if the calc is different to the subsequent calculations"""
        return p_data

    def calculate(self, p_data):
        """ Calculations"""
        ewma_result_column = "ewma_" + str(self._ewma_period)
        p_data = self._initial(p_data)
        # TODO: Convert next line from SMA to ewma
        # Simple Moving Average
        # p_data[ewma_result_column] = p_data[self._ewma_column].rolling(
        #    window=self._ewma_period, win_type='triang').mean().shift(1)

        # Pandas EWM implimentation
        # https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.ewm.html
        # http://pandas.pydata.org/pandas-docs/stable/computation.html#exponentially-weighted-windows
        ewma_alpha = 1 / self._ewma_period
        p_data[ewma_result_column] \
            = p_data[self._ewma_column].ewm(alpha=ewma_alpha, min_periods=self._ewma_period).mean()

        # http://pbpython.com/weighted-average.html
        # https://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.average.html
        # weights_vector = list(range(self._ewma_period, 0, -1))
        # weights_vector = weights_vector / sum(weights_vector)
        # print("/nWeights Vector: " + str(weights_vector))
        # p_data[ewma_result_column] = np.convolve(p_data[self._ewma_column],
        #                                        weights_vector, 'same')

        # p_data[ewma_result_column] = np.average(p_data[self._ewma_column],
        #                                       weights=weights_vector)

        # Option 1 Using Numpy Convolve
        # From https://stackoverflow.com/questions/12816011/weighted-moving-average-with-numpy-convolve
        # w = [1.0/self._ewma_period]*self._ewma_period
        # p_data["ewma_"+str(self._ewma_period)] = np.convolve(p_data[self._ewma_column],w,'valid')

        # Option 2 using Pandas Rolling
        # https://stackoverflow.com/questions/39742797/calculating-weighted-moving-average-using-pandas-rolling-method
        # construct thet weights array
        weights = np.arange(1, self._ewma_period + 1)

        # construct the fucntion to calcualte ewma for each point
        def ewma(w):
            def g(x):
                return (w / x)
            return g

        # apply the ewma function to each pont in the series
        # p_data["ewma_"+str(self._ewma_period)] = \
        #    p_data[self._ewma_column].rolling(window=self._ewma_period) \
        #    .apply(ewma(weights))#.sum()/self._ewma_period

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
