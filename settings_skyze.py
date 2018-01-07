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
data_intervals = [
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

intervals = pd.DataFrame(data_intervals)
intervals = intervals.set_index('Name')

# access by:   intervals.get_value("5_MIN","Seconds")

# EXCHANGES
exchange_list = {
    "Binance":
        {"Name": "Binance",
         "Directory_name": "Binance",
         "Class_name": "binance",
         "Data_intervals": ["DAY_1", "HOUR_4", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 178 rows"},

    "Bitfinex":
        {"Name": "Bitfinex",
         "Directory_name": "Bitfinex",
         "Class_name": "bitfinex2",
         "Data_intervals": ["DAY_1", "HOUR_3", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "all: 120 rows"},

    "Bitmex":
        {"Name": "Bitmex",
         "Directory_name": "Bitmex",
         "Class_name": "bitmex",
         "Data_intervals": ["DAY_1", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 100 rows"},

    # no timeframes
    "BitStamp":
        {"Name": "BitStamp",
         "Directory_name": "BitStamp",
         "Class_name": "bitStamp",
         "Data_intervals": [],
         "ccxt_support": True,
         "Data_provided": ""},

    "Bittrex":
        {"Name": "Bittrex",
         "Directory_name": "Bittrex",
         "Class_name": "bittrex",
         "Data_intervals": ["DAY_1", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 214 rows"},

    "Bithumb":
        {"Name": "Bithumb",
         "Directory_name": "Bithumb",
         "Class_name": "bithumb",
         "Data_intervals": [],
         "ccxt_support": True,
         "Data_provided": ""},

    "CCTX":
        {"Name": "CCTX",
         "Directory_name": "CCTX",
         "Class_name": "cctx",
         "Data_intervals": [],
         "ccxt_support": True,
         "Data_provided": ""},

    # no timeframes
    "CoinMarketCap":
        {"Name": "CoinMarketCap",
         "Directory_name": "CMC",
         "Class_name": "CoinMarketCap",
         "Data_intervals": ["DAY_1"],
         "ccxt_support": False,
         "Data_provided": ""},

    "Cryptopia":
        {"Name": "Cryptopia",
         "Directory_name": "Cryptopia",
         "Class_name": "Cryptopia",
         "Data_intervals": ["TICK"],
         "ccxt_support": False,
         "Data_provided": ""},

    "GDAX":
        {"Name": "GDAX",
         "Directory_name": "GDAX",
         "Class_name": "gdax",
         "Data_intervals": ["DAY_1", "HOUR_4", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": ""},

    "HitBTC":
        {"Name": "HitBTC",
         "Directory_name": "HitBTC",
         "Class_name": "hitbtc2",
         "Data_intervals": ["DAY_1", "HOUR_4", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 100"},

    "Huobipro":
        {"Name": "Huobipro",
         "Directory_name": "Huobipro",
         "Class_name": "huobipro",
         "Data_intervals": ["DAY_1", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 34 rows"},

    "Kraken":
        {"Name": "Kraken",
         "Directory_name": "Kraken",
         "Class_name": "kraken",
         "Data_intervals": ["DAY_1", "HOUR_4", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 160 rows"},

    "OKEx":
        {"Name": "OKEx",
         "Directory_name": "OKEx",
         "Class_name": "okex",
         "Data_intervals": ["DAY_1", "HOUR_4", "HOUR_1", "MIN_5", "MIN_1"],
         "ccxt_support": True,
         "Data_provided": "1d: 17 rows"},

    "Poloniex":
        {"Name": "Poloniex",
         "Directory_name": "Poloniex",
         "Class_name": "PoloniexSkyze",
         "Data_intervals": ["DAY_1", "HOUR_4", "HOUR_2", "MIN_5"],
         "ccxt_support": False,
         "Data_provided": "Full - 1d: 1329"},

    "IGMarkets":
        {"Name": "IGMarkets",
         "Directory_name": "IGMarkets",
         "Class_name": "IGMarkets",
         "Data_intervals": [],
         "ccxt_support": False,
         "Data_provided": ""}
}


# ROLLBAR ERROR LOGGING
rollbar_access_token = '8f67acbc427a4d6ba80c31516bd355da'
