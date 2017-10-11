"""Created on 11/10/2017
@author: michaelnew"""
# Library Imports
# 3rd parties

# Our Library
from Screeners.ScreenerAbstract import *
from Indicators.SimpleMovingAverage import SimpleMovingAverage
from Indicators.Crosses import Crosses


class SMACrossOverScreener(ScreenerAbstract):
    """Class doc"""

    # Static Class Variables
    name = "SuperTrend CrossOver Screener"
    version = 1.0
    description = "Uses a fast and slow STC crossover combined with a long EMA and big fat candle to trigger trade signals."

    def __init__(self):

    @classmethod
    def getName(self):
        """ Getter """
        return self.name

    @classmethod
    def getVersion(self):
        """ Getter """
        return self.version

    @classmethod
    def getDescription(self):
        """ Getter """
        return self.description

    @classmethod
    def getResult(self):
        """ Getter """
        return sel


f.result

    def calculateSignals(self,
                         p_data        # pd dataframe series
                         ):
        """Calculates and returns screener signals"""
