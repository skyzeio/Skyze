# 
# Data
#
# Reads in Market Data Files and Prints Statistics
#
# Bugs 

# from Exception import BaseException

#--- Imports -----------------------------------------------------------------------------------
import datetime
from Market_Data.CoinMarketCap import CoinMarketCap
from Market_Data.Cryptopia import Cryptopia
from Market_Data.PoloniexSkyze import PoloniexSkyze
from Portfolio import Portfolio
#--- Global Variables  -----------------------------------------------------------------------------------
     
                
#----------------------------------------------------------------------------------------------------------
#
#    RUN SWITCHES
#
#----------------------------------------------------------------------------------------------------------


run_strategy    = False
run_statistics  = False
run_cryptopia   = False
run_poloniex    = False

cmc_load        = False
cryptopia_load  = True
poloniex_load   = True
load_type       = "all"     # all | ico ! custom_list | do_nothing


# custom_list = [ 'fuda-energy', 'golos-gold', 'growers-international', 'fibocoins', 'falcoin', 'deuscoin', 
#                 'bagcoin', 'gycoin', 'fargocoin', 'lepaoquan', 'pura', 'dynamiccoin', 'sigmacoin', 'techshares', 
#                 'bitfid', 'asset-backed-coin', 'infchain', 'achain', 'health-care-chain', 'vechain', 'walton', 
#                 'xenixcoin', 'caliphcoin', 'digital-money-bits', 'swaptoken', 'future-digital-currency', 'powercoin', 
#                 'eboostcoin', 'krypstal', 'gxshares', 'byteball', 'ark', 'factom', 'dogecoin', 'siacoin', 'steem', 
#                 'stellar', 'bytecoin-bcn', 'bitshares', 'waves', 'zcash', 'stratis', 'lisk', 'bitconnect', 'hshare', 
#                 'neo', 'ethereum-classic', 'monero', 'iota', 'nem', 'dash', 'litecoin', 'ripple', 'bitcoin-cash', 
# custom_list_cmc = [ 'minex']        # asset
# custom_list_cmc = [ 'stellar' ]
custom_list_cmc = [ 'bitcoin']      # currency
custom_list_cryptopia = [ 'ETH_BTC'] # 10/9/17 20:32 ROW 982
custom_list_poloniex = ['BTC_AMP'] #, 'BTC_ARDR', 'BTC_BCH', 'BTC_BCN', 'BTC_BCY', 'BTC_BELA', 'BTC_BLK', 'BTC_BTCD']


#----------------------------------------------------------------------------------------------------------
#
#    MAIN BODY
#
#----------------------------------------------------------------------------------------------------------
start_time = datetime.datetime.now()
print('=== Begin ========== '+ str(start_time)+ ' ========== '); print()


portfolio = Portfolio()

if run_strategy:
#     strat = StrategySTC()
    pass

# print(cmc.scrapeAllCurrencies())

if run_statistics:
    bruce = portfolio.getMarketsICO()
    mkt_stat = portfolio.calculateStats(bruce, "Coin Market Cap", "DAY_1")   #WORKING ON RETURNING DATAFRAME
    print("mkt_stat: " + str(mkt_stat.head(5)))
    print("describe: " + str(mkt_stat.describe()))
    print("describe 2: " + str(mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,1,4,5]]))
    print(type(mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,1,4,5]]))
    portfolio.saveStatsToExcel( mkt_stat )
    # mkt_deta?arketDetailsToCSV(mkt_details)     # All markets
   

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
    
if run_cryptopia == True:
    cryptopia = Cryptopia()
    print(cryptopia.getAllMarkets())

if run_poloniex == True:
    poloniex = PoloniexSkyze()
#     print(poloniex.getAllMarkets())
    poloniex.updateMarketData(custom_list_poloniex)
    
#pprint(cmc.markets)
end_time = datetime.datetime.now() 
run_time = end_time-start_time
print(); print( '=== End ========== '+ str(end_time) + ' ========== ' + " run time: "+ str(run_time) + ' ========== ' ) 