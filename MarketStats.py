#----------------------------------------------------------------------------------------------------------
#
#    CLASS: Market Stats
#
#----------------------------------------------------------------------------------------------------------

#--- Imports -----------------------------------------------------------------------------------
import datetime as datetime



class MarketStats:

    def __init__(self):
        self.market_name     = ""
        self.days            = 0
        self.startDate       = 1
        self.endDate         = 1
        self.initialPrice    = 0
        self.highestHigh     = 0
        self.highestHighDate = 1
        self.highMult        = 0
        self.lowestLow       = 0
        self.lowestLowDate   = 1
        self.lowMult         = 0
        self.lowHighRatio    = 0

    # Converting to Dictionary format to then easily convert to Pandas DataFrame
    def toDict( self ):
        return {
                'market_name'       : self.market_name,
                'days'              : self.days,
                'startDate'         : self.startDate,
                'endDate'           : self.endDate,
                'initialPrice'      : self.initialPrice,
                'highestHigh'       : self.highestHigh,
                'highestHighDate'   : self.highestHighDate,
                'highMult'          : self.highMult,
                'lowestLow'         : self.lowestLow,
                'lowestLowDate'     : self.lowestLowDate,
                'lowMult'           : self.lowMult,
                'lowHighRatio'      : self.lowHighRatio,
        }




    # Converting to Pandas DataFrame

    def toDataFrame( self ):
        x= pd.DataFrame.from_records( self.toDict(), index=[self.toDict()['market_name']] )
        return x






    def calculateStats( self, p_mkt_name, p_mktData ):
        self.market_name = p_mkt_name
#         self.days = p_mktData.count()["High"]
#         self.startDate = p_mktData["Date"][self.days-1].strftime("%B %d, %Y")
#         self.endDate   = p_mktData["Date"][0].strftime("%B %d, %Y")
#         self.initialPrice = p_mktData["Open"][self.days-1]
#         self.highestHigh = p_mktData.max()["High"]
#         self.highestHighDate = p_mktData.loc[p_mktData['High'].argmax(), "Date"].strftime("%B %d, %Y")
#         self.highMult = round(self.highestHigh/self.initialPrice,2)
#         self.lowestLow = p_mktData.min()["Low"]
#         self.lowestLowDate = p_mktData.loc[p_mktData['Low'].argmin(), "Date"].strftime("%B %d, %Y")
#         self.lowMult = round(1-self.lowestLow/self.initialPrice,2)
#         self.lowHighRatio = round(self.highestHigh/self.lowestLow,2)
        self.market_name     = p_mkt_name
        self.days            = p_mktData.High.count()
        self.startDate       = p_mktData.index[0].to_datetime().strftime("%B %d, %Y")
        self.endDate         = p_mktData.index[self.days-1].to_datetime().strftime("%B %d, %Y")
        self.initialPrice    = p_mktData.Open[self.days-1]
        self.highestHigh     = p_mktData.High.max()
        self.highestHighDate = p_mktData.High.argmax().strftime("%B %d, %Y")
        self.highMult        = round(self.highestHigh/self.initialPrice,2)
        self.lowestLow       = p_mktData.Low.min()
        self.lowestLowDate   = p_mktData.High.argmin().strftime("%B %d, %Y")
        self.lowMult         = round(1-self.lowestLow/self.initialPrice,2)
        self.lowHighRatio    = round(self.highestHigh/self.lowestLow,2)

        return


    def printStats( self ):
        print("Market: "+self.market_name)
        print("From: "+str(self.startDate)+" To: "+str(self.endDate))
        print("Number of Days: "+str(self.days))
        print("Initial Price:  "+str(self.initialPrice))
        print("Highest High:   "+str(self.highestHigh)+"  "+str(self.highMult)+"   on "+str(self.highestHighDate))
        print("Lowest Low:     "+str(self.lowestLow)+"  "+str(self.lowMult)+"   on "+str(self.lowestLowDate))
        print("Low High Ratio: "+str(self.lowHighRatio))
        return
