#----------------------------------------------------------------------------------------------------------
#
#   CLASS StrategySTC
#
#----------------------------------------------------------------------------------------------------------

# 3rd Party
import datetime

# Our System
from StrategyAbstract import StrategyAbstract
from Portfolio import Portfolio
from Market import Market
from MarketStrategy import MarketStrategy
from BackTester import BackTester

from Indicators.BigFatCandle            import BigFatCandle
from Indicators.WeightedMovingAverage   import WeightedMovingAverage
from Indicators.MovingAverage           import MovingAverage
from Indicators.TrueRange               import TrueRange
from Indicators.AverageTrueRange        import AverageTrueRange
from Indicators.SuperTrend              import SuperTrend


class StrategySTC (StrategyAbstract):

    strategy_name = "Super Trend Cross Over CT v01" 
    

    def __init__(self, p_start, p_end):
        StrategyAbstract.__init__(self, p_start, p_end)
        self.strategy_data = ""
        self.results = ""
        self.start_date = p_start
        self.end_date = p_end
        
        # Indicators
        self.fatRatio = 0.65
        self.wma_period = 4
        self.atr_period = 4
        self.fast_st_period = 5
        self.fast_st_multipler = 3
        self.indicators = [ BigFatCandle(self.fatRatio),
                            WeightedMovingAverage(self.wma_period, "Close"),
                            TrueRange(),
                            MovingAverage(self.wma_period, "Close"),
                            AverageTrueRange(self.atr_period),
                            SuperTrend (self.fast_st_period, self.fast_st_multipler)
                          ]
    
    # 
    
    def getMarketData(self, p_market_name, p_length):
        return
    
    # 
    
    def getResults(self ):
        return
    
    # 
    
    def stcScreener(self, p_market_list):
        for market in p_market_list:
            signal = 0
            market_data = self.getMarketData(150, p_length)         # DataFrame
            #signal = market_data apply stcSignal OR over the last 5 days
        return signal



        
    def calculateIndicators(self,p_data):
        super(StrategySTC, self).calculateIndicators(p_data)





def run():
    start_time = datetime.datetime.now()
    print('=== Begin ========== '+ str(start_time)+ ' ========== '); print()
    
    # Backtest information
    title = ['Super Trend Cross Over']
    initial_equity = 10000.0
    start_date = datetime.datetime(2014, 1, 1)
    end_date = datetime.datetime(2017, 1, 1)
    markets = ["test_coin_10rows"]
    strategies = ["StrategySTC"]
    exchange = "Cryptopia"
    Interval = "Day_1"
#     markets = ["Bitcoin","DaleCoin","Tierion"]
#     strategies = ["StrategySTC","StrategySTC","StrategySTC"]
    
    #Create the Market Strategy list for the Portfolio
    market_strategies = []
    for market,strategy in zip (markets,strategies):
        market_strategies.append(MarketStrategy(market, exchange, interval, strategy,start_date, end_date)) 
    
    # Use the MAC Strategy
#     events_queue = queue.Queue()
    
    # set up the portfolio
    portfolio = Portfolio()
    portfolio.addMarketStrategy(market_strategies)
    
    # run the backetest
    backtester = BackTester(title, initial_equity, market_strategies, start_date, end_date)
    results = backtester.runBacktest()
    
    # Set up the backtest
#     backtest = TradingSession(
#         config, strategy, tickers,
#         initial_equity, start_date, end_date,
#         events_queue, title=title,
#         benchmark=tickers[1],
#    )
#     results = backtest.start_trading(testing=testing)

    end_time = datetime.datetime.now() 
    run_time = end_time-start_time
    print(); print('=== End ========== '+ str(end_time) + ' ========== ' + " run time: "+ str(run_time) + ' ========== ') 
    
    return portfolio





if __name__ == "__main__":
    
    # Configuration data
#     testing = False
#     config = settings.from_file(
#         settings.DEFAULT_CONFIG_FILENAME, testing
#    )
    markets = ["AAPL", "SPY"]
    filename = None
    run()
#     run(config, testing, tickers, filename)
        