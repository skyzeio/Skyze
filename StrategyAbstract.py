'''
Created on 02/09/2017

@author: michaelnew
'''

class  StrategyAbstract(object):
    '''
    classdocs
    '''


    def __init__(self, p_start, p_end):
        '''
        Constructor
        '''
        self.strategy_data = ""
        self.results = ""
        self.start_date = p_start
        self.end_date = p_end
        self.indicators = []
        
        
    def calculateIndicators(self, p_data):
        for indicator in self.indicators:
            print(indicator.getName())
            result = indicator.calculate(p_data)
            print(result)
        
        return result
