'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import pandas as pd

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract





class WeightedMovingAverage(IndicatorAbstract):
    '''
    classdocs
    '''
    name = "Weighted Moving Average v01"



    def __init__( self, 
                  p_wma_period,  
                  p_wma_column
                ):
        ''' Constructor '''
        
#             raise exceptionality
        
        if p_wma_period < 0:
            pass
        
        self.wma_period             = p_wma_period     
        self.wma_column             = p_wma_column   
        
        self.result = pd.DataFrame()
        self.error = []
        
        
        
    def initial(self, p_data):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''

        return p_data
    
    
    
    def calculate (self, 
                   p_data        # pd dataframe series
                     ):
        '''  Calculations '''
        p_data = self.initial( p_data )
        # TODO: Convert next line from SMA to WMA
        p_data["WMA_"+str(self.wma_period)] = p_data[self.wma_column].rolling(window=self.wma_period, win_type='triang').mean().shift(1)
        return p_data
    
    
    
    def getResult (self ):
        ''' Getter '''
        return self.result
    
    
    
    def getName(self ):
        ''' Getter '''
        return self.name
    
    
    