"""Created on 02/09/2017
    @author: michaelnew"""
# 3rd Party
import pandas as pd

# Skyze Imports
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract


class BigFatCandle(IndicatorAbstract):
    """classdocs"""

    # Static Variables
    _name = "Big Fat Candle"
    _version = 1.0

    def __init__(self,
                 # how big the body (o-c) of the candle should be .. range 0 to 1
                 p_fat_ratio
                 ):
        """Constructor"""
        if p_fat_ratio < 0 or p_fat_ratio > 1:
            #             raise exceptionality
            pass

        self._fat_ratio = p_fat_ratio      # between 0 and 1
        self._result = pd.DataFrame()
        self._error = []

    def inititial(self):
        """Calculate the first value if the calc is different to the subsequent calculations"""
        pass

    def calculate(self,
                  p_data        # pd dataframe series
                  ):
        """Calculations"""
        p_data["BigFatCandle"] = abs(p_data['Open'] - p_data['Close']) \
            / (p_data['High'] - p_data['Low']) \
            >= self._fat_ratio
        p_data["BFC_ratio"] = abs(p_data['Open'] - p_data['Close']) \
            / (p_data['High'] - p_data['Low'])

        return p_data

    @classmethod
    def getResult(self):
        """ Getter """
        return self._result

    @classmethod
    def getName(self):
        """ Getter """
        return self._name

    @classmethod
    def getVersion(self):
        """ Getter """
        return self._version
