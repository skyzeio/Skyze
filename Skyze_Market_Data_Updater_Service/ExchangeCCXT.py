'''Created on 06 Jan 2018  @author: michaelnew'''

# 3rd Party Imports
import pandas as pd
from datetime import datetime

import ccxt

# Skyze Libraries
import Skyze_Standard_Library.settings_skyze as settings_skyze
from Skyze_Standard_Library.settings_skyze import exchange_list
from Skyze_Market_Data_Updater_Service.ExchangeCCXTAbstract import ExchangeCCXTAbstract
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Standard_Library.Market import Market
from Skyze_Message_Logger_Service.SkyzeMessageLoggerService import *


class ExchangeCCXT (ExchangeCCXTAbstract, ExceptionSkyzeAbstract):
  '''Creates an exchange object using the ccxt API '''

  def __init__(self, exchange, message_bus=None, logger=None):
    source_name = exchange_list[exchange]["Name"]
    source_dir_name = exchange_list[exchange]["Directory_name"]
    exchange_intervals = exchange_list[exchange]["Data_intervals"]
    max_start_date = datetime(2010, 1, 1)
    default_end_date = datetime.now()

    # Create the exchange specific object
    exchange = eval('ccxt.%s ()' % exchange_list[exchange]["Class_name"])

    super().__init__(exchange, source_name, source_dir_name,
                     max_start_date, default_end_date,
                     exchange_intervals,
                     message_bus, logger)

  def printAllExchangeDetails(self):
    '''Prints selected details from all exchanges in ccxt'''
    for ident in ccxt.exchanges:
      print("\n")
      print(ident)
      exchange = eval('ccxt.%s ()' % ident)
      print(exchange)
      print("Feetch OHLC: ", exchange.hasFetchOHLCV)
      try:
        print(exchange.timeframes)
      except:
        print("NO Timeframes")
      try:
        print("Fetch Tickers: ", exchange.hasFetchTickers)
      except:
        print("NO Fetch Tickers")

  def printAllExchangeDataLoadPeriods(self):
    # exchange_list = ["bittrex"]
    for ident in ccxt.exchanges:
      print("\n")
      print(ident)
      exchange = eval('ccxt.%s ()' % ident)
      print(exchange)
      print("Feetch OHLC: ", exchange.hasFetchOHLCV)
      try:
        print(exchange.timeframes)
      except:
        print("NO Timeframes")
      try:
        print("Fetch Tickers: ", exchange.hasFetchTickers)
      except:
        print("NO Fetch Tickers")

  def getAllMarkets(self, p_save_excel=False):
    '''Get all Markets'''
    all_markets = self._exchange.load_markets()

    if p_save_excel:
      pd.DataFrame.from_dict(all_markets). \
          to_excel(settings_skyze.data_file_path +
                   '/' + self.source_name + '_markets.xlsx', index=False)

    # Convert to list of ccxt market symbol's
    all_markets = [symbol for symbol in all_markets]

    return all_markets

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

  def _createExchangeObject(self, exchange):
    ''' Depricated ... now instantiating class using "eval" in __init__'''
    if exchange == "Binance":
      exchange = ccxt.binance()
    elif exchange == "Bitfinex":
      exchange = ccxt.bitfinex2()
    elif exchange == "Bitmex":
      exchange = ccxt.bitmex()
    elif exchange == "BitStamp":
      exchange = ccxt.binance()
    elif exchange == "Bittrex":
      exchange = ccxt.binance()
    elif exchange == "Bithumb":
      exchange = ccxt.bithumb()
    elif exchange == "CCTX":
      exchange = ccxt.cctx()
    elif exchange == "GDAX":
      exchange = ccxt.gdax()
    elif exchange == "HitBC":
      exchange = ccxt.hitbc()
    elif exchange == "Huobipro":
      exchange = ccxt.huobipro()
    elif exchange == "Kraken":
      exchange = ccxt.kraken()
    elif exchange == "OKEx":
      exchange = ccxt.okex()
    else:
      raise "Exception ExchangeCCXT::_createExchangeObject - ccxt Exchange not valid"

    return exchange
