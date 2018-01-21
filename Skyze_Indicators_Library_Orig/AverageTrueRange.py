"""Created on 04/09/2017
@author: michaelnew"""

# 3rd parties
import pandas as pd

# Our Library
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract
from Skyze_Indicators_Library.TrueRange import TrueRange
from Skyze_Indicators_Library.MovingAverage import MovingAverage


class AverageTrueRange(IndicatorAbstract):
    """classdocs
         TR =max[high-low),abs(high-close{prev}),abs(low-close{prev})]
         df['ATR'] = df['TR'].ewm(span = 10).mean()"""

    # Static Variables
    _name = "Average True Range"
    _version = 1.0

    def __init__(self, p_atr_period):
        """Constructor"""

#             raise exceptionality
        if p_atr_period < 0:
            pass

        self._atr_period = p_atr_period

        self._result = pd.DataFrame()
        self._error = []

    def initial(self, p_data):
        """Calculate the first value if the calc is different to the subsequent calculations"""

        return p_data

    def calculate(self, p_data):
        """Calculations"""
        atr_name = 'ATR_' + str(self._atr_period)
        p_data = self.initial(p_data)
        # Create and calculate the true range indicator
        true_range = TrueRange()
        p_data = true_range.calculate(p_data)
        # Average True Range over the series
        p_data[atr_name] = p_data["True_Range"] \
            .rolling(window=self._atr_period).mean().shift(1)

        return p_data

    def getResult(self):
        """Getter"""
        return self._result

    def getName(self):
        """Getter"""
        return self._name

    def getVersion(self):
        """Getter"""
        return self._version
