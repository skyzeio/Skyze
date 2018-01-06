# IMPORTS
import pandas as pd

# RUN ENVIRONMENT
run_environment = "Mike's Laptop"

# PATHS
data_file_path = "Data/Trading/"
log_file_path = "Logs/"
test_data_file_path = "Unit_Test/Test_Data/"
target_results_file_path = "Unit_Test/Test_Data/"
test_results_file_path = "Unit_Test/Test_Results/"


# CCXT INTERVAL NOTATION (there may be more this is Bitfinex)
# {'1m': '1m', '5m': '5m', '15m': '15m', '30m': '30m', '1h': '1h',
#   '3h': '3h', '6h': '6h', '12h': '12h', '1d': '1D', '1w': '7D',
#   '2w': '14D', '1M': '1M'}
dict_list = [
    {"Name": "TICK",    "ccxt":   "",  "Seconds":     0, "Directory_name": "tick"},
    {"Name": "MIN_1",   "ccxt": "1m",  "Seconds":    60,
        "Directory_name": "minutes_1"},
    {"Name": "MIN_5",   "ccxt": "5m",  "Seconds":   300,
        "Directory_name": "minutes_5"},
    {"Name": "MIN_15",  "ccxt": "15m",  "Seconds":   900,
        "Directory_name": "minutes_15"},
    {"Name": "MIN_30",  "ccxt": "30m",  "Seconds":  1800,
        "Directory_name": "minutes_30"},
    {"Name": "HOUR_1",  "ccxt": "1h",  "Seconds":   3600,  "Directory_name": "hours_1"},
    {"Name": "HOUR_2",  "ccxt": "2h",  "Seconds":   7200,  "Directory_name": "hours_2"},
    {"Name": "HOUR_3",  "ccxt": "3h",  "Seconds":  10800,  "Directory_name": "hours_3"},
    {"Name": "HOUR_4",  "ccxt": "4h",  "Seconds":  14400,  "Directory_name": "hours_4"},
    {"Name": "DAY_1",   "ccxt": "1d",  "Seconds":  86400,  "Directory_name": "day_1"},
    {"Name": "WEEK_1",  "ccxt": "1w",  "Seconds": 604800,  "Directory_name": "week_1"},
    {"Name": "MONTH_1", "ccxt": "1M",  "Seconds": 2592000, "Directory_name": "month_1"}
]

intervals = pd.DataFrame(dict_list)
intervals = intervals.set_index('Name')

# access by:   intervals.get_value("5_MIN","Seconds")


# EXCHANGES
exch_list = [
    {"Name": "Coin Market Cap",
        "Directory_name": "CMC",
        "Class_name": "CoinMarketCap"},
    {"Name": "Cryptopia",
        "Directory_name": "Cryptopia",
        "Class_name": "Cryptopia"},
    {"Name": "Poloniex",
        "Directory_name": "Poloniex",
        "Class_name": "PoloniexSkyze"},
    {"Name": "IGMarkets",
        "Directory_name": "IGMarkets",
        "Class_name": "IGMarkets"}
]

exchanges = pd.DataFrame(exch_list)
exchanges = exchanges.set_index('Name')

# access by:   exchanges.get_value("Cryptopia","Directory_name")

# ROLLBAR ERROR LOGGING
rollbar_access_token = '8f67acbc427a4d6ba80c31516bd355da'
