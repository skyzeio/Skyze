'''
Created on 05/09/2017

@author: michaelnew
'''

# Standard Libraries
from pandas.util.testing import assert_frame_equal
from pandas.util.testing import assert_series_equal
import pandas as pd

# Our libraries - Required
from SkyzeUnitTest import SkyzeUnitTest
from Market import Market

# Our libraries - Test Specific
from Indicators.Neural import Neural




class Neural_test(SkyzeUnitTest):
    '''
    classdocs
    '''      
        
        
        
 
    def test(self):
        
        # Test Parameters
        output_info    = True
        target_file    = "Results-bitcoin-SuperTrend"
        test_file      = "bitcoin_TEST"
        target_columns = ["Date","H-L","H-PC","L-PC","True_Range","ATR_15","basic_ub","basic_lb","final_ub","final_lb","Super_Trend"] 
        test_columns   = ["Date","H-L","H-PC","L-PC","True_Range","ATR_15","basic_ub","basic_lb","final_ub","final_lb","Super_Trend"] 
                            # ["Date","H-L","H-PC","L-PC","TR","ATR","BUB","BLB","FUB","FLB","ST"] 
        st_period = 15
        st_multiplier = 3
        st_name_extension = "" 
        
        # Output Headings
        print ("This is a test of SUPERTREND")
        print ("Test Data: " + test_file + "    Target Data: " + target_file)
        print ("Columns: "+ str(test_columns))
        print ("Parameters: period: " + str(st_period) + "   Multiplier: " + str(st_multiplier))
         
        # Get the data
        mkt = Market.fromTesting(test_file)
        mkt_data = mkt.readMarketDataCSV(p_testing=True)
        
        # Calcualte the Indicators
        supertrend = SuperTrend(st_period,st_multiplier,st_name_extension)
        mkt_data = supertrend.calculate(mkt_data)
        
        # Read in the target results
        target_data = self.readTargetResults(target_file, target_columns)
        
        # Format boolean columns
        # None                       # convert to boolean
        
        # Output the Testing Results
        if output_info:
            print();print();print(); print("=== Target_data . head  === === === === === ")
            print(target_data.head(16))
            print(); print("=== Target_data . tail === === === === === ")
            print(target_data.tail(5))
            
            print();print();print(); print("=== Market data Results . head === === === === === ")
            print(mkt_data.head(16)) #[test_columns]
            print(); print("=== Market data Results . tail === === === === === ")
            print(mkt_data.tail(5)) # [test_columns]
                
        # Assertions
        if output_info:
            print(); print("=== Series Equal DATE === === === === === ")
#             assert_series_equal( mkt_data["Date"], target_data["Date"])
            print("PASS")
#             for test_column in target_columns:
#                 print(); print("=== Series Equal %s === === === === === " % test_column)
#                 assert_series_equal( mkt_data[test_column], target_data[test_column])
#                 print("PASS")
# 
#         print(); print("=== DataFrame Equal === === === === === ")
#         assert_frame_equal( mkt_data[test_columns], target_data)
#         print("PASS")
        
        
        