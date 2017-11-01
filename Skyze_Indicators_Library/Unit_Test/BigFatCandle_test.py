"""Created on 05/09/2017
    @author: michaelnew"""


# Standard Libraries


# Our libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *

# Our libraries - Test Specific
from Skyze_Indicators_Library.BigFatCandle import *


class BigFatCandle_test(UnitTestSkyzeAbstract):
    """Test the Crosses class"""

    def test(self):
        """ Tests the most common everything works path"""
        # Test Parameters
        output_info = True
        save_test_run_to_excel = True
        package_name = "Skyze_Indicators_Library"
        test_path = BigFatCandle.getName() + "/"
        target_file = "Target-Results-BigFatCandle-bitcoin"
        test_file = "bitcoin_TEST"
        target_columns = ["BigFatCandle", "BFC_ratio"]
        test_columns = ["BigFatCandle", "BFC_ratio"]
        boolean_columns = ["BigFatCandle"]
        column_sets = []

        # Indicator Parameters
        bfc_fat_ratio = 0.65

        # Output Headings
        self.printTestHeader(package_name, BigFatCandle.getName()
                             + " Indicator", test_file, target_file, test_columns)
        print("\tFat Ratio:\t" + str(bfc_fat_ratio))

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(
            package_name, test_path, test_file,
            target_file, target_columns)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data,
                           target_data, BigFatCandle.getName(), column_sets)

        # Calcualte the Indicators
        big_fat_candle = BigFatCandle(bfc_fat_ratio)
        mkt_data = big_fat_candle.calculate(mkt_data)

        # Save Test Results to Excel
        if save_test_run_to_excel:
            self.saveTestResults(mkt_data, BigFatCandle.getName(),
                                 p_testing=True)

        # Output the Test run calculations
        self.printDataSets("Test Run", output_info, mkt_data, column_sets)

        # Assert by series
        self.assertBySeriesDiffs(output_info, mkt_data,
                                 target_data, target_columns, boolean_columns)

        # Assert the data frame
        print("\n=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", mkt_data, target_data)


if __name__ == '__main__':
    unittest.main()
