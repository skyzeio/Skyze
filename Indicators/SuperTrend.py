'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import unittest
import pandas as pd
import numpy as np

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract
from Indicators.AverageTrueRange import AverageTrueRange






class SuperTrend(IndicatorAbstract):
    '''
    classdocs
    '''
    name = "SuperTrend v01"



    def __init__( self,
                  p_st_period,
                  p_st_multiplier,
                  p_name_extension = ""
                ):
        ''' Constructor '''

        #  raise exceptionality
        if p_st_period < 0:
            pass

        if p_st_multiplier < 0:
            pass

        # set the Name extionsion
        if p_name_extension != "":
            self.name_extension        = "_"+p_name_extension
        else:
            self.name_extension = ""

        # Set members
        self.st_period             = p_st_period
        self.st_multiplier         = p_st_multiplier

        self.result = pd.DataFrame()
        self.error = []



    def initial(self, p_data):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''

        return p_data



    def calculate (self,
                   p_data        # pd dataframe series
                     ):
        '''  Calculations
            BASIC UPPERBAND =  (HIGH + LOW) / 2 + Multiplier * ATR
            BASIC LOWERBAND =  (HIGH + LOW) / 2 - Multiplier * ATR

            FINAL UPPERBAND = IF( (Current BASICUPPERBAND  < Previous FINAL UPPERBAND) and (Previous Close > Previous FINAL UPPERBAND)) THEN
                                    (Current BASIC UPPERBAND) ELSE Previous FINALUPPERBAND)

            FINAL LOWERBAND = IF( (Current BASIC LOWERBAND  > Previous FINAL LOWERBAND) and (Previous Close < Previous FINAL LOWERBAND)) THEN
                                    (Current BASIC LOWERBAND) ELSE Previous FINAL LOWERBAND)

            SUPERTREND = IF(Current Close <= Current FINAL UPPERBAND ) THEN Current FINAL UPPERBAND ELSE Current  FINAL LOWERBAND

        '''
        p_data = self.initial( p_data )

        atr = AverageTrueRange(self.st_period)
        p_data = atr.calculate(p_data)
#         p_data["Av_Tr_Rge"] = atr.calculate(p_data)

        # calculate Basic bounds
        p_data["basic_ub"+self.name_extension] = (p_data["High"]+p_data["Low"])/2 + self.st_multiplier*p_data["ATR_"+ str(self.st_period)]
        p_data["basic_lb"+self.name_extension] = (p_data["High"]+p_data["Low"])/2 - self.st_multiplier*p_data["ATR_"+ str(self.st_period)]

        # for i, row in p_data.iterrows():    # pre date as the index
        for i, (index, row) in enumerate(p_data.iterrows()):
            print(p_data.head(5)); print("i"); print(i); print("row"); print(row)
            if i < self.st_period:
                p_data.set_value(index, 'basic_ub'+self.name_extension, 0.00)
                p_data.set_value(index, 'basic_lb'+self.name_extension, 0.00)
                p_data.set_value(index, 'final_ub'+self.name_extension, 0.00)
                p_data.set_value(index, 'final_lb'+self.name_extension, 0.00)
                p_data.set_value(index, 'Super_Trend'+self.name_extension, 0.00)
            else:
                p_data.set_value(index, 'final_ub'+self.name_extension, (p_data.get_value(index, 'basic_ub'+self.name_extension)
                                             if p_data.get_value(index, 'basic_ub'+self.name_extension) < p_data.get_value(i-1, 'final_ub'+self.name_extension) or
                                                p_data.get_value(i-1, 'Close') > p_data.get_value(i-1, 'final_ub'+self.name_extension)
                                             else p_data.get_value(i-1, 'final_ub'+self.name_extension)))
                p_data.set_value(index, 'final_lb'+self.name_extension, (p_data.get_value(index, 'basic_lb'+self.name_extension)
                                             if p_data.get_value(index, 'basic_lb'+self.name_extension) > p_data.get_value(i-1, 'final_lb'+self.name_extension) or
                                                p_data.get_value(i-1, 'Close') < p_data.get_value(i-1, 'final_lb'+self.name_extension)
                                             else p_data.get_value(i-1, 'final_lb'+self.name_extension)))

                p_data.set_value(index, 'Super_Trend'+self.name_extension, (p_data.get_value(index, 'final_ub'+self.name_extension)
                                                         if ( ( p_data.get_value(i-1, 'Super_Trend'+self.name_extension) == p_data.get_value(i-1, 'final_ub'+self.name_extension) ) and
                                                              ( p_data.get_value(index, 'Close')         <= p_data.get_value(index, 'final_ub'+self.name_extension)   )       )
                                                         else ( p_data.get_value(index, 'final_lb'+self.name_extension)
                                                                   if ( (p_data.get_value(i-1, 'Super_Trend'+self.name_extension) == p_data.get_value(i-1, 'final_ub'+self.name_extension) ) and
                                                                        (p_data.get_value(index, 'Close')          > p_data.get_value(index, 'final_ub'+self.name_extension)   )       )
                                                                   else ( p_data.get_value(index, 'final_lb'+self.name_extension)
                                                                             if ( (p_data.get_value(i-1, 'Super_Trend'+self.name_extension) == p_data.get_value(i-1, 'final_lb'+self.name_extension) ) and
                                                                                  (p_data.get_value(index, 'Close')        >= p_data.get_value(index, 'final_lb'+self.name_extension)    )      )
                                                                             else (p_data.get_value(index, 'final_ub'+self.name_extension)
                                                                                       if ( (p_data.get_value(i-1, 'Super_Trend'+self.name_extension) == p_data.get_value(i-1, 'final_lb'+self.name_extension) ) and
                                                                                            (p_data.get_value(index, 'Close')          < p_data.get_value(index, 'final_lb'+self.name_extension)   )      )
                                                                                       else 0.00
                                                                                  )
                                                                            )
                                                               )
                                                    )
                                    )

        return p_data



#                 # Mark the trend direction up/down
#                 p_data['STX'] = np.where((p_data['Super_Trend'] > 0.00), np.where((p_data['Close'] < p_data['Super_Trend']), 'down',  'up'), np.NaN)

#             p_data["STR_FUB"][index] = if ( ( p_data["STR_BUB"][index] <  p_data["STR_FUB"][index-1] )   and
#                                             ( p_data["Close"][index]   >  p_data["STR_FUB"][index-1] )
#                                           ):
#                                                 p_data["STR_BUB"]
#                                         else:
#                                             p_data["STR_FUB"][index-1]
#             p_data["STR_FLB"][index] =  if ( ( p_data["STR_BLB"][index] >  p_data["STR_FLB"][index-1] )   and
#                                             ( p_data["Close"][index]    <  p_data["STR_FLB"][index-1] )
#                                           ):
#                                                 p_data["STR_BLB"][index]
#                                         else:
#                                             p_data["STR_FLB"][index-1]
#
#             # calculate Super Trend
#             col_name = "Super_Trend_"+str(self.st_multiplier)+"_"+str(self.st_period)
#             p_data[col_name] = if ( p_data["Close"][index] <=  p_data["final_ub"][index] ):
#                                     p_data["final_ub"][index]
#                                 else:
#                                     p_data["STR_FLB"][index]



    def getResult (self ):
        ''' Getter '''
        return self.result



    def getName(self ):
        ''' Getter '''
        return self.name
