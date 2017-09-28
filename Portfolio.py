#----------------------------------------------------------------------------------------------------------
#
#    CLASS: Portfolio
#
#----------------------------------------------------------------------------------------------------------

# --- 3rd party imports -------------
import pandas as pd
from pandas import ExcelWriter
import os
import sys
import datetime
import inspect

# --- Our Imports -------------------
from DataAccess import DataAccess
import settings
from Market import Market
from MarketStats import MarketStats
from BackTester import BackTester
from ExceptionSkyzeAbstract import ExceptionSkyzeAbstract


class Portfolio(DataAccess, ExceptionSkyzeAbstract):

    def __init__(self):
        super().__init__()
#         markets_ICO = ["AUGUR", "ark","neo"]
        self.markets_ICO = ["LLToken","BITFID","EOT-Token","Ulatech","BRAT","Walton","Aureus","AdCoin", "Tierion","MonacoCoin",
                            "OX-Fina","Protean","Dalecoin","ElectionChain","SIGMAcoin","NamoCoin","Achain","bitqy",
                            "ATMCoin","Dochain","Nebulas-Token","XTD-Coin","Frazcoin","TrueFlip","VeChain","Hshare",
                             "MyBit-Token","Krypstal","Growers-International","YOYOW","Smoke","Bolenum","0x",
                             "Health-Care-Chain","The-ChampCoin","Excelcoin","Timereum","Sojourn","Etheriya",
                             "CoinonatX","InvestFeed","Monster-Byte","Dent","BitAsean","Digital-Developers-Fund",
                             "AdShares","BlockCAT","DeepOnion","InfChain","AppleCoin","Shadow-Token","Rupaya",
                             "Dentacoin","Nexxus","Stakecoin","Blocktix","NEVERDIE","First-Bitcoin-Capital","BiblePay",
                             "Rustbits","Mao-Zedong","IOU1","Centra","Bytom","Wink","CoinDash","Minex","Etherx",
                             "Stox","HBCoin","Fuda-Energy","FiboCoins","FundYourselfNow","district0x","Compcoin",
                             "OpenAnx","KekCoin","BlakeStar","Cream","Birds","Aseancoin","Mothership","GeyserCoin",
                             "InsureX","PeopleCoin","EmberCoin","CampusCoin","Primalbase"]
        self.market_stats_all = pd.DataFrame
        self.portfolio_market_strategies = []          # List of Market Objects



    def getMarketsICO(self):
        return self.markets_ICO


    def marketStatsAll(self):
        return self.market_stats_all



    def getPortfolioMarketStrategies(self):
        return self.portfolio_market_strategies



    def addMarkets(self, p_markets, p_exchange, p_interval):
        ''' INPUT     list of market names as strings
            OUTPUT    nil
            FUNCTION  creates market objects for each market listed and adds to the internal list
        '''
        for market in p_markets:
            mkt_obj = Market(market, p_exchange, p_interval)
            self.portfolio_market_strategies.append(mkt_obj)


    def addMarketStrategy (self,p_market_strategies):
        ''' INPUT     list of market names, strategy pairs
            OUTPUT    nil
            FUNCTION  creates market objects for each market listed and adds to the internal list
        '''
        for market_strategy in p_market_strategies:
            self.portfolio_market_strategies.append(market_strategy)




    def getMarketNames (self):
        ''' Returns a string of market names '''
        market_names = ""
        for market_strategy in self.portfolio_market_strategies:
            market_names = market_names + ", " + market_strategy.getMarketName()
        return market_names[2:]



    def printICOStats(self, p_mkt_stats):
        for market_name in p_mkt_stats:
                mstats.printStats()
                print(); print(); print()





    def saveStatsToExcel(self, mkt_stat):
        # TODO This function should probably be in the MarketStats class
        # TODO add the error list to the saved excel
        # TODO add the runtime statistics to the excel file
        file_path = self.fileName("Market Stats "+datetime.datetime.now().strftime("%d. %B %Y %I:%M%p"),"xlsx")
        print("File save to:   " + file_path)

        writer = ExcelWriter(file_path, engine='openpyxl')
        mkt_stat.to_excel(writer,'Stats')

        mkt_stat.describe().to_excel(writer,'Stats', startrow=len(mkt_stat)+2, index=True)
        # TODO get the below working
#        mkt_stat.describe(percentiles=[.05,.1,.2,.3,.4,.5,.6,.7,.8,.9,.95])[[0,1,4,5]].to_excel(writer,'Stats', startrow=len(mkt_stat)+2, index=True)

        writer.save()




    # TODO: hardwired for only single exchange and inteval .. make the market list be a list of tuples (m,e,i)
    def calculateStats(self, p_market_list, p_exchange, p_interval):
        market_stats = [] #pd.DataFrame()
        error_list   = []

        market_count = 0
        total_markets = len(p_market_list)
        print("Market count: "+str(total_markets))
        for market_name in p_market_list:
            market_count += 1
            mkt = Market(market_name, p_exchange, p_interval)


            try:
                print(str(market_count)+" of "+str(total_markets)+" "+mkt.getMarketName() +", " + mkt.getInterval() +" on " + mkt.getExchange())
                mkt_data = mkt.readMarketDataCSV()       # self.readMarketDataCSV()
            except IOError:
                print("ERROR: Portfolio::calculateStats   ")
                self.printException(inspect.currentframe().f_lineno, market_name + " does not exist. "+str(sys.exc_info()[0]))
                error_list = ["NO FILE: "+market_name] + error_list
                print(); print(); print()
                continue
                break
            except:
                self.printException(inspect.currentframe().f_lineno,"ERROR: unknown - "+str(sys.exc_info()[0]))
#                 print(sys.exc_info()[0])
                error_list = ["ERROR: "+market_name] + error_list
                print(); print(); print()
            else:
                mstats = MarketStats()
                mstats.calculateStats(market_name, mkt_data)
                market_stats.append(mstats.toDict())
#                 print(mstats.toDataFrame())

        #convert to dataframe
        return pd.DataFrame.from_records(market_stats, index="market_name")




    def getBacktestMarkets(self, p_markets):
        # TODO: implement the real code
        return self.market_strategies



    def backtestIndependent(self, p_title, p_initial_equity, p_market_strategies, p_start_date, p_end_date, p_scope = "all"):

        # Get the list of MarketStrategies to backtest
        backtest_markets = []
        if p_market_strategies == "all":
            backtest_markets = self.portfolio_market_strategies
        else:
            backtest_markets = self.getBacktestMarkets()

        # Set up the backtester
        backtester = BackTester(title, p_initial_equity, backtest_markets, p_start_date, p_end_date)
        results = backtester.runBacktest()
