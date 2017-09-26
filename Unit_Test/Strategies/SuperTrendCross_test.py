'''
Created on 05/09/2017

@author: michaelnew
'''


# 3rd Party

# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Market import Market

# Skyze imports
from Strategies.SuperTrendCross import SuperTrendCross
import Market



class SuperTrendCross_test(unittest.TestCase):
    '''
    classdocs
    '''



    def test(self):

        # Test Parameters
        output_info    = True
        target_file    = "Results-bitcoin-SuperTrend"
        test_file      = "bitcoin_TEST"                 # "Test-bitcoin-SuperTrend"
        target_columns = ["ST_Signal"]
        test_columns   = ["ST_Signal"]

        # Strategy Parameters
        p_wma_period         = 90
        p_wma_column         = "Close"
        p_fast_st_multiplier = 3
        p_fast_st_period     = 15
        p_slow_st_multiplier = 3.5
        p_slow_st_period     = p_fast_st_period
        p_fat_ratio          = 0.65

        # Output Headings
        print ("\n\n======= This is a test of SUPERTREND STRATEGY ==============")
        print ("Test data: " + test_file + "    \nTarget data: " + target_file)
        print ("Columns: "+ str(test_columns))
        print ("Parameters: period: " + str(st_period) + "   Multiplier: " + str(st_multiplier))

        # Get the data
        mkt = Market.fromTesting(test_file)
        mkt_data = mkt.readMarketDataCSV(p_testing=True)

        # Create the Strategy
        stc = SuperTrendCross(
                                p_wma_period,
                                p_wma_column,
                                p_fast_st_multiplier,
                                p_fast_st_period,
                                p_slow_st_multiplier,
                                p_slow_st_period,
                                p_fat_ratio
                            )

        # Calculate the strategy
        stc.calculate(mkt_data)

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
            # Columm by colum assertions
            print(); print("=== Series Equal DATE === === === === === ")
#             assert_series_equal( mkt_data["Date"], target_data["Date"])
            print("PASS")

        # Assert data frame equal
        print(); print("=== DataFrame Equal === === === === === ")
        assert_frame_equal( mkt_data[test_columns], target_data)
        print("PASS")









if __name__ == '__main__':
    unittest.main()
