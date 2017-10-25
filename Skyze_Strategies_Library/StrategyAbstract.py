"""Created on 08/09/2017
@author: michaelnew"""


# Library Imports
# 3rd parties
import pandas as pd

# Skyze Imports
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

    def saveToExcel(self, df):
        pass
