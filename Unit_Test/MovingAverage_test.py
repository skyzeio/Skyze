"""Created on 05/09/2017

@author: michaelnew"""


# 3rd Party

# Our libraries - Required
from Market import Market

# Skyze imports
from Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Skyze_Indicators_Library.MovingAverage import MovingAverage


class MovingAverage_test(UnitTestSkyzeAbstract):
    """Test class for the MovingAverage Indicator"""

    def test(self):
        """Main positive test case"""
        # Test Parameters
        output_info = True
        package_name = "Indicators"
        target_file = "Target-Results-MovingAverage-bitcoin"
        test_path = package_name + "/" + MovingAverage.getName() + "/"
        test_file = "bitcoin_TEST"
        target_columns = ["MA_15"]
        test_columns = ["MA_15"]

        # Remove spaces etc from test path
        test_path = test_path.replace(" ", "")

        # Strategy Parameters
        p_ma_period = 15
        p_ma_column = "Close"

        # Output Headings
        self.printTestHeader(test_file, target_file, test_columns)
        print("    MA period: " + str(p_ma_period) +
              " on column: " + p_ma_column)

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(
            test_path, test_file, target_file, target_columns)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data,
                           target_data, MovingAverage.getName())

        # Create the Strategy
        ma = MovingAverage(
            p_ma_period,
            p_ma_column
        )

        # Calculate the strategy
        ma.calculate(mkt_data)

        # Output the Test run calculations
        self.printTestRun(output_info, mkt_data)

        # Assert by series
        self.assertBySeries(output_info, mkt_data, target_data, target_columns)

        # Assert the data frame
        print()
        print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", mkt_data, target_data)


if __name__ == '__main__':
    unittest.main()
