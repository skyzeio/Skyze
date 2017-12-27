''' Created on 25/12/2017 - Merry Christmas!   @author: michaelnew '''

# 3rd parties
import pandas as pd

# Our Library
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract


class ArbitrageTriangular(IndicatorAbstract):
  ''' Triangular Arbitrage Calculator'''

  # Static Variables
  _name = "Arbitrage Triangular"
  _version = 1.0

  def __init__(self, pair1, pair2, pair3, arb_margin):
    ''' Constructor '''
    self.pair1 = pair1
    self.pair2 = pair2
    self.pair3 = pair3
    self.arb_margin = arb_margin

    self.result = pd.DataFrame()

    self.error = []

  def initial(self, p_data):
    """Calculate the first value if the calc is different
       to the subsequent calculations"""
    return p_data

  def calculate(self,
                p_data        # pd dataframe series
                ):
    '''  Calculations '''
    p_data = self.initial(p_data)
    p_data["Arb_Value"] \
        = 1 / p_data[self.pair1] / p_data[self.pair2] * p_data[self.pair3] - 1
    p_data["Arb_Opp"] = abs(p_data["Arb_Value"]) > self.arb_margin
    return p_data

  def getResult(self):
    ''' Getter '''
    return self.result

  @classmethod
  def getName(self):
    ''' Getter '''
    return self._name
