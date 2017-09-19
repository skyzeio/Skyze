'''
Created on 04/09/2017

@author: michaelnew
'''

# 3rd parties
import csv
import numpy as np
import sklearn
import matplotlib
import matplotlib.pyplot as plt

# Our Library
from Indicators.IndicatorAbstract import IndicatorAbstract
from ExceptionSkyzeAbstract import ExceptionSkyzeAbstract



prices = []
dates  = []

def get_data(filename):
    with open(filename,'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
                
    return

    
    
    

class Neural(IndicatorAbstract,ExceptionSkyzeAbstract):
    '''
    classdocs
    '''
    name = "Moving Average v01"



    def __init__( self
                ):
        ''' Constructor '''
        
#             raise exceptionality
        pass
        
        
        
    def initial(self, p_data):
        ''' Calculate the first value if the calc is different to the subsequent calculations '''

        return p_data
    
    
    
    def calculate (self, 
                   p_data        # pd dataframe series
                     ):
        '''  Calculations '''
        p_data = self.initial( p_data )
        #p_data["MA_"+str(self.ma_period)] = p_data[self.ma_column].rolling(window=self.ma_period).mean().shift(1)
                
        #def predict_prices(dates,prices,x):
        dates = ""
        prices = ""
        x = 29
        dates = np.reshope(dates,(len(dates),1))
        
        svr_lin  = SVR(kernal='linear',C=1e3)
        svr_poly = SVR(kernel='poly',C=1e3, degree=2)
        svr_rbf  = SVR(kernel='rbf', C=1e3, gamma=0.1)
        
        svr_lin.fit(dates,prices)
        svr_poly.fit(dates,prices)
        svr_rbf.fit(dates,prices)
        
        plt.scatter(dates,prices, color='black', label = 'Date')
        plt.xlabel('Date')
        plt.ylabel('Price')
        plt.title('Support Vector Regression')
        plt.show()
        
        p_data["SVR_LIN"]  = svr_lin.predict(x)[0]
        p_data["SVR_POLY"] = svr_poly.predict(x)[0]
        p_data["SVR_RBF"]  = svr_rbf.predict(x)[0]

        return p_data
    
    
    
    def getResult (self ):
        ''' Getter '''
        return self.result
    
    
    
    def getName(self ):
        ''' Getter '''
        return self.name
    
    
print("Hello")
    
plt.scatter(dates,prices, color='blac,', label = 'Date')
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('Support Vector Regression')
plt.show()