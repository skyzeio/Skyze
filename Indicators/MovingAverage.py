'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import pandas as pd

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract





class MovingAverage(IndicatorAbstract):
    '''
    classdocs
    '''

    # Static Variables
    name = "Moving Average"
    version = 1.0



    def __init__(self,
                  p_ma_period,
                  p_ma_column
               ):
        ''' Constructor '''

#             raise exceptionality

        if p_ma_period < 0:
            pass

        self.ma_period             = p_ma_period
        self.ma_column             = p_ma_column

        self.result = pd.DataFrame()
        self.error = []



    def initial(self, p_data):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''

        return p_data



    def calculate (self,
                   p_data        # pd dataframe series
                    ):
        '''  Calculations '''
        p_data = self.initial(p_data)
        p_data["MA_"+str(self.ma_period)] = p_data[self.ma_column].rolling(window=self.ma_period).mean().shift(1)

        return p_data



    def getResult (self):
        ''' Getter '''
        return self.result



    def getName(self):
        ''' Getter '''
        return self.name
