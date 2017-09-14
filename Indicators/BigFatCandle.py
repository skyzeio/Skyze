'''
Created on 02/09/2017

@author: michaelnew
'''
# 3rd Party
import pandas as pd

# Skyze Imports
from Indicators.IndicatorAbstract import IndicatorAbstract



class BigFatCandle(IndicatorAbstract):
    '''
    classdocs
    '''
    name = "Big Fat Candle"

    def __init__( self, 
                  p_fatRatio            # how big the body (o-c) of the candle should be .. range 0 to 1
                ):
        ''' Constructor '''
        if p_fatRatio < 0 or p_fatRatio > 1 :
#             raise exceptionality
            pass
        
        self.fatRatio = p_fatRatio      # between 0 and 1
        self.result = pd.DataFrame()
        self.error = []
        
    def inititial(self):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''
        pass
    
    def calculate (self, 
                   p_data        # pd dataframe series
                     ):
        '''  Calculations '''
        p_data["BigFatCandle"] = abs(p_data['Open']- p_data['Close'])/(p_data['High']-p_data['Low']) > self.fatRatio

#         for data in p_market_data:
#             abs(p_bar.open-p_bar.close)/(p_bar.high-p_bar.low) >= p_fatRatio
        return p_data
    
    
    
    def getResult (self ):
        ''' Getter '''
        return self.result
    
    def getName(self ):
        ''' Getter '''
        return self.name