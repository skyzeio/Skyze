
# 3rd Party imports
import os
import pandas as pd
from dateutil import parser


def removeSpaces(text):
  return text.replace(" ", "")


def readCSV(file_path, file_name, column_names):
  "Opens the file and reads the data"

  # set the file path
  file_path += file_name + ".csv"
  print("\nCSV File Path:\t" + file_path)

  try:
    df = pd.read_csv(
        file_path,
        header=None,
        names=column_names
        #                         index_col = "Date"
    )
  except IOError as err:
    print("File Error:   " + file_path)
    print(
        "FileNotFound - Skyze_Utility::readCSV .... IOError File does not exist")
    raise IOError(
        "FileNotFound Raised - Skyze_Utility::readCSV .... IOError File does not exist\nFile Path:   " + file_path)
    return
  except:
    print("UNKNOWN EXCEPTION - Skyze_Utility::readCSV\n")
    print("File path:   " + file_path)
    print(sys.exc_info())
    return
  else:
    # Convert the date column to a date !
    #             d['Date'] = pd.to_datetime(d['Date'].astype(str), format='%Y%m%d')  # NOT NEEDED after making date the index column
    df.index = [parser.parse(str(d)) for d in df["Date"]]
    del df["Date"]
    return df
