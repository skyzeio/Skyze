"""Created on 04/09/2017
@author: michaelnew"""

# 3rd parties
import pandas as pd
import numpy as np

# Our Library
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract


class Crosses(IndicatorAbstract):
    """classdocs
         Determine if two series cross and the direction
         if UP then the series_cross will move from below the
                series_base to above it
         if DOWN then the series_cross will move from above the
                series_base to below it"""

    # Static Variables
    _name = "Crosses"
    _version = 1.0

    def __init__(self, p_series_cross, p_series_base,
                 p_direction="Up", p_col_name="Crosses"):
        """Constructor"""

        # raise exceptionality
        if p_direction != "Up" or p_direction != "Down":
            pass

        # Indicator Parameters
        self._series_cross = p_series_cross
        self._series_base = p_series_base
        self._direction = p_direction

        # Optional Parameters
        self._column_name = p_col_name

        # Standard members
        self._result = pd.DataFrame()
        self._error = []

    def _initial(self, p_data):
        """Calculate the first value if the calc is different
            to the subsequent calculations"""

        return p_data

    def direction(self, x):
        direct = np.NaN
        if x[0] < x[0].shift(1) and self.direction == "Up":
                # Negative to positive = crosses up
            direct = True
        elif x[0] > x[0].shift(1) and self.direction == "Down":
            # Positive to negative = crosses down
            direct = True
        return direct

    def calculate(self, p_data):
        """ Calculate"""
        p_data = self._initial(p_data)
        diff_column = self._column_name + 'diff'

        # Difference between series on each row
        p_data[diff_column] = p_data[self._series_cross] - \
            p_data[self._series_base]

        # Change in sign of the difference from previous to current row
        p_data[self._column_name] = \
            np.sign(p_data[diff_column].shift(1)) != \
            np.sign(p_data[diff_column])

        # TODO: Calculate the UP or DOWN options
#         p_data[self.column_name+"_direction"] = 1 #p_data[[self.column_name+'diff']].apply(self.direction("Up"), axis=1)

        # Set cross to False if the inputs are NaN
        p_data[self._column_name] \
            = np.where(p_data[diff_column].isnull(),
                       np.NaN, p_data[self._column_name])    # this diff is null
        p_data[self._column_name] \
            = np.where(p_data[diff_column].shift(1).isnull(),
                       np.NaN, p_data[self._column_name])    # previous diff is null
        # convert to boolean
        p_data[self._column_name] = p_data[self._column_name] == 1
        p_data["Direction"] = np.NaN

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
