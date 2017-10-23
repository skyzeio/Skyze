'''
Created on 05/09/2017

@author: michaelnew
'''


# Standard Libraries


# Our libraries - Required
from Unit_Test.UnitTestSkyzeAbstract import *

# Our libraries - Test Specific
from Skyze_Indicators_Library.SuperTrend import SuperTrend


class SuperTrend_test(UnitTestSkyzeAbstract):
    """Test the Crosses class"""

    def _parseInt(self, mkt_data, target_data):
        print("About to multiply")

        def parseInt(x):
            price_multiplier = 100000000
            return int(x * price_multiplier)

        mkt_data["Open"] = mkt_data["Open"].apply(parseInt)
        mkt_data["High"] = mkt_data["High"].apply(parseInt)
        mkt_data["Low"] = mkt_data["Low"].apply(parseInt)
        mkt_data["Close"] = mkt_data["Close"].apply(parseInt)
        target_data["Open"] = target_data["Open"].apply(parseInt)
        target_data["High"] = target_data["High"].apply(parseInt)
        target_data["Low"] = target_data["Low"].apply(parseInt)
        target_data["Close"] = target_data["Close"].apply(parseInt)
        print("Done")

    def test(self):
        """ Tests the most common everything works path"""
        # Test Parameters
        output_info = True
        package_name = "Indicators"
        test_path = package_name + "/" + SuperTrend.name + "/"
        target_file = "Target-Results-SuperTrend-bitcoin"
        test_file = "bitcoin_TEST"
        target_columns = ["H-L", "H-PC", "L-PC", "True_Range", "ATR_15",
                          "basic_ub", "basic_lb", "final_ub", "final_lb", "Super_Trend"]
        test_columns = ["H-L", "H-PC", "L-PC", "True_Range", "ATR_15",
                        "basic_ub", "basic_lb", "final_ub", "final_lb", "Super_Trend"]

        # Indicator Parameters
        st_period = 15
        st_multiplier = 3
        st_name_extension = ""

        # Output Headings
        self.printTestHeader(test_file, target_file, test_columns)
        print("     period: " + str(st_period) + "   Multiplier: "
              + str(st_multiplier))

        # Load test and result data
        mkt_data, target_data = self.getTestAndResultData(
            test_path, test_file, target_file, target_columns)

        # Could parse the data to 10e8 int
        # didn't work as python kernal kept crashing
        # mkt_data, target_data = slef.parseInt(mkt_data, target_data)

        # Output the Testing Info
        self.printTestInfo(output_info, mkt_data,
                           target_data, SuperTrend.getName())

        # Calcualte the Indicators
        supertrend = SuperTrend(st_period, st_multiplier, st_name_extension)
        mkt_data = supertrend.calculate(mkt_data)

        # Output the Test run calculations
        self.printTestRun(output_info, mkt_data)

        # Assert by series
        self.assertBySeriesDiffs(
            output_info, mkt_data, target_data, target_columns)

        # Assert the data frame
        print()
        print("=== DataFrame Equal === === === === === ")
        self.dataframe_assert("Final Results", mkt_data, target_data)


if __name__ == '__main__':
    unittest.main()
