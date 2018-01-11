"""Created on 05/09/2017 @author: michael new"""


# 3rd Party

# Our libraries - Required
from Skyze_Standard_Library.Market import Market
from Skyze_Standard_Library.Skyze_Utility import readCSV

# Skyze imports
from Skyze_Standard_Library.Unit_Test.UnitTestSkyzeAbstract import *       # Parent import
from Skyze_Indicators_Library.ArbitrageTriangular import ArbitrageTriangular
import Skyze_Standard_Library.settings_skyze as settings_skyze


class ArbitrageTriangular_test(UnitTestSkyzeAbstract):
  """Test class for the ArbitrageTriangular Indicator"""

  def test(self):
    """Main positive test case"""
    # Test Parameters
    output_info = True
    save_test_run_to_excel = False
    package_name = "Skyze_Indicators_Library"
    target_file = "Target-Results-ArbitrageTriangular-USD-BTC-ETH-USD"
    test_file = "ArbitrageTriangular_TEST"
    test_columns = ["Date", "BTCUSD", "BTCETH", "ETHUSD"]
    target_columns = test_columns + ["Arb_Value", "Arb_Opp"]
    boolean_columns = ["Arb_Opp"]
    column_sets = []

    # Strategy Parameters
    p_pair1 = "BTCUSD"
    p_pair2 = "BTCETH"
    p_pair3 = "ETHUSD"
    p_arb_margin = 0.02  # 2%

    # Output Headings
    self.printTestHeader(package_name, ArbitrageTriangular.getName(),
                         test_file, target_file, test_columns)
    print("   Pair 1: " + str(p_pair1) +
          "   Pair 2: " + str(p_pair2) +
          "   Pair 3: " + str(p_pair3) +
          "   Arb Margin: " + str(p_arb_margin))
    print("\nTarget columns: " + str(target_columns))

    # Load test and result data =============================================
    # Form the path
    test_path = package_name + "/" + settings_skyze.test_data_file_path
    # Remove spaces etc from test path
    test_path = test_path.replace(" ", "")
    print("\nTest file path: " + test_path)
    # Get the test data
    test_data = readCSV(test_path, test_file, test_columns)
    print("Rows in test data:\t" + str(len(test_data)) + "\n")

    # Read in the target results
    target_path = package_name + "/" + settings_skyze.target_results_file_path \
        + ArbitrageTriangular.getName() + "/"
    # Remove spaces etc from test path
    target_path = target_path.replace(" ", "")
    print("Settings results path:\t" +
          settings_skyze.target_results_file_path)
    print("Target Path:\t" + target_path)
    print("\nTarget Data:\t" + target_file)
    print("\nTarget file path: " + target_path + "\n")
    target_data = readCSV(target_path, target_file, target_columns)
    print("\n\n")

    # Format boolean columns
    if boolean_columns != None:
      for column in boolean_columns:
        target_data[column] = target_data[column] == 1

    # =======================================================================

    # Output the Testing Info
    self.printTestInfo(output_info, test_data,
                       target_data, ArbitrageTriangular.getName(), column_sets)

    # Create the Strategy
    arb = ArbitrageTriangular(
        p_pair1,
        p_pair2,
        p_pair3,
        p_arb_margin
    )

    # Calculate the strategy
    arb.calculate(test_data)

    # Save Test Results to Excel
    if save_test_run_to_excel:
      print("Saving to Excel:")
      arb._saveToExcel(test_data, settings_skyze.test_results_file_path)

    # Output the Test run calculations
    self.printDataSets("Test Run", output_info, test_data, column_sets)

    # Series asserts
    target_columns.pop(0)  # Don't need the date col as it is the index
    self.assertBySeries(output_info, test_data, target_data,
                        target_columns, boolean_columns)
    # Assert the data frame
    print()
    print("=== DataFrame Equal === === === === === ")
    self.dataframe_assert("Final Results", test_data, target_data)


if __name__ == '__main__':
  unittest.main()
