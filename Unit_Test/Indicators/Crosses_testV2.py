

# Standard Libraries


# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Market import Market

# Our libraries - Test Specific
from Indicators.Crosses import Crosses
from Indicators.MovingAverage import MovingAverage




class Crosses_test(UnitTestSkyzeAbstract):
    '''
    classdocs
    '''


#         super(Crosses_test, self).__init__(self)


    def test(self):

        # Test Parameters
        output_info    = False
        target_file    = "Results-bitcoin-Crosses"
        test_file      = "bitcoin_TEST"
        target_columns = ["MA_15","MA_30","Crossesdiff","Crosses"]            # ["Date","MA_15","MA_30","TGT_DIFF","TGT_CROSS"]
        test_columns   = ["MA_15","MA_30","Crossesdiff","Crosses"]

        self.printTestHeader(test_file, target_file, test_columns)

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(test_file,target_file,target_columns)

        # Format boolean columns
        target_data["Crosses"] = target_data["Crosses"] == 1                        # convert to boolean

        # Calcualte the Indicators
        mkt_data = MovingAverage(15,"Close").calculate(mkt_data)
        mkt_data = MovingAverage(30,"Close").calculate(mkt_data)
        crosses = Crosses("MA_15","MA_30","Up")
        mkt_data = crosses.calculate(mkt_data)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data, target_data, "SuperTrend")

        # Assert by series
        self.assertBySeries(output_info, mkt_data, target_data, target_columns)

        # Assert the data frame
        print(); print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", mkt_data, target_data)







if __name__ == '__main__':
    unittest.main()
