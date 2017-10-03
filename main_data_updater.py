'''
Created on 21/08/2017
@author: michaelnew

Manages the data updates from our data sources

Used like a comandline with switches to run various functions

'''

#--- Imports ---------------------------------------------------------------------------------------------

# 3rd Party libraries
import datetime

# Skyze modules
from Market_Data.CoinMarketCap import CoinMarketCap
from Market_Data.Cryptopia import Cryptopia
from Market_Data.PoloniexSkyze import PoloniexSkyze


#----------------------------------------------------------------------------------------------------------
#
#    RUN SWITCHES
#
#----------------------------------------------------------------------------------------------------------


# === Data load Switches =====
cmc_load = False
cryptopia_load = True
poloniex_load = False

# === Data load Type =====
load_type = "all"     # Laod_type Options are:
#        all             ... the exchanege will call get all markets then download all
#        ico             ... will use the custom ICO list
#        custom_list     ... will use the custom list
#        do_nothing      ... won't do anything ... can be do nothing or any text other than above options


# === Custom Load Lists =====
custom_list_cmc = ['maker']      # currency
custom_list_cryptopia = ['CEFS_DOGE', 'CEFS_LTC', 'CEFS_BTC', 'RICKS_DOGE', 'RICKS_LTC', 'RICKS_BTC', 'R_DOGE', 'R_LTC', 'R_BTC', 'KAYI_DOGE', 'KAYI_LTC', 'KAYI_BTC', 'KING_DOGE', 'KING_LTC', 'KING_BTC', 'APX_DOGE', 'APX_LTC', 'APX_BTC', 'QWARK_DOGE', 'QWARK_LTC', 'QWARK_BTC', 'KNC_DOGE', 'KNC_LTC', 'KNC_BTC', 'HDLB_DOGE', 'HDLB_LTC', 'HDLB_BTC', 'HAC_DOGE', 'HAC_LTC', 'HAC_BTC', 'COR_DOGE', 'COR_LTC', 'COR_BTC', 'MCI_DOGE', 'MCI_LTC', 'MCI_BTC', 'XBL_DOGE', 'XBL_LTC', 'XBL_BTC', 'IQT_DOGE', 'IQT_LTC', 'IQT_BTC', 'BOP_DOGE', 'BOP_LTC', 'BOP_BTC', 'DP_DOGE', 'DP_LTC', 'DP_BTC', 'EQT_DOGE', 'EQT_LTC', 'EQT_BTC', 'XMCC_DOGE', 'XMCC_LTC', 'XMCC_BTC', 'BTM_DOGE', 'BTM_LTC', 'BTM_BTC', 'CTR_DOGE', 'CTR_LTC', 'CTR_BTC', 'NEBL_DOGE', 'NEBL_LTC', 'NEBL_BTC', 'BKCAT_DOGE', 'BKCAT_LTC', 'BKCAT_BTC', 'ORME_DOGE', 'ORME_LTC', 'ORME_BTC', 'MTL_DOGE', 'MTL_LTC',
                         'MTL_BTC', 'WILD_DOGE', 'WILD_LTC', 'WILD_BTC', 'XLC_DOGE', 'XLC_LTC', 'XLC_BTC', 'NDAO_DOGE', 'NDAO_LTC', 'NDAO_BTC', 'STRC_DOGE', 'STRC_LTC', 'STRC_BTC', 'XFT_DOGE', 'XFT_LTC', 'XFT_BTC', 'SPR_DOGE', 'SPR_LTC', 'SPR_BTC', 'ZEN_DOGE', 'ZEN_LTC', 'ZEN_BTC', 'BDL_DOGE', 'BDL_LTC', 'BDL_BTC', 'CRM_DOGE', 'CRM_LTC', 'CRM_BTC', 'ATH_DOGE', 'ATH_LTC', 'ATH_BTC', 'RKC_DOGE', 'RKC_LTC', 'RKC_BTC', 'MBRS_DOGE', 'MBRS_LTC', 'MBRS_BTC', 'MTNC_DOGE', 'MTNC_LTC', 'MTNC_BTC', 'NEO_DOGE', 'NEO_LTC', 'NEO_BTC', 'DBIX_DOGE', 'DBIX_LTC', 'DBIX_BTC', 'PAY_DOGE', 'PAY_LTC', 'PAY_BTC', 'QTUM_DOGE', 'QTUM_LTC', 'QTUM_BTC', 'OMG_DOGE', 'OMG_LTC', 'OMG_BTC', 'MYB_DOGE', 'MYB_LTC', 'MYB_BTC', 'CMPCO_DOGE', 'CMPCO_LTC', 'CMPCO_BTC', 'CNNC_DOGE', 'CNNC_LTC', 'CNNC_BTC', 'SKIN_DOGE', 'SKIN_LTC', 'SKIN_BTC', 'KGB_DOGE', 'KGB_LTC', 'KGB_BTC', 'ETT_DOGE', 'ETT_LTC']
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


# Data load switches
data_load_switch = cmc_load or cryptopia_load or poloniex_load
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
               ' ========== ' + " run time: " + str(run_time) + ' ========== ')
