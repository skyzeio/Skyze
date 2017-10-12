'''
Created on 08/09/2017

@author: michaelnew
'''
#----------------------------------------------------------------------------------------------------------
#
#   CLASS Poloniex
#
#        Information Provider
#
#----------------------------------------------------------------------------------------------------------




# 3rd Party Imports
from pprint import pprint
import pandas as pd
from pandas.io.json import json_normalize
import datetime as datetime
import urllib
import urllib.request as urllibReq
import requests
# import os
import re
# import csv
import sys

from inspect import stack
import inspect

# Skyze Libraries
import settings
from Skyze_Market_Data_Updater.MarketDataSourceAbstract import MarketDataSourceAbstract
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Market import Market


'''
Get Market History


'''

class IGMarkets (MarketDataSourceAbstract,ExceptionSkyzeAbstract) :

    def __init__(self):
        source_name             = "IG Markets"
        source_dir_name         = "ig_markets"
        url_list_all_markets    = ""
        max_start_date          = datetime.datetime(2010,1,1)
        default_end_date        = datetime.datetime.now()
        url_market_history      = ""
#         exchange_intervals      = ["DAY_1", "HOUR_4", "HOUR_2","MIN_5"]
        exchange_intervals      = ["DAY_1", "HOUR_4", "HOUR_2"]

        super().__init__(source_name, source_dir_name, url_list_all_markets, max_start_date,
                          default_end_date, url_market_history, exchange_intervals)




    def getAllMarkets(self, p_save_excel = False):
        """
            Returns a list of all markets (currency pairs) on the exchange



        """
        print("Get all markets")
        # query the website and return the html to the variable ‘page’
        all_markets = requests.get(self.url_list_all_markets[0])    # <class 'dict'>
        all_markets = pd.DataFrame(all_markets.json())           # all_markets.json() is class 'dict'

#         payload = pd.DataFrame(list(all_markets.Data))

        if p_save_excel:
            payload.to_excel(settings.data_file_path+'/Cryptopia_Markets.xlsx', index=False)

        return list(all_markets.columns.values)





    def formatMarketHistoryURL(self, p_market, p_interval, p_start_date, p_end_date):

        # "https://poloniex.com/public?command=returnChartData&currencyPair={0}&start={1}&end={2}&period={3}"
        formatted_url = self.url_market_history.format(p_market, p_start_date.strftime("%s"), p_end_date.strftime("%s"), p_interval)

        return formatted_url





        '''
            get Historical Data
            https://poloniex.com/public?command=returnChartData&currencyPair={0}&start={1}&end={2}&period={3}

            Returns     [{"date":1405699200,"high":0.0045388,"low":0.00403001,"open":0.00404545,"close":0.00427592,
                        "volume":44.11655644,"quoteVolume":10259.29079097,"weightedAverage":0.00430015}, ...]

        '''



    def post_process_market_history(self, p_market_history):

        # Request failures
        if p_market_history.status_code != 200:
            raise ExceptionSkyzeAbstract()

        payload = pd.DataFrame(p_market_history.json())              # all_markets.json() is class 'dict'
        if len(payload) > 0:
            pd.DatetimeIndex(payload.date*10**9)
            payload.index = pd.to_datetime(payload.date*10**9)       # Set the date as the index
            payload.drop('date', axis=1, inplace=True)               # Delete the date column
            #payload = payload.iloc[::-1]                             # Reverse the order to time ascending

        '''
            Return DataFrame has columns [  close high low open quoteVolume volume ]
        '''
        return payload





if __name__ == "__main__":
    print("MAIN")
    cryptopia = Cryptopia()
    cryptopia.getAllMarkets()
