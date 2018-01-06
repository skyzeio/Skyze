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
from datetime import datetime
import urllib
import urllib.request as urllibReq
import requests
# import os
import re
# import csv
import sys

from inspect import stack
import inspect

import ccxt

# Skyze Libraries
import settings_skyze
from Skyze_Market_Data_Updater_Service.ExchangeCCXTAbstract import ExchangeCCXTAbstract
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Standard_Library.Market import Market
from Skyze_Message_Logger_Service.SkyzeMessageLoggerService import *


class ExchangeCCXT (ExchangeCCXTAbstract, ExceptionSkyzeAbstract):

  def __init__(self, message_bus=None, logger=None):
    source_name = "Bitfinex"
    source_dir_name = "Bitfinex"
    max_start_date = datetime(2010, 1, 1)
    default_end_date = datetime.now()
    exchange_intervals = ["DAY_1", "HOUR_3", "HOUR_1", "MIN_5", "MIN_1"]
    exchange = ccxt.bitfinex2()

    super().__init__(exchange, source_name, source_dir_name,
                     max_start_date, default_end_date,
                     exchange_intervals,
                     message_bus, logger)

  def getAllMarkets(self, p_save_excel=False):
    '''Get all Markets
    {'BTC/USD':
        {'maker': 0.001, 'taker': 0.002,
        'precision': {'price': 5, 'amount': 5},
        'limits': {'amount': {'min': 0.002, 'max': 2000.0},
        'price': {'min': 1e-05, 'max': 100000.0},
        'cost': {'min': None, 'max': None}},
        'id': 'BTCUSD', 'symbol': 'BTC/USD',
        'base': 'BTC', 'quote': 'USD', 'baseId': 'BTC', 'quoteId': 'USD',
        'info':{'pair': 'btcusd','price_precision': 5,'initial_margin': '30.0',
                 'minimum_margin': '15.0', 'maximum_order_size': '2000.0',
                 'minimum_order_size': '0.002', 'expiration': 'NA'}
    }, .... }'''
    all_markets = self._exchange.load_markets()

    if p_save_excel:
      pd.DataFrame.from_dict(all_markets). \
          to_excel(settings_skyze.data_file_path +
                   '/' + self.source_name + '_markets.xlsx', index=False)

    # Convert to list of ccxt market symbol's
    all_markets = [symbol for symbol in all_markets]

    return all_markets

  def formatMarketHistoryURL(self, p_market, p_interval, p_start_date, p_end_date):

    # "https://poloniex.com/public?command=returnChartData&currencyPair={0}&start={1}&end={2}&period={3}"
    formatted_url = self.url_market_history.format(
        p_market, p_start_date.strftime("%s"), p_end_date.strftime("%s"), p_interval)

    return formatted_url

    '''
            get Historical Data
            https://poloniex.com/public?command=returnChartData&currencyPair={0}&start={1}&end={2}&period={3}

            Returns     [{"date":1405699200,"high":0.0045388,"low":0.00403001,"open":0.00404545,"close":0.00427592,
                        "volume":44.11655644,"quoteVolume":10259.29079097,"weightedAverage":0.00430015}, ...]

        '''

  def post_process_market_history(self, p_market_history):

    # TODO Request failures
    # if p_market_history.status_code != 200:
    #   raise ExceptionSkyzeAbstract()

    # Convert to dataframe
    payload = pd.DataFrame(p_market_history, columns=[
                           'date', 'open', 'high', 'low', 'close', 'volume'])

    if len(payload) > 0:
      pd.DatetimeIndex(payload.date * 10**6)
      # Set the date as the index
      payload.index = pd.to_datetime(payload.date * 10**6)
      # Delete the date column
      payload.drop('date', axis=1, inplace=True)
      # payload = payload.iloc[::-1]                             # Reverse the order to time ascending

    '''Return DataFrame has columns [  close high low open quoteVolume volume ]
        '''
    return payload
