# Unit Test Process

## Skyze Unit Test Class
to do

## Unit Testing Indicators and Strategies
1. __Create the Unit Test file__
   * Copy the SuperTrend_test file and rename with
   ```ClassBeingTested_test.py ```
   * update the test specific lines   
* __Create Test Calculations Excel spreadsheet__
   * Save it as ```Test-Calcs-ClassBeingTested-MarketDataName.xlsx``` in the ```REPO/Data/Trading/Test_Data``` directory e.g. ```Test-Calcs-SuperTrend-Bitcoin.xlsx```
   * include the Market data columns OHLCVMC. This allows us to check the market data is same in both the excel and python
   * calculate the results in adjacent columns
   * ensure Excel column names match with the Dataframe column names
   * have a head row with no spaces in the column name
* __Save results to CSV__
   * Once excel is accurate save it as a csv with same name ```Target-Results-ClassBeingTested.csv ``` in the same directory
   * Check that the csv does not have any extra rows at the end of the file or columns (empty ,,, at end of rows)
* __Run the unit test __
   * from the repo directory with command ```python3 ClassBeingTested_test.py```
* __Results__
   * if you want to see the detailed results then set ```output_info    = True```. this will display detail to the console as well as save the test output to an excel file in the test directory as the name ```Test-Output-Filename.xls``` where Filename is set in the unit test class
