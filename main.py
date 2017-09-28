'''
Created on 21/08/2017
@author: michaelnew

MAIN - used to run general functions .. until split off into their own main....py files

Used like a comandline with switches to run various functions

'''

#--- Imports ---------------------------------------------------------------------------------------------
# 3rd Party
import datetime
import argparse

# Skyze
from Portfolio import Portfolio


#----------------------------------------------------------------------------------------------------------
#
#    PARSE ARGUEMENTS
#
#----------------------------------------------------------------------------------------------------------

parser = argparse.ArgumentParser('Utility to run Skyze modules')



#----------------------------------------------------------------------------------------------------------
#
#    RUN SWITCHES
#
#----------------------------------------------------------------------------------------------------------



# === Run Switches =====
# This runs various functions - I use this to tesst things at the moment
run_strategy    = False
run_statistics  = True
run_cryptopia   = False
run_poloniex    = False
#----------------------------------------------------------------------------------------------------------
#
#    MAIN BODY
#
#----------------------------------------------------------------------------------------------------------
# Track runtime
start_time = datetime.datetime.now()
print('=== Begin Main General ========== '+ str(start_time)+ ' ========== '); print()


portfolio = Portfolio()


# For Strategy Testing
if run_strategy:
#     strat = StrategySTC()
    pass



# For statistics testing
if run_statistics:
    ico_markets = portfolio.getMarketsICO()
    mkt_stat = portfolio.calculateStats(ico_markets, "Coin Market Cap", "DAY_1")   #WORKING ON RETURNING DATAFRAME
    print("\n\nmkt_stat: \n" + str(mkt_stat.head(5)))
    print("\n\ndescribe: \n" + str(mkt_stat.describe()))
#    print("describe 2: " + str(mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,3,4]]))
#    print(type(mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,3,4]]))
    portfolio.saveStatsToExcel(mkt_stat)



# Run Switches
if run_cryptopia == True:
    print("=== RUN CRYPTOPIA ===")
    cryptopia = Cryptopia()
    print(cryptopia.getAllMarkets())

if run_poloniex == True:
    print("=== RUN POLONIEX ===")
    poloniex = PoloniexSkyze()
#     print(poloniex.getAllMarkets())
#     poloniex.updateMarketData(custom_list_poloniex)
    poloniex.processMarketDataFilesCSV()


# Calculate and print run time
end_time = datetime.datetime.now()
run_time = end_time-start_time
print(); print('=== End ========== '+ str(end_time) + ' ========== ' + " run time: "+ str(run_time) + ' ========== ')
