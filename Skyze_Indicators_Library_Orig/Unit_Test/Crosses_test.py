'''
Created on 05/09/2017

@author: michaelnew
'''


# Standard Libraries


# Our libraries - Required
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *       # Parent import

# Our libraries - Test Specific
from Skyze_Indicators_Library.Crosses import Crosses
from Skyze_Indicators_Library.MovingAverage import MovingAverage


class Crosses_test(UnitTestSkyzeAbstract):
    """Test the Crosses class"""

    # def childSetUp(self):

    def test(self):
        """Preapre for testing
            calling it 'child' so this can be moved to the parent class """
        # Test Parameters
        self.output_info = True
        self.package_name = "Skyze_Indicators_Library"
        self.test_path = Crosses.getName() + "/"
        self.target_file = "Results-bitcoin-Crosses"
        self.test_file = "bitcoin_TEST"
        self.target_columns = ["MA_15", "MA_30",
                               "Crossesdiff", "Crosses", "Crosses_direction"]
        self.test_columns = ["MA_15", "MA_30",
                             "Crossesdiff", "Crosses", "Crosses_direction"]
        self.column_sets = []

        # Indicator Parameters
        self.slow_ma_period = 15
        self.fast_ma_period = 30

        # Output Headings
        self.printTestHeader(self.package_name, Crosses.getName()
                             + " Indicator", self.test_file, self.target_file,
                             self.test_columns)
        print("     slow: " + str(self.slow_ma_period) +
              "   fast: " + str(self.fast_ma_period))

        # Load test and result data
        self.mkt_data, self.target_data = self.getTestAndResultData(
            self.package_name, self.test_path, self.test_file,
            self.target_file, self.target_columns)

        # Output the Testing Info
        self.printTestInfo(self.output_info, self.mkt_data,
                           self.target_data, Crosses.getName())

        # Format boolean columns
        self.target_data["Crosses"] = self.target_data["Crosses"] == 1

        # Calcualte the Input Indicators
        self.mkt_data = MovingAverage(
            self.slow_ma_period, "Close").calculate(self.mkt_data)
        self.mkt_data = MovingAverage(
            self.fast_ma_period, "Close").calculate(self.mkt_data)

        # Calculate the Indicator to test
        crosses = Crosses("MA_15", "MA_30", "Up")
        self.mkt_data = crosses.calculate(self.mkt_data)

        # Output the Test run calculations
        self.printTestRun(self.output_info, self.mkt_data, self.column_sets)

        # Output summary stats into the test run
        print("\n=== Test Run Stats === === === === === ")
        print(self.mkt_data.loc[self.mkt_data.Crosses == True].head(10))
        print("Number of crosses: " +
              str(len(self.mkt_data.loc[self.mkt_data.Crosses == True])) +
              " of " + str(len(self.mkt_data)))

        # Assert by series
        self.assertBySeriesDiffs(self.output_info, self.mkt_data,
                                 self.target_data, self.target_columns)

        # Assert the data frame
        print("\n=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", self.mkt_data, self.target_data)

        return


if __name__ == '__main__':
    unittest.main()
