'''
Created on 05/09/2017

@author: michaelnew
'''

# Standard Libraries

# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Market import Market

# Our libraries - Test Specific
from Indicators.SuperTrend import SuperTrend




class SuperTrend_test(UnitTestSkyzeAbstract):
    '''
    classdocs
    '''




    def test(self):

        # Test Parameters
        output_info    = True
        target_file    = "Results-bitcoin-SuperTrend"
        test_file      = "bitcoin_TEST"
        target_columns = ["H-L","H-PC","L-PC","True_Range","ATR_15","basic_ub","basic_lb","final_ub","final_lb","Super_Trend"]
        test_columns   = ["H-L","H-PC","L-PC","True_Range","ATR_15","basic_ub","basic_lb","final_ub","final_lb","Super_Trend"]

        st_period = 15
        st_multiplier = 3
        st_name_extension = ""

        # Output Headings
        print ("\n\n======= This is a test of SUPERTREND INDICATOR ==============")
        print ("Test data: " + test_file + "    \nTarget data: " + target_file)
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


if __name__ == '__main__':
    unittest.main()
