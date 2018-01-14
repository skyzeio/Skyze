"""Created on 25/10/2017
@author: michaelnew"""


# 3rd Party

# Our libraries - Required
from Skyze_Standard_Library.Market import Market

# Skyze imports
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Skyze_Indicators_Library.AverageTrueRange import AverageTrueRange


class AverageTrueRange_test(UnitTestSkyzeAbstract):
    """Test class for the AverageTrueRange Indicator"""

    def test(self):
        """Main positive test case"""
        # Test Parameters
        output_info = True
        package_name = "Skyze_Indicators_Library"
        target_file = "Target-Results-AverageTrueRange-bitcoin"
        test_path = AverageTrueRange.getName() + "/"
        test_file = "bitcoin_TEST"
        target_columns = ["ATR_15"]
        test_columns = ["ATR_15"]

        # Remove spaces etc from test path
        test_path = test_path.replace(" ", "")

        # Strategy Parameters
        p_atr_period = 15
        p_atr_column = "Close"

        # Output Headings
        self.printTestHeader(test_file, target_file, test_columns)
        print("    MA period: " + str(p_atr_period) +
              " on column: " + p_atr_column)

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(
            package_name, test_path, test_file,
            target_file, target_columns)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data,
                           target_data, AverageTrueRange.getName())

        # Create the Strategy
        atr = AverageTrueRange(p_atr_period, p_atr_column)

        # Calculate the strategy
        atr.calculate(mkt_data)

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
