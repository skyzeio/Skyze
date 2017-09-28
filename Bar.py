#----------------------------------------------------------------------------------------------------------
#
#   CLASS Bar
#
#-------------------------------------------------------------------------------------------- --------------

import numpy as np


class Bar:

    def __init__(  self,
                    p_open,
                    p_high,
                    p_low,
                    p_close,
                    p_volume,
                    p_high_low_order
               ):
        self.open = p_open
        self.high = p_high
        self.low = p_low
        self.close = p_close
        self.volume = p_volume
        self.high_low_order = p_high_low_order
        
    
    
    def getOpen(self):
        return self.open
    
    
    def getHigh(self):
        return self.high
    
    
    def getLow(self):
        return self.low
    
    
    def getClose(self):
        return self.close
    
    
    def getVolume(self):
        return self.volume
    
    
    def getHighLowOrder(self):
        return self.high_low_order
    
    
       