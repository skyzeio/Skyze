'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import pandas as pd
import numpy as np

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract





class TrueRange(IndicatorAbstract):
    '''
    classdocs
        TR =max[high-low),abs(high-close{prev}),abs(low-close{prev})]
        
    '''
    name = "Average True Range v01"



    def __init__( self ):
        ''' Constructor '''
        
#             raise exceptionality
        
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

        p_data['H-L']   = abs(p_data['High']-p_data['Low'])
        p_data['H-PC']  = abs(p_data['High']-p_data['Close'].shift(1))
        p_data['L-PC']  = abs(p_data['Low']-p_data['Close'].shift(1))
        p_data['True_Range']    = p_data[['H-L','H-PC','L-PC']].max(axis=1).round(6)
        
        p_data['True_Range'] = np.where(p_data['H-PC'].notnull(), p_data['True_Range'], 'NaN')
#         p_data['True Range']    = if  p_data['H-PC'] == "NaN" or p_data['L-PC'] == "NaN" : 

#         del p_data['H-L']
#         del p_data['H-PC']
#         del p_data['L-PC']
        
        return p_data
    
    
    
    def getResult (self ):
        ''' Getter '''
        return self.result
    
    
    
    def getName(self ):
        ''' Getter '''
        return self.name
    
    
    