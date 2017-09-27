# IMPORTS
import pandas as pd

# PATHS
data_file_path    = "Data/Trading/"
testing_file_path = "Unit_Test/Test_Data/"
results_file_path = "Unit_Test/Test_Data/"

# INTERVALS
dict_list = [
                {"Name":"TICK",    "Seconds":      0,    "Directory_name":"tick"       },
                {"Name":"MIN_5",   "Seconds":    300,  "Directory_name":"minutes_5"    },
                {"Name":"MIN_15",  "Seconds":    900,  "Directory_name":"minutes_5"    },
                {"Name":"MIN_30",  "Seconds":   1800,  "Directory_name":"minutes_5"    },
                {"Name":"HOUR_1",  "Seconds":   3600,  "Directory_name":"hours_1"      },
                {"Name":"HOUR_2",  "Seconds":   7200,  "Directory_name":"hours_2"      },
                {"Name":"HOUR_4",  "Seconds":  14400,  "Directory_name":"hours_4"      },
                {"Name":"DAY_1",   "Seconds":  86400,  "Directory_name":"day_1"        },
                {"Name":"WEEK_1",  "Seconds": 604800,  "Directory_name":"week_1"       },
                {"Name":"MONTH_1", "Seconds":   3600,  "Directory_name":"month_1"      }
            ]

intervals = pd.DataFrame(dict_list)
intervals = intervals.set_index('Name')

# access by:   intervals.get_value("5_MIN","Seconds")




# EXCHANGES
exch_list = [
                {"Name":"Coin Market Cap",    "Directory_name":"CMC"            },
                {"Name":"Cryptopia",          "Directory_name":"Cryptopia"      },
                {"Name":"Poloniex",           "Directory_name":"Poloniex"       },
                {"Name":"IGMarkets",          "Directory_name":"IGMarkets"      }
            ]

exchanges = pd.DataFrame(exch_list)
exchanges = exchanges.set_index('Name')

# access by:   exchanges.get_value("Cryptopia","Directory_name")
