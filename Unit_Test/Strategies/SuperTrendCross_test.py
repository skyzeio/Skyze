'''
Created on 05/09/2017

@author: michaelnew
'''

# 3rd Party
import unittest
import pandas as pd

# for writing to excel
import os
# import win32com.client
from pandas import ExcelWriter

# Skyze imports
import settings
from Indicators.SuperTrendCross import SuperTrendCross
from Market import Market

class SuperTrendCross_test(unittest.TestCase):
    '''
    classdocs
    '''
          
         
 
    def test(self):

        result = True
        self.assertEqual(result, True, "OH NO!")
        
        # Get the data
#         mkt = Market("Test-bitcoin-SuperTrend")
        mkt = Market.fromTesting(test_file)
        mkt_data = mkt.readMarketDataCSV(p_testing=True)
        
        # Create the Indicator
        p_wma_period         = 90
        p_wma_column         = "Close"
        p_fast_st_multiplier = 3
        p_fast_st_period     = 15
        p_slow_st_multiplier = 3.5
        p_slow_st_period     = p_fast_st_period
        stc = SuperTrendCross(
                                p_wma_period,  
                                p_wma_column,
                                p_fast_st_multiplier,     
                                p_fast_st_period,
                                p_slow_st_multiplier,     
                                p_slow_st_period
                            )
        
        print();print();print(); print("=== Super Trend Cross Calc === === === === === ")
        print();print();print(); print("=== Original market ================")
        print(mkt_data.head(0))
        print(mkt_data.tail(5))
        
        # Calculate the indicator
        stc.calculate(mkt_data)
        
        # Print Results
        print();print();print(); print("=== Super Trend Cross Calc === === === === === ")
        print(mkt_data.head(5))
        print(mkt_data.tail(10))
         

#         xlApp=win32com.client.Dispatch("Excel.Application")
#         wb = xlApp.Workbooks.Open(Filename="C:\Full Location\To\excelsheet.xlsm")
        
#         # WRITE IN DATA FRAME TO SHEET 5
        writer = ExcelWriter(settings.testing_file_path+'Test Results.xlsx')
        mkt_data.to_excel(writer,'Results')
        writer.save() 
         