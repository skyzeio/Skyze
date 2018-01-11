"""Created on 08/09/2017
@author: michaelnew"""


# Library Imports
# 3rd parties
import pandas as pd
from datetime import datetime

# Skyze Imports
import Skyze_Standard_Library.settings_skyze as settings_skyze
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Standard_Library.SkyzeLogger import SkyzeLogger


# https://stackoverflow.com/questions/11254553/double-inheritance-causes-metaclass-conflict
# class CombinedMeta(ExceptionSkyzeAbstract.__metaclass__, UnitTestSkyzeAbstract.__metaclass__):
#    pass


class StrategyAbstract(object):
    """classdocs"""
#    __metaclass__=CombinedMeta

    # Static Class Variables
    _name = "StrategyAbstract v01"
    _description = "Parent class for all strategies."
    _buy_signal = 1
    _sell_signal = -1

    def __init__(self):
        """Constructor"""
        # Standard member variables
        self._signals = pd.DataFrame()
        self._error = []

    def _saveToExcel(self, df, path, append_date=True):
        # Construct the file name
        file_name = path + '/' + self._name
        if append_date:
            file_name += "-" + str(datetime.now())
        file_name += '.xlsx'
        # Save to excel
        df.to_excel(file_name, index=True)

    def saveToExcelSignals(self, path, append_date=True):
        self._saveToExcel(self._signals, path)
