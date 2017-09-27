'''
Created on 05/09/2017

@author: michaelnew
'''


# 3rd Party

# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Market import Market

# Skyze imports
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Strategies.SuperTrendCross import SuperTrendCross



class SuperTrendCross_test(UnitTestSkyzeAbstract):
    '''
        Test class for the SuperTrendCross strategy
    '''



    def test(self):

        # Test Parameters
        output_info    = True
        target_file    = "Target-Results-SuperTrendCross-bitcoin"
        test_file      = "bitcoin_TEST"
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
        p_days_since_cross   = 5

        # Output Headings
        self.printTestHeader(test_file, target_file, test_columns)
        print ("    WMA period: " + str(p_wma_period) + " on column: " + p_wma_column )
        print ("    Fast ST Multiplier: " + str(p_fast_st_multiplier) + " on period: " + str(p_fast_st_period))
        print ("    Slow ST Multiplier: " + str(p_slow_st_multiplier) + " on period: " + str(p_slow_st_period))
        print ("    Fat Ratio: " + str(p_fat_ratio))
        print ("    Crossing period: " + str(p_days_since_cross))

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(test_file,target_file,target_columns)

        # Create the Strategy
        stc = SuperTrendCross(
                                p_wma_period,
                                p_wma_column,
                                p_fast_st_multiplier,
                                p_fast_st_period,
                                p_slow_st_multiplier,
                                p_slow_st_period,
                                p_fat_ratio,
                                p_days_since_cross
                            )

        # Calculate the strategy
        stc.calculateSignals(mkt_data)

        # Output the Testing Info
        self.printTestInfo( output_info, mkt_data, target_data, stc.getName() )

        # Assert by series
        self.assertBySeries( output_info, mkt_data, target_data, target_columns )

        # Assert the data frame
        print(); print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert( "Final Results", mkt_data, target_data)







if __name__ == '__main__':
    unittest.main()
