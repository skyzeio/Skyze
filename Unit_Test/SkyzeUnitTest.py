'''
Created on 05/09/2017

@author: michaelnew
'''
# 3rd Party Libraries
import os
import unittest
import pandas as pd

# Skyze Libraries
import settings




class SkyzeUnitTest(unittest.TestCase):
    '''
    classdocs
    '''
        
        
    def readTargetResults( self, p_results_file, p_column_names ): 
        "Opens the file and reads the data" 
        
    #     print("File Path: " + settings.data_file_path)
        file_path = os.path.join(settings.results_file_path, "%s.csv" % p_results_file)
        
        
        try:
            # d is type <class 'pandas.core.frame.DataFrame'>
            d = pd.read_csv(
                        file_path, 
                        header=None ,
                        names = p_column_names,
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
            # Convert the date column to a date !    
            print(d)        
            d['Date'] = pd.to_datetime(d['Date'].astype(str), format='%Y%m%d')
              
            return d  
        