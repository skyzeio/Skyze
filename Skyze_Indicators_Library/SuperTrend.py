"""Calculations for Super Trend Indicator

    Created on 04/09/2017
    @author: michaelnew

    From:
    http://www.freebsensetips.com/blog/detail/7/What-is-supertrend-indicator-its-calculation
    https://tradingqna.com/t/super-trend-calculation-1st-row-issue/21193
    https://technicianapp.com/resources/average-true-range-atr-trailing-stop/

    BASIC UPPERBAND =  (HIGH + LOW) / 2 + Multiplier * ATR
    BASIC LOWERBAND =  (HIGH + LOW) / 2 - Multiplier * ATR

    FINAL UPPERBAND
       = IF((Current BASICUPPERBAND  < Previous FINAL UPPERBAND) and
                (Previous Close > Previous FINAL UPPERBAND))
          THEN
               (Current BASIC UPPERBAND) ELSE Previous FINALUPPERBAND)

    FINAL LOWERBAND
       = IF((Current BASIC LOWERBAND  > Previous FINAL LOWERBAND) and
             (Previous Close < Previous FINAL LOWERBAND))
          THEN
             (Current BASIC LOWERBAND) ELSE Previous FINAL LOWERBAND)

    SUPERTREND
       = IF(Current Close <= Current FINAL UPPERBAND)
          THEN Current FINAL UPPERBAND
          ELSE Current  FINAL LOWERBAND


    ==== Python Code can be found at
    https://stackoverflow.com/questions/44935269/supertrend-code-using-pandas-python
    END

    === Keeping this in case it is needed

    super_trend = (final_ub
         if ((prev_supertrend == prev_final_ub)
              and (curr_close <= curr_final_ub))
         else (curr_final_lb
               if ( (prev_supertrend == prev_final_ub)
                    and (curr_close > curr_final_ub))
               else (curr_final_lb
                     if ((prev_supertrend == prev_final_lb)
                          and (curr_close >= curr_final_lb))
                     else (curr_final_ub
                           if ((prev_supertrend
                                    == prev_final_lb)
                                and (curr_close < curr_final_lb))
                           else 0.00
                           )
                     )
                )
             )"""

# 3rd parties
import pandas as pd
import numpy as np

# Our Library
from Skyze_Indicators_Library.IndicatorAbstract import IndicatorAbstract
from Skyze_Indicators_Library.AverageTrueRange import AverageTrueRange


# CLASS DEFINITION =========================

class SuperTrend(IndicatorAbstract):
    '''
    classdocs
    '''

    # Static Variables
    name = "SuperTrend"
    version = 1.0

    def __init__(
        self,
        p_st_period,
        p_st_multiplier,
        p_name_extension=""
    ):
        ''' Constructor '''

        #  raise exceptionality
        if p_st_period < 0:
            pass

        if p_st_multiplier < 0:
            pass

        # set the Name extionsion
        if p_name_extension != "":
            self.name_extension = "_" + p_name_extension
        else:
            self.name_extension = ""

        # Set members
        self.st_period = p_st_period
        self.st_multiplier = p_st_multiplier

        self.result = pd.DataFrame()
        self.error = []

    def initial(self, p_data):
        """Calculate the first value if the calc is different
            to the subsequent calculations"""
        return p_data

    def calculate(self,
                  p_data        # pd dataframe series
                  ):
        """Calculations for Super Trend Indicator"""
        # Set up column names
        bub_name = 'basic_ub' + self.name_extension
        blb_name = 'basic_lb' + self.name_extension
        fub_name = 'final_ub' + self.name_extension
        flb_name = 'final_lb' + self.name_extension
        st_name = 'Super_Trend' + self.name_extension
        atr_name = 'ATR_' + str(self.st_period)

        # Initiate data
        p_data = self.initial(p_data)

        # Calculate the AverageTrueRange
        atr = AverageTrueRange(self.st_period)
        # converting to np.float64 to avoid type miscasts later
        p_data = atr.calculate(p_data)

        # calculate Basic bounds
        curr_high_low_midpoint = (p_data["High"] + p_data["Low"]) / 2
        curr_band_amount = self.st_multiplier * p_data[atr_name]
        # Upper Bound
        p_data[bub_name] = curr_high_low_midpoint + curr_band_amount
        # Lower Bound
        p_data[blb_name] = curr_high_low_midpoint - curr_band_amount

        # for i, row in p_data.iterrows():    # pre date as the index
        for i, (index, row) in enumerate(p_data.iterrows()):
            if i < self.st_period + 1:
                p_data.set_value(index, bub_name, 0.00)
                p_data.set_value(index, blb_name, 0.00)
                p_data.set_value(index, fub_name, 0.00)
                p_data.set_value(index, flb_name, 0.00)
                p_data.set_value(index, st_name, 0.00)
            else:
                # Get values for the calcuations
                curr_basic_ub = p_data.get_value(index, bub_name)
                prev_final_ub = p_data.get_value(prev_index, fub_name)
                curr_close = p_data.get_value(index, 'Close')
                prev_close = p_data.get_value(prev_index, 'Close')
                curr_basic_lb = p_data.get_value(index, blb_name)
                prev_final_lb = p_data.get_value(prev_index, flb_name)
                prev_supertrend = p_data.get_value(prev_index, st_name)

                # Calculate Final Bands
                if (i == self.st_period + 1):
                    # Set the initial value (calc is different)
                    final_ub = curr_basic_ub
                    final_lb = curr_basic_lb
                else:
                    # Calculate Final Upper Band
                    final_ub = (curr_basic_ub
                                if ((curr_basic_ub < prev_final_ub
                                     and prev_close > prev_final_ub))
                                else prev_final_ub)
                    # Calculate Final Lower Band
                    final_lb = (curr_basic_lb  # Bar's lowerbound
                                if ((curr_basic_lb > prev_final_lb
                                     and prev_close < prev_final_lb)
                                    or (i == self.st_period))
                                else prev_final_lb)
                # Add final bands to the dataframe
                p_data.set_value(index, fub_name, final_ub)
                p_data.set_value(index, flb_name, final_lb)

                # Calculate Super Trend
                curr_final_ub = p_data.get_value(index, fub_name)
                curr_final_lb = p_data.get_value(index, flb_name)
                super_trend = (final_ub
                               if curr_close <= curr_final_ub
                               else curr_final_lb)
                p_data.set_value(index, st_name,
                                 super_trend)

            # Remember the previous index for the next iteration
            prev_index = index

        return p_data


#                 # Mark the trend direction up/down
#                 p_data['STX'] = np.where((p_data['Super_Trend'] > 0.00), np.where((p_data['Close'] < p_data['Super_Trend']), 'down',  'up'), np.NaN)

#             p_data["STR_FUB"][index] = if ((p_data["STR_BUB"][index] <  p_data["STR_FUB"][index-1])   and
#                                             (p_data["Close"][index]   >  p_data["STR_FUB"][index-1])
#                                          ):
#                                                 p_data["STR_BUB"]
#                                         else:
#                                             p_data["STR_FUB"][index-1]
#             p_data["STR_FLB"][index] =  if ((p_data["STR_BLB"][index] >  p_data["STR_FLB"][index-1])   and
#                                             (p_data["Close"][index]    <  p_data["STR_FLB"][index-1])
#                                          ):
#                                                 p_data["STR_BLB"][index]
#                                         else:
#                                             p_data["STR_FLB"][index-1]
#
#             # calculate Super Trend
#             col_name = "Super_Trend_"+str(self.st_multiplier)+"_"+str(self.st_period)
#             p_data[col_name] = if (p_data["Close"][index] <=  p_data["final_ub"][index]):
#                                     p_data["final_ub"][index]
#                                 else:
#                                     p_data["STR_FLB"][index]

    def getResult(self):
        ''' Getter '''
        return self.result

    @classmethod
    def getName(self):
        ''' Getter '''
        return self.name
