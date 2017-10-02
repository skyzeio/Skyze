"""
Created on 05/09/2017

@author: michaelnew
"""


# 3rd Party

# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Market import Market

# Skyze imports
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Strategies.SuperTrendCrossScreener import SuperTrendCrossScreener



class SuperTrendCrossScreener_test(UnitTestSkyzeAbstract):
    """Test class for the SuperTrendCrossScreener strategy"""

    def test_signal(self):
        """ Tests Signal on the most common everything works path"""
        # Test Parameters
        output_info    = True
        package_name = "Strategies"
        test_path = package_name + "/" + SuperTrendCrossScreener.getName() + "/"
        target_file    = "Target-Results-SuperTrendCrossScreener-bitcoin"
        test_file      = "bitcoin_TEST"
        target_columns = ['WMA_90', 'H-L', 'H-PC', 'L-PC', 'True_Range', 'ATR_15',
         'basic_ub_Fast', 'basic_lb_Fast', 'final_ub_Fast', 'final_lb_Fast',
         'Super_Trend_Fast', 'basic_ub_Slow',  'basic_lb_Slow', 'final_ub_Slow',
         'final_lb_Slow', 'Super_Trend_Slow', 'Bull1', 'Bull2', 'Bull3', 'Bull31',
         'Crs_Bulldiff', 'Crs_Bull', 'Direction', 'Bull5', 'Bullish', 'Bear1',
         'Bear2', 'Bear3', 'Bear31', 'Crs_Beardiff', 'Crs_Bear', 'Bear5', 'Bearish',
         'Signal']
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
        print("    WMA period: " + str(p_wma_period) + " on column: " + p_wma_column)
        print("    Fast ST Multiplier: " + str(p_fast_st_multiplier) + " on period: " + str(p_fast_st_period))
        print("    Slow ST Multiplier: " + str(p_slow_st_multiplier) + " on period: " + str(p_slow_st_period))
        print("    Fat Ratio: " + str(p_fat_ratio))
        print("    Crossing period: " + str(p_days_since_cross))

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(test_path, test_file, target_file, target_columns)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data, target_data, SuperTrendCrossScreener.getName())

        # Create the Strategy
        stc = SuperTrendCrossScreener(
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

        # Output the Test run calculations
        self.printTestRun(output_info, mkt_data)

        # Let's have a look at the signal column
        print("\n\n=== Columns ======")
        print(mkt_data.columns.values)
        print("\n\n=== Shorts ======")
        print("Bearish count: ", end='')
        print(len(mkt_data.loc[mkt_data.Bearish]))
        print(mkt_data[["Close","Signal"]].loc[mkt_data.Bearish].head(10))
        print("\nShort Signal count: ", end='')
        print(len(mkt_data.loc[mkt_data.Signal == -1]))
        print(mkt_data[["Close","Signal"]].loc[mkt_data.Signal == -1].head(10))
        print("\n\n=== Longs ======")
        print("Bullish count: ", end='')
        print(len(mkt_data.loc[mkt_data.Bullish]))
        print(mkt_data[["Close","Signal"]].loc[mkt_data.Bullish].head(10))
        print("\nLong Signal count: ", end='')
        print(len(mkt_data.loc[mkt_data.Signal == 1]))
        print(mkt_data[["Close","Signal"]].loc[mkt_data.Signal == 1].head(10))

        print("\n\n=== Describe ======")
        print(mkt_data[["WMA_90","Bull1","Bull2","Bull3","Bull5","Bullish"]].describe())

        # Commented out as there is no target file to assert with
        # Assert by series
        self.assertBySeries(output_info, mkt_data, target_data, target_columns)

        # Assert the data frame
        print(); print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", mkt_data, target_data)


if __name__ == '__main__':
    unittest.main()
