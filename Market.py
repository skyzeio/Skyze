       
#----------------------------------------------------------------------------------------------------------
#
#   CLASS Market
#
#        represents a particular market (trading pair e.g. USD/AUD or Share/AUD or Bitcon/Eth
#                   on a particular exchange / broker e.g. IG, Poloniex, Bittrex, Cryptopia, ASX
#                   over a particular time period (interval) e.g. tick, 5 min, hourly, 4 hour, daily
#
#----------------------------------------------------------------------------------------------------------

# 3rd Party Libraries
import os
import sys
import csv
import pandas as pd
from dateutil import parser
from pathlib2 import Path                       # OO File management

# Skyze Libraries
import settings
import ExceptionSkyzeAbstract
# import Portfolio





class Market():
    

    def __init__(self, p_market_name, p_exchange, p_interval, p_market_data = [] ):
            self.market_name = p_market_name
            self.exchange = p_exchange
            self.interval = p_interval
            self.market_data = p_market_data
            
    
    @classmethod
    def fromTesting(cls, p_market_name , p_market_data = []):
            return cls(p_market_name,"","",p_market_data)

    
    def getMarketName( self ):
        return self.market_name 

    
    def getInterval( self ):
        return self.interval 

    
    def getExchange( self ):
        return self.exchange 
    
    
        
    
    # creates the full path and file name
    def constructFileName( self, p_testing ):
        file_name = ""
        if p_testing:
            file_name = os.path.join(settings.testing_file_path, "%s.csv" % p_market)
        else:
            file_name = os.path.join( settings.data_file_path, 
                                      "%s.csv" % ( settings.exchanges.get_value(self.exchange,"Directory_name") + "/"
                                                  + self.interval + "/"
                                                  + self.market_name) 
                                    )
            
            
        return file_name
                

        
    #    Read Data from CSV
    #    INPUT
    #           p_market    String
    #    OUTPUT
    #            pandas DataFrame
    #
    
    def readMarketDataCSV( self, p_market = "NOTPASSED", p_testing = False ): 
        "Opens the file and reads the data" 
        
        # default parameter handling
        if p_market == "NOTPASSED" : 
            p_market = self.market_name
#         p_market = "Bitcoin"

        file_path = self.constructFileName(p_testing)
        print("File Path: " + file_path)
        
        
        try:
            # df is type <class 'pandas.core.frame.DataFrame'>
            df = pd.read_csv(
                        file_path, 
                        header=None ,
                        names = [
                                  "Date", "Open", "High", "Low",
                                  "Close", "Volume", "MarketCap","HLOrder"
                                ],
#                         index_col = "Date"
                        )
        except IOError as err:
            print("File Error:   " + file_path)
            print("FileNotFound - Market::readMarketDataCSV .... IOError File does not exist")
#             raise IOError ("FileNotFound","EXCEPTION Market::readMarketDataCSV .... IOError File does not exist")
            return
        except:
            print("AN EXCEPTION - Market::readMarketDataCSV( p_market )")
            print("File path:   " + file_path)
            print(sys.exc_info())
            return
        else:
            # Convert the date column to a date !
#             d['Date'] = pd.to_datetime(d['Date'].astype(str), format='%Y%m%d')  # NOT NEEDED after making date the index column
              
            df.index = [parser.parse(str(d)) for d in df["Date"]]
            del df["Date"]
            return df 
        
        
        
    def saveMarketDataV01 (self, p_file_path = "", p_save_type="CSV" ):
        # Save the file to CSV 
        my_file = Path(p_file_path)
        if my_file.is_file():
            # File exists
            with open(p_file_path, 'a') as myfile:
                wr = csv.writer(myfile)
                # Add a empty row to ensure the CSV is written starting on the next row
                # Reverse it so it is date ascending (newest at the end)
                wr.writerows(list(reversed(self.market_data)))
        else:
            # No file so create new file
            with open(p_file_path, 'w') as myfile:
                wr = csv.writer(myfile)
                # Reverse it so it is date ascending (newest at the end)
                wr.writerows(reversed(self.market_data))
        return
        
        
        
    def saveMarketData (self, p_file_path = "", p_save_type="CSV" ):
        # Save the file to CSV 
        my_file = Path(p_file_path)
        if my_file.is_file():
            # File exists
            with open(p_file_path, 'a') as myfile:
                self.market_data.to_csv(myfile, header=False, date_format='%Y-%m-%d %H:%M:%S')
#                 wr = csv.writer(myfile)
                # Add a empty row to ensure the CSV is written starting on the next row
                # Reverse it so it is date ascending (newest at the end)
#                 print(len(self.market_data))
#                 wr.writerows(list(reversed(self.market_data)))
        else:
            # No file so create new file
            self.market_data.to_csv(p_file_path, header=False, date_format='%Y-%m-%d %H:%M:%S')
            
#             with open(p_file_path, 'w') as myfile:
#                 wr = csv.writer(myfile)
#                 # Reverse it so it is date ascending (newest at the end)
#                 wr.writerows(reversed(self.market_data))
        return