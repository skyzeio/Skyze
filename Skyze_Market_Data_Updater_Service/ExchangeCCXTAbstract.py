'''Created on 08/09/2017  @author: michaelnew'''

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import os
import re
import csv
import sys

import inspect

from ccxt.base.errors import ExchangeError
from ccxt.base.errors import NotSupported
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import RequestTimeout
from ccxt.base.errors import ExchangeNotAvailable

import requests
from pathlib2 import Path                       # OO File management
import urllib
import urllib.request as urllibReq
# deque to get last lines of CSV file
from collections import deque

# Asynch messaging Q
# import zmq


# skyze libraries
import settings_skyze
import Skyze_Standard_Library.Colourful_Printing as cp
from Skyze_Standard_Library.Market import Market
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
from Skyze_Standard_Library.SkyzeLogger import SkyzeLogger
from Skyze_Messaging_Service.SkyzeMessageBusService import *
from Skyze_Message_Logger_Service.SkyzeMessageLoggerService import *
# Messages
from Skyze_Messaging_Service.Messages.MessageDataReceived import MessageDataReceived
from Skyze_Messaging_Service.Messages.MessageMarketDataUpdaterRunComplete \
    import MessageMarketDataUpdaterRunComplete


class ExchangeCCXTAbstract(object):
  ''' Uses the ccxt class to interface with Exchanges'''

  def __init__(self, p_exchange, p_source_name, p_source_dir_name,
               p_max_start_date, p_default_end_date,
               p_exchange_intervals, message_bus=None, logger=None):
    '''Constructor'''
    # cctx exchange object
    self._exchange = p_exchange
    # Data source name e.g. Cryptopia, IGMarkets etc
    self._source_name = p_source_name
    self._source_dir_name = p_source_dir_name
    # Earliest data available from that data source
    self._max_start_date = p_max_start_date
    self._default_end_date = p_default_end_date
    # Exchange retry settings
    self._ddos_time_out = 50  # 50 seconds works
    self._general_time_out = 10  # Seconds
    self._retry_max = 5
    # Skyze Infrastructure
    self._logger = logger
    self._message_bus = message_bus

    if p_exchange_intervals == []:
      raise ExceptionSkyzeAbstract(
          "MarketDataSource Init - exchagne interval parameter required")

    self._exchange_intervals = settings_skyze.intervals.ix[p_exchange_intervals]

  def _getType(self):
    return self.__class__.__name__

  def getMarketsForCurrency(self):
    '''

    '''
    return "NOT IMPIMENTED"

  def getCurrencies(self):
    '''
    '''
    return "NOT IMPIMENTED"

  def convertMonthString(self,
                         p_month_str       # String of 3 characters representing the month
                         ):
    ''' Converts month in Jan form to 01 form'''

    month_num_string = "ERR"

    if p_month_str == "Jan":
      month_num_string = "01"
    elif p_month_str == "Feb":
      month_num_string = "02"
    elif p_month_str == "Mar":
      month_num_string = "03"
    elif p_month_str == "Apr":
      month_num_string = "04"
    elif p_month_str == "May":
      month_num_string = "05"
    elif p_month_str == "Jun":
      month_num_string = "06"
    elif p_month_str == "Jul":
      month_num_string = "07"
    elif p_month_str == "Aug":
      month_num_string = "08"
    elif p_month_str == "Sep":
      month_num_string = "09"
    elif p_month_str == "Oct":
      month_num_string = "10"
    elif p_month_str == "Nov":
      month_num_string = "11"
    elif p_month_str == "Dec":
      month_num_string = "12"

    return month_num_string

  # creates the full path and file name
  def fileName(self, p_market_name, p_interval):
    return os.path.join(settings_skyze.data_file_path,
                        "%s.csv" % (self._source_dir_name + "/"
                                    + p_interval + "/"
                                    + p_market_name)
                        )

  def post_process_file(self, p_market, p_interval):
    pass

  def getLoadDates(self, p_market, p_interval, p_load_start_date, p_file_path):
    ''' Opens the CSV file ... gets the date from the first (File Start date)
        and last (file end date) of the file
        Add the interval to the end date to calculate the load_start_date
    '''
    file_start_date = "No File"
    file_end_date = "No File"
    load_start_date = p_load_start_date

    # Create File
    my_file = Path(p_file_path)
    if my_file.is_file():
      # File Exiss
      try:
        # Get the File Start date from the last row
        top = pd.read_csv(p_file_path, nrows=0)
      except:
        print(
            "UNKNOWN ERROR: MarketDataSourceAbstract::getLoadDates .. read csv file")
        print(sys.exc_info()[0])
      else:
        file_start_date = top.columns.values[0]

        # Get the File End date from the last row
        with open(p_file_path, 'r') as f:
          q = deque(f, 2)
          # Handle the case where theris only one row in the file
          if len(q) == 2:
            if q[1] == "\n":
              file_end_date = datetime.strptime(
                  q[0][:q[0].find(',')], "%Y-%m-%d %H:%M:%S")
            else:
              file_end_date = datetime.strptime(
                  q[1][:q[1].find(',')], "%Y-%m-%d %H:%M:%S")
          else:
            file_end_date = datetime.strptime(
                q[0][:q[0].find(',')], "%Y-%m-%d %H:%M:%S")

        # ensure correct type of interval (int) as chagnes when coming from CMC to numpy.Int64
        interval = p_interval.Seconds
        if type(p_interval.Seconds) != "int":
          interval = int(p_interval.Seconds)

        # Add the interval
        load_start_date = file_end_date + \
            timedelta(0, interval) + timedelta(0, 3600)

    return file_start_date, file_end_date, load_start_date

  def getHistoricalData(self, p_market, p_interval, p_start_date="", p_end_date=""):
    ''' Calls ccxt to get the historical data which is returned in the follwing
        format:
        [  [
                1504541580000, // UTC timestamp in milliseconds
                4235.4,        // (O)pen price
                4240.6,        // (H)ighest price
                4230.0,        // (L)owest price
                4230.7,        // (C)losing price
                37.72941911    // (V)olume
            ],    ...     ]
    '''
    # Set dates
    if p_start_date == "":
      p_start_date = self._default_start_date
    if p_end_date == "":
      p_end_date = self._default_end_date

    # Format date for the ccxt call
    start_date_unix_ts = int(p_start_date.timestamp() * 1000)
    cp.prt(cp.pink("Mike START DATE = since: "), p_start_date,
           cp.blue("\tSTART DATE UNIX TS = since: "), start_date_unix_ts)

    success = True
    for try_count in range(1, self._retry_max):
      try:
          # ccxt call
          # market_history = bfx.fetch_ohlcv ('AVT/BTC', '1d',
          #                                  bfx.milliseconds() - 1000 * 86400 * 1000)
        cp.prt(cp.bold(cp.green(f"market_history = self._exchange.fetch_ohlcv('{p_market}'" +
                                ",'" + p_interval + "', since=" + str(start_date_unix_ts) + ")")))
        market_history = self._exchange.fetch_ohlcv(p_market,
                                                    p_interval,
                                                    since=start_date_unix_ts)
      except DDoSProtection:
        success = False
        cp.prt(cp.red(
            f"Attempt {try_count} - CCXT DDoS Protection Exception - Waiting {self._ddos_time_out} seconds"))
        time.sleep(self._ddos_time_out)
      except ExchangeError:
        success = False
        cp.prt(
            cp.red(f"Attempt {try_count} - CCXT ExchangeError Exception - Waiting {self._general_time_out} seconds"))
        time.sleep(self._general_time_out)
      except NotSupported:
        success = False
        cp.prt(cp.red(
            f"Attempt {try_count} - CCXT NotSupported Exception - Waiting {self._general_time_out} seconds"))
      except AuthenticationError:
        success = False
        cp.prt(
            cp.red(f"Attempt {try_count} - CCXT AuthenticationError Exception - Waiting {self._general_time_out} seconds"))
        time.sleep(self._general_time_out)
      except RequestTimeout:
        success = False
        cp.prt(
            cp.red(f"Attempt {try_count} - CCXT RequestTimeout Exception - Waiting {self._general_time_out} seconds"))
        time.sleep(self._general_time_out)
      except ExchangeNotAvailable:
        success = False
        cp.prt(
            cp.red(f"Attempt {try_count} - CCXT ExchangeNotAvailable Exception - Waiting {self._general_time_out} seconds"))
        time.sleep(self._general_time_out)
      except e:
        success = False
        cp.prt(cp.red(
            f"Attempt {try_count} - Unknown Exception::ExchangeCCXTAbstract::getHistoricalData - self._exchange.fetch_ohlcv - Waiting {self._general_time_out} seconds"))
        time.sleep(self._general_time_out)
      else:
        # once successful leave the retry loop
        break

    if success:
        # format the data to Skyze format
      payload = self.post_process_market_history(market_history)
    else:
      cp.prt(cp.bold(cp.red(f"*** DATALOAD FAILED ***")))
      payload = None

    return payload

  def updateMarketData(self, p_market_list="all"):
    ''' Iterates through the market list and calls the exchagne API to
            get the historical data
        Saves the data into CSV
        Tracks errors adding the market pair name to the error list
    '''
    # TODO have the output go to a log file as well as the screen
    # TODO include the runtime stats in the log file
    # TODO at the end of processing below, try again on the error list ... as often the
    #      error is due to internet connectivity. Maybe pause five then run on the error list

    # Set the market list
    if p_market_list == "all":
      mkt_list = self.getAllMarkets()
    else:
      mkt_list = p_market_list

    # Log header info
    download_total = str(len(mkt_list))
    interval_total = len(self._exchange_intervals)
    log_msg = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    log_msg += f"Exchange: {self._source_name} ==============================="
    log_msg += f"\nMarkets to downlaod: {download_total}  ... each market has "
    log_msg += f"{interval_total} intervals"
    log_msg += f"\nList of Markets: {list((mkt_list))}"
    log_msg += f"Rate Limit: {self._exchange.rateLimit}"
    self._logger.log_info(log_msg, print_log=False)

    # Loop throuth the Markets
    error_list = []
    no_data_list = []
    mkt_count = 0
    for market in mkt_list:
      mkt_count += 1
      cp.prt(cp.bold(cp.pink("==============================================")))
      log_msg = f"\n\n{mkt_count} of {download_total} . {market}"
      self._logger.log_info(log_msg, print_log=False)

      # Loop through the intervals
      for index, interval in self._exchange_intervals.iterrows():
        # Default start date if data not previously laoded
        load_start_date = self._max_start_date
        load_end_date = self._default_end_date

        # Get the load dates
        file_path = self.fileName(market.replace('/', '_'),
                                  interval.Directory_name)
        file_start_date, file_end_date, load_start_date = self.getLoadDates(
            market, interval, load_start_date, file_path)

        # Print the dates
        log_msg = f"\n\nInterval: {interval.Directory_name}   Seconds: "
        log_msg += f"{interval.Seconds}   Load start time: {datetime.now()}"
        log_msg += f"\nFile: {file_path}"
        log_msg += f"\nFile Start: {file_start_date}   End: {file_end_date}"
        log_msg += f"\nLoad Start: {load_start_date}   End: {load_end_date}"
        self._logger.log_info(log_msg, print_log=False)

        # Calls the URL
        try:
          market_data = self.getHistoricalData(
              market, interval.ccxt,
              load_start_date + timedelta(hours=10),
              load_end_date + timedelta(hours=10))
        except urllib.error.HTTPError as err:
          new_exception = ExceptionSkyzeAbstract()
          err_msg = "ERROR: HHTP - Probably wrong file name in URL - " \
              + str(err.args) + " --- " + str(sys.exc_info()[0])
          new_exception.reportException(self.__class__.__name__,
                                        inspect.currentframe().f_lineno,
                                        err_msg,
                                        self._logger,
                                        to_print=False, to_raise=False)
          error_list = error_list.append(market)
        except:
          new_exception = ExceptionSkyzeAbstract()
          new_exception.reportException(self.__class__.__name__,
                                        inspect.currentframe().f_lineno,
                                        "ERROR: unknown -",
                                        self._logger,
                                        to_print=False, to_raise=False)
          error_list = [market] + error_list
        else:
          if market_data is not None:
            # Check for no data message
            if len(market_data) == 0:
              log_msg = "No data found for this market."
              self._logger.log_info(log_msg, print_log=False)
            else:

              # Log
              log_msg = f"Number of Rows imported: {len(market_data)}"
              self._logger.log_info(log_msg, print_log=False)

              # Save the data
              mkt = Market(market.replace('/', '_'), self._source_dir_name,
                           interval.Directory_name, market_data,
                           p_reversed=True)
              mkt.saveMarketData(p_file_path=file_path)

              # exchange specific post processing
              self.post_process_file(market, interval.Directory_name)

              # send the message
              if self._message_bus != None:
                # Send a message if we are attached to the bus
                # Don't send if not attached
                msg = MessageDataReceived(
                    self._getType(), market, interval.Directory_name)
                self._message_bus.publishMessage(msg)
      break
      time.sleep(self._exchange.rateLimit / 1000 * 1.5)

    # Log end of update run
    end_log_msg = f"\n\n\nSuccess: {len(mkt_list)}"
    end_log_msg += f"\nError:   {len(error_list)}\n{error_list}"
    end_log_msg += f"\nNo Data:   NOT IMP ... {len(no_data_list)}\n{no_data_list}"
    end_log_msg += f"\nList of Markets: \n{list((mkt_list))}"
    self._logger.log_info(end_log_msg, print_log=False)
    # end of update message
    end_run_msg = MessageMarketDataUpdaterRunComplete(
        self._source_name, self._exchange_intervals, len(error_list),
        error_list, market_pairs=mkt_list)
    self._message_bus.publishMessage(end_run_msg)
    self._logger.log_info(end_run_msg.getJSON(), print_log=False)

  def removeDuplicateRowsCSV(self, p_market, p_interval):
    ''' Removes duplicate rows from a CSV file
        Opens a file, saves only unique rows to a temp file, deletes the original file and renames the temp file
    '''
    # Get the file names
    data_file_name = self._fileName(p_market, p_interval)
    temp_file_name = self._fileName(p_market + "_TEMP", p_interval)

    # Iterate through the file and only write unique lines to the temp file
    with open(data_file_name, 'r') as data_file, open(temp_file_name, 'w') as temp_file:
      seen = set()  # set for fast O(1) amortized lookup
      seen.add("1970-01-01 00:00:00,0,0,0,0,0,0,0\n")
      duplicate_count = 0
      for line in data_file:
        if line in seen:
          duplicate_count += 1
          continue  # skip duplicate

        seen.add(line)            # unique so add the line
        temp_file.write(line)

    # Clean up files
    os.remove(data_file_name)                    # delete the old data file
    # rename the temp file to the data file name
    os.rename(temp_file_name, data_file_name)

    return duplicate_count

  def processMarketDataFilesCSV(self, p_market_list="all"):
    ''' Iterates through the market list, opens the data file,
        runs a process over it and saves it
    '''

    if p_market_list == "all":
      mkt_list = self.getAllMarkets()
    else:
      mkt_list = p_market_list

    process_total = str(len(mkt_list))
    interval_total = len(self._exchange_intervals)
    print("Markets to process: " + process_total +
          "    ... each market has " + str(interval_total) + " intervals")
    print("List of Markets: " + str(list((mkt_list))))

    # convert market format from / to _
    mkt_list = [w.replace('/', '_') for w in mkt_list]

    # Loop throuth the Markets
    error_list = []
    no_file_list = []
    mkt_count = 0
    for market in mkt_list:
      mkt_count += 1
      print()
      print(str(mkt_count) + " of " + process_total + ". " + market)

      for index, interval in self._exchange_intervals.iterrows():

        # Get the load dates
        file_path = self._fileName(market, interval.Directory_name)
        file_start_date, file_end_date, load_start_date = self._getLoadDates(
            market, interval, self._max_start_date, file_path)

        # Print the dates
        print()
        print("Interval: " + interval.Directory_name + "   Seconds: " +
              str(interval.Seconds) + "   Process start time: " + str(datetime.now()))
        print("File: " + file_path)
        print("File Start: " + str(file_start_date) +
              "   End: " + str(file_end_date))

        # Process the file
        # TODO Pass this function as a parameter
        duplicate_count = self._removeDuplicateRowsCSV(
            market, interval.Directory_name)
        print("Dupliates removed: " + str(duplicate_count))

    print()
    print()
    print()
    print("Success: " + str(len(mkt_list)))  # -len(error_list)))
    #-str(len(no_data_list))
    print("Error:   " + str(len(error_list)))
    print(error_list)
    print("No Data:   NOT IMPLEMENTED ... " + str(len(error_list)))
    print(no_data_list)
    print("List of Markets: " + str(list((mkt_list))))
