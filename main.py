'''
Created on 21/08/2017
@author: michaelnew

Used like a comandline with switches to run various functions

'''

#--- Imports ---------------------------------------------------------------------------------------------
import datetime
from Market_Data.CoinMarketCap import CoinMarketCap
from Market_Data.Cryptopia import Cryptopia
from Market_Data.PoloniexSkyze import PoloniexSkyze
from Portfolio import Portfolio
     
                
#----------------------------------------------------------------------------------------------------------
#
#    RUN SWITCHES
#
#----------------------------------------------------------------------------------------------------------



# === Run Switches =====
# This runs various functions - I use this to tesst things at the moment
run_strategy    = False
run_statistics  = False
run_cryptopia   = False
run_poloniex    = False

# === Data load Switches =====
cmc_load        = False
cryptopia_load  = True
poloniex_load   = False

# === Data load Type =====
load_type       = "custom_list"     # Laod_type Options are:
                                    #        all             ... the exchanege will call get all markets then download all
                                    #        ico             ... will use the custom ICO list
                                    #        custom_list     ... will use the custom list
                                    #        do_nothing      ... won't do anything ... can be do nothing or any text other than above options



# === Custom Load Lists =====
custom_list_cmc = [ 'bitcoin']      # currency
custom_list_cryptopia = ['MST_BTC', 'BCN_DOGE', 'BCN_LTC', 'XRA_BTC', 'SKR_DOGE', 'LIT_BTC'] 
custom_list_poloniex = ['BTC_AMP'] #, 'BTC_ARDR', 'BTC_BCH', 'BTC_BCN', 'BTC_BCY', 'BTC_BELA', 'BTC_BLK', 'BTC_BTCD']


#----------------------------------------------------------------------------------------------------------
#
#    MAIN BODY
#
#----------------------------------------------------------------------------------------------------------
# Track runtime
start_time = datetime.datetime.now()
print('=== Begin ========== '+ str(start_time)+ ' ========== '); print()


portfolio = Portfolio()


# For Strategy Testing
if run_strategy:
#     strat = StrategySTC()
    pass



# For statistics testing
if run_statistics:
    ico_markets = portfolio.getMarketsICO()
    mkt_stat = portfolio.calculateStats(ico_markets, "Coin Market Cap", "DAY_1")   #WORKING ON RETURNING DATAFRAME
    print("mkt_stat: " + str(mkt_stat.head(5)))
    print("describe: " + str(mkt_stat.describe()))
    print("describe 2: " + str(mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,1,4,5]]))
    print(type(mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,1,4,5]]))
    portfolio.saveStatsToExcel( mkt_stat )
   
   
   
# Data load switches
if load_type == "all":
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
elif load_type == "ico":
    print("=== UPDATE MARKET DATA - ICO ===")
    if cmc_load: 
        cmc = CoinMarketCap()
        mkt_data = cmc.updateMarketData(portfolio.markets_ICO)
    if cryptopia_load: 
        crypt = Cryptopia()
        crypt.updateMarketData(portfolio.cryptopia_ICO)
elif load_type == "custom_list":
    print("=== UPDATE MARKET DATA - CUSTOM ===")
    if cmc_load: 
        cmc = CoinMarketCap()
        cmc.updateMarketData(custom_list_cmc)
    if cryptopia_load: 
        crypt = Cryptopia()
        crypt.updateMarketData(custom_list_cryptopia)
    if poloniex_load: 
        poloniex = PoloniexSkyze()
        poloniex.updateMarketData(custom_list_poloniex)



# Run Switches
if run_cryptopia == True:
    cryptopia = Cryptopia()
    print(cryptopia.getAllMarkets())

if run_poloniex == True:
    poloniex = PoloniexSkyze()
#     print(poloniex.getAllMarkets())
    poloniex.updateMarketData(custom_list_poloniex)


# Calculate and print run time
end_time = datetime.datetime.now() 
run_time = end_time-start_time
print(); print( '=== End ========== '+ str(end_time) + ' ========== ' + " run time: "+ str(run_time) + ' ========== ' ) 