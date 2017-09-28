#----------------------------------------------------------------------------------------------------------
#
#   CLASS Bar
#
#-------------------------------------------------------------------------------------------- --------------

import pandas as pd
import numpy as np
from datetime import datetime
from datetime import date




class StrategyData (pd.DataFrame):

    def __init__(  self,
                    p_market_name,
                    p_start_date,
                    p_end_date
               ):
        self.market_name = p_market_name
        self.start_date = p_start_date
        self.end_date = p_end_date
        
        # load Market History
        
        
    
    
    def getMarketName(self):
        return self.market_name
    
    
    def getStartDate(self):
        return self.start_date
    
    
    def getEndDate(self):
        return self.end_date
    
    
       
    
    def loadMarket(self):
        return
    
    
        
    
    def addIndicator(self):
        return
    
    
        
    
    def addIndicator(self):
        return
    