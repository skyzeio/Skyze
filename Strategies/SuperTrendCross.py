'''
Created on 03/09/2017

@author: michaelnew




                C   O   N   F   I   D   E   N   T   I   A   L




                this file contains confidential information

                    unless you are Mike New ... Read no further

                        :)























                                no scrolling :)

'''
# Library Imports
# 3rd parties

# Our Library
from Strategies.StrategyAbstract        import *
from Indicators.WeightedMovingAverage   import WeightedMovingAverage
from Indicators.SuperTrend              import SuperTrend
from Indicators.Crosses                 import Crosses
import ExceptionSkyzeAbstract




class SuperTrendCross(StrategyAbstract):
    '''
    classdocs
    '''

    # TODO How to hide the content of confidential trading strategy files?

    # Static Class Variables
    name = "SuperTrend CrossOver Screener v01"
    description = "Uses a fast and slow STC crossover combined with a long EMA and big fat candle to trigger trade signals."




    def __init__(self,
                  p_wma_period,
                  p_wma_column,                   # Open/High/Low/Close/Volume/etc
                  p_fast_st_multiplier,
                  p_fast_st_period,
                  p_slow_st_multiplier,
                  p_slow_st_period,
                  p_fatRatio,
                  p_days_since_cross
               ):
        ''' Constructor '''

        # Validate parameters
        if p_slow_st_multiplier < p_fast_st_multiplier:
            # Parameter Error
            pass

        if p_wma_period < 0:
            # Parameter Error
            pass

        if p_fast_st_multiplier < 0:
            # Parameter Error
            pass

        if p_fast_st_period < 0:
            # Parameter Error
            pass

        if p_slow_st_multiplier < 0:
            # Parameter Error
            pass

        if p_slow_st_period < 0:
            # Parameter Error
            pass

        if p_fatRatio < 0:
            # Parameter Error
            pass

        if p_days_since_cross < 0:
            # Parameter Error
            pass

        # assign parameters to member variables
        self.wma_period             = p_wma_period
        self.wma_column             = p_wma_column
        self.fast_st_multiplier     = p_fast_st_multiplier
        self.fast_st_period         = p_fast_st_period
        self.slow_st_multiplier     = p_slow_st_multiplier
        self.slow_st_period         = p_slow_st_period
        self.days_since_cross       = p_days_since_cross

        # Standard member variables
        self.result = pd.DataFrame()
        self.error = []




    def inititial(self):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''
        pass




    def calc_signal(self, x):
        ''' returns buy or sell '''
        signal = 0
        if   (x[0]) == 1 : signal = self.buy_signal
        elif (x[1]) == 1 : signal = self.sell_signal
        return signal




    def calculateSignals (self,
                            p_data        # pd dataframe series
                         ):
        '''  Calculations '''
        # Indicators
        p_data = WeightedMovingAverage(self.wma_period, self.wma_column).calculate(p_data)                   # WMA TODO: Why is WMA not returning the result column?
        p_data = SuperTrend(self.fast_st_period, self.fast_st_multiplier,"Fast").calculate(p_data)           # Fast SuperTrend
        p_data = SuperTrend(self.slow_st_period, self.slow_st_multiplier,"Slow").calculate(p_data)           # Slow SuperTrend



        # -------- bull side  ----------------------------------
        p_data["Bull1"]  = p_data["Close"] > p_data["WMA_"+str(self.wma_period)]              # Close above WMA
        # bull2 = summation[3](close crosses over highest[15](high)[1])>0                     # Highest close for 15 dats - V01 Original code
        p_data["Bull2"]  = p_data["High"]  > p_data["High"].rolling(self.fast_st_period,min_periods=self.fast_st_period).max().shift(1)         # V03
        # previous was deprecated Series.rolling(center=False,window=15).max()
        p_data["Bull3"]  = p_data["Close"] > p_data["Super_Trend_Slow"]                       # Close above slow Super Trend
        p_data["Bull31"] = p_data["Close"] > p_data["Super_Trend_Fast"]                       # Close above fast Super Trend
        # bull4 = summation[3](fastST crosses under close)>0                                  # Close is above the fST in the last three days
        # bull41 = summation[3](slowST crosses under close)>0                                 # Close is below the fST in the last three days
        # bu5 = (fastST>slowST)
        #
        #  v01 orgininal bullish signal
        #  bullish = bull1 and bull2 and ((bull3 and bull4) or (bull31 and bull41)) and bu5summation[15](bu1 and bu2 and bu3 and bu4 and bu5)>0
        #
        #  Updated for signal at STX crossover - v02
        p_data = Crosses("Super_Trend_Fast","Super_Trend_Slow","Up", p_col_name="Crs_Bull").calculate(p_data)  # Calculate crosses
        p_data["Bull5"] = p_data["Crs_Bull"].rolling(self.days_since_cross).sum()            # Did a cross happen in the last X bars?

        # Set the bullish indicator if below conditions are met
        p_data["Bullish"] = p_data["Bull1"] & p_data["Bull2"] & p_data["Bull3"] & p_data["Bull31"] & p_data["Bull5"]

        print(p_data["Bullish"])


        # -------- sell side  ----------------------------------
        p_data["Bear1"]  = p_data["Close"] > p_data["WMA_"+str(self.wma_period)]              # Close above WMA
        # bear2 = summation[3](close crosses under lowest[15](low)[1])>0                      # Original code from Nigel's programmer
        # p_data["Bear2"]  = p_data["High"]  < pd.rolling_min(p_data["Low"],15).shift(1)      # V03
        p_data["Bear2"]  = p_data["Low"]  < p_data["Low"].rolling(self.fast_st_period,min_periods=self.fast_st_period).min().shift(1)         # V03
        # previous was deprecated Series.rolling(center=False,window=15).max()
        p_data["Bear3"]  = p_data["Close"] < p_data["Super_Trend_Slow"]                       # Close above slow Super Trend
        p_data["Bear31"] = p_data["Close"] < p_data["Super_Trend_Fast"]                       # Close above fast Super Trend
        # bear4 = summation[3](fastST crosses over close)>0
        # bear41 = summation[3](slowST crosses over close)>0
        # bu5 = (fastST>slowST)
        #
        #  v01 orgininal bearishsignal
        # bearish = bear1 and bear2 and ((bear3 and bear4) or (bear31 and bear41)) and bu5summation[15](bu1 and bu2 and bu3 and bu4 and bu5)>0
        #
        #  Updated for signal at STX crossover - v02
        p_data = Crosses("Super_Trend_Fast","Super_Trend_Slow","Down" , p_col_name="Crs_Bear").calculate(p_data)  # Calculate crosses
        p_data["Bear5"] = p_data["Crs_Bear"].rolling(self.days_since_cross).sum()            # Did a cross happen in the last X bars?

        # Set the bearish indicator if below conditions are met
        p_data["Bearish"] = p_data["Bear1"] & p_data["Bear2"] & p_data["Bear3"] & p_data["Bear31"] & p_data["Bear5"]    #  Super trend cross is bearish

        #   if (bullish):  signal = 1  elif (bearish):     signal = -1
        p_data["Signal"] = p_data[["Bullish","Bearish"]].apply(self.calc_signal, axis=1)

        self.result = p_data
        return self.result




    def getResult (self):
        ''' Getter '''
        return self.result



    def getName(self):
        ''' Getter '''
        return self.name



    def getDescription(self):
        ''' Getter '''
        return self.description




# ===== Pro Real Time Code ==============================================================================================================
#
# --------- indicators  --------------------------------
# wma = weightedaverage[90](close)
# slowST = supertrend[10,15]
# fastST = supertrend[3.5,15]
#
# -------- bull side  ----------------------------------
# bull1 = close>wma                                                              Close above WMA
# bull2 = summation[3](close crosses over highest[15](high)[1])>0              Highest close for 15 dats - V01 Original code
# bull2 = high > highest[15](high)[1]                                            V03
# bull3 = close>slowST                                                           Close above slow Super Trend
# bull31 = close>fastST                                                          Close above fast Super Trend
# bull4 = summation[3](fastST crosses under close)>0                             Close is above the fST in the last three days
# bull41 = summation[3](slowST crosses under close)>0                            Close is below the fST in the last three days
# bu5 = (fastST>slowST)
#
#  v01 orgininal bullish signal
#  bullish = bull1 and bull2 and ((bull3 and bull4) or (bull31 and bull41)) and bu5summation[15](bu1 and bu2 and bu3 and bu4 and bu5)>0
#
#  Updated for signal at STX crossover - v02
# bull5 = summation[5](fastST crosses over slowST)>0                            Super trend cross is bullish
# bullish = bull1 and bull2 and bull3 and bull31 and bull5
#
# -------- sell side  ----------------------------------
# bear1 = close<wma
# bear2 = summation[3](close crosses under lowest[15](low)[1])>0             Original code from Nigel's programmer
# bear2 = close < lowest[15](low)[1]                                           v03
# bear3 = close<slowST
# bear31 = close<fastST
# bear4 = summation[3](fastST crosses over close)>0
# bear41 = summation[3](slowST crosses over close)>0
# bu5 = (fastST>slowST)
#
#  v01 orgininal bearishsignal
# bearish = bear1 and bear2 and ((bear3 and bear4) or (bear31 and bear41)) and bu5summation[15](bu1 and bu2 and bu3 and bu4 and bu5)>0
#
#  Updated for signal at STX crossover - v02
# bear5 = summation[5](fastST crosses under slowST)>0                           Super trend cross is bearish
# bearish = bear1 and bear2 and bear3 and bear31 and bear5
#
#
# signal = 0
# if (bullish) THEN
# signal = 1
# ELSE
# if (bearish) THEN
# signal = -1
# ENDIF
# ENDIF
#
# return signal
#
# screener [bullish] (bullish as "SuperTrend signal")
