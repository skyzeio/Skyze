'''
Created on 02/09/2017

@author: michaelnew
'''

import sys

from Market import Market
# from StrategyAbstract import StrategyAbstract
import pandas as pd

class MarketStrategy(object):
    '''
    classdocs
    '''

    def __init__(self, p_market, p_strategy, p_start_date, p_end_date):
        '''  Constructor '''
        self.market = Market(p_market)
        self.result = pd.DataFrame
        self.start_date = p_start_date
        self.end_date = p_end_date
        
        # dynamically create the strategy name
        # https://stackoverflow.com/questions/4821104/python-dynamic-instantiation-from-string-name-of-a-class-in-dynamically-imported
        module = __import__(p_strategy)
        class_ = getattr(module, p_strategy)
        self.strategy = class_(p_start_date, p_end_date)
      
      
        
    def getMarket(self):
        '''  Getter '''
        return self.market
    
    def getStrategy(self):
        '''  Getter '''
        return self.strategy
    
    def getResult(self):
        '''  Getter '''
        return self.result
    
    def getMarketName(self):
        ''' Getter '''
        return self.market.getMarketName()
    
    def toPrint(self):
        ''' Printer '''
        return "Market: " + self.market.getMarketName() + ", Strategy: " + self.strategy.strategy_name + ", Start: " + self.start_date.strftime("%B %d, %Y") + " End: " + self.end_date.strftime("%B %d, %Y")