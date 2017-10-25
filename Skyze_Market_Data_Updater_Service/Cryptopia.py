'''
Created on 08/09/2017

@author: michaelnew
'''
#----------------------------------------------------------------------------------------------------------
#
#   CLASS Cryptopia
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
import os
import re
# import csv
import sys

from inspect import stack
import inspect

# Skyze Libraries
import settings_skyze
from Skyze_Market_Data_Updater_Service.MarketDataSourceAbstract import MarketDataSourceAbstract
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Standard_Library.Market import Market


class Cryptopia (MarketDataSourceAbstract):

    def __init__(self, message_bus=None, logger=None):
        source_name = "Cryptopia"
        source_dir_name = "Cryptopia"
        url_list_all_markets = "https://www.cryptopia.co.nz/api/GetTradePairs"
        max_start_date = datetime.datetime(2014, 1, 1)
        default_end_date = datetime.datetime.now()
        url_market_history = "https://www.cryptopia.co.nz/api/GetMarketHistory/{0}/{1}"
        exchange_intervals = ["TICK"]

        super().__init__(source_name, source_dir_name, url_list_all_markets,
                         max_start_date, default_end_date, url_market_history,
                         exchange_intervals, message_bus, logger)

    def getAllMarkets(self, p_save_excel=False):
        """
            Returns a list of all markets (currency pairs) on the exchange

            https://www.cryptopia.co.nz/api/GetTradePairs
            {"Id":5447,"Label":"OMG/DOGE","Currency":"OmiseGo","Symbol":"OMG","BaseCurrency":"Dogecoin","BaseSymbol":"DOGE",
            "Status":"OK","StatusMessage":null,"TradeFee":0.20000000,"MinimumTrade":0.00000001,"MaximumTrade":100000000.0,
            "MinimumBaseTrade":1.00000000,"MaximumBaseTrade":100000000.0,"MinimumPrice":0.00000001,"MaximumPrice":100000000.0},

        """
        print("Get all markets")
        # query the website and return the html to the variable ‘page’
        # TODO add a timeout e.g. no internet connection ... at the moment it just sits and waits ....
        all_markets = requests.get(
            self.url_list_all_markets[0])    # <class 'dict'>
        # all_markets.json() is class 'dict'
        all_markets = pd.DataFrame(all_markets.json())

        payload = pd.DataFrame(list(all_markets.Data))

        if p_save_excel:
            payload.to_excel(settings_skyze.data_file_path +
                             '/Cryptopia_Markets.xlsx', index=False)

        return payload.Label

    def formatMarketHistoryURL(self, p_market, p_interval, p_start_date, p_end_date):

        # calculate hours to get
        hours_to_get = int(
            (p_end_date - p_start_date).total_seconds() // 3600 - 9)

        formatted_url = self.url_market_history.format(p_market, hours_to_get)

        return formatted_url

    def post_process_file(self, p_market, p_interval):
        print("POST PROCESS FILE ... " + self.source_name + " ... " + p_market)
        # Get the file names
        data_file_name = self.fileName(p_market, p_interval)
        temp_file_name = self.fileName(p_market + "_TEMP", p_interval)

        # Iterate through the file and only write unique lines to the temp file
        with open(data_file_name, 'r') as data_file, open(temp_file_name, 'w') as temp_file:
            seen = set()  # set for fast O(1) amortized lookup
            for line in data_file:
                if line in seen:
                    continue  # skip duplicate

                seen.add(line)
                temp_file.write(line)

        # Clean up files
        os.remove(data_file_name)  # delete the data file
        # rename the temp file to the data file name
        os.rename(temp_file_name, data_file_name)

        ''' RETURN HISTORICAL DATA
            https://www.cryptopia.co.nz/api/GetMarketHistory/%s/%i
            %s is the market name string
            %i is the hours back to return data for ... Possibly a max of 4 days history

            Returns

        '''

    def post_process_market_history(self, p_market_history):

        # Request failures
        if p_market_history.status_code == 503:
            raise ExceptionSkyzeAbstract()

        # all_markets.json() is class 'dict'
        market_history = pd.DataFrame(p_market_history.json())
        payload = pd.DataFrame(list(market_history.Data))
        if len(payload) > 0:
            # all_markets.json() is class 'dict'
            pd.DatetimeIndex(payload.Timestamp * 10**9)
            # Set the Timestamp as the indes
            payload.index = pd.to_datetime(payload.Timestamp * 10**9)
            # Reverse teh order to time ascending
            payload = payload.iloc[::-1]

        '''
            Return DataFrame has columns [ Amount     Label     Price   Timestamp     Total    TradePairId  Type  ]
        '''
        return payload


if __name__ == "__main__":
    print("MAIN")
    cryptopia = Cryptopia()
    cryptopia.getAllMarkets()
