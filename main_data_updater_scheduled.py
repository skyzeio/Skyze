'''
Created on 21/08/2017
@author: michaelnew

Manages the data updates from our data sources

Used like a comandline with switches to run various functions

'''

#--- Imports -------------------------------------------------------------------

# 3rd Party libraries
import datetime
import rollbar
from apscheduler.schedulers.blocking import BlockingScheduler

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
load_type = "custom_list
"     # Laod_type Options are:
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


def run_update(cmc_load, cryptopia_load, poloniex_load, load_type):
    # Track runtime
    start_time = datetime.datetime.now()
    print('=== Begin Market Updater ========== ' +
          str(start_time) + ' ========== ')
    print()
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

        # Calculate and print run time
        end_time = datetime.datetime.now()
        run_time = end_time - start_time
        print(); print('=== End ========== ' + str(end_time) +
                       ' ===== ===== ' + " run time: " + str(run_time) + ' ========== ')
    except:
        # Catch all exceptions
        rollbar.report_exc_info()
        # equivalent to rollbar.report_exc_info(sys.exc_info())


def sched_notice():
    start_time = datetime.datetime.now()
    print('\n\n\n=== Begin Market Update SCHEDULER ========== ' +
          str(start_time) + ' ========== \n')
    sched.print_jobs()
    print("\n\n")


#----------------------------------------------------------------------------------------------------------
#
#    MAIN BODY
#
#----------------------------------------------------------------------------------------------------------


sched = BlockingScheduler()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour='0-23')
def cryptopia_hourly_update():
    print('Scheduler:: Triggering:: cryptopia_hourly_update')
    custom_list_cryptopia = custom_list_cryptopia_high_freq
    run_update(False, True, False, "custom_list")
    sched_notice()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, minute: 10)
def cryptopia_morning_update():
    print('Scheduler:: Triggering:: cryptopia_morning_update')
    custom_list_cryptopia = custom_list_cryptopia_high_freq
    run_update(False, True, False, "custom_list")
    sched_notice()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=16, minute: 10)
def cryptopia_arvo_update():
    print('Scheduler:: Triggering:: cryptopia_arvo_update')
    custom_list_cryptopia = custom_list_cryptopia_high_freq
    run_update(False, True, False, "custom_list")
    sched_notice()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=14, minute=30)
def cmc_daily_update():
    print('Scheduler:: Triggering:: CMC all markets Daily Update at 2:30pm.')
    run_update(True, False, False, "all")
    sched_notice()


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=10, minute=12)
def poloniex_daily_update():
    print('Scheduler:: Triggering:: Poloniex all markets Daily Update at 10:12am')
    run_update(True, False, False, "all")
    sched_notice()


sched_notice()

# sched.configure()
sched.start()
