'''
Created on 05/09/2017

@author: michaelnew
'''


# Standard Libraries


# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import

# Our libraries - Test Specific
from Indicators.Crosses import Crosses
from Indicators.MovingAverage import MovingAverage



class Crosses_test(UnitTestSkyzeAbstract):
    '''
    classdocs
    '''



    def test(self):

        # Test Parameters
        output_info    = False
        package_name   = "Indicators"
        test_path      = Crosses.name + "/"+package_name + "/"
        target_file    = "Results-bitcoin-Crosses"
        test_file      = "bitcoin_TEST"
        target_columns = ["MA_15","MA_30","Crossesdiff","Crosses"]            # ["Date","MA_15","MA_30","TGT_DIFF","TGT_CROSS"]
        test_columns   = ["MA_15","MA_30","Crossesdiff","Crosses"]

        # Indicator Parameters
        slow_ma_period = 15
        fast_ma_period = 30


        # Output Headings
        self.printTestHeader(test_file, target_file, test_columns)
        print ("     slow: " + str(slow_ma_period) + "   fast: " + str(fast_ma_period))

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData( test_path, test_file, target_file, target_columns )

        # Format boolean columns
        target_data["Crosses"] = target_data["Crosses"] == 1

        # Calcualte the Input Indicators
        mkt_data = MovingAverage(slow_ma_period,"Close").calculate(mkt_data)
        mkt_data = MovingAverage(fast_ma_period,"Close").calculate(mkt_data)

        # Calculate the Indicator to test
        crosses = Crosses("MA_15","MA_30","Up")
        mkt_data = crosses.calculate(mkt_data)

        # Output the Testing Info
        self.printTestInfo( output_info, mkt_data, target_data, crosses.getName())

        # Assert by series
        self.assertBySeries( output_info, mkt_data, target_data, target_columns )

        # Assert the data frame
        print(); print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert( "Final Results", mkt_data, target_data)





if __name__ == '__main__':
    unittest.main()
