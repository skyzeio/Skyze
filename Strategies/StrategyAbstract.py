'''
Created on 08/09/2017

@author: michaelnew
'''


# Library Imports
# 3rd parties
import pandas as pd

# Our Library
from Unit_Test.UnitTestSkyzeAbstract import UnitTestSkyzeAbstract
#import ExceptionSkyzeAbstract



# https://stackoverflow.com/questions/11254553/double-inheritance-causes-metaclass-conflict
#class CombinedMeta(ExceptionSkyzeAbstract.__metaclass__, UnitTestSkyzeAbstract.__metaclass__):
#    pass





class StrategyAbstract( UnitTestSkyzeAbstract ):
    '''
    classdocs
    '''
#    __metaclass__=CombinedMeta


    def __init__(self):
        '''
        Constructor
        '''

    def saveToExcel(self, p_df):
        pass
