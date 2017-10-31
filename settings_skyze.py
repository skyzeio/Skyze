# IMPORTS
import pandas as pd

# RUN ENVIRONMENT
run_environment = "Mike's Laptop"

# PATHS
data_file_path = "Data/Trading/"
log_file_path = "Logs/"
test_data_file_path = "Unit_Test/Test_Data/"
target_results_file_path = "Unit_Test/Test_Data/"
test_target_results_file_path = "Unit_Test/Test_Results/"
test_target_results_file_path = "Unit_Test/Test_Results/"


# INTERVALS
dict_list = [
    {"Name": "TICK",    "Seconds":      0,    "Directory_name": "tick"},
    {"Name": "MIN_5",   "Seconds":    300,  "Directory_name": "minutes_5"},
    {"Name": "MIN_15",  "Seconds":    900,  "Directory_name": "minutes_5"},
    {"Name": "MIN_30",  "Seconds":   1800,  "Directory_name": "minutes_5"},
    {"Name": "HOUR_1",  "Seconds":   3600,  "Directory_name": "hours_1"},
    {"Name": "HOUR_2",  "Seconds":   7200,  "Directory_name": "hours_2"},
    {"Name": "HOUR_4",  "Seconds":  14400,  "Directory_name": "hours_4"},
    {"Name": "DAY_1",   "Seconds":  86400,  "Directory_name": "day_1"},
    {"Name": "WEEK_1",  "Seconds": 604800,  "Directory_name": "week_1"},
    {"Name": "MONTH_1", "Seconds":   3600,  "Directory_name": "month_1"}
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
