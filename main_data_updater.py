"""Created on 21/08/2017
@author: michaelnew

Manages the data updates from our data sources

Used like a comandline with switches to run various functions"""

#--- Imports -------------------------------------------------------------------

# 3rd Party libraries
import datetime
from halo import Halo
import rollbar

# Skyze modules
from Skyze_Market_Data_Updater_Service.CoinMarketCap import CoinMarketCap
from Skyze_Market_Data_Updater_Service.Cryptopia import Cryptopia
from Skyze_Market_Data_Updater_Service.PoloniexSkyze import PoloniexSkyze


#--- Rollbar Error reporting ---------------------------------------------------
rollbar.init('8f67acbc427a4d6ba80c31516bd355da',
             'Mike Laptop')  # access_token, environment
rollbar.report_message(
    'main_data_updater.py - Rollbar is configured correctly')

#-------------------------------------------------------------------------------
#
#    RUN SWITCHES
#
#-------------------------------------------------------------------------------


# === Data load Switches =====
cmc_load = False
cryptopia_load = True
poloniex_load = False

# === Data load Type =====
load_type = "all"     # Laod_type Options are:
#            all             ... the exchanege will call get all markets then download all
#            ico             ... will use the custom ICO list
#            custom_list     ... will use the custom list
#            do_nothing      ... won't do anything ... can be do nothing or any text other than above options


# === Custom Load Lists =====
custom_list_cmc = ['maker']      # currency
custom_list_cryptopia_high_freq = [
    'ETH_BTC', 'LTC_BTC', 'HSR_BTC', 'PAC_DOGE', 'SPR_BTC', 'ODN_BTC']
custom_list_cryptopia = custom_list_cryptopia_high_freq
# , 'BTC_ARDR', 'BTC_BCH', 'BTC_BCN', 'BTC_BCY', 'BTC_BELA', 'BTC_BLK', 'BTC_BTCD']
custom_list_poloniex = ['ETH_CVC']


#----------------------------------------------------------------------------------------------------------
#
#    MAIN BODY
#
#----------------------------------------------------------------------------------------------------------
# Track runtime
start_time = datetime.datetime.now()
print('=== Begin Market Updater ========== ' + str(start_time) + ' ========== ')
print()

# decorator @Halo(text='Loading', spinner='dots')

spinner = Halo(text='Loading', spinner='dots')
spinner.start()

# Data load switches
data_load_switch = cmc_load or cryptopia_load or poloniex_load
try:
    if load_type == "all" and data_load_switch:
        print("=== UPDATE MARKET DATA - ALL ===")
        if cmc_load:
            cmc = CoinMarketCap()
            cmc.updateMarketData()
        if cryptopia_load:
            crypt = Cryptopia()
            crypt.updateMarketData()
        if poloniex_load:
            poloniex = PoloniexSkyze()
            poloniex.updateMarketData()
    elif load_type == "ico" and data_load_switch:
        print("=== UPDATE MARKET DATA - ICO ===")
        if cmc_load:
            cmc = CoinMarketCap()
            mkt_data = cmc.updateMarketData(portfolio.markets_ICO)
        if cryptopia_load:
            crypt = Cryptopia()
            crypt.updateMarketData(portfolio.cryptopia_ICO)
    elif load_type == "custom_list" and data_load_switch:
        if cmc_load:
            print("=== UPDATE MARKET DATA - CUSTOM ===")
            cmc = CoinMarketCap()
            cmc.updateMarketData(custom_list_cmc)
        if cryptopia_load:
            crypt = Cryptopia()
            crypt.updateMarketData(custom_list_cryptopia)
        if poloniex_load:
            poloniex = PoloniexSkyze()
            poloniex.updateMarketData(custom_list_poloniex)
except:
    # Catch all exceptions
    rollbar.report_exc_info()
    # equivalent to rollbar.report_exc_info(sys.exc_info())

    # Calculate and print run time
end_time = datetime.datetime.now()
run_time = end_time - start_time
print(); print('=== End ========== ' + str(end_time) +
               ' ========== ' + " run time: " + str(run_time) + ' ========== ')

spinner.stop()
