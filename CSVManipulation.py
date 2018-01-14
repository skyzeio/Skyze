
from Skyze_Standard_Library.Market import *
import pandas as pd
from pathlib2 import Path


class CSVManipulation(object):
  def __init__(self):
    self.files = \
        ["BTC_AMP", "BTC_BCH", "BTC_BCN", "BTC_BLK", "BTC_BTCD",
         "BTC_CVC", "BTC_DASH", "BTC_ETC", "BTC_ETH", "BTC_GAS", "BTC_GNO",
         "BTC_GNT", "BTC_LSK", "BTC_LTC", "BTC_MAID", "BTC_NXT", "BTC_OMG",
         "BTC_REP", "BTC_STEEM", "BTC_STR", "BTC_XMR", "BTC_XRP", "BTC_ZEC",
         "BTC_ZRX", "ETH_BCH", "ETH_CVC", "ETH_ETC", "ETH_GAS", "ETH_GNO",
         "ETH_GNT", "ETH_LSK", "ETH_OMG", "ETH_REP", "ETH_STEEM", "ETH_ZEC",
         "ETH_ZRX", "USDT_BCH", "USDT_BTC", "USDT_DASH", "USDT_ETC", "USDT_ETH",
         "USDT_LTC", "USDT_NXT", "USDT_REP", "USDT_STR", "USDT_XMR", "USDT_XRP",
         "USDT_ZEC", "XMR_BCN", "XMR_BLK", "XMR_BTCD", "XMR_DASH", "XMR_LTC",
         "XMR_MAID", "XMR_NXT", "XMR_ZEC"]
    self.trading_data_path = "Data/Trading/Poloniex/minutes_5"

  def saveCSV(self, df):
    if my_file.is_file():
      # File exists
      with open(p_file_path, 'a') as myfile:
        self.market_data.to_csv(
            myfile, header=False, date_format='%Y-%m-%d %H:%M:%S')
#                 wr = csv.writer(myfile)
        # Add a empty row to ensure the CSV is written starting on the next row
        # Reverse it so it is date ascending (newest at the end)
#                 print(len(self.market_data))
#                 wr.writerows(list(reversed(self.market_data)))
    else:
      # Create directory paths
      os.makedirs(os.path.dirname(p_file_path), exist_ok=True)
      # No file so create new file
      with open(p_file_path, 'w') as myfile:
        self.market_data.to_csv(
            p_file_path, header=False, date_format='%Y-%m-%d %H:%M:%S')
    return

  def savePDtoCSV(self, df, p_file_path):
    my_file = Path(p_file_path)
    if my_file.is_file():
      # File exists
      with open(p_file_path, 'a') as myfile:
        df.to_csv(
            myfile, header=False, date_format='%Y-%m-%d %H:%M:%S')
    else:
      # Create directory paths
      os.makedirs(os.path.dirname(p_file_path), exist_ok=True)
      # No file so create new file
      with open(p_file_path, 'w') as myfile:
        df.to_csv(
            p_file_path, header=False, date_format='%Y-%m-%d %H:%M:%S')

  def prepareTriArbFiles(self):
    ''' TODO This will add to the existing file when it saves - thus duplicating
      data - might want to delete existing version of the save file then save'''
    for file in self.files:
      file_path = self.trading_data_path + "/" + file + ".csv"
      print("File: " + file_path)

      df = pd.read_csv(file_path,
                       header=None,
                       names=["Date", "Open", "High", "Low",
                              "Close", "Volume", "MarketCap"]
                       #                         index_col = "Date"
                       )

      print("Rows in original mkt data:\t" +
            file + " - " + str(len(df)))
      one_month = 30 * 24 * 12
      reduced_df = df.iloc[-one_month:]

      # Remove rows with Nan's
      rows_before = len(reduced_df)
      reduced_df = reduced_df.dropna()
      rows_after = len(reduced_df)
      print("Nan's dropped: " + str(rows_before - rows_after) +
            "\tRows remaining: " + str(rows_after) +
            "\t% Dropped: " + str((rows_before - rows_after) / rows_before))

      # Check for duplicates
      print("Rows duplicated: " +
            str(len(reduced_df[reduced_df.index.duplicated()])))
      reduced_df = reduced_df.drop_duplicates()
      print("Dropped - New row count: " + str(len(reduced_df)) + "\n")

      # Save the file
      save_file_path = "Data/Testing/ArbTriange/Poloniex/minutes_5/" + file + ".csv"
      self.savePDtoCSV(reduced_df, save_file_path)

    return


if __name__ == '__main__':
  x = CSVManipulation()
  x.prepareTriArbFiles()
