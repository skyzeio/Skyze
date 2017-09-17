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
from Indicators.Crosses import Crosses
from Indicators.MovingAverage import MovingAverage




class Crosses_test(SkyzeUnitTest):
    '''
    classdocs
    '''      
        
        
#         super(Crosses_test, self).__init__(self)
        
 
    def test(self):
        print ("This is a test of CROSSES")
        
        # Test Parameters
        output_info    = False
        target_file    = "Results-bitcoin-Crosses"
        test_file      = "bitcoin_TEST"
        target_columns = ["Date","MA_15","MA_30","Crossesdiff","Crosses"]            # ["Date","MA_15","MA_30","TGT_DIFF","TGT_CROSS"]
        test_columns   = ["Date","MA_15","MA_30","Crossesdiff","Crosses"]
        
        # Get the data
        mkt = Market.fromTesting(test_file)
        mkt_data = mkt.readMarketDataCSV(p_testing=True)
        
        # Calcualte the Indicators
        mkt_data = MovingAverage(15,"Close").calculate(mkt_data)
        mkt_data = MovingAverage(30,"Close").calculate(mkt_data)
        crosses = Crosses("MA_15","MA_30","Up")
        mkt_data = crosses.calculate(mkt_data)
        
        # Read in the target results
        target_data = self.readTargetResults(target_file, target_columns)
        
        # Format boolean columns
        target_data["Crosses"] = target_data["Crosses"] == 1                        # convert to boolean
        
        # Output the Testing Results
        if output_info:
            print();print();print(); print("=== Target_data . head  === === === === === ")
            print(target_data.head(16))
            print(); print("=== Target_data . tail === === === === === ")
            print(target_data.tail(5))
            
            print();print();print(); print("=== Market data Results . head === === === === === ")
            print(mkt_data[test_columns].head(16))
            print(); print("=== Market data Results . tail === === === === === ")
            print(mkt_data[test_columns].tail(5))
        
        # Assertions
        if output_info:
            print(); print("=== Series Equal DATE === === === === === ")
            assert_series_equal( mkt_data["Date"], target_data["Date"])
            print("PASS")
            print(); print("=== Series Equal MA_15 === === === === === ")
            assert_series_equal( mkt_data["MA_15"], target_data["MA_15"])
            print("PASS")
            print(); print("=== Series Equal MA_30 === === === === === ")
            assert_series_equal( mkt_data["MA_30"], target_data["MA_30"])
            print("PASS")
            print(); print("=== Series Equal Crossesdiff === === === === === ")
            assert_series_equal( mkt_data["Crossesdiff"], target_data["Crossesdiff"])
            print("PASS")
            print(); print("=== Series Equal Crosses === === === === === ")
            print(mkt_data[mkt_data["Crosses"]==True].count())
            print(target_data[target_data["Crosses"]==True].count())
            assert_series_equal( mkt_data["Crosses"], target_data["Crosses"])
            print("PASS")
        print(); print("=== DataFrame Equal === === === === === ")
        assert_frame_equal( mkt_data[test_columns], target_data)
        print("PASS")
        
        
        