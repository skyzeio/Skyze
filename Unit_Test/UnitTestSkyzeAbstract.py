'''
Created on 05/09/2017

@author: michaelnew
'''
# 3rd Party Libraries
import os
import unittest
from pandas.util.testing import assert_frame_equal
from pandas.util.testing import assert_series_equal
import pandas as pd
from dateutil import parser

# Skyze Libraries
import settings




class UnitTestSkyzeAbstract(unittest.TestCase):
    '''
    classdocs
    '''


    def readTargetResults( self, p_results_file, p_column_names ):
        "Opens the file and reads the data"

    #     print("File Path: " + settings.data_file_path)
        file_path = os.path.join(settings.results_file_path, "%s.csv" % p_results_file)

        column_names = ["Date"] + p_column_names

        try:
            # d is type <class 'pandas.core.frame.DataFrame'>
            target_results = pd.read_csv(
                                            file_path,
                                            header=None ,
                                            names = column_names,
                                            skiprows = 1
                                        )
        except IOError as err:
            print("File Error:   " + file_path)
            raise IOError ("FileNotFound","EXCEPTION SkyzeUnitTest::readTargetResults .... IOError File does not exist")
            return
        except:
            print("AN EXCEPTION - SkyzeUnitTest::readTargetResults( p_market )")
            print("File path:   " + file_path)
            print(sys.exc_info())
            return
        else:
            # Convert the date column to a date ! ...... Not needed now date is the index
            #target_results['Date'] = pd.to_datetime(target_results['Date'].astype(str), format='%Y%m%d')

            # Move the date column to the index
            target_results.index = [parser.parse(str(d)) for d in target_results["Date"]]
            del target_results["Date"]

            return target_results
