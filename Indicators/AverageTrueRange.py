'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import pandas as pd

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract
from Indicators.TrueRange       import TrueRange
from Indicators.MovingAverage   import MovingAverage




class AverageTrueRange(IndicatorAbstract):
    '''
    classdocs
        TR =max[high-low),abs(high-close{prev}),abs(low-close{prev})]
        df['ATR'] = df['TR'].ewm(span = 10).mean()
    '''
    name = "Average True Range v01"



    def __init__( self, p_atr_period ):
        ''' Constructor '''
        
#             raise exceptionality
        if p_atr_period < 0:
            pass
                
        self.atr_period = p_atr_period
        
        
        self.result = pd.DataFrame()
        self.error = []
        
        
        
    def initial(self, p_data):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''

        return p_data
    
    
    
    def calculate ( self, 
                    p_data        # pd dataframe series
                  ):
        '''  Calculations '''
        p_data = self.initial( p_data )
        true_range = TrueRange()
        p_data = true_range.calculate(p_data)
        p_data['ATR_' + str(self.atr_period)] = p_data["True_Range"].rolling(window=self.atr_period).mean().shift(1)
#         print(p_data)
        return p_data
    
    
    
    def getResult (self ):
        ''' Getter '''
        return self.result
    
    
    
    def getName(self ):
        ''' Getter '''
        return self.name
    
    
    