#----------------------------------------------------------------------------------------------------------
#
#   CLASS CoinMarketCap
#
#        Information Provider
#
#----------------------------------------------------------------------------------------------------------
import datetime
import os
import re
import csv
import sys
from pprint import pprint
import requests
from pathlib2 import Path                       # OO File management
import urllib
import urllib.request as urllibReq
from bs4 import BeautifulSoup                   # Webscraping
import pandas as pd
# deque to get last lines of CSV file
from collections import deque

# Skyze Libraries
from Skyze_Market_Data_Updater_Service.MarketDataSourceAbstract import MarketDataSourceAbstract
from Skyze_Standard_Library.ExceptionSkyzeAbstract import ExceptionSkyzeAbstract
import settings_skyze
from Market import Market


class CoinMarketCap (MarketDataSourceAbstract):

    def __init__(self, message_bus=None, logger=None):
        source_name = "Coin Market Cap"
        source_dir_name = "CMC"
        url_list_all_markets = ""
        max_start_date = datetime.datetime(2010, 1, 1)
        default_end_date = datetime.datetime.now()
        url_market_history = ""
        exchange_intervals = ["DAY_1"]

        super().__init__(source_name, source_dir_name, url_list_all_markets,
                         max_start_date, default_end_date, url_market_history,
                         exchange_intervals, message_bus, logger)

    def constructScrapeURL(self, marketStr, p_start_date, p_end_date):
        start_date = p_start_date.strftime('%Y%m%d')
        end_date = p_end_date.strftime('%Y%m%d')
        return "https://coinmarketcap.com/currencies/%(mkt)s/historical-data/?start=%(startDate)s&end=%(endDate)s" % {"mkt": marketStr, "startDate": start_date, "endDate": end_date}

    def scrapeAllCMCMarkets(self, crypto_type):
        """
            Looking for the currency full name as taht is what the historical data list uses
            <table claass="table dataTAble no-footer" id="currencies-all"
                <tr id="id-bitcion"
                    <td class="no-wrap currency-name">
                        <img src="https://files.coinmarketcap.com/static/img/coins/16x16/bitcoin.png" class="currency-logo" alt="Bitcoin">
                        <a href="/currencies/bitcoin/">Bitcoin</a>
                    </td>
        """
        if crypto_type == "currencies":
            scrape_page = "https://coinmarketcap.com/currencies/views/all/"
        else:
            scrape_page = "https://coinmarketcap.com/assets/views/all/"
        print(scrape_page)
        # query the website and return the html to the variable ‘page’
        page = urllibReq.urlopen(scrape_page)

        # parse the html using beautiful soap and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')

        # Take out the <div> of name and get its value
        name_box = soup.find('h1', attrs={'class': 'name'})

        result = []
        allrows = soup.findAll('tr')
        for row in allrows:
            #             print(row.get('id'))
            id = row.get('id')
            result.append(id)
#             result.append([])
#             allcols = row.findAll('td')
#             for col in allcols:
#                 thestrings = col.findAll(text=True)
#                 a = re.sub('[,]', '', thestrings[0])
#                 result[-1].append(a)

        result.pop(0)   # remove blank first element

        # remove the "id-" from the front of each name
        shortened = []
        shortened.insert(0, 'foo')
        for id in result:
            #             shortened.append([])
            shortened.append(id[3:])
#             shortened[-1].append(id[3:])

        shortened.pop(0)   # remove blank first element

        return shortened

    def scrapeHistoricalData(self, p_markets, p_startDate="20170727", p_endDate=""):
        # . CMC URL: https://coinmarketcap.com/assets/0x/historical-data/?start=20100101&end=20170826

        if p_endDate == "":
            p_endDate = datetime.date.today().strftime('%Y%m%d')

        # CMC uses - for spaces in the URL
        # CMC uses - instead of spaces in the URL
        marketStr = re.sub(" ", "-", p_markets)
#         marketStr = re.sub("\\.", "", marketStr)     # CMC removes . in the URL MIKE TODO
        scrape_page = self.constructScrapeURL(
            marketStr, p_startDate, p_endDate)
        print(scrape_page)

        # query the website and return the html to the variable ‘page’
        page = urllibReq.urlopen(scrape_page)

        # parse the html using beautiful soap and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')

        # Take out the <div> of name and get its value
        name_box = soup.find('h1', attrs={'class': 'name'})

        result = []
        allrows = soup.findAll('tr')
        for row in allrows:
            result.append([])
            allcols = row.findAll('td')
            for col in allcols:
                thestrings = col.findAll(text=True)
                a = re.sub('[,]', '', thestrings[0])
                result[-1].append(a)

        result.pop(0)

        return result

    # GET MARKET DETAILS
    #
    # Inputs
    #    Nil
    # Outputs
    #    Pandas DataFrame market details
    #
    # URL returns
    #     [  {
    #         "id": "bitcoin",
    #         "name": "Bitcoin",
    #         "symbol": "BTC",
    #         "rank": "1",
    #         "price_usd": "4366.26",
    #         "price_btc": "1.0",
    #         "24h_volume_usd": "1510950000.0",
    #         "market_cap_usd": "72161558885.0",
    #         "available_supply": "16527087.0",
    #         "total_supply": "16527087.0",
    #         "percent_change_1h": "0.38",
    #         "percent_change_24h": "0.56",
    #         "percent_change_7d": "5.71",
    #         "last_updated": "1503817467"    },  ....... ]

    def getMarketDetails(self):

        # Get the URL JSON
        request = requests.get(url='https://api.coinmarketcap.com/v1/ticker/')
        # request=requests.get(url='https://api.coinmarketcap.com/v1/ticker/?limit=3')

        # convert to DataFrame
        market_Details_DF = pd.DataFrame(request.json())

        return market_Details_DF

    # See Get Market Details for format of p_marketDetails

    def saveMarketDetailsToCSV(self, p_market_details):
        #         print(type(p_market_details))
        #         if str(type(p_market_details)) == "<class 'list'>":
        #             # It's a List
        #             print("list")
        #             mkt_data = self.scrapeHistoricalData(p_market_details)
        #             print(mkt_data)
        #         else:
        #             print("Not list")
        #             print(p_market_details["id"].tolist())
        #             # It's a Pandas DataFrame
        #             mkt_data = self.scrapeHistoricalData(p_market_details["id"].tolist())

        # Save to CSV
        file_path = os.path.join(
            settings_skyze.data_file_path, "CoinMarketCapMarkets.csv")
        p_markets.to_csv(file_path, header=False,
                         date_format='%Y-%m-%d %H:%M:%S')
        return

    # Converts month in Jan form to 01 form

    def convertMonthString(self,
                           p_month_str       # String of 3 characters representing the month
                           ):

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

    # Input
    #    scraped market data with date "26 Aug 2017"
    # Output
    #    market data with date "20170826"

    def convertScrapedDateFormat(self,
                                 p_market_data     # Scraed data - List of lists
                                 ):
        for row in p_market_data:
            row[0] = row[0][7:] + \
                self.convertMonthString(row[0][:3]) + row[0][4:6]

        return p_market_data


#     def saveHistoricalDataToCSV(self,
#                                  p_market_name,     # String
#                                  p_market_data      # List of scraped data
#                                ):
#
#         # Save to CSV
#         file_path = os.path.join(settings_skyze.data_file_path, "%s.csv" % p_market_name)
#         print(p_market_data)
#         #p_market_data.to_csv(file_path,header=False, date_format='%Y-%m-%d %H:%M:%S')
#
#         # Format the date column
#         p_market_data = self.convertScrapedDateFormat(p_market_data)
#
#         with open(file_path, 'w') as myfile:
#                     wr = csv.writer(myfile)
#                     wr.writerows(p_market_data)
#         return

    def updateMarketData(self, p_market_list="all"):
        ''' Iterates through the market list and calls the exchagne API to get the historical data
            Saves the data into CSV
            Tracks errors adding the market pair name to the error list
        '''
        if p_market_list == "all":
            mkt_list = self.scrapeAllCMCMarkets("currencies")
            mkt_list = mkt_list + self.scrapeAllCMCMarkets("assets")
        else:
            mkt_list = p_market_list

        download_total = str(len(mkt_list))
        print("Markets to downlaod: " + download_total)
        # Loop throuth the Markets
        error_list = []
        no_data_list = []
        mkt_count = 0
        for market in mkt_list:  # self.markets:
            #             print("No Data:   "+str(len(no_data_list)))
            #             print(no_data_list)
            mkt_count += 1
            print()
            print(str(mkt_count) + " of " +
                  download_total + ". " + market)  # MIKE [0]

            # Default start date if data not previously laoded
            load_start_date = self.max_start_date
            load_end_date = self.default_end_date

            # Get the load dates
            file_path = self.fileName(market, "day_1")
            file_start_date, file_end_date, load_start_date = self.getLoadDates(
                market, self.exchange_intervals.loc["DAY_1"], load_start_date, file_path)
#             load_start_date = load_start_date + datetime.timedelta(1,0)

            # Print the dates
            print("File: " + file_path)
            print("File Start: " + str(file_start_date) +
                  "   End: " + str(file_end_date))
            print("Load Start: " + str(load_start_date) +
                  "   End: " + str(load_end_date))

            # Scrape the webpage
            try:
                market_data = self.scrapeHistoricalData(
                    market, load_start_date, load_end_date)
            except urllib.error.HTTPError as err:
                print(
                    "HTTP ERROR: CoinMarketCap::updateMarketData: Probably wrong file name in URL" + str(err.args))
                error_list = error_list.append(market)
# MIKE to do
#             except http.client.BadStatusLine as err:
#                 print("HTTP BadStatusLine: updateMarketData: "+str(err.args))
#                 error_list = [market] + error_list
            except:
                print(
                    "UNKNOWN ERROR: CoinMarketCap::updateMarketData ... market_data = self.scrapeHistoricalData")
                print(sys.exc_info()[0])
                error_list = market + error_list
            else:
                # Check for no data message
                if market_data[0] == ['No data was found for the selected time period.']:
                    print("No data found for this market.")
#                     no_data_list = market + no_data_list
#                     no_data_list = no_data_list.append(market)
                else:

                    # Format the date column
                    market_data = self.convertScrapedDateFormat(market_data)

                    # Print number of rows
                    print("Number of rows imported: " +
                          str(len(market_data) - 1))

                    payload = pd.DataFrame(market_data, columns=[
                                           "Date", "Open", "High", "Low", "Close", "Volume", "MC"])
                    if len(payload) > 0:
                        payload.Date = pd.to_datetime(
                            payload.Date, format="%Y%m%d")     # convert to datetime
#                         payload.Date2 = payload.Date[0].strftime('%Y-%m-%d %H:%M:%S')
#                         pd.DatetimeIndex(payload[0]*10**9)                # all_markets.json() is class 'dict'
                        # Set the Timestamp as the indes
                        payload = payload.set_index('Date')
                        # Reverse teh order to time ascending
                        payload = payload.iloc[::-1]
                #         print(payload.head(5))
                #         print(payload.tail(5))

                    # Save the data
                    mkt = Market(market, self.source_dir_name,
                                 "Day_1", payload)
                    mkt.saveMarketData(p_file_path=file_path)
#
#                     # Save the file to CSV
#                     my_file = Path(file_path)
#                     if my_file.is_file():
#                         # File exists
#                         with open(file_path, 'a') as myfile:
#                             wr = csv.writer(myfile)
#                             # Ignore the first row in the scraped data as it is a repeat
#                             # Add a empty row to ensure the CSV is written starting on the next row
#                             # Reverse it so it is date ascending (newest at the end)
#                             wr.writerows(list(reversed(market_data))[1:])
#     #                         wr.writerows([[]]+list(reversed(market_data))[1:])
#                     else:
#                         # No file so create new file
#                         with open(file_path, 'w') as myfile:
#                             wr = csv.writer(myfile)
#                             # Reverse it so it is date ascending (newest at the end)
#                             wr.writerows(reversed(market_data))

        print()
        print()
        print()
        print("Success: " + str(len(mkt_list)))  # -len(error_list)))
        #-str(len(no_data_list))
        print("Error:   " + str(len(error_list)))
        print(error_list)
        print("No Data:   NOT IMPLEMENTED ... " + str(len(no_data_list)))
        print(no_data_list)


if __name__ == "__main__":
    print("MAIN")
