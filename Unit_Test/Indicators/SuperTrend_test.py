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
        target_file    = "Target-Results-SuperTrend-bitcoin"
        test_file      = "bitcoin_TEST"
        target_columns = ["Open","High","Low","Close","Volume","MarketCap","H-L","H-PC","L-PC","True_Range","ATR_15","basic_ub","basic_lb","final_ub","final_lb","Super_Trend"]
        test_columns   = ["Open","High","Low","Close","Volume","MarketCap","H-L","H-PC","L-PC","True_Range","ATR_15","basic_ub","basic_lb","final_ub","final_lb","Super_Trend"]

        # Indicator Parameters
        st_period = 15
        st_multiplier = 3
        st_name_extension = ""

        # Output Headings
        print ("\n\n======= This is a test of SUPERTREND INDICATOR ==============")
        print ("Test data: " + test_file + "    \nTarget data: " + target_file)
        print ("Columns: " + str(len(test_columns)) + " ... "+ str(test_columns))
        print ("Parameters: ")
        print ("     period: " + str(st_period) + "   Multiplier: " + str(st_multiplier))

        # Get the data
        mkt = Market.fromTesting(test_file)
        mkt_data = mkt.readMarketDataCSV(p_testing=True)
        print("Rows in mkt data: "+str(len(mkt_data)))

        # Calcualte the Indicators
        supertrend = SuperTrend(st_period,st_multiplier,st_name_extension)
        mkt_data = supertrend.calculate(mkt_data)

        # Read in the target results
        target_data = self.readTargetResults(target_file, target_columns)
        print("\n\n")

        # Format boolean columns
        # None                       # convert to boolean

        # Output the Testing Info
        self.printTestInfo( output_info, mkt_data, target_data, "SuperTrend" )

        # Assert by series
        self.assertBySeries( output_info, mkt_data, target_data, target_columns )

        # Assert the data frame
        print(); print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert( "Final Results", mkt_data, target_data)


if __name__ == '__main__':
    unittest.main()
