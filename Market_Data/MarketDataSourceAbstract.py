'''
Created on 08/09/2017

@author: michaelnew
'''

import pandas as pd
from datetime import datetime, timedelta
import os
import re
import csv
import sys

import inspect

import requests
from pathlib2 import Path                       # OO File management
import urllib
import urllib.request as urllibReq
from collections import deque                   # deque to get last lines of CSV file


# skyze libraries
import settings
from Market import Market
from ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
# from exceptions import BaseException


class MarketDataSourceAbstract(ExceptionSkyzeAbstract):
    '''
    classdocs
    '''


    def __init__(self, p_source_name, p_source_dir_name, p_url_list_all_markets, p_max_start_date, 
                 p_default_end_date, p_url_market_history, p_exchange_intervals ):
        '''
        Constructor
        '''
        self.source_name             = p_source_name
        self.source_dir_name         = p_source_dir_name
        self.url_list_all_markets    = p_url_list_all_markets,          # For some reason the str is cast to a tuple
        self.max_start_date          = p_max_start_date
        self.default_end_date        = p_default_end_date
        self.url_market_history      = p_url_market_history
        
        
        if p_exchange_intervals == []:  
            raise ExceptionSkyzeAbstract("MarketDataSource Init - exchagne interval parameter required")
        
        self.exchange_intervals      = settings.intervals.ix[p_exchange_intervals]
        pass
    
    
    
    
                
    def getMarketsForCurrency (self):
        ''' 
            
        '''
        return "NOT IMPIMENTED"
    
    
    
    
                
    def getCurrencies (self):
        ''' 
        '''
        return "NOT IMPIMENTED"
    
    
    
    
    
    
    def convertMonthString( self, 
                  p_month_str       # String of 3 characters representing the month
                  ):
        ''' Converts month in Jan form to 01 form
        '''
        
        month_num_string = "ERR"
        
        if   p_month_str == "Jan" : month_num_string = "01"
        elif p_month_str == "Feb" : month_num_string = "02"
        elif p_month_str == "Mar" : month_num_string = "03"
        elif p_month_str == "Apr" : month_num_string = "04"
        elif p_month_str == "May" : month_num_string = "05"
        elif p_month_str == "Jun" : month_num_string = "06"
        elif p_month_str == "Jul" : month_num_string = "07"
        elif p_month_str == "Aug" : month_num_string = "08"
        elif p_month_str == "Sep" : month_num_string = "09"
        elif p_month_str == "Oct" : month_num_string = "10"
        elif p_month_str == "Nov" : month_num_string = "11"
        elif p_month_str == "Dec" : month_num_string = "12"
            
        return month_num_string
    
        
        
        
    
    # creates the full path and file name
    def fileName( self, p_market_name, p_interval ):
        return os.path.join( settings.data_file_path, 
                             "%s.csv" % ( self.source_dir_name + "/"
                                          + p_interval + "/"
                                          + p_market_name) 
                            )
         
         
         
         
                
    def post_process_file(self, p_market, p_interval):
        pass
                     
    
    
    
    
    def getLoadDatesCMC (self, p_market, p_load_start_date, p_file_path):
        file_start_date = "No File"
        file_end_date = "No File"
        load_start_date = p_load_start_date
        
        # Create File
        my_file = Path(p_file_path)
        if my_file.is_file():
            # File Exiss        
            #Get the End date from the first row
            try:
                top = pd.read_csv(p_file_path,nrows=0)
#                 except pd.io.common.EmptyData.Error:
#                     file_start_date = "No File"
            except:
                print("UNKNOWN ERROR: CoinMarketCap::updateMarketData .. read csv file")
                print(sys.exc_info()[0])
                error_list = p_market + error_list
            else:
                file_start_date = top.columns.values[0][:11]
                
                #Get the Start date from the last row
                with open(p_file_path, 'r') as f:
                    q = deque(f, 2)
                    if len(q) == 2:
                        if q[1] == "\n" : 
                            load_start_date = file_end_date = q[0][:8]
                        else:
                            load_start_date = file_end_date = q[1][:8]
                    else:
                        load_start_date = file_end_date = q[0][:8]
                    
                #print(q)
#                 load_start_date = file_end_date = q[0][:8] #11
        
        if file_end_date == "No File":
            load_start_date = "20100101"
        
        return file_start_date, file_end_date, load_start_date
                     
    
    
    
    
    def getLoadDates (self, p_market, p_interval, p_load_start_date, p_file_path):
        file_start_date = "No File"
        file_end_date = "No File"
        load_start_date = p_load_start_date
        
        # Create File
        my_file = Path(p_file_path)
        if my_file.is_file():
            # File Exiss        
            try:
                #Get the File Start date from the last row
                top = pd.read_csv(p_file_path,nrows=0)
            except:
                print("UNKNOWN ERROR: MarketDataSourceAbstract::getLoadDates .. read csv file")
                print(sys.exc_info()[0])
            else:
                file_start_date = top.columns.values[0]
                
                #Get the File End date from the last row
                with open(p_file_path, 'r') as f:
                    q = deque(f, 2)
                    if len(q) == 2:
                        if q[1] == "\n" : 
                            file_end_date = datetime.strptime( q[0][:q[0].find(',')], "%Y-%m-%d %H:%M:%S" )
                        else:
                            file_end_date = datetime.strptime( q[1][:q[1].find(',')], "%Y-%m-%d %H:%M:%S" )
                    else:
                        file_end_date = datetime.strptime( q[0][:q[0].find(',')], "%Y-%m-%d %H:%M:%S" )
                        
                load_start_date = file_end_date + timedelta(0,p_interval.Seconds)  # Add a second
                            
        return file_start_date, file_end_date, load_start_date
                
                
                
                
        
    
    def getHistoricalData( self, p_market, p_interval, p_start_date="", p_end_date="" ):
        '''
            Returns 
        '''
        # Set dates
        if p_start_date == "" :   p_start_date = self.default_start_date
        if p_end_date == ""   :   p_end_date   = self.default_end_date
        
        # Get the URL
        market_history_url = self.formatMarketHistoryURL( p_market, p_interval, p_start_date, p_end_date )
        print("URL: "+market_history_url)
        
        # Call the API
        market_history = requests.get( market_history_url )    # <class 'dict'>
        
        # format the data to Skyze format
        payload = self.post_process_market_history(market_history)
        
        return payload
        
#         # Request failures
#         if market_history.status_code == 503:
#             raise ExceptionSkyzeAbstract()
#         
#         market_history = pd.DataFrame(market_history.json())                                        # all_markets.json() is class 'dict'
#         payload = pd.DataFrame(list(market_history.Data)) 
#         if len(payload) > 0: 
#             pd.DatetimeIndex(payload.Timestamp*10**9)                                                   # all_markets.json() is class 'dict'
#             payload.index = pd.to_datetime(payload.Timestamp*10**9)                                     # Set the Timestamp as the indes
#             payload = payload.iloc[::-1]                                                                # Reverse teh order to time ascending
#         
#         '''
#             Return DataFrame has columns [ Amount     Label     Price   Timestamp     Total    TradePairId  Type  ]
#         '''
#          
#         return payload
    
    
    
        
    
    
    
    
    def updateMarketData( self, p_market_list ="all" ): 
        if p_market_list == "all":
            mkt_list = self.getAllMarkets() # TODO .Label for poloniex or cmc? Move to subclass
        else:
            mkt_list = p_market_list
            
        download_total = str(len(mkt_list))
        interval_total = len(self.exchange_intervals)
        print("Markets to downlaod: " + download_total + "    ... each market has " + str(interval_total) + " intervals")
        
        # convert market format from / to _
        mkt_list = [w.replace('/', '_') for w in mkt_list]
        
        # Loop throuth the Markets
        error_list = []
        no_data_list = []
        mkt_count = 0
        for market in mkt_list: #self.markets:
#             print("No Data:   "+str(len(no_data_list)))
#             print(no_data_list)
            mkt_count += 1
            print(); print(str(mkt_count)+" of "+download_total+". "+market )
            
            for index, interval in self.exchange_intervals.iterrows():
                # Default start date if data not previously laoded
                load_start_date = self.max_start_date   
                load_end_date   = self.default_end_date
                
                # Get the load dates
                file_path = self.fileName(market, interval.Directory_name)
                file_start_date, file_end_date, load_start_date = self.getLoadDates(market, interval, load_start_date, file_path)
                
                # Print the dates
                print()
                print("Interval: "+interval.Directory_name + "   Seconds: " + str(interval.Seconds)+"   Load start time: "+str(datetime.now() ))
                print("File: "+file_path)
                print("File Start: "+str(file_start_date)+"   End: "+str(file_end_date))
                print("Load Start: "+str(load_start_date)+"   End: "+str(load_end_date))
                
                # Calls the URL
                try:
                    market_data = self.getHistoricalData( market, interval.Seconds, load_start_date + timedelta(hours=10), load_end_date + timedelta(hours=10) ) 
                except urllib.error.HTTPError as err:
                    self.printException(inspect.currentframe().f_lineno,"ERROR: HHTP - Probably wrong file name in URL - "+str(err.args)+" --- "+str(sys.exc_info()[0]))
                    error_list = error_list.append(market)
                except:
                    self.printException(inspect.currentframe().f_lineno,"ERROR: unknown -")
                    error_list = [market] + error_list
                else:
                    # Check for no data message
                    if len(market_data)  == 0:
                        print("No data found for this market.")
                    else:
                    
                        # Format the date column
                        print("Number of Rows imported: "+str(len(market_data)))
                        
                        # Save the data
                        mkt = Market(market, market_data)
                        mkt.saveMarketData( p_file_path = file_path )
                        
                        # exchange specific post processing
                        self.post_process_file(market,interval.Directory_name)
                
        print(); print(); print();
        print("Success: "+str(len(mkt_list))) #-len(error_list)))   
        #-str(len(no_data_list))
        print("Error:   "+str(len(error_list)))
        print(error_list)
        print("No Data:   NOT IMPLEMENTED ... "+str(len(no_data_list)))
        print(no_data_list)