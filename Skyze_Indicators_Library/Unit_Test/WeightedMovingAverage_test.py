'''
Created on 05/09/2017

@author: michaelnew
'''


# 3rd Party

# Our libraries - Required
from Skyze_Standard_Library.Market import Market

# Skyze imports
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Skyze_Indicators_Library.WeightedMovingAverage import WeightedMovingAverage


class WeightedMovingAverage_test(UnitTestSkyzeAbstract):
    """Test class for the WeightedMovingAverage Indicator"""

    def test(self):
        """Main positive test case"""
        # Test Parameters
        output_info = True
        package_name = "Skyze_Indicators_Library"
        target_file = "Target-Results-WeightedMovingAverage-bitcoin"
        test_path = WeightedMovingAverage.getName() + "/"
        test_file = "bitcoin_TEST"
        target_columns = ["WMA_15"]
        test_columns = ["WMA_15"]

        # Remove spaces etc from test path
        test_path = test_path.replace(" ", "")

        # Strategy Parameters
        p_wma_period = 15
        p_wma_column = "Close"

        # Output Headings
        self.printTestHeader(test_file, target_file, test_columns)
        print("    WMA period: " + str(p_wma_period) +
              " on column: " + p_wma_column)

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(
            package_name, test_path, test_file,
            target_file, target_columns)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data, target_data,
                           WeightedMovingAverage.getName())

        # Create the Strategy
        wma = WeightedMovingAverage(
            p_wma_period,
            p_wma_column
        )

        # Calculate the strategy
        wma.calculate(mkt_data)

        # Output the Test run calculations
        self.printTestRun(output_info, mkt_data)

        # Assert by series
        self.assertBySeries(
            output_info, mkt_data, target_data, ["Close"] + target_columns)

        # Assert the data frame
        print()
        print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", mkt_data, target_data)


if __name__ == '__main__':
    unittest.main()
