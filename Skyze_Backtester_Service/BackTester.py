'''
Created on 02/09/2017

@author: michaelnew
'''

import pandas as pd
from Skyze_Standard_Library.Market import Market
from MarketStrategy import MarketStrategy
from datetime import datetime





class BackTester(object):
    '''
    classdocs
    '''


    def __init__(self, p_title, p_initial_equity, p_market_strategies, p_start_date, p_end_date, p_scope="all"):
        '''
        Constructor
        '''
        self.title              = p_title
        self.initial_equity     = p_initial_equity
        self.market_strategies  = p_market_strategies
        self.start_date         = p_start_date
        self.end_date           = p_end_date
        self.scope              = p_scope
        
        self.results = pd.DataFrame()
        
        
        
        
    def getBacktestMarkets(self):
        # TODO: implement the real code
        return self.market_strategies
        
        
        
        
    def runBacktest(self):
        count = 0
        total_tests = len(self.market_strategies)
        for market_strategy in self.market_strategies :
            count += 1
            print(str(count)+" of "+str(total_tests)+": "+market_strategy.getMarketName())
            market = market_strategy.getMarket()
            strategy = market_strategy.getStrategy()
            print(market_strategy.toPrint())
            #load the market data
            data = market.readMarketDataCSV()
            print("From BackTester::runBackTester")
            print()
            data = strategy.calculateIndicators(data)
            
        return
    
    
    
    
    
    